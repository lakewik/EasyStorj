# -*- coding: utf-8 -*-
from functools import partial
from sys import platform
import os

import hashlib
import json
import logging
import mimetypes
import threading
import time

import multiprocessing


import requests
import storj

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMessageBox

from crypto.crypto_tools import CryptoTools
from crypto.file_crypto_tools import FileCrypto
from engine import StorjEngine
from qt_interfaces.file_upload_new import Ui_SingleFileUpload
from utilities.backend_config import Configuration
from utilities.tools import Tools
from node_details import NodeDetailsUI

from resources.html_strings import html_format_begin, html_format_end
from resources.constants import MAX_RETRIES_UPLOAD_TO_SAME_FARMER, \
    MAX_RETRIES_NEGOTIATE_CONTRACT, AUTO_SCROLL_UPLOAD_DOWNLOAD_QUEUE, BUCKETS_LIST_SORTING_ENABLED, \
    MAX_UPLOAD_CONNECTIONS_AT_SAME_TIME,\
    FARMER_NODES_EXCLUSION_FOR_UPLOAD_ENABLED, BLACKLISTING_MODE, MAX_ALLOWED_UPLOAD_CONCURRENCY,\
    CONTRACT_NEGOTIATION_ITERATION_DELAY, DATA_TABLE_EDIT_ENABLED, MAX_RETRIES_TOKEN_RESOLVING
from resources.internal_backend_config_variables import APPLY_SELECTED_BUCKET_TO_UPLOADER


class SingleFileUploadUI(QtGui.QMainWindow):
    __logger = logging.getLogger('%s.SingleFileUploadUI' % __name__)

    def __init__(self, parent=None, bucketid=None, filepath=None, start=False, dashboard_instance=None, row_data=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui_single_file_upload = Ui_SingleFileUpload()
        self.ui_single_file_upload.setupUi(self)
        self.setAcceptDrops(True)
        self.ui_single_file_upload.file_path.setDragEnabled(True)
        self.ui_single_file_upload.file_path.setAcceptDrops(True)
        self.ui_single_file_upload.file_path.installEventFilter(self)

        self.first_bucket_id = bucketid

        self.upload_started = False
        # open bucket manager
        QtCore.QObject.connect(
            self.ui_single_file_upload.start_upload_bt,
            QtCore.SIGNAL('clicked()'),
            self.check_next_files_to_upload)
        # open file select dialog
        QtCore.QObject.connect(
            self.ui_single_file_upload.file_path_select_bt,
            QtCore.SIGNAL('clicked()'),
            self.select_file_path)
        # open tmp directory select dialog
        QtCore.QObject.connect(
            self.ui_single_file_upload.tmp_path_select_bt,
            QtCore.SIGNAL('clicked()'),
            self.select_tmp_directory)

        # handle cancel action
        QtCore.QObject.connect(
            self.ui_single_file_upload.cancel_bt,
            QtCore.SIGNAL('clicked()'),
            self.handle_cancel_action)

        QtCore.QObject.connect(
            self.ui_single_file_upload.add_file_to_table_bt,
            QtCore.SIGNAL('clicked()'),
            self.insert_selected_to_files_queue_table)



        self.ui_single_file_upload.files_queue_table_widget.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

        self.ui_single_file_upload.shard_queue_table_widget.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

        self.ui_single_file_upload.files_queue_table_widget. \
            customContextMenuRequested.connect(
            partial(self.display_files_table_context_menu))

        self.ui_single_file_upload.shard_queue_table_widget. \
            customContextMenuRequested.connect(
            partial(self.display_shards_queue_table_context_menu))

        self.already_used_farmers_nodes = []

        self.configuration = Configuration()

        self.tools = Tools()

        self.storj_engine = StorjEngine()

        self.initialize_upload_queue_table()
        self.dashboard_instance = dashboard_instance

        self.ui_single_file_upload.uploaded_shards.setText("Waiting...")

        self.is_upload_active = False
        self.current_active_connections = 0

        self.ui_single_file_upload.connections_onetime.setValue(
            int(MAX_UPLOAD_CONNECTIONS_AT_SAME_TIME))  # user can set it manually default value from constants file

        if platform == 'linux' or platform == 'linux2':
            # linux
            self.temp_dir = '/tmp'
        elif platform == 'darwin':
            # OS X
            self.temp_dir = '/tmp'
        elif platform == 'win32':
            # Windows
            self.temp_dir = 'C:\\Windows\\temp\\'
        self.ui_single_file_upload.tmp_path.setText(self.temp_dir)

        # initialize variables
        self.shards_already_uploaded = 0
        self.uploaded_shards_count = 0
        self.upload_queue_progressbar_list = []
        self.files_queue_progressbar_list = []



        self.connect(self, QtCore.SIGNAL('addRowToUploadQueueTable'), self.add_row_upload_queue_table)

        self.connect(self, QtCore.SIGNAL('incrementShardsProgressCounters'), self.increment_shards_progress_counters)
        self.connect(self, QtCore.SIGNAL('updateUploadTaskState'), self.update_upload_task_state)
        self.connect(self, QtCore.SIGNAL('updateShardUploadProgress'), self.update_shard_upload_progess)
        self.connect(self, QtCore.SIGNAL('showFileNotSelectedError'), self.show_error_not_selected_file)
        self.connect(self, QtCore.SIGNAL('showInvalidPathError'), self.show_error_invalid_file_path)
        self.connect(self, QtCore.SIGNAL('showInvalidTemporaryPathError'), self.show_error_invalid_temporary_path)
        self.connect(self, QtCore.SIGNAL('refreshOverallProgress'), self.refresh_overall_progress)
        self.connect(self, QtCore.SIGNAL('showFileUploadedSuccessfully'), self.show_upload_finished_message)
        self.connect(self, QtCore.SIGNAL('finishUpload'),
                     lambda: self.finish_upload(os.path.split(
                                                str(self.ui_single_file_upload.file_path.text()))[1],
                                                str(self.current_selected_bucket_id)))
        self.connect(self, QtCore.SIGNAL('setCurrentUploadState'), self.set_current_status)
        self.connect(self, QtCore.SIGNAL('updateShardUploadCounters'), self.update_shards_counters)
        self.connect(self, QtCore.SIGNAL('setCurrentActiveConnections'), self.set_current_active_connections)
        self.connect(self, QtCore.SIGNAL('setShardSize'), self.set_shard_size)
        self.connect(self, QtCore.SIGNAL('createShardUploadThread'), self.createNewShardUploadThread)
        self.connect(self, QtCore.SIGNAL('droppedFileToTable'), self.append_dropped_files_to_table)
        self.connect(self, QtCore.SIGNAL('checkNextFilesToUpload'), self.check_next_files_to_upload)
        self.connect(self, QtCore.SIGNAL('initializeUploadQueueTable'), self.initialize_upload_queue_table)
        self.connect(self, QtCore.SIGNAL('paintFileSize'), self.paint_file_size)
        self.connect(self, QtCore.SIGNAL('paintFrame'), self.paint_file_frame)
        self.connect(self, QtCore.SIGNAL('paintPUSHToken'), self.paint_push_token)
        self.connect(self, QtCore.SIGNAL('setOverallProgress'), self.paint_overall_progress)
        self.connect(self, QtCore.SIGNAL('disableButtonsForUpload'), self.disable_buttons_for_upload)
        self.connect(self, QtCore.SIGNAL('updateOngoingBridgeRequests'), self.update_ongoing_bridge_requests)

        # self.connect(self, QtCore.SIGNAL('handleCancelAction'), self.ha)

        # resolve buckets and put to buckets combobox
        self.createBucketResolveThread()
        self.ui_single_file_upload.files_list_view_bt.mousePressEvent = self.display_files_queue_change


        self.is_files_queue_table_visible = False

        # self.emit(QtCore.SIGNAL("addRowToUploadQueueTable"), "important", "information")
        # self.emit(QtCore.SIGNAL("addRowToUploadQueueTable"), "important", "information")
        # self.emit(QtCore.SIGNAL("incrementShardsProgressCounters"))

        # self.initialize_shard_queue_table(file_pointers)

        self.ui_single_file_upload.file_path.textChanged.connect(self.normalize_file_path)
        #self.ui_single_file_upload.file_path.mouseReleaseEvent.connect(self.normalize_file_path)

        self.shard_upload_percent_list = []

        self.ui_single_file_upload.overall_progress.setValue(0)

        self.prepare_files_queue_table()

        self.clip = QtGui.QApplication.clipboard()

        # apply shard size from configuration to number edit field
        self.ui_single_file_upload.max_shard_size.setMaximum(9999999)

        self.ui_single_file_upload.max_shard_size.setValue(int(self.configuration.max_shard_size_united()))
        self.ui_single_file_upload.shard_size_unit.setCurrentIndex(int(self.configuration.max_shard_size_unit()))

        self.ongoing_bridge_requests = 0

        self.ui_single_file_upload.connections_onetime.setMaximum(MAX_ALLOWED_UPLOAD_CONCURRENCY)

        if DATA_TABLE_EDIT_ENABLED == False:
            self.ui_single_file_upload.shard_queue_table_widget.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)

        self.current_row = 0

        if start:
            self.add_row_files_queue_table(row_data)
            self.check_next_files_to_upload()
            self.current_selected_bucket_id = dashboard_instance.current_selected_bucket_id


    def update_ongoing_bridge_requests(self):
        self.ui_single_file_upload.ongoing_bridge_requests.setText(str(self.ongoing_bridge_requests))

    def disable_buttons_for_upload(self):
        self.ui_single_file_upload.connections_onetime.setEnabled(False)
        self.ui_single_file_upload.start_upload_bt.setDisabled(True)
        self.ui_single_file_upload.start_upload_bt.setStyleSheet(("QPushButton:hover{\n"
                                                                  "  background-color: #8C8A87;\n"
                                                                  "  border-color: #8C8A87;\n"
                                                                  "}\n"
                                                                  "QPushButton:active {\n"
                                                                  "  background-color: #8C8A87;\n"
                                                                  "  border-color: #8C8A87;\n"
                                                                  "}\n"
                                                                  "QPushButton{\n"
                                                                  "  background-color: #8C8A87;\n"
                                                                  "    border: 1px solid #8C8A87;\n"
                                                                  "    color: #fff;\n"
                                                                  "    border-radius: 7px;\n"
                                                                  "}"))

    def paint_overall_progress(self, overall_progress):
        self.ui_single_file_upload.overall_progress.setValue(int(overall_progress))
        return True

    def paint_file_frame(self, file_frame):
        self.ui_single_file_upload.file_frame_id.setText(str(file_frame))
        return True

    def paint_push_token(self, PUSH_token):
        self.ui_single_file_upload.push_token.setText(str(PUSH_token))
        return True

    def paint_file_size(self, file_size):
        self.ui_single_file_upload.file_size.setText(str(file_size))
        return True

    def check_next_files_to_upload(self):


        self.current_row = 0

        self.upload_queue_progressbar_list = []

        self.files_row_upload_state_array = []


        if self.upload_started != True:
            print "Begin upload..."
            self.files_already_uploaded = 0
            self.files_queue_tablemodel = self.ui_single_file_upload.files_queue_table_widget.model()
            rows_count = self.ui_single_file_upload.files_queue_table_widget.rowCount()

            self.files_to_upload = rows_count

            i = 0
            while i < rows_count:
                self.files_row_upload_state_array.append(False)

                i += 1

        if self.files_already_uploaded == 0 and self.files_to_upload == 0:
            QtGui.QMessageBox.about(
                self, 'Warning', 'Please add file to queue  to begin upload.')
        else:
            filepath_index = self.files_queue_tablemodel.index(self.files_already_uploaded, 1)  # get file path
            # We suppose data are strings
            self.current_file_path = str(self.files_queue_tablemodel.data(
                filepath_index).toString())

            if self.files_already_uploaded >= self.files_to_upload:
                self.emit(QtCore.SIGNAL("showFileUploadedSuccessfully"))  # if no any file left to upload
                self.ui_single_file_upload.file_path.setEnabled(True)
                self.upload_started = False
            else:
                self.ui_single_file_upload.file_path.setText(str(self.current_file_path))

                self.createNewUploadThread()
                self.ui_single_file_upload.file_path.setDisabled(True)
                self.upload_started = True


        return True


    def insert_selected_to_files_queue_table(self):
        row_data = {}
        row_data["file_path"] = str(self.ui_single_file_upload.file_path.text())
        if row_data["file_path"] != "":
            self.add_row_files_queue_table(row_data)

        return True

    def eventFilter(self, object, event):
        if object is self.ui_single_file_upload.file_path:
            if event.type() == QtCore.QEvent.DragEnter:
                if event.mimeData().hasUrls():
                    event.accept()  # must accept the dragEnterEvent or else the dropEvent can't occur !!!
                    print "accept"
                else:
                    event.ignore()
                    print "ignore"
            if event.type() == QtCore.QEvent.Drop:
                if event.mimeData().hasUrls():  # if file or link is dropped
                    urlcount = len(event.mimeData().urls())  # count number of drops
                    url = event.mimeData().urls()[0]  # get first url
                    object.setText(url.toString())  # assign first url to editline
                    # event.accept()  # doesnt appear to be needed
            return False  # lets the event continue to the edit
        return False

    def normalize_file_path(self):
        current_recent_file_path = str(self.ui_single_file_upload.file_path.text())
        current_recent_file_path = current_recent_file_path.replace('file:/', '')
        self.ui_single_file_upload.file_path.setText(current_recent_file_path)
        return True

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
        else:
            event.ignore()

    def dropEvent(self, event):
        if event.mimeData().hasUrls:
            event.setDropAction(QtCore.Qt.CopyAction)
            event.accept()
            paths = []
            for path in event.mimeData().urls():
                paths.append(str(path.toLocalFile()))
            self.emit(QtCore.SIGNAL("droppedFileToTable"), paths)
        else:
            event.ignore()

    def resizeEvent(self, event):
        current_window_width = self.frameGeometry().width()
        if current_window_width < 980 and self.is_files_queue_table_visible:
            #self.is_files_queue_table_visible = False
            #self.ui_single_file_upload.files_list_view_bt.setPixmap(QtGui.QPixmap(":/resources/rarrow.png"))
            print "Closed"
        elif current_window_width > 980 and not self.is_files_queue_table_visible:
            #self.is_files_queue_table_visible = True
            #self.ui_single_file_upload.files_list_view_bt.setPixmap(QtGui.QPixmap(":/resources/larrow.jpg"))
            print "Opened"

    def keyPressEvent(self, e):
        # copy upload queue table content to clipboard #
        if (e.modifiers() & QtCore.Qt.ControlModifier):
            selected = self.ui_single_file_upload.shard_queue_table_widget.selectedRanges()

            if e.key() == QtCore.Qt.Key_C:  # copy
                s = ""

                for r in xrange(selected[0].topRow(), selected[0].bottomRow() + 1):
                    for c in xrange(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                        try:
                            s += str(self.ui_single_file_upload.shard_queue_table_widget.item(r, c).text()) + "\t"
                        except AttributeError:
                            s += "\t"
                    s = s[:-1] + "\n"  # eliminate last '\t'
                self.clip.setText(s)

    def append_dropped_files_to_table(self, paths):
        row_data = {}
        for url in paths:
            if os.path.exists(url):
                row_data["file_path"] = str(url)
                self.add_row_files_queue_table(row_data)
                if url != "":
                    self.ui_single_file_upload.file_path.setText("")
                self.ui_single_file_upload.file_path.setText(str(url))
                #print url
        return True


    def display_shards_queue_table_context_menu(self, position):
        tablemodel = self.ui_single_file_upload.shard_queue_table_widget.model()
        rows = sorted(set(index.row() for index in
                          self.ui_single_file_upload.shard_queue_table_widget.
                          selectedIndexes()))
        i = 0
        selected_row = 0
        any_row_selected = False
        for row in rows:
            any_row_selected = True
            node_index = tablemodel.index(row, 2)  # get nodeID
            # We suppose data are strings
            selected_node_addr = str(tablemodel.data(
                node_index).toString())
            selected_node_addr_parsed = selected_node_addr.split("/")
            selected_row = row
            i += 1

        if any_row_selected:
            menu = QtGui.QMenu()
            nodeDetailsAction = menu.addAction('Node details...')
            action = menu.exec_(self.ui_single_file_upload.shard_queue_table_widget.mapToGlobal(position))

            if action == nodeDetailsAction:
                self.node_details_window = NodeDetailsUI(self, selected_node_addr_parsed[1])
                self.node_details_window.show()
                print "Node details requested"


    def display_files_table_context_menu(self, position):
        tablemodel = self.ui_single_file_upload.files_queue_table_widget.model()
        rows = sorted(set(index.row() for index in
                          self.ui_single_file_upload.files_queue_table_widget.
                          selectedIndexes()))
        i = 0
        selected_row = 0
        any_row_selected = False
        for row in rows:
            any_row_selected = True
            filename_index = tablemodel.index(row, 0)  # get shard Index
            # We suppose data are strings
            self.current_selected_file_name = str(tablemodel.data(
                filename_index).toString())
            selected_row = row
            i += 1

        if any_row_selected:
            menu = QtGui.QMenu()
            fileDeleteFromTableAction = menu.addAction('Delete file from table')
            action = menu.exec_(self.ui_single_file_upload.files_queue_table_widget.mapToGlobal(position))

            if action == fileDeleteFromTableAction:
                # ask user and delete if sure
                msgBox = QtGui.QMessageBox(
                    QtGui.QMessageBox.Question,
                    'Question',
                    'Are you sure that you want to remove file '
                    '"%s" from upload queue?' %
                    str(self.current_selected_file_name),
                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

                result = msgBox.exec_()

                if result == QtGui.QMessageBox.Yes:
                    self.ui_single_file_upload.files_queue_table_widget.removeRow(int(selected_row))
                    print "Delete action"

    def shardUploadInitThread(self, shard, chapters, frame, file_name):
        shard_upload_init_thread = threading.Thread(
            target=self.createNewShardUploadThread(
                shard=shard,
                chapters=chapters,
                frame=frame,
                file_name=file_name
            ), args=())
        shard_upload_init_thread.start()


    def display_files_queue_change(self, x):
        self.animation = QtCore.QPropertyAnimation(self, "size")
        # self.animation.setDuration(1000) #Default 250ms

        if self.is_files_queue_table_visible:
            self.animation.setEndValue(QtCore.QSize(980, 611))
            self.is_files_queue_table_visible = False
            self.ui_single_file_upload.files_list_view_bt.setPixmap(QtGui.QPixmap(":/resources/rarrow.png"))
        else:
            self.animation.setEndValue(QtCore.QSize(1371, 611))
            self.is_files_queue_table_visible = True
            self.ui_single_file_upload.files_list_view_bt.setPixmap(QtGui.QPixmap(":/resources/larrow.jpg"))

        self.animation.start()


    def prepare_files_queue_table(self):
        self.files_queue_table_header = ['File name', 'Path', 'Size', 'Progress']
        self.ui_single_file_upload.files_queue_table_widget.setColumnCount(4)
        self.ui_single_file_upload.files_queue_table_widget.setRowCount(0)
        horHeaders = self.files_queue_table_header
        self.ui_single_file_upload.files_queue_table_widget.setHorizontalHeaderLabels(horHeaders)
        self.ui_single_file_upload.files_queue_table_widget.resizeColumnsToContents()
        self.ui_single_file_upload.files_queue_table_widget.resizeRowsToContents()
        self.ui_single_file_upload.files_queue_table_widget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

    def set_shard_size(self, shard_size):
        self.ui_single_file_upload.shardsize.setText(str(self.tools.human_size(int(shard_size))))

    def handle_cancel_action(self):
        if self.is_upload_active:
            msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Question, "Question",
                                       "Are you sure that you want cancel upload and close this window?",
                                       (QtGui.QMessageBox.Yes | QtGui.QMessageBox.No))
            result = msgBox.exec_()
            if result == QtGui.QMessageBox.Yes:
                self.close()
        else:
            self.close()


    def add_row_files_queue_table(self, row_data):


        self.files_queue_progressbar_list.append(QtGui.QProgressBar())

        self.files_queue_table_row_count = self.ui_single_file_upload.files_queue_table_widget.rowCount()

        self.ui_single_file_upload.files_queue_table_widget.setRowCount(
            self.files_queue_table_row_count + 1)

        self.ui_single_file_upload.files_queue_table_widget.setItem(
            self.files_queue_table_row_count, 0, QtGui.QTableWidgetItem(os.path.split(str(row_data['file_path']))[1]))
        self.ui_single_file_upload.files_queue_table_widget.setItem(
            self.files_queue_table_row_count, 1, QtGui.QTableWidgetItem(row_data['file_path']))

        self.ui_single_file_upload.files_queue_table_widget.setItem(
            self.files_queue_table_row_count, 2, QtGui.QTableWidgetItem(str(self.tools.human_size(os.path.getsize(str(row_data['file_path']))))))

        self.ui_single_file_upload.files_queue_table_widget.setCellWidget(
            self.files_queue_table_row_count, 3, self.files_queue_progressbar_list[self.files_queue_table_row_count])



    def show_upload_finished_message(self):
        self.is_upload_active = False
        self.ui_single_file_upload.connections_onetime.setEnabled(True)
        self.ui_single_file_upload.start_upload_bt.setStyleSheet(("QPushButton:hover{\n"
                                                                  "  background-color: #83bf20;\n"
                                                                  "  border-color: #83bf20;\n"
                                                                  "}\n"
                                                                  "QPushButton:active {\n"
                                                                  "  background-color: #93cc36;\n"
                                                                  "  border-color: #93cc36;\n"
                                                                  "}\n"
                                                                  "QPushButton{\n"
                                                                  "  background-color: #88c425;\n"
                                                                  "    border: 1px solid #88c425;\n"
                                                                  "    color: #fff;\n"
                                                                  "    border-radius: 7px;\n"
                                                                  "}"))

        self.ui_single_file_upload.start_upload_bt.setEnabled(True)
        self.ui_single_file_upload.file_path.setText("")
        QMessageBox.information(self, 'Success!', 'File uploaded successfully!')

    def refresh_overall_progress(self, base_percent):
        """
        """
        total_percent_to_upload = self.all_shards_count * 100
        total_percent_uploaded = sum(self.shard_upload_percent_list) * 100
        actual_percent_uploaded = total_percent_uploaded / total_percent_to_upload
        total_percent = (base_percent * 100) + (0.90 * actual_percent_uploaded)

        if int(total_percent) >= 100:
            self.ui_single_file_upload.overall_progress.setValue(int(99))
        else:
            self.ui_single_file_upload.overall_progress.setValue(int(total_percent))

    def set_current_active_connections(self):
        self.ui_single_file_upload.current_active_connections.setText(str(self.current_active_connections))

    def update_shards_counters(self):
        self.ui_single_file_upload.uploaded_shards.setText(str(self.shards_already_uploaded) + "/" + str(self.all_shards_count))

    def update_shard_upload_progess(self, row_position_index, value):
        #print str(row_position_index) +  "pozycja"
        self.upload_queue_progressbar_list[row_position_index].setValue(value)
        return 1

    def update_upload_task_state(self, row_position, state):
        self.ui_single_file_upload.shard_queue_table_widget.setItem(int(row_position), 3,
                                                                    QtGui.QTableWidgetItem(str(state)))

    def show_error_not_selected_file(self):
        QMessageBox.about(self, 'Error', 'Please select file which you want to upload!')

    def show_error_invalid_file_path(self):
        QMessageBox.about(self, 'Error', 'File path seems to be invalid!')

    def show_error_invalid_temporary_path(self):
        QMessageBox.about(self, 'Error', 'Temporary path seems to be invalid!')

    def createBucketResolveThread(self):
        bucket_resolve_thread = threading.Thread(target=self.initialize_buckets_select_list, args=())
        bucket_resolve_thread.start()

    def initialize_buckets_select_list(self):
        """Get all the buckets in which it is possible to store files, and
        show the names in the dropdown list"""
        self.__logger.debug('Buckets')
        self.__logger.debug('Resolving buckets from Bridge to buckets combobox...')

        self.buckets_list = []
        self.bucket_id_list = []
        self.bucket_id_name_2D_list = []
        self.storj_engine = StorjEngine()
        try:
            for bucket in self.storj_engine.storj_client.bucket_list():
                self.bucket_id_name_2D_list.append([str(bucket.id), str(bucket.name).decode('utf8')])  # append buckets to list

            if BUCKETS_LIST_SORTING_ENABLED:
                self.bucket_id_name_2D_list = sorted(self.bucket_id_name_2D_list, key=lambda x: x[1], reverse=False)

            for arr_data in self.bucket_id_name_2D_list:
                self.buckets_list.append(arr_data[1])
                self.bucket_id_list.append(arr_data[0])
        except storj.exception.StorjBridgeApiError as e:
            self.__logger.error(e)
            QMessageBox.about(
                self,
                'Unhandled bucket resolving exception',
                'Exception: %s' % e)

        self.ui_single_file_upload.save_to_bucket_select.addItems(self.buckets_list)

        if APPLY_SELECTED_BUCKET_TO_UPLOADER:
            self.ui_single_file_upload.save_to_bucket_select.setCurrentIndex(int(self.dashboard_instance.current_bucket_index))

    def increment_shards_progress_counters(self):
        # self.shards_already_uploaded += 1
        # self.ui_single_file_upload.shards_uploaded.setText(
        #   html_format_begin + str(self.shards_already_uploaded) + html_format_end)
        return 1

    def add_row_upload_queue_table(self, row_data):
        self.upload_queue_progressbar_list.append(QtGui.QProgressBar())

        self.upload_queue_table_row_count = self.ui_single_file_upload.shard_queue_table_widget.rowCount()

        self.ui_single_file_upload.shard_queue_table_widget.setRowCount(
            self.upload_queue_table_row_count + 1)
        self.ui_single_file_upload.shard_queue_table_widget.setCellWidget(
            self.upload_queue_table_row_count, 0, self.upload_queue_progressbar_list[self.upload_queue_table_row_count])
        self.ui_single_file_upload.shard_queue_table_widget.setItem(
            self.upload_queue_table_row_count, 1, QtGui.QTableWidgetItem(row_data['hash']))
        self.ui_single_file_upload.shard_queue_table_widget.setItem(
            self.upload_queue_table_row_count, 2, QtGui.QTableWidgetItem(
                '%s:%d' % (row_data['farmer_address'], row_data['farmer_port']) + "/" + row_data['farmer_id']))
        self.ui_single_file_upload.shard_queue_table_widget.setItem(
            self.upload_queue_table_row_count, 3, QtGui.QTableWidgetItem(
                str(row_data['state'])))
        self.ui_single_file_upload.shard_queue_table_widget.setItem(
            self.upload_queue_table_row_count, 4, QtGui.QTableWidgetItem(
                str(row_data['token'])))
        self.ui_single_file_upload.shard_queue_table_widget.setItem(
            self.upload_queue_table_row_count, 5, QtGui.QTableWidgetItem(
                str(row_data['shard_index'])))

        if AUTO_SCROLL_UPLOAD_DOWNLOAD_QUEUE:
            self.ui_single_file_upload.shard_queue_table_widget.scrollToBottom()

        self.upload_queue_progressbar_list[self.upload_queue_table_row_count].setValue(0)

        self.__logger.info(row_data)

    def select_tmp_directory(self):
        self.selected_tmp_dir = QtGui.QFileDialog.getExistingDirectory(
            None,
            'Select a folder:',
            self.temp_dir,
            QtGui.QFileDialog.ShowDirsOnly)
        self.__logger.debug('Chosen temp dir: %s', self.selected_tmp_dir)
        self.ui_single_file_upload.tmp_path.setText(str(self.selected_tmp_dir).decode('utf-8'))

    def select_file_path(self):
        self.ui_single_file_upload.file_path.setText(str(QtGui.QFileDialog.getOpenFileName()).decode('utf-8'))

    def createNewUploadThread(self):
        # self.download_thread = DownloadTaskQtThread(url, filelocation, options_chain, progress_bars_list)
        # self.download_thread.start()
        # self.download_thread.connect(self.download_thread, QtCore.SIGNAL('setStatus'), self.test1, Qt.QueuedConnection)
        # self.download_thread.tick.connect(progress_bars_list.setValue)
        # Refactor to QtTrhead

        #upload_thread = multiprocessing.Process(target=self.file_upload_begin, args=())
        upload_thread = threading.Thread(target=self.file_upload_begin, args=())
        upload_thread.start()

    def initialize_upload_queue_table(self):

        # initialize variables
        self.shards_already_uploaded = 0
        self.uploaded_shards_count = 0
        self.upload_queue_progressbar_list = []

        self.upload_queue_table_header = ['Progress', 'Hash', 'Farmer', 'State', 'Token', 'Shard index']
        self.ui_single_file_upload.shard_queue_table_widget.setColumnCount(6)
        self.ui_single_file_upload.shard_queue_table_widget.setRowCount(0)
        horHeaders = self.upload_queue_table_header
        self.ui_single_file_upload.shard_queue_table_widget.setHorizontalHeaderLabels(horHeaders)
        self.ui_single_file_upload.shard_queue_table_widget.resizeColumnsToContents()
        self.ui_single_file_upload.shard_queue_table_widget.resizeRowsToContents()

        self.ui_single_file_upload.shard_queue_table_widget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

    def set_current_status(self, current_status):
        self.ui_single_file_upload.current_state.setText(html_format_begin + current_status + html_format_end)

    def createNewShardUploadThread(self, shard, chapters, frame, file_name):
        # another worker thread for single shard uploading and it will retry if download fail

        #pool = multiprocessing.Pool()

        print "starting thread for shard"
        # upload_thread = multiprocessing.Process(
        # upload_thread = pool.apply_async(
        upload_thread = threading.Thread(
            self.upload_shard(
                shard=shard,
                chapters=chapters,
                frame=frame,
                file_name_ready_to_shard_upload=file_name
            ), args=())
        #pool.close()
        #pool.join()
        upload_thread.start()
        print "zakonczono"

    def _add_shard_to_table(self, frame_content, shard, chapters):
        """
        Add a row to the shard table and return the row number
        """
        # Add items to shard queue table view
        tablerowdata = {}
        tablerowdata['farmer_address'] = frame_content['farmer']['address']
        tablerowdata['farmer_port'] = frame_content['farmer']['port']
        tablerowdata['farmer_id'] = frame_content['farmer']['nodeID']
        tablerowdata['hash'] = str(shard.hash)
        tablerowdata['state'] = 'Uploading...'
        tablerowdata['token'] = frame_content['token']
        tablerowdata['shard_index'] = str(chapters)

        # self.__logger.warning('"log_event_type": "debug"')
        self.__logger.debug('"title": "Contract negotiated"')
        self.__logger.debug('"description": "Storage contract negotiated \
                     with: "' +
                            str(frame_content["farmer"]["address"]) + ":" +
                            str(frame_content["farmer"]["port"]))
        self.ongoing_bridge_requests -= 1

        # add row to table
        self.emit(QtCore.SIGNAL('addRowToUploadQueueTable'), tablerowdata)
        self.emit(QtCore.SIGNAL('updateOngoingBridgeRequests'))

        rowcount = self.ui_single_file_upload.shard_queue_table_widget.rowCount()
        return rowcount

    def _read_in_chunks(self, file_object, shard_size, rowposition, blocksize=1024, chunks=-1, shard_index=None):
        """Lazy function (generator) to read a file piece by piece.
        Default chunk size: 1k."""
        # chunk number (first is 0)
        i = 0
        while chunks:
            data = file_object.read(blocksize)
            if not data:
                break
            yield data
            i += 1
            t1 = float(shard_size) / float(blocksize)
            if shard_size <= blocksize:
                t1 = 1

            percent_uploaded = int(round((100.0 * i) / t1))

            # self.__logger.debug(i)
            chunks -= 1

            # update progress bar in upload queue table
            self.emit(QtCore.SIGNAL("updateShardUploadProgress"), int(rowposition), percent_uploaded)
            self.shard_upload_percent_list[shard_index] = percent_uploaded
            self.emit(QtCore.SIGNAL("refreshOverallProgress"), 0.1)  # update overall progress bar

    def upload_shard(self, shard, chapters, frame, file_name_ready_to_shard_upload):

        self.semaphore.acquire()

        contract_negotiation_tries = 0

        print self.already_used_farmers_nodes

        while MAX_RETRIES_NEGOTIATE_CONTRACT > contract_negotiation_tries:
            contract_negotiation_tries += 1
            exchange_report = storj.model.ExchangeReport()

            # emit signal to add row to upload queue table
            # self.emit(QtCore.SIGNAL("addRowToUploadQueueTable"), "important", "information")

            self.__logger.debug('Negotiating contract')
            self.__logger.debug('Trying to negotiate storage contract for \
shard at index %s' % chapters)
            if contract_negotiation_tries > 1:
                self.emit(
                    QtCore.SIGNAL('setCurrentUploadState'),
                    'Trying to negotiate storage contract for shard at index %s... Retry %s... ' % (
                        str(chapters), contract_negotiation_tries))
                self.ongoing_bridge_requests += 1
                self.emit(QtCore.SIGNAL('updateOngoingBridgeRequests'))
            else:
                self.emit(
                    QtCore.SIGNAL('setCurrentUploadState'),
                    'Trying to negotiate storage contract for shard at index %s...' % str(chapters))
                self.ongoing_bridge_requests += 1
                self.emit(QtCore.SIGNAL('updateOngoingBridgeRequests'))

            try:
                if FARMER_NODES_EXCLUSION_FOR_UPLOAD_ENABLED:
                    frame_content = self.storj_engine.storj_client.frame_add_shard(
                        shard, frame.id, excludes=self.already_used_farmers_nodes)
                else:
                    frame_content = self.storj_engine.storj_client.frame_add_shard(shard, frame.id)
                # Add a row to the table
                rowposition = self._add_shard_to_table(
                    frame_content,
                    shard,
                    chapters)

                rowposition = self.current_row
                self.current_row += 1

                self.__logger.debug('-' * 30)
                self.__logger.debug(frame_content['farmer']['address'])

                farmerNodeID = frame_content['farmer']['nodeID']

                if BLACKLISTING_MODE == 1:
                    self.already_used_farmers_nodes.append(farmerNodeID)  # add item to array of already used farmers nodes

                url = 'http://' + frame_content['farmer']['address'] + ':' + \
                      str(frame_content['farmer']['port']) + '/shards/' + \
                      frame_content['hash'] + '?token=' + \
                      frame_content['token']
                self.__logger.debug('URL: %s', url)

                self.__logger.debug('-' * 30)

                # files = {'file': open(file_path + '.part%s' % chapters)}
                # headers = {'content-type: application/octet-stream', 'x-storj-node-id: ' + str(farmerNodeID)}

                self.emit(
                    QtCore.SIGNAL('setCurrentUploadState'),
                    'Uploading shard %s to farmer...' % str(chapters + 1))

                self.emit(QtCore.SIGNAL("setCurrentUploadState"),
                          'Uploading shard %s to farmer...' % str(chapters + 1))

                # begin recording exchange report

                current_timestamp = int(time.time())

                exchange_report.exchangeStart = str(current_timestamp)
                exchange_report.farmerId = str(farmerNodeID)
                exchange_report.dataHash = str(shard.hash)

                shard_size = int(shard.size)

                farmer_tries = 0
                response = None
                success_shard_upload = False

                while MAX_RETRIES_UPLOAD_TO_SAME_FARMER > farmer_tries:
                    farmer_tries += 1
                    try:
                        self.__logger.debug(
                            'Upload shard at index ' +
                            str(shard.index) + ' to ' +
                            str(frame_content['farmer']['address']) +
                            ':' +
                            str(frame_content['farmer']['port']))

                        mypath = os.path.join(self.tmp_path,
                                              file_name_ready_to_shard_upload +
                                              '-' + str(chapters + 1))

                        self.current_active_connections += 1
                        self.emit(QtCore.SIGNAL('setCurrentActiveConnections'))
                        with open(mypath, 'rb') as f:
                            response = requests.post(
                                url,
                                data=self._read_in_chunks(
                                    f,
                                    shard_size,
                                    rowposition,
                                    shard_index=chapters
                                ),
                                timeout=1)

                        j = json.loads(str(response.content))
                        if j.get('result') == 'The supplied token is not accepted':
                            raise storj.exception.StorjFarmerError(
                                storj.exception.SuppliedTokenNotAcceptedError)

                        if response.status_code != 200 and response.status_code != 304:
                            raise storj.exception.StorjFarmerError(
                                77)  # Raise general farmer failure

                        success_shard_upload = True

                    except storj.exception.StorjFarmerError as e:
                        print str(e)
                        self.__logger.error(e)
                        self.current_active_connections -= 1
                        self.emit(QtCore.SIGNAL('setCurrentActiveConnections'))

                        # upload failed due to Farmer Failure
                        if e.code == 10002:
                            self.__logger.error('The supplied token not accepted')
                        continue

                    except Exception as e:
                        print str(e)
                        self.__logger.error(e)
                        self.current_active_connections -= 1
                        self.emit(QtCore.SIGNAL('setCurrentActiveConnections'))

                        # update shard upload state
                        self.emit(
                            QtCore.SIGNAL('updateUploadTaskState'),
                            rowposition,
                            'First try failed. Retrying... (' + str(farmer_tries) + ')')

                        self.emit(QtCore.SIGNAL("setCurrentUploadState"),
                                  'First try failed. Retrying... (' + str(farmer_tries) + ')')

                        self.__logger.warning('Shard upload error')
                        self.__logger.warning('Error while uploading shard to:\
                                %s:%s. Retrying... (%s)' % (
                            frame_content["farmer"]["address"],
                            frame_content["farmer"]["port"],
                            farmer_tries))
                        continue

                    else:
                        # update progress bar in upload queue table
                        percent_uploaded = 100
                        self.emit(QtCore.SIGNAL("updateShardUploadProgress"), int(rowposition), percent_uploaded)
                        self.shard_upload_percent_list[chapters] = percent_uploaded
                        self.emit(QtCore.SIGNAL("refreshOverallProgress"), 0.1)  # update overall progress bar
                        self.current_active_connections -= 1
                        self.emit(QtCore.SIGNAL('setCurrentActiveConnections'))
                        self.emit(
                            # update already uploaded shards count
                            QtCore.SIGNAL('incrementShardsProgressCounters'))
                        self.shards_already_uploaded += 1

                        # update already uploaded shards count
                        self.emit(QtCore.SIGNAL('updateShardUploadCounters'))
                        self.__logger.debug(
                            'Shard uploaded successfully to %s:%s' % (
                                frame_content["farmer"]["address"],
                                frame_content["farmer"]["port"]))

                        self.emit(QtCore.SIGNAL("updateUploadTaskState"), rowposition,
                                  "Uploaded!")  # update shard upload state

                        self.__logger.debug('%s shards, %s sent' %
                                            (self.all_shards_count,
                                             self.shards_already_uploaded))

                        if int(self.all_shards_count) <= int(self.shards_already_uploaded):
                            # send signal to save to bucket after all files are uploaded
                            self.emit(
                                QtCore.SIGNAL('finishUpload'))
                        break

                if not success_shard_upload:
                    if BLACKLISTING_MODE == 2:
                        self.already_used_farmers_nodes.append(
                            farmerNodeID)  # Add item to array of already used farmers nodes
                    # Update shard upload state
                    self.emit(
                        QtCore.SIGNAL('updateUploadTaskState'),
                        rowposition,
                        'Failed. Trying to upload to another farmer...')

                self.__logger.debug(response.content)

                j = json.loads(str(response.content))
                if j.get('result') == 'The supplied token is not accepted':
                    farmer_error_class = storj.exception.FarmerError(10002)
                    SUPPLIED_TOKEN_NOT_ACCEPTED_ERROR = farmer_error_class.SUPPLIED_TOKEN_NOT_ACCEPTED
                    raise storj.exception.StorjFarmerError(
                        storj.exception.SuppliedTokenNotAcceptedError)

            except storj.exception.StorjBridgeApiError as e:
                print str(e)
                self.__logger.error(e)

                # upload failed due to Storj Bridge failure
                self.__logger.error('Exception raised while trying to negotiate contract')
                self.__logger.error('Bridge exception')
                self.__logger.error('Exception raised while trying \
to negotiate storage contract for shard at index %s' % chapters)
                self.ongoing_bridge_requests -= 1
                self.emit(QtCore.SIGNAL('updateOngoingBridgeRequests'))
                continue

            except Exception as e:
                print str(e)
                self.__logger.error(e)

                # now send Exchange Report
                # upload failed probably while sending data to farmer
                self.__logger.error('Error occured while trying to upload shard or negotiate contract. Retrying... ')

                self.__logger.error('Unhandled exception')
                self.__logger.error('Unhandled exception occured while trying \
to upload shard or negotiate contract for shard at index %s. Retrying...' % str(chapters))
                current_timestamp = int(time.time())

                exchange_report.exchangeEnd = str(current_timestamp)
                exchange_report.exchangeResultCode = exchange_report.FAILURE
                exchange_report.exchangeResultMessage = exchange_report.STORJ_REPORT_UPLOAD_ERROR

                self.emit(
                    QtCore.SIGNAL('setCurrentUploadState'),
                    'Sending Exchange Report for shard %s' % str(chapters + 1))
                # self.storj_engine.storj_client.send_exchange_report(exchange_report) # send exchange report
                self.ongoing_bridge_requests -= 1
                self.emit(QtCore.SIGNAL('updateOngoingBridgeRequests'))
                continue

            # uploaded with success
            current_timestamp = int(time.time())
            # prepare second half of exchange heport
            exchange_report.exchangeEnd = str(current_timestamp)
            exchange_report.exchangeResultCode = exchange_report.SUCCESS
            exchange_report.exchangeResultMessage = exchange_report.STORJ_REPORT_SHARD_UPLOADED
            self.emit(QtCore.SIGNAL("setCurrentUploadState"),
                      "Sending Exchange Report for shard " + str(chapters + 1))
            self.__logger.info("Shard " + str(chapters + 1) +
                               " successfully added and exchange report sent.")
            # self.storj_engine.storj_client.send_exchange_report(exchange_report) # send exchange report
            # Release the semaphore when the download is finished
            self.semaphore.release()
            break

    def finish_upload(self, bname, bucket_id):
        self.crypto_tools = CryptoTools()
        self.__logger.debug('HMAC')
        self.__logger.debug('Generating HMAC...')
        hash_sha512_hmac_b64 = self.crypto_tools.prepare_bucket_entry_hmac(self.shard_manager_result.shards)
        hash_sha512_hmac = hashlib.sha224(str(hash_sha512_hmac_b64["SHA-512"])).hexdigest()
        self.__logger.debug(hash_sha512_hmac)
        # save

        # import magic
        # mime = magic.Magic(mime=True)
        # mime.from_file(file_path)

        self.__logger.debug(self.frame.id)
        self.__logger.debug("Now upload file")

        data = {
            'x-token': self.push_token.id,
            'x-filesize': str(self.uploaded_file_size),
            'frame': self.frame.id,
            'mimetype': self.file_mime_type,
            'filename': str(bname) + str(self.fileisdecrypted_str),
            'hmac': {
                'type': "sha512",
                # 'value': hash_sha512_hmac["sha512_checksum"]
                'value': hash_sha512_hmac
            },
        }

        self.__logger.debug('Finishing upload')
        self.__logger.debug('Adding file %s to bucket...' % str(bname))
        self.emit(QtCore.SIGNAL("setCurrentUploadState"), "Adding file to bucket...")

        success = False
        try:
            response = self.storj_engine.storj_client._request(
                method='POST', path='/buckets/%s/files' % bucket_id,
                # files={'file' : file},
                headers={
                    'x-token': self.push_token.id,
                    'x-filesize': str(self.uploaded_file_size),
                },
                json=data,
            )
            success = True
        except storj.exception.StorjBridgeApiError as e:
            QMessageBox.about(self, "Unhandled bridge exception", "Exception: " + str(e))
        if success:
            self.__logger.debug('"title": "File uploaded"')
            self.__logger.debug('"description": "File uploaded successfully!"')
            #self.emit(QtCore.SIGNAL("showFileUploadedSuccessfully"))
            self.files_already_uploaded += 1
            self.emit(QtCore.SIGNAL("checkNextFilesToUpload"))

            self.emit(QtCore.SIGNAL("setCurrentUploadState"), "File uploaded successfully!")
            self.dashboard_instance.createNewFileListUpdateThread()

    def file_upload_begin(self):

        self.semaphore = threading.BoundedSemaphore(
            int(self.ui_single_file_upload.connections_onetime.value()))

        self.emit(QtCore.SIGNAL("setOverallProgress"), 0)
        #self.ui_single_file_upload.overall_progress.setValue(0)

        file_path = None
        self.validation = {}

        self.emit(QtCore.SIGNAL("initializeUploadQueueTable"))
        #self.initialize_upload_queue_table()

        encryption_enabled = True

        # get temporary files path
        self.tmp_path = str(self.ui_single_file_upload.tmp_path.text())
        self.__logger.debug('Temporary path chosen: %s' % self.tmp_path)


        # TODO: redundant lines?
        # get temporary files path
        if self.ui_single_file_upload.file_path.text() == "":
            self.tmp_path = "/tmp"
            self.validation["file_path"] = False
            self.emit(QtCore.SIGNAL("showFileNotSelectedError"))  # show error missing file path
            self.__logger.error("temporary path missing")
        else:
            self.tmp_path = str(self.ui_single_file_upload.tmp_path.text())
            self.validation["file_path"] = True
            file_path = str(self.ui_single_file_upload.file_path.text()).decode('utf-8')

        if self.validation["file_path"]:

            try:
                self.current_bucket_index = self.ui_single_file_upload.save_to_bucket_select.currentIndex()
                self.current_selected_bucket_id = self.bucket_id_list[self.current_bucket_index]
            except:
                print "Error"

            bucket_id = str(self.current_selected_bucket_id)


            bname = os.path.split(file_path)[1]  # File name

            self.__logger.debug(bname + "npliku")

            # Temporary replace magic with mimetypes python library
            if mimetypes.guess_type(file_path)[0] is not None:
                file_mime_type = mimetypes.guess_type(file_path)[0]
            else:
                file_mime_type = "text/plain"

            file_mime_type = "text/plain"

            # mime = magic.Magic(mime=True)
            # file_mime_type = str(mime.from_file(file_path))

            self.__logger.debug(file_mime_type)
            # file_mime_type = str("A")

            file_existence_in_bucket = False

            # if self.configuration.sameFileNamePrompt or self.configuration.sameFileHashPrompt:
            # file_existence_in_bucket =
            # self.storj_engine.storj_client.check_file_existence_in_bucket(bucket_id=bucket_id,
            # filepath=file_path) # check if exist file with same file name

            if file_existence_in_bucket == 1:
                # QInputDialog.getText(self, 'Warning!', 'File with name ' + str(bname) + " already exist in bucket! Please use different name:", "test" )
                self.__logger.warning("Same file exist!")

            self.fileisdecrypted_str = ""
            if self.ui_single_file_upload.encrypt_files_checkbox.isChecked():
                # encrypt file
                self.emit(QtCore.SIGNAL("setCurrentUploadState"), "Encrypting file...")
                # self.__logger.warning('"log_event_type": "debug"')
                self.__logger.debug('"title": "Encryption"')
                self.__logger.debug('"description": "Encrypting file..."')

                file_crypto_tools = FileCrypto()
                # Path where to save the encrypted file in temp dir
                file_path_ready = os.path.join(self.tmp_path,
                                               '%s.encrypted' % bname)
                self.__logger.debug('Call encryption method')
                # begin file encryption
                file_crypto_tools.encrypt_file(
                    "AES",
                    file_path,
                    file_path_ready,
                    self.storj_engine.account_manager.get_user_password())
                file_name_ready_to_shard_upload = bname + ".encrypted"
                self.fileisdecrypted_str = ""
            else:
                self.fileisdecrypted_str = "[DECRYPTED]"
                file_path_ready = file_path
                file_name_ready_to_shard_upload = bname

            self.__logger.debug('Temp path: %s' % self.tmp_path)
            self.__logger.debug(file_path_ready + "sciezka2")

            def get_size(file_like_object):
                return os.stat(file_like_object.name).st_size

            # file_size = get_size(file)

            file_size = os.stat(file_path).st_size
            self.uploaded_file_size = file_size
            self.file_mime_type = file_mime_type


            self.emit(QtCore.SIGNAL("paintFileSize"), str(self.tools.human_size(int(file_size))))

            #self.ui_single_file_upload.file_size.setText(str(self.tools.human_size(int(file_size))))

            self.is_upload_active = True
            self.emit(QtCore.SIGNAL("disableButtonsForUpload"))


            self.__logger.debug('PUSH token')

            self.emit(QtCore.SIGNAL("setCurrentUploadState"), "Resolving PUSH Token for upload...")
            self.__logger.debug('Resolving PUSH Token for upload...')

            push_token = None
            PUSH_token_resolve_retries = 0

            while PUSH_token_resolve_retries < MAX_RETRIES_TOKEN_RESOLVING:
                try:
                    PUSH_token_resolve_retries += 1
                    # Get the PUSH token from Storj Bridge
                    push_token = self.storj_engine.storj_client.token_create(bucket_id,
                                                                             'PUSH')
                    self.push_token = push_token
                except storj.exception.StorjBridgeApiError as e:
                    self.is_upload_active = False
                    QMessageBox.about(self, "Unhandled PUSH token create exception", "Exception: " + str(e))
                else:
                    break

            self.emit(QtCore.SIGNAL("paintPUSHToken"), str(push_token.id))
            #self.ui_single_file_upload.push_token.setText(
             #   str(push_token.id))  # set the PUSH Token

            self.__logger.debug("PUSH Token ID: " + push_token.id)

            self.__logger.debug('Frame')
            self.emit(QtCore.SIGNAL("setCurrentUploadState"), "RResolving frame for file upload...")
            self.__logger.debug('Resolving frame for file upload...')

            frame = None  # initialize variable
            try:
                frame = self.storj_engine.storj_client.frame_create()  # Create file frame
                self.frame = frame
            except storj.exception.StorjBridgeApiError as e:
                self.is_upload_active = False
                QMessageBox.about(
                    self,
                    'Unhandled exception while creating file staging frame',
                    'Exception: %s' % e)
                self.__logger.debug('"title": "Frame"')
                self.__logger.debug('"description": "Error while resolving frame for\
                    file upload..."')

            self.emit(QtCore.SIGNAL("paintFrame"), str(frame.id))
            #self.ui_single_file_upload.file_frame_id.setText(str(frame.id))

            self.__logger.debug('Frame ID: %s', frame.id)
            # Now encrypt file
            self.__logger.debug('%s sciezka', file_path_ready)

            # Now generate shards
            self.emit(QtCore.SIGNAL('setCurrentUploadState'), 'Splitting file to shards...')
            self.__logger.debug('Sharding')
            self.__logger.debug('Splitting file to shards...')

            max_shard_size_setting = self.tools.generate_max_shard_size(
                max_shard_size_input=self.ui_single_file_upload.max_shard_size.value(),
                shard_size_unit=int(self.ui_single_file_upload.shard_size_unit.currentIndex()))
            print str(max_shard_size_setting) + " max shard size"
            shards_manager = storj.model.ShardManager(filepath=file_path_ready,
                                                      tmp_path=self.tmp_path,
                                                      max_shard_size=int(max_shard_size_setting)/2)
            self.all_shards_count = len(shards_manager.shards)
            self.emit(QtCore.SIGNAL("updateShardUploadCounters"))

            self.shard_manager_result = shards_manager
            # self.ui_single_file_upload.current_state.setText(
            #   html_format_begin + "Generating shards..." + html_format_end)
            # shards_manager._make_shards()
            #shards_count = shards_manager.num_chunks # fix because new version of sdk
            shards_count = self.all_shards_count
            # create file hash
            self.__logger.debug('file_upload() push_token=%s', push_token)

            # upload shards to frame
            self.__logger.debug('Shards count %s' % shards_count)

            # set shards count
            self.all_shards_count = shards_count

            chapters = 0

            for shard in shards_manager.shards:
                #self.upload_queue_progressbar_list.append(QtGui.QProgressBar())
                self.emit(QtCore.SIGNAL("setShardSize"), int(shard.size))

                self.shard_upload_percent_list.append(0)
                #self.emit(QtCore.SIGNAL("createShardUploadThread"), shard, chapters, frame, file_name_ready_to_shard_upload)
                #self.emit(QtCore.SIGNAL("_createShardUploadThread"), shard, chapters, frame, file_name_ready_to_shard_upload)
                #self.createNewShardUploadThread(shard, chapters, frame, file_name_ready_to_shard_upload)
                #self.createNewShardUploadThread(shard, chapters, frame, file_name_ready_to_shard_upload)
                #print "wysylanie sharda..." + str(shard.index)
                #chapters += 1
                #time.sleep(1)

            threads = [threading.Thread(
                target=self.upload_shard,
                args=(shard,
                      int(shard.index),
                      frame,
                      file_name_ready_to_shard_upload)) for shard in shards_manager.shards]
            self.current_line = 0
            for t in threads:
                #self.shards_already_uploaded += 1
                #row_lock.acquire()
                print "starting thread..."
                t.start()
                self.current_line += 1
                #row_lock.release()
                time.sleep(CONTRACT_NEGOTIATION_ITERATION_DELAY)

            for t in threads:
                t.join()






                # delete encrypted file TODO

                # self.emit(QtCore.SIGNAL("finishUpload")) # send signal to save to bucket after all filea are uploaded

                # finish_upload(self)
