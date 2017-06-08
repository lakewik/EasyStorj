# -*- coding: utf-8 -*-

from sys import platform

import os

import logging
import json
import requests
import storj
import storj.exception
import threading
import time

from functools import partial
from PyQt4 import QtCore, QtGui
from six.moves import queue as Queue

from .crypto.file_crypto_tools import FileCrypto
from .engine import StorjEngine
from .qt_interfaces.file_download_new import Ui_SingleFileDownload
from .resources.html_strings import html_format_begin, html_format_end
from .utilities.sharder import ShardingTools
from .utilities.tools import Tools
from .utilities.account_manager import AccountManager
from .resources.constants import USE_USER_ENV_PATH_FOR_TEMP, \
    MAX_DOWNLOAD_CONNECTIONS_AT_SAME_TIME, \
    ALLOW_DOWNLOAD_FARMER_POINTER_CANCEL_BY_USER, \
    FARMER_NODES_EXCLUSION_FOR_DOWNLOAD_ENABLED, \
    MAX_DOWNLOAD_REQUEST_BLOCK_SIZE, FILE_POINTERS_ITERATION_DELAY, \
    DEFAULT_MAX_FARMER_DOWNLOAD_READ_TIMEOUT, MAX_ALLOWED_DOWNLOAD_CONCURRENCY, \
    MAX_POINTERS_RESOLVED_IN_ONE_PART, GET_DEFAULT_TMP_PATH_FROM_ENV_VARIABLES, \
    GET_HOME_PATH_FROM_ENV_VARIABLES


queue = Queue.Queue()
row_lock = threading.Lock()

logging.basicConfig(
    level=logging.DEBUG,
    format='%(levelname)s %(message)s')


class SingleFileDownloadUI(QtGui.QMainWindow):

    __logger = logging.getLogger('%s.SingleFileDownloadUI' % __name__)

    def __init__(self, parent=None, bucketid=None, fileid=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui_single_file_download = Ui_SingleFileDownload()
        self.ui_single_file_download.setupUi(self)
        self.storj_engine = StorjEngine()  # init StorjEngine
        self.filename_from_bridge = ''
        self.tools = Tools()

        self.bucket_id = bucketid
        self.file_id = fileid

        self.ui_single_file_download.shard_queue_table.setContextMenuPolicy(
            QtCore.Qt.CustomContextMenu)

        self.ui_single_file_download.shard_queue_table.\
            customContextMenuRequested.connect(
                partial(self.display_table_context_menu))

        self.tools = Tools()

        self.is_upload_active = False

        self.account_manager = AccountManager()  # init AccountManager

        self.user_password = self.account_manager.get_user_password()

        # Open file select dialog
        QtCore.QObject.connect(self.ui_single_file_download.file_path_select_bt,
                               QtCore.SIGNAL('clicked()'),
                               self.select_file_save_path)
        # open tmp directory select dialog
        QtCore.QObject.connect(self.ui_single_file_download.tmp_dir_bt,
                               QtCore.SIGNAL('clicked()'),
                               self.select_tmp_directory)
        # open tmp directory select dialog
        QtCore.QObject.connect(self.ui_single_file_download.cancel_bt,
                               QtCore.SIGNAL('clicked()'),
                               self.handle_cancel_action)
        # begin file downloading process
        QtCore.QObject.connect(self.ui_single_file_download.start_download_bt,
                               QtCore.SIGNAL('clicked()'),
                               lambda: self.createNewDownloadInitThread(
                                   bucketid,
                                   fileid))

        self.connect(self,
                     QtCore.SIGNAL('incrementShardsDownloadProgressCounters'),
                     self.increment_shards_download_progress_counters)
        self.connect(self, QtCore.SIGNAL('updateShardDownloadProgress'),
                     self.update_shard_download_progess)
        self.connect(self, QtCore.SIGNAL('refreshOverallDownloadProgress'),
                     self.refresh_overall_download_progress)
        self.connect(self,
                     QtCore.SIGNAL('showDestinationFileNotSelectedError'),
                     self.show_error_not_selected_file)
        self.connect(self, QtCore.SIGNAL('showInvalidDestinationPathError'),
                     self.show_error_invalid_file_path)
        self.connect(self,
                     QtCore.SIGNAL('showInvalidTemporaryDownloadPathError'),
                     self.show_error_invalid_temporary_path)
        self.connect(self, QtCore.SIGNAL('updateDownloadTaskState'),
                     self.update_download_task_state)
        self.connect(self, QtCore.SIGNAL('showStorjBridgeException'),
                     self.show_storj_bridge_exception)
        self.connect(self, QtCore.SIGNAL('showUnhandledException'),
                     self.show_unhandled_exception)
        self.connect(self, QtCore.SIGNAL('showFileDownloadedSuccessfully'),
                     self.show_download_finished_message)
        self.connect(self, QtCore.SIGNAL('showException'),
                     self.show_unhandled_exception)
        self.connect(self, QtCore.SIGNAL('addRowToDownloadQueueTable'),
                     self.add_row_download_queue_table)
        self.connect(self, QtCore.SIGNAL('setCurrentState'),
                     self.set_current_status)
        self.connect(self, QtCore.SIGNAL('updateShardCounters'),
                     self.update_shards_counters)
        self.connect(self, QtCore.SIGNAL('retryWithNewDownloadPointer'),
                     self.retry_dl_thread)
        self.connect(self, QtCore.SIGNAL('showDestinationPathNotSelectedMsg'),
                     self.show_error_invalid_file_path)
        self.connect(self, QtCore.SIGNAL('selectFileDestinationPath'),
                     self.select_file_save_path)
        self.connect(self, QtCore.SIGNAL('askFileOverwrite'),
                     self.ask_overwrite)
        self.connect(self, QtCore.SIGNAL('setCurrentActiveConnections'),
                     self.set_current_active_connections)
        self.connect(self, QtCore.SIGNAL('finishDownload'),
                     lambda: self.finish_download(str(os.path.split(
                         str(self.ui_single_file_download.file_save_path.
                             text()))[1]).decode('utf-8')))

        self.overwrite_question_result = None
        self.overwrite_question_closed = False

        self.ui_single_file_download.current_state.\
            setText('Waiting for user action...')
        self.ui_single_file_download.downloaded_shards.\
            setText('Waiting for user...')
        self.shards_already_downloaded = 0

        self.createNewInitializationThread(bucketid, fileid)

        self.shard_download_percent_list = []

        # init limit variables
        self.max_retries_download_from_same_farmer = 3
        self.max_retries_get_file_pointers = 30

        self.semaphore = threading.BoundedSemaphore(
            MAX_DOWNLOAD_CONNECTIONS_AT_SAME_TIME)

        # user can set it manually default value from constants file
        self.ui_single_file_download.connections_onetime.setValue(
            int(MAX_DOWNLOAD_CONNECTIONS_AT_SAME_TIME))

        # set default paths
        temp_dir = ''
        if platform == 'linux' or platform == 'linux2':
            # linux
            if GET_DEFAULT_TMP_PATH_FROM_ENV_VARIABLES:
                try:
                    temp_dir = str(os.environ['TEMP'])
                except Exception as e:
                    temp_dir = '/tmp'
                    print str(e)
            else:
                temp_dir = '/tmp'

        elif platform == 'darwin':
            # OS X
            temp_dir = '/tmp'

        elif platform == 'win32':
            # Windows
            if USE_USER_ENV_PATH_FOR_TEMP:
                temp_dir = os.path.join(
                    self.tools.get_home_user_directory().decode('utf-8'),
                    'AppData', 'Local', 'Temp')
            elif GET_DEFAULT_TMP_PATH_FROM_ENV_VARIABLES:
                try:
                    temp_dir = str(os.environ['HOME'])
                except BaseException:
                    temp_dir = '/tmp'
            else:
                temp_dir = 'C:\\Windows\\temp'

        self.ui_single_file_download.tmp_dir.setText(temp_dir)

        # set config variables
        self.combine_tmpdir_name_with_token = False

        # set overall progress to 0
        self.ui_single_file_download.overall_progress.setValue(0)

        self.current_active_connections = 0

        self.already_started_shard_downloads_count = 0
        self.all_shards_count = 0

        self.another_farmer_manual_requests = []

        self.rowpositions_in_progress = []
        self.pointers_exclusions = [[]]

        self.ui_single_file_download.connections_onetime.setMaximum(MAX_ALLOWED_DOWNLOAD_CONCURRENCY)

        self.clip = QtGui.QApplication.clipboard()

    def keyPressEvent(self, e):
        # copy upload queue table content to clipboard #
        if (e.modifiers() & QtCore.Qt.ControlModifier):
            selected = self.ui_single_file_download.shard_queue_table.selectedRanges()

            if e.key() == QtCore.Qt.Key_C:  # copy
                s = ""

                for r in xrange(selected[0].topRow(), selected[0].bottomRow() + 1):
                    for c in xrange(selected[0].leftColumn(), selected[0].rightColumn() + 1):
                        try:
                            s += str(self.ui_single_file_download.shard_queue_table.item(r, c).text()) + "\t"
                        except AttributeError:
                            s += "\t"
                    s = s[:-1] + "\n"  # eliminate last '\t'
                self.clip.setText(s)


    def display_table_context_menu(self, position):
        tablemodel = self.ui_single_file_download.shard_queue_table.model()
        rows = sorted(set(index.row() for index in
                          self.ui_single_file_download.shard_queue_table.
                          selectedIndexes()))
        i = 0
        selected_row = 0
        for row in rows:
            index = tablemodel.index(row, 4)  # get shard Index
            # We suppose data are strings
            self.current_selected_shard_index = str(tablemodel.data(
                index).toString())
            selected_row = row
            i += 1

        # Check if checked and if it is in progress
        if ALLOW_DOWNLOAD_FARMER_POINTER_CANCEL_BY_USER and i == 1\
                and self.rowpositions_in_progress[selected_row]:

            menu = QtGui.QMenu()
            anotherFarmerUseAction = menu.addAction(
                'Try to use another farmer...')
            action = menu.exec_(self.ui_single_file_download.
                                shard_queue_table.mapToGlobal(position))

            if action == anotherFarmerUseAction:

                msgBox = QtGui.QMessageBox(
                    QtGui.QMessageBox.Question,
                    'Question',
                    'Are you sure that you want to get another pointer for '
                    'shard at index %s?' %
                    str(self.current_selected_shard_index),
                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)

                result = msgBox.exec_()

                if result == QtGui.QMessageBox.Yes:
                    self.another_farmer_manual_requests[
                        int(self.current_selected_shard_index)] = True

    def set_current_active_connections(self):
        self.ui_single_file_download.current_active_connections.setText(
            str(self.current_active_connections))

    def show_destination_path_not_selected_msg(self):
        return 1

    def handle_cancel_action(self):
        if self.is_upload_active:
            msgBox = QtGui.QMessageBox(
                QtGui.QMessageBox.Question,
                'Question',
                "Are you sure that you want cancel download and close \
this window?",
                QtGui.QMessageBox.Yes | QtGui.QMessageBox.No)
            result = msgBox.exec_()
            if result == QtGui.QMessageBox.Yes:
                self.close()
        else:
            self.close()

    def update_shards_counters(self):
        self.ui_single_file_download.downloaded_shards.setText(
            '%s/%s' % (self.shards_already_downloaded, self.all_shards_count))

    def initialize_download_queue_table(self):
        # initialize variables
        self.shards_already_downloaded = 0
        self.downloaded_shards_count = 0
        self.download_queue_progressbar_list = []

        self.download_queue_table_header = ['Progress',
                                            'Hash',
                                            'Farmer',
                                            'State',
                                            'Shard index']
        self.ui_single_file_download.shard_queue_table.setColumnCount(5)
        self.ui_single_file_download.shard_queue_table.setRowCount(0)
        horHeaders = self.download_queue_table_header
        self.ui_single_file_download.shard_queue_table.\
            setHorizontalHeaderLabels(horHeaders)
        self.ui_single_file_download.shard_queue_table.resizeColumnsToContents()
        self.ui_single_file_download.shard_queue_table.resizeRowsToContents()

        self.ui_single_file_download.shard_queue_table.horizontalHeader().\
            setResizeMode(QtGui.QHeaderView.Stretch)

    def add_row_download_queue_table(self, row_data):
        """
        Add a row to the download queue table
        """
        self.download_queue_progressbar_list.append(QtGui.QProgressBar())
        self.download_queue_table_row_count = \
            self.ui_single_file_download.shard_queue_table.rowCount()
        self.ui_single_file_download.shard_queue_table.setRowCount(
            self.download_queue_table_row_count + 1)
        self.ui_single_file_download.shard_queue_table.setCellWidget(
            self.download_queue_table_row_count, 0,
            self.download_queue_progressbar_list[
                self.download_queue_table_row_count])
        self.ui_single_file_download.shard_queue_table.setItem(
            self.download_queue_table_row_count, 1,
            QtGui.QTableWidgetItem(row_data['hash']))
        self.ui_single_file_download.shard_queue_table.setItem(
            self.download_queue_table_row_count, 2,
            QtGui.QTableWidgetItem('%s:%s' % (
                row_data['farmer_address'],
                row_data['farmer_port'])))
        self.ui_single_file_download.shard_queue_table.setItem(
            self.download_queue_table_row_count, 3,
            QtGui.QTableWidgetItem(str(row_data['state'])))
        self.ui_single_file_download.shard_queue_table.setItem(
            self.download_queue_table_row_count, 4,
            QtGui.QTableWidgetItem(str(row_data['shard_index'])))
        self.download_queue_progressbar_list[
            self.download_queue_table_row_count].setValue(0)

    def _add_shard_to_table(self, pointers_content, chapters):
        """
        Add a row to the shard table and return the row number
        """
        # Add items to shard queue table view
        # self.rowpositions_in_progress.append(False)
        tablerowdata = {}
        tablerowdata['farmer_address'] = pointers_content['farmer']['address']
        tablerowdata['farmer_port'] = pointers_content['farmer']['port']
        tablerowdata['hash'] = str(pointers_content['hash'])
        tablerowdata['state'] = 'Downloading...'
        tablerowdata['shard_index'] = str(chapters)

        self.__logger.debug('Resolved pointer for download: %s:%s' % (
            pointers_content['farmer']['address'],
            pointers_content['farmer']['port']))
        # Add row to table
        self.emit(QtCore.SIGNAL('addRowToDownloadQueueTable'), tablerowdata)

        rowcount = self.ui_single_file_download.shard_queue_table.rowCount()

        return rowcount

    def show_download_finished_message(self):
        self.ui_single_file_download.start_download_bt.setStyleSheet(
            ('QPushButton:hover{\n'
             '  background-color: #83bf20;\n'
             '  border-color: #83bf20;\n'
             '}\n'
             'QPushButton:active {\n'
             '  background-color: #93cc36;\n'
             '  border-color: #93cc36;\n'
             '}\n'
             'QPushButton{\n'
             '  background-color: #88c425;\n'
             '    border: 1px solid #88c425;\n'
             '    color: #fff;\n'
             '    border-radius: 7px;\n'
             '}'))

        self.ui_single_file_download.connections_onetime.setEnabled(True)
        self.ui_single_file_download.start_download_bt.setEnabled(True)

        QtGui.QMessageBox.information(self, 'Success!',
                                      'File downloaded successfully!')


    def show_unhandled_exception(self, exception_content):
        QtGui.QMessageBox.critical(self, 'Unhandled error',
                                   str(exception_content))

    def show_storj_bridge_exception(self, exception_content):
        try:
            j = json.loads(str(exception_content))
            if j.get('error') == 'Failed to get retrieval token':
                QtGui.QMessageBox.critical(
                    self,
                    'Bridge error',
                    '%s. Please wait and try again.' % j['error'])
            else:
                QtGui.QMessageBox.critical(self, 'Bridge error',
                                           str(j['error']))
        except BaseException:
            QtGui.QMessageBox.critical(self, 'Bridge error',
                                       str(exception_content))

    def update_download_task_state(self, row_position, state):
        self.ui_single_file_download.shard_queue_table.setItem(
            int(row_position), 3, QtGui.QTableWidgetItem(str(state)))

    def show_error_not_selected_file(self):
        QtGui.QMessageBox.about(self, 'Error',
                                'Please select destination file save path!')

    def show_error_invalid_file_path(self):
        QtGui.QMessageBox.about(
            self, 'Error', 'Destination file save path seems to be invalid!')

    def show_error_invalid_temporary_path(self):
        QtGui.QMessageBox.about(self, 'Error',
                                'Temporary path seems to be invalid!')

    def refresh_overall_download_progress(self, base_percent):
        total_percent_to_download = self.all_shards_count * 100
        total_percent_downloaded = sum(self.shard_download_percent_list) * 100

        actual_percent_downloaded = total_percent_downloaded / \
            total_percent_to_download

        total_percent = (base_percent * 100) + \
            (0.90 * actual_percent_downloaded)

        self.ui_single_file_download.overall_progress.setValue(
            int(total_percent))

    def createNewDownloadInitThread(self, bucket_id, file_id):
        """
        Interface for callers
        """
        self.ui_single_file_download.overall_progress.setValue(0)
        self.initialize_download_queue_table()
        threading.Thread(target=self.download_begin,
                         args=(bucket_id, file_id)).start()

    def createNewInitializationThread(self, bucket_id, file_id):
        file_name_resolve_thread = threading.Thread(
            target=self.set_file_metadata,
            args=(bucket_id, file_id))
        file_name_resolve_thread.start()

    def get_file_frame_id(self, bucket_id, file_id):
        try:
            file_metadata = self.storj_engine.storj_client.file_metadata(
                bucket_id, file_id)
            self.file_frame = file_metadata.frame
        except storj.exception.StorjBridgeApiError as e:
            # Emit Storj Bridge Exception
            self.emit(QtCore.SIGNAL('showStorjBridgeException'),
                      'Error while resolving file frame ID. %s' % e)
        except Exception as e:
            # Emit unhandled Exception
            self.emit(QtCore.SIGNAL('showUnhandledException'),
                      'Unhandled error while resolving file frame ID. %s' % e)
        else:
            return self.file_frame

    def set_file_metadata(self, bucket_id, file_id):
        try:
            self.emit(QtCore.SIGNAL('setCurrentState'),
                      'Getting file metadata...')
            file_metadata = self.storj_engine.storj_client.file_metadata(
                bucket_id, file_id)
            self.ui_single_file_download.file_name.setText(
                str(file_metadata.filename.replace(
                    '[DECRYPTED]', '')).decode('utf-8'))

            tools = Tools()
            self.ui_single_file_download.file_id.setText(file_id)

            self.ui_single_file_download.file_save_path.setText(
                os.path.join(
                    tools.get_home_user_directory().decode('utf-8'),
                    file_metadata.filename.replace(
                        '[DECRYPTED]', '')).decode('utf-8'))

            self.filename_from_bridge = file_metadata.filename.decode('utf-8')

            self.resolved_file_metadata = True
            self.emit(QtCore.SIGNAL('setCurrentState'),
                      'Waiting for user action...')
        except UnicodeDecodeError:
            pass
        except storj.exception.StorjBridgeApiError as e:
            # Emit Storj Bridge Exception
            self.emit(QtCore.SIGNAL('showStorjBridgeException'),
                      'Error while resolving file metadata %s' % e)
        except Exception as e:
            # Emit unhandled Exception
            self.emit(QtCore.SIGNAL('showUnhandledException'),
                      'Unhandled error while resolving file metadata %s' % e)

    # Wait for signal to do shards joining and encryption
    def finish_download(self, file_name):
        self.__logger.debug('Finish download for %s' % file_name)
        fileisencrypted = False
        if '[DECRYPTED]' in self.filename_from_bridge:
            fileisencrypted = False
        else:
            fileisencrypted = True

        # Join shards
        sharding_tools = ShardingTools()
        self.emit(QtCore.SIGNAL('setCurrentState'), 'Joining shards...')
        self.__logger.debug('Joining shards...')

        if fileisencrypted:
            sharding_tools.join_shards(
                os.path.join(self.tmp_path, file_name),
                '-',
                '%s.encrypted' % self.destination_file_path)
        else:
            sharding_tools.join_shards(
                os.path.join(self.tmp_path, file_name),
                '-',
                self.destination_file_path)

        self.__logger.debug('%s.encrypted' % os.path.join(self.tmp_path,
                                                          file_name))

        if fileisencrypted:
            # decrypt file
            self.emit(QtCore.SIGNAL('setCurrentState'), 'Decrypting file...')

            self.__logger.debug('Decrypting file...')
            self.__logger.debug('Output file %s' %
                                str(self.destination_file_path))
            file_crypto_tools = FileCrypto()
            # Begin file decryption
            file_crypto_tools.decrypt_file(
                'AES',
                '%s.encrypted' % self.destination_file_path,
                str(self.destination_file_path),
                str(self.user_password))

        self.__logger.debug('Downloading completed successfully!')
        self.emit(QtCore.SIGNAL('setCurrentState'),
                  'Downloading completed successfully!')
        self.is_upload_active = False
        self.emit(QtCore.SIGNAL('showFileDownloadedSuccessfully'))

        # Remove temp files
        try:
            # Remove shards
            file_shards = map(lambda i: '%s-%s' % (
                os.path.join(self.tmp_path,
                             file_name), i),
                range(self.all_shards_count))
            map(os.remove, file_shards)
            # Remove encrypted file
            os.remove('%s.encrypted' % self.destination_file_path)
        except OSError as e:
            self.__logger.error(e)

        return True

    def retry_dl_thread(self, shard_index, old_ip):
        dl = threading.Thread(target=self.retry_download_with_new_pointer,
                              args=(shard_index, old_ip))
        dl.start()
        # dl.join()

    def retry_download_with_new_pointer(self, shard_index, old_ip):
        MAX_ATTEMPT = 200
        pointer = None
        self.__logger.debug('Look for a farmer different from %s' % old_ip)
        attempts = 0
        while attempts < MAX_ATTEMPT:
            try:
                attempts += 1
                self.__logger.debug('attempt %s' % attempts)
                tnp = threading.Thread(
                    target=self.get_shard_pointers,
                    args=(self.bucket_id,
                          self.file_id,
                          '1',
                          str(shard_index)))
                time.sleep(1)
                tnp.start()
                pointers = queue.get()
                # tnp.join()
                pointer = pointers[0]
                self.__logger.debug('Found farmer %s' %
                                    pointer.get('farmer')['address'])
                if pointer.get('farmer')['address'] != old_ip:
                    break

            except storj.exception.StorjFarmerError as err:
                self.__logger.error(err)
                continue
                # exit(0)
            except Exception as err:
                self.__logger.error(err)
                continue
                # exit(0)

        try:
            if pointer.get('farmer')['address'] == old_ip:
                self.__logger.error('This will raise an exception')
                raise storj.exception.StorjFarmerError('Farmer not found')
        except BaseException:
            self.__logger.error('Farmer not found! Unable to download shard!')

        options_array = {}
        options_array['tmp_path'] = self.tmp_path
        options_array['progressbars_enabled'] = '1'
        options_array['file_size_is_given'] = '1'
        options_array['shards_count'] = str(self.all_shards_count)
        row_lock.acquire()
        # TEST
        self.current_line += 1
        tsd = threading.Thread(target=self.shard_download,
                               args=(pointer,
                                     self.destination_file_path,
                                     options_array))
        tsd.start()
        # self.current_line += 1
        row_lock.release()
        tsd.join()
        # self.shard_download(pointer, self.destination_file_path, options_array)

    def ask_overwrite(self, file_name):
        msgBox = QtGui.QMessageBox(
            QtGui.QMessageBox.Question,
            'Question',
            'File %s already exist! Do you want to overwrite?' %
            str(file_name).decode('utf-8'),
            (QtGui.QMessageBox.Yes | QtGui.QMessageBox.No))

        self.overwrite_question_result = msgBox.exec_()
        self.overwrite_question_closed = True

    def get_file_pointers_count(self, bucket_id, file_id):
        file_frame = self.get_file_frame_id(bucket_id, file_id)
        frame_data = self.storj_engine.storj_client.frame_get(file_frame.id)
        return len(frame_data.shards)

    def get_shard_pointers(self, bucket_id, file_id, num_of_shards='1',
                           shard_index='0', stages=0, stage=0):
        tries_get_file_pointers = 0
        success = False
        while self.max_retries_get_file_pointers > tries_get_file_pointers:
            tries_get_file_pointers += 1
            time.sleep(1)
            if tries_get_file_pointers > 1:
                self.emit(
                    QtCore.SIGNAL('setCurrentState'),
                    'Resolving pointers. Retry %s ...' % (
                        tries_get_file_pointers))
            else:
                if stage > 1:
                    self.emit(QtCore.SIGNAL('setCurrentState'),
                              'Resolving pointers - Stage %s of %s' % (
                                  stage, stages))
                else:
                    self.emit(QtCore.SIGNAL('setCurrentState'),
                              'Resolving shards pointers...')

            try:
                if FARMER_NODES_EXCLUSION_FOR_DOWNLOAD_ENABLED:
                    pointers = self.storj_engine.storj_client.file_pointers(
                        bucket_id,
                        file_id,
                        limit=num_of_shards,
                        skip=shard_index,
                        exclude=self.pointers_exclusions[int(shard_index)])
                else:
                    pointers = self.storj_engine.storj_client.file_pointers(
                        bucket_id,
                        file_id,
                        limit=num_of_shards,
                        skip=shard_index)

                # validate returned data

                for pointer in pointers:
                    tmp1 = pointer.get('farmer')['address']

                # return pointers
                success = True
                queue.put(pointers)
                break

            except storj.exception.StorjBridgeApiError as e:
                self.__logger.debug('Bridge error' + str(e))
                self.__logger.debug('Error while resolving file pointers \
            to download  with ID :%s ...' % file_id)
                # Emit Storj Bridge Exception
                self.emit(QtCore.SIGNAL('showStorjBridgeException'),
                          str(e))
                continue
            except Exception as e:
                self.__logger.error('Exception while resolving file pointers.' + str(e))
                continue
        if success is not True:
            queue.put('error')

    def download_begin(self, bucket_id, file_id):

        self.semaphore = threading.BoundedSemaphore(
            int(self.ui_single_file_download.connections_onetime.value()))

        self.overwrite_question_closed = False
        self.validation = {}

        self.all_shards_count = self.get_file_pointers_count(
            bucket_id, file_id)
        self.shards_already_downloaded = 0

        self.destination_file_path = \
            str(self.ui_single_file_download.file_save_path.text()).\
            decode('utf-8')
        self.tmp_path = \
            str(self.ui_single_file_download.tmp_dir.text()).decode('utf-8')

        if self.tmp_path == '':
            if platform == 'linux' or platform == 'linux2':
                # linux
                self.tmp_path = '/tmp'
            elif platform == 'darwin':
                # OS X
                self.tmp_path = '/tmp'
            elif platform == 'win32':
                # Windows
                if USE_USER_ENV_PATH_FOR_TEMP:
                    self.tmp_path = os.path.join(
                        str(self.tools.get_home_user_directory()).decode(
                            'utf-8'),
                        'AppData', 'Local', 'Temp')
                else:
                    self.tmp_path = 'C:\\Windows\\temp'

        file_name = os.path.split(self.destination_file_path)[1]

        if self.destination_file_path == '':
            # show error missing destination path
            self.validation['file_path'] = False
            self.emit(QtCore.SIGNAL('showDestinationPathNotSelectedMsg'))
            self.__logger.error('missing destination file path')
        else:
            self.validation['file_path'] = True

        if os.path.isfile(self.destination_file_path):
            self.emit(QtCore.SIGNAL('askFileOverwrite'), str(file_name))

            while not self.overwrite_question_closed:
                time.sleep(0.1)
                pass

            if self.overwrite_question_result == QtGui.QMessageBox.Yes:
                self.validation['file_path'] = True
            else:
                self.validation['file_path'] = False
                # emit signal to select new file path
                self.emit(QtCore.SIGNAL('selectFileDestinationPath'))

        if self.validation['file_path']:
            self.ui_single_file_download.start_download_bt.setStyleSheet(
                ('QPushButton:hover{\n'
                 '  background-color: #8C8A87;\n'
                 '  border-color: #8C8A87;\n'
                 '}\n'
                 'QPushButton:active {\n'
                 '  background-color: #8C8A87;\n'
                 '  border-color: #8C8A87;\n'
                 '}\n'
                 'QPushButton{\n'
                 '  background-color: #8C8A87;\n'
                 '    border: 1px solid #8C8A87;\n'
                 '    color: #fff;\n'
                 '    border-radius: 7px;\n'
                 '}'))

            self.ui_single_file_download.start_download_bt.setDisabled(True)

            self.ui_single_file_download.connections_onetime.setEnabled(False)

            self.emit(QtCore.SIGNAL('updateShardCounters'))

            self.__logger.debug('Resolving file pointers to download\
file with ID %s: ...' % file_id)

            self.is_upload_active = True

            options_array = {}
            options_array['tmp_path'] = self.tmp_path
            options_array['progressbars_enabled'] = '1'
            options_array['file_size_is_given'] = '1'
            options_array['shards_count'] = \
                str(self.all_shards_count)

            # Get all the pointers
            # shard_pointer = self.get_shard_pointers(
            #     bucket_id=bucket_id,
            #     file_id=file_id,
            #     num_of_shards=str(self.all_shards_count))

            try:
                applied_shards_count = 0
                shard_pointer = []
                self.pointers_exclusions = [[] for i3 in range(self.all_shards_count)]
                stages = 0
                while applied_shards_count < self.all_shards_count:
                    stages += 1
                    applied_shards_count += MAX_POINTERS_RESOLVED_IN_ONE_PART

                applied_shards_count = 0
                shard_pointer = []
                i = 0
                while applied_shards_count < self.all_shards_count:
                    i += 1
                    thread_pointers = threading.Thread(
                        target=self.get_shard_pointers,
                        args=(bucket_id,
                              file_id,
                              str(MAX_POINTERS_RESOLVED_IN_ONE_PART),
                              applied_shards_count,
                              stages, i))  # limit, skip
                    applied_shards_count += MAX_POINTERS_RESOLVED_IN_ONE_PART
                    thread_pointers.start()
                    # thread_pointers.join()
                    shard_pointer = shard_pointer + queue.get()

                threads = [threading.Thread(
                    target=self.shard_download,
                    args=(p,
                          self.destination_file_path,
                          options_array)) for p in shard_pointer]
                self.current_line = 0
                s_index = 0

                for t in threads:
                    # self.pointers_exclusions.append([s_index])
                    self.already_started_shard_downloads_count += 1
                    self.another_farmer_manual_requests.append(False)
                    row_lock.acquire()
                    t.start()
                    self.current_line += 1
                    row_lock.release()
                    s_index += 1
                    # print self.pointers_exclusions
                    time.sleep(FILE_POINTERS_ITERATION_DELAY)

                for t in threads:
                    t.join()

                if shard_pointer == 'error':
                    print "Lost shard pointer! Unable to download file form network"
                    raise Exception()
            except BaseException:
                self.__logger.error(
                    'Error while initializing download proccess...')

    def update_shard_download_progess(self, row_position_index, value):
        self.download_queue_progressbar_list[row_position_index].\
            setValue(value)
        return 1

    def increment_shards_download_progress_counters(self):
        # self.shards_already_downloaded += 1
        self.ui_single_file_download.downloaded_shards.setText(
            '%s%s%s' % (html_format_begin,
                        str(self.shards_already_downloaded),
                        html_format_end))

    def set_current_status(self, current_status):
        self.ui_single_file_download.current_state.setText(str(current_status))

    def select_tmp_directory(self):
        self.selected_tmp_dir = QtGui.QFileDialog.getExistingDirectory(
            None, 'Select a folder:', '', QtGui.QFileDialog.ShowDirsOnly)
        self.ui_single_file_download.tmp_dir.setText(
            str(self.selected_tmp_dir).decode('utf-8'))

    def select_file_save_path(self):
        file_save_path = QtGui.QFileDialog.getSaveFileName(
            self, 'Save file to...',
            str(self.ui_single_file_download.file_save_path.text()).decode(
                'utf-8'))
        self.ui_single_file_download.file_save_path.setText(file_save_path)

    def calculate_final_hmac(self):
        return 1

    def create_download_connection(self, url, path_to_save, options_chain,
                                   rowposition, shard_index):
        self.rowpositions_in_progress.append(False)
        local_filename = str(path_to_save).decode('utf-8')
        downloaded = False
        farmer_tries = 0

        self.__logger.debug('Downloading shard at index %s from farmer. %s' % (
            shard_index, url))

        tries_download_from_same_farmer = 0
        self.current_active_connections += 1
        cancelled_manually = False
        file_size_not_integral = False
        while self.max_retries_download_from_same_farmer > \
                tries_download_from_same_farmer:
            tries_download_from_same_farmer += 1
            farmer_tries += 1
            try:
                '''
                if self.another_farmer_manual_requests[int(shard_index)]:  # if this is True
                    self.another_farmer_manual_requests[int(shard_index)] = False
                    self.emit(QtCore.SIGNAL('updateDownloadTaskState'),
                              rowposition,
                              "Cancelled by user! Getting another farmer...")
                    tries_download_from_same_farmer = self.max_retries_download_from_same_farmer  # force max retries due to use cancel
                    cancelled_manually = True
                    break
                '''

                # self.rowpositions_in_progress[int(rowposition)] = True
                self.emit(QtCore.SIGNAL('setCurrentActiveConnections'))
                self.emit(QtCore.SIGNAL('updateDownloadTaskState'),
                          rowposition,
                          'Downloading...')  # update shard downloading state

                if tries_download_from_same_farmer > 1:
                    self.emit(QtCore.SIGNAL('setCurrentState'),
                              'Downloading shard %s. Retry %s' % (
                                  shard_index,
                                  tries_download_from_same_farmer))
                else:
                    self.emit(QtCore.SIGNAL('setCurrentState'),
                              'Downloading shard %s' % shard_index)

                if options_chain['handle_progressbars'] != '1':
                    r = requests.get(
                        url, timeout=DEFAULT_MAX_FARMER_DOWNLOAD_READ_TIMEOUT)
                    # requests
                    with open(local_filename, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=1024):
                            if chunk:  # filter out keep-alive new chunks
                                f.write(chunk)
                else:
                    r = requests.get(
                        url,
                        timeout=DEFAULT_MAX_FARMER_DOWNLOAD_READ_TIMEOUT,
                        stream=True)

                    if options_chain['file_size_is_given'] == '1':
                        file_size = options_chain['shard_file_size']
                    else:
                        file_size = int(r.headers['Content-Length'])

                    chunk = 1
                    t1 = float(file_size) / MAX_DOWNLOAD_REQUEST_BLOCK_SIZE

                    if file_size <= MAX_DOWNLOAD_REQUEST_BLOCK_SIZE:
                        t1 = 1

                    i = 0
                    self.__logger.debug('File size: %s' % file_size)
                    self.__logger.debug('Chunks: %s' % t1)
                    f = open(local_filename, 'wb')
                    for chunk in r.iter_content(
                            MAX_DOWNLOAD_REQUEST_BLOCK_SIZE):
                        '''
                        try:
                            if self.another_farmer_manual_requests[int(shard_index)]:  # if this is True
                                self.another_farmer_manual_requests[int(shard_index)] = False
                                self.emit(QtCore.SIGNAL('updateDownloadTaskState'),
                                          rowposition,
                                          "Cancelled by user! Getting another farmer...")
                                tries_download_from_same_farmer = self.max_retries_download_from_same_farmer  # force max retries due to use cancel
                                cancelled_manually = True
                                break
                        except:
                            pass
                        '''

                        i += 1
                        f.write(chunk)
                        if int(round((100.0 * i) / t1)) > 100:
                            percent_downloaded = 100
                        else:
                            percent_downloaded = int(round((100.0 * i) / t1))
                        # Update progress bar in upload queue table
                        self.emit(
                            QtCore.SIGNAL('updateShardDownloadProgress'),
                            int(rowposition),
                            percent_downloaded)
                        self.shard_download_percent_list[shard_index] = \
                            percent_downloaded
                        # Update progress bar in upload queue table
                        self.emit(QtCore.SIGNAL(
                            'refreshOverallDownloadProgress'),
                            0.1)

                    f.close()
                self.__logger.debug('%s rowposition started' % rowposition)
                self.__logger.debug('%s status http' % r.status_code)
                if r.status_code != 200 and r.status_code != 304:
                    raise storj.exception.StorjFarmerError(22)

                # check file size integrity
                expected_shard_size = file_size
                downloaded_shard_size = os.stat(local_filename).st_size

                if expected_shard_size != downloaded_shard_size:
                    file_size_not_integral = True
                    raise storj.exception.StorjFarmerError(12)

                downloaded = True

            except storj.exception.StorjFarmerError as e:
                # Update shard download state
                if file_size_not_integral:
                    self.emit(QtCore.SIGNAL('updateDownloadTaskState'),
                              rowposition,
                              'First try failed. Shard size integrity check \
failed! Retrying... (%s)' % farmer_tries)
                else:
                    self.emit(QtCore.SIGNAL('updateDownloadTaskState'),
                              rowposition,
                              'First try failed. Retrying... (%s)' % farmer_tries)

                continue
            except Exception as e:
                self.__logger.error(e)
                self.__logger.debug(
                    'Unhandled error while transfering data to farmer')
                self.__logger.debug('Error occured while downloading\
shard at index %s. Retrying ...(%s)' % (shard_index, farmer_tries))
                # Update shard download state
                self.emit(QtCore.SIGNAL('updateDownloadTaskState'),
                          rowposition,
                          'First try failed. Retrying... (%s)' % farmer_tries)
                continue
            else:
                downloaded = True
                break

        if not downloaded:
            self.current_active_connections -= 1
            self.emit(QtCore.SIGNAL('setCurrentActiveConnections'))
            # Update shard download state
            self.emit(QtCore.SIGNAL('updateDownloadTaskState'),
                      rowposition,
                      "Error while downloading from this farmer. \
Getting another farmer pointer...")

            if cancelled_manually:
                self.emit(QtCore.SIGNAL('updateDownloadTaskState'),
                          rowposition,
                          "Cancelled by user! Getting another farmer...")

            time.sleep(1)
            # Retry download with new download pointer
            self.__logger.debug('Retry with new downoad pointer')
            self.semaphore.release()
            self.emit(QtCore.SIGNAL('retryWithNewDownloadPointer'),
                      shard_index, url.split(':')[1].replace('//', ''))

        else:
            self.current_active_connections -= 1
            self.emit(QtCore.SIGNAL('setCurrentActiveConnections'))
            self.__logger.debug('Shard downloaded')
            self.__logger.debug('Shard at index ' +
                                str(shard_index) +
                                ' downloaded successfully.')
            self.shards_already_downloaded += 1
            # Update already downloaded shards count
            self.emit(
                QtCore.SIGNAL('incrementShardsDownloadProgressCounters'))
            # Update already downloaded shards count
            self.emit(QtCore.SIGNAL('updateShardCounters'))
            # Update shard download state
            self.emit(QtCore.SIGNAL('updateDownloadTaskState'),
                      rowposition,
                      'Downloaded!')
            # Release the semaphore when the download is finished
            self.semaphore.release()
            if int(self.all_shards_count) <= \
                    int(self.shards_already_downloaded):
                # Send signal to begin file shards join and decryption
                # after all shards are downloaded
                self.emit(QtCore.SIGNAL('finishDownload'))
            return

    def shard_download(self, pointer, file_save_path, options_array):
        # Acquire lock for row_number
        row_lock.acquire()
        # Acquire a semaphore
        self.semaphore.acquire()
        self.__logger.debug('Beginning download proccess...')
        options_chain = {}
        file_name = os.path.split(file_save_path)[1]

        try:
            self.pointers_exclusions[int(pointer['index'])].append(
                pointer.get('farmer')['nodeID'])
        except BaseException:
            self.semaphore.release()
            self.emit(QtCore.SIGNAL('retryWithNewDownloadPointer'),
                      pointer['index'], 'http://%s:%s/shards/%s?token=%s' % (
                pointer.get('farmer')['address'],
                str(pointer.get('farmer')['port']),
                pointer['hash'],
                pointer['token']))

        try:
            # check ability to write files to selected directories
            if not self.tools.isWritable(os.path.split(file_save_path)[0]):
                raise IOError('13')
            if not self.tools.isWritable(self.tmp_path):
                raise IOError('13')

            if options_array['progressbars_enabled'] == '1':
                options_chain['handle_progressbars'] = '1'

            if options_array['file_size_is_given'] == '1':
                options_chain['file_size_is_given'] = '1'

            self.__logger.debug('Shard size: %s' % pointer['size'])

            part = pointer['index']
            self.__logger.debug('Shard index %s' % part)

            self.tmp_path = options_array['tmp_path']

            self.emit(QtCore.SIGNAL('setCurrentState'),
                      'Starting download threads...')
            self.emit(QtCore.SIGNAL('setCurrentState'),
                      'Started download shard at index %s...' % part)

            options_chain['rowposition'] = part
            self.shard_download_percent_list.append(0)

            # self.__logger.debug(pointer)
            options_chain['shard_file_size'] = int(pointer['size'])
            # Generate download URL
            url = 'http://%s:%s/shards/%s?token=%s' % (
                pointer.get('farmer')['address'],
                str(pointer.get('farmer')['port']),
                pointer['hash'],
                pointer['token'])
            self.__logger.debug(url)

            # Add a row to the table
            self._add_shard_to_table(pointer, part)
            line_number = self.current_line
            # Release the lock for the row_number
            row_lock.release()

            self.__logger.debug('Download shard number %s with row number %s' %
                                (part, line_number))

            if self.combine_tmpdir_name_with_token:
                self.create_download_connection(
                    url,
                    '%s-%s' % (
                        os.path.join(self.tmp_path,
                                     pointer['token'],
                                     file_name),
                        part),
                    options_chain,
                    line_number - 1,
                    part)
            else:
                self.create_download_connection(
                    url,
                    '%s-%s' % (os.path.join(self.tmp_path, file_name), part),
                    options_chain,
                    line_number - 1,
                    part)

            self.__logger.debug('%s-%s' % (os.path.join(self.tmp_path,
                                                        file_name),
                                           part))

        except IOError as e:
            self.__logger.error('Perm error %s' % e)
            if str(e) == str(13):
                # Emit Storj Bridge Exception
                self.emit(
                    QtCore.SIGNAL('showException'),
                    'Error while saving or reading file or temporary file.\
Probably this is caused by insufficient permisions.Please check if you \
have permissions to write or read from selected directories.')
        except Exception as e:
            self.__logger.debug('Unhandled error')
            self.__logger.error(e)
