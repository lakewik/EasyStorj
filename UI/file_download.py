# -*- coding: utf-8 -*-

import json
import os
from sys import platform
import requests
from PyQt4 import QtCore, QtGui

from utilities.sharder import ShardingTools
from utilities.tools import Tools
from qt_interfaces.file_download_new import Ui_SingleFileDownload
from crypto.file_crypto_tools import FileCrypto
from engine import StorjEngine
import storj
import threading

from utilities.log_manager import logger

from resources.html_strings import html_format_begin, html_format_end
from utilities.account_manager import AccountManager
import time
from resources.constants import USE_USER_ENV_PATH_FOR_TEMP


class SingleFileDownloadUI(QtGui.QMainWindow):

    def __init__(self, parent=None, bucketid=None, fileid=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui_single_file_download = Ui_SingleFileDownload()
        self.ui_single_file_download.setupUi(self)
        self.storj_engine = StorjEngine()  # init StorjEngine
        self.filename_from_bridge = ""
        self.tools = Tools()

        self.rowposition2 = 0

        self.bucket_id = bucketid
        self.file_id = fileid

        # init loggers
        # self.log_handler = LogHandler()
        # logging.setLoggerClass(get_global_logger(self.log_handler))
        # logger.addHandler(self.log_handler)

        # self.initialize_shard_queue_table(file_pointers)

        self.tools = Tools()

        self.is_upload_active = False

        self.account_manager = AccountManager()  # init AccountManager

        self.user_password = self.account_manager.get_user_password()

        # open file select dialog
        QtCore.QObject.connect(self.ui_single_file_download.file_path_select_bt,
                               QtCore.SIGNAL("clicked()"),
                               self.select_file_save_path)
        # open tmp directory select dialog
        QtCore.QObject.connect(self.ui_single_file_download.tmp_dir_bt,
                               QtCore.SIGNAL("clicked()"),
                               self.select_tmp_directory)
        # open tmp directory select dialog
        QtCore.QObject.connect(self.ui_single_file_download.cancel_bt,
                               QtCore.SIGNAL("clicked()"),
                               self.handle_cancel_action)
        # begin file downloading process
        QtCore.QObject.connect(self.ui_single_file_download.start_download_bt,
                               QtCore.SIGNAL("clicked()"),
                               lambda: self.createNewDownloadInitThread(
                                   bucketid,
                                   fileid))

        self.connect(self,
                     QtCore.SIGNAL("incrementShardsDownloadProgressCounters"),
                     self.increment_shards_download_progress_counters)
        self.connect(self, QtCore.SIGNAL("updateShardDownloadProgress"),
                     self.update_shard_download_progess)
        self.connect(self, QtCore.SIGNAL("refreshOverallDownloadProgress"),
                     self.refresh_overall_download_progress)
        self.connect(self,
                     QtCore.SIGNAL("showDestinationFileNotSelectedError"),
                     self.show_error_not_selected_file)
        self.connect(self, QtCore.SIGNAL("showInvalidDestinationPathError"),
                     self.show_error_invalid_file_path)
        self.connect(self,
                     QtCore.SIGNAL("showInvalidTemporaryDownloadPathError"),
                     self.show_error_invalid_temporary_path)
        self.connect(self, QtCore.SIGNAL("updateDownloadTaskState"),
                     self.update_download_task_state)
        self.connect(self, QtCore.SIGNAL("showStorjBridgeException"),
                     self.show_storj_bridge_exception)
        self.connect(self, QtCore.SIGNAL("showUnhandledException"),
                     self.show_unhandled_exception)
        self.connect(self, QtCore.SIGNAL("showFileDownloadedSuccessfully"),
                     self.show_download_finished_message)
        self.connect(self, QtCore.SIGNAL("showException"),
                     self.show_unhandled_exception)
        self.connect(self, QtCore.SIGNAL("addRowToDownloadQueueTable"),
                     self.add_row_download_queue_table)
        self.connect(self, QtCore.SIGNAL("setCurrentState"),
                     self.set_current_status)
        self.connect(self, QtCore.SIGNAL("updateShardCounters"),
                     self.update_shards_counters)
        self.connect(self, QtCore.SIGNAL("retryWithNewDownloadPointer"),
                     self.retry_download_with_new_pointer)
        self.connect(self, QtCore.SIGNAL("showDestinationPathNotSelectedMsg"),
                     self.show_error_invalid_file_path)
        self.connect(self, QtCore.SIGNAL("selectFileDestinationPath"),
                     self.select_file_save_path)
        self.connect(self, QtCore.SIGNAL("askFileOverwrite"),
                     self.ask_overwrite)
        self.connect(self, QtCore.SIGNAL('setCurrentActiveConnections'),
                     self.set_current_active_connections)
        self.connect(self, QtCore.SIGNAL("finishDownload"),
                     lambda: self.finish_download(
                         str(os.path.split(str(self.ui_single_file_download.file_save_path.text()))[1]).decode('utf-8')))

        self.overwrite_question_result = None
        self.overwrite_question_closed = False

        self.ui_single_file_download.current_state.setText("Waiting for user action...")
        self.ui_single_file_download.downloaded_shards.setText("Waiting for user...")
        self.shards_already_downloaded = 0

        self.createNewInitializationThread(bucketid, fileid)

        self.shard_download_percent_list = []

        # init limit variables
        self.max_retries_download_from_same_farmer = 3
        self.max_retries_get_file_pointers = 30

        # set default paths
        temp_dir = ''
        if platform == 'linux' or platform == 'linux2':
            # linux
            temp_dir = '/tmp'
        elif platform == 'darwin':
            # OS X
            temp_dir = '/tmp'
        elif platform == 'win32':
            # Windows
            if USE_USER_ENV_PATH_FOR_TEMP:
                temp_dir = os.path.join(
                    self.get_home_user_directory().decode('utf-8'),
                    'AppData\\Local\\Temp')
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

    def set_current_active_connections(self):
        self.ui_single_file_download.current_active_connections.setText(str(self.current_active_connections))

    def show_destination_path_not_selected_msg(self):
        return 1

    def handle_cancel_action(self):
        if self.is_upload_active:
            msgBox = QtGui.QMessageBox(
                QtGui.QMessageBox.Question,
                "Question",
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
            "%s/%s" % (self.shards_already_downloaded, self.all_shards_count))

    def initialize_download_queue_table(self):
        # initialize variables
        self.shards_already_downloaded = 0
        self.downloaded_shards_count = 0
        self.download_queue_progressbar_list = []

        self.download_queue_table_header = ['Progress', 'Hash', 'Farmer', 'State', 'Shard index']
        self.ui_single_file_download.shard_queue_table.setColumnCount(5)
        self.ui_single_file_download.shard_queue_table.setRowCount(0)
        horHeaders = self.download_queue_table_header
        self.ui_single_file_download.shard_queue_table.setHorizontalHeaderLabels(horHeaders)
        self.ui_single_file_download.shard_queue_table.resizeColumnsToContents()
        self.ui_single_file_download.shard_queue_table.resizeRowsToContents()

        self.ui_single_file_download.shard_queue_table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

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
            QtGui.QTableWidgetItem(row_data["hash"]))
        self.ui_single_file_download.shard_queue_table.setItem(
            self.download_queue_table_row_count, 2,
            QtGui.QTableWidgetItem(
                row_data["farmer_address"] + ":" +
                str(row_data["farmer_port"])))
        self.ui_single_file_download.shard_queue_table.setItem(
            self.download_queue_table_row_count, 3,
            QtGui.QTableWidgetItem(str(row_data["state"])))
        self.ui_single_file_download.shard_queue_table.setItem(
            self.download_queue_table_row_count, 4,
            QtGui.QTableWidgetItem(str(row_data["shard_index"])))
        self.download_queue_progressbar_list[
            self.download_queue_table_row_count].setValue(0)

    def _add_shard_to_table(self, pointers_content, chapters):
        """
        Add a row to the shard table and return the row number
        """
        # Add items to shard queue table view
        tablerowdata = {}
        tablerowdata["farmer_address"] = pointers_content["farmer"]["address"]
        tablerowdata["farmer_port"] = pointers_content["farmer"]["port"]
        tablerowdata["hash"] = str(pointers_content["hash"])
        tablerowdata["state"] = "Downloading..."
        tablerowdata["shard_index"] = str(chapters)

        logger.debug('Resolved pointer for download : ' +
                     str(pointers_content["farmer"]["address"]) + ":" +
                     str(pointers_content["farmer"]["port"]))
        # Add row to table
        self.emit(QtCore.SIGNAL("addRowToDownloadQueueTable"), tablerowdata)

        rowcount = self.ui_single_file_download.shard_queue_table.rowCount()
        return rowcount

    def show_download_finished_message(self):
        self.ui_single_file_download.start_download_bt.setStyleSheet(
            ("QPushButton:hover{\n"
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
        QtGui.QMessageBox.information(self, "Success!",
                                      "File downloaded successfully!")

    def show_unhandled_exception(self, exception_content):
        QtGui.QMessageBox.critical(self, "Unhandled error", str(exception_content))

    def show_storj_bridge_exception(self, exception_content):
        try:
            j = json.loads(str(exception_content))
            if j.get("error") == "Failed to get retrieval token":
                QtGui.QMessageBox.critical(
                    self,
                    'Bridge error',
                    "%s. Please wait and try again." % j['error'])
            else:
                QtGui.QMessageBox.critical(self, "Bridge error", str(j["error"]))

        except:
            QtGui.QMessageBox.critical(self, "Bridge error", str(exception_content))

    def update_download_task_state(self, row_position, state):
        self.ui_single_file_download.shard_queue_table.setItem(
            int(row_position), 3, QtGui.QTableWidgetItem(str(state)))

    def show_error_not_selected_file(self):
        QtGui.QMessageBox.about(self, "Error",
                                "Please select destination file save path!")

    def show_error_invalid_file_path(self):
        QtGui.QMessageBox.about(
            self, "Error", "Destination file save path seems to be invalid!")

    def show_error_invalid_temporary_path(self):
        QtGui.QMessageBox.about(self, "Error",
                                "Temporary path seems to be invalid!")

    def refresh_overall_download_progress(self, base_percent):
        total_percent_to_download = self.all_shards_count * 100
        total_percent_downloaded = sum(self.shard_download_percent_list) * 100

        actual_percent_downloaded = total_percent_downloaded / \
            total_percent_to_download

        total_percent = (base_percent * 100) + \
            (0.90 * actual_percent_downloaded)

        # logger.info("%s %s total_percent_downloaded" %
        #     actual_percent_downloaded, base_percent)

        self.ui_single_file_download.overall_progress.setValue(
            int(total_percent))

    def createNewDownloadInitThread(self, bucket_id, file_id):
        """
        Interface for callers
        """
        self.ui_single_file_download.overall_progress.setValue(0)
        self.initialize_download_queue_table()
        self.download_begin(bucket_id, file_id)

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
            self.emit(QtCore.SIGNAL("showStorjBridgeException"),
                      "Error while resolving file frame ID. %s" % e)
        except Exception as e:
            # Emit unhandled Exception
            self.emit(QtCore.SIGNAL("showUnhandledException"),
                      "Unhandled error while resolving file frame ID. %s" % e)
        else:
            return self.file_frame

    def set_file_metadata(self, bucket_id, file_id):
        try:
            self.emit(QtCore.SIGNAL("setCurrentState"),
                      "Getting file metadata...")
            file_metadata = self.storj_engine.storj_client.file_metadata(
                bucket_id, file_id)
            self.ui_single_file_download.file_name.setText(
                str(file_metadata.filename.replace(
                    "[DECRYPTED]", "")).decode('utf-8'))

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
            self.emit(QtCore.SIGNAL("showStorjBridgeException"),
                      "Error while resolving file metadata %s" % e)
        except Exception as e:
            # Emit unhandled Exception
            self.emit(QtCore.SIGNAL("showUnhandledException"),
                      "Unhandled error while resolving file metadata %s" % e)

    # Wait for signal to do shards joining and encryption
    def finish_download(self, file_name):
        logger.debug('Finish download for %s' % file_name)
        fileisencrypted = False
        if "[DECRYPTED]" in self.filename_from_bridge:
            fileisencrypted = False
        else:
            fileisencrypted = True

        # Join shards
        sharing_tools = ShardingTools()
        self.emit(QtCore.SIGNAL("setCurrentState"), "Joining shards...")
        logger.debug('Joining shards...')

        if fileisencrypted:
            sharing_tools.join_shards(
                os.path.join(self.tmp_path, file_name),
                '-',
                '%s.encrypted' % self.destination_file_path)
        else:
            sharing_tools.join_shards(
                os.path.join(self.tmp_path, file_name),
                '-',
                self.destination_file_path)

        logger.debug("%s.encrypted" % os.path.join(self.tmp_path, file_name))

        if fileisencrypted:
            # decrypt file
            self.emit(QtCore.SIGNAL("setCurrentState"), "Decrypting file...")

            logger.debug('Decrypting file...')
            logger.debug('Output file %s' % str(self.destination_file_path))
            file_crypto_tools = FileCrypto()
            # Begin file decryption
            file_crypto_tools.decrypt_file(
                "AES",
                str(self.destination_file_path) + ".encrypted",
                str(self.destination_file_path),
                str(self.user_password))

        logger.debug("pobrano")
        logger.debug('Downloading completed successfully!')
        self.emit(QtCore.SIGNAL("setCurrentState"),
                  "Downloading completed successfully!")
        self.is_upload_active = False
        self.emit(QtCore.SIGNAL("showFileDownloadedSuccessfully"))
        return True

    def retry_download_with_new_pointer(self, shard_index):
        pointers = self.get_shard_pointers(
            bucket_id=self.bucket_id,
            file_id=self.file_id,
            num_of_shards="1",
            shard_index=str(shard_index))
        pointer = pointers[0]
        options_array = {}
        options_array["tmp_path"] = self.tmp_path
        options_array["progressbars_enabled"] = "1"
        options_array["file_size_is_given"] = "1"
        options_array["shards_count"] = str(self.all_shards_count)
        self.shard_download(pointer, self.destination_file_path, options_array)

    def ask_overwrite(self, file_name):
        msgBox = QtGui.QMessageBox(
            QtGui.QMessageBox.Question,
            'Question',
            'File %s already exist! Do you want to overwrite?' % str(file_name).decode('utf-8'),
            (QtGui.QMessageBox.Yes | QtGui.QMessageBox.No))

        self.overwrite_question_result = msgBox.exec_()
        self.overwrite_question_closed = True

    def get_file_pointers_count(self, bucket_id, file_id):
        file_frame = self.get_file_frame_id(bucket_id, file_id)
        frame_data = self.storj_engine.storj_client.frame_get(file_frame.id)
        return len(frame_data.shards)

    def get_shard_pointers(self, bucket_id, file_id, num_of_shards="1", shard_index="0"):
        pointers = self.storj_engine.storj_client.file_pointers(
            bucket_id,
            file_id,
            limit=num_of_shards,
            skip=shard_index)
        return pointers

    def download_begin(self, bucket_id, file_id):
        self.overwrite_question_closed = False
        self.validation = {}

        self.all_shards_count = self.get_file_pointers_count(
            bucket_id, file_id)
        self.shards_already_downloaded = 0

        self.destination_file_path = \
            str(self.ui_single_file_download.file_save_path.text()).decode('utf-8')
        self.tmp_path = \
            str(self.ui_single_file_download.tmp_dir.text()).decode('utf-8')

        if self.tmp_path == "":
            if platform == "linux" or platform == "linux2":
                # linux
                self.tmp_path = "/tmp"
            elif platform == "darwin":
                # OS X
                self.tmp_path = "/tmp"
            elif platform == "win32":
                # Windows
                self.tmp_path = "C:\\Windows\\temp"

        file_name = os.path.split(self.destination_file_path)[1]

        if self.destination_file_path == "":
            # show error missing destination path
            self.validation["file_path"] = False
            self.emit(QtCore.SIGNAL("showDestinationPathNotSelectedMsg"))
            logger.error("missing destination file path")
        else:
            self.validation["file_path"] = True

        if os.path.isfile(self.destination_file_path):
            self.emit(QtCore.SIGNAL("askFileOverwrite"), str(file_name))

            while not self.overwrite_question_closed:
                pass

            if self.overwrite_question_result == QtGui.QMessageBox.Yes:
                self.validation["file_path"] = True
            else:
                self.validation["file_path"] = False
                # emit signal to select new file path
                self.emit(QtCore.SIGNAL("selectFileDestinationPath"))

        if self.validation["file_path"]:
            self.ui_single_file_download.start_download_bt.setStyleSheet(
                ("QPushButton:hover{\n"
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

            self.emit(QtCore.SIGNAL("updateShardCounters"))

            logger.debug('Resolving file pointers to download\
file with ID %s: ...' % file_id)

            self.is_upload_active = True
            tries_get_file_pointers = 0
            while self.max_retries_get_file_pointers > tries_get_file_pointers:
                tries_get_file_pointers += 1
                time.sleep(1)
                try:
                    if tries_get_file_pointers > 1:
                        self.emit(
                            QtCore.SIGNAL("setCurrentState"),
                            "Resolving pointers. Retry %s ..." % (
                                tries_get_file_pointers))
                    else:
                        self.emit(QtCore.SIGNAL("setCurrentState"),
                                  "Resolving pointer for shards")
                    options_array = {}
                    options_array["tmp_path"] = self.tmp_path
                    options_array["progressbars_enabled"] = "1"
                    options_array["file_size_is_given"] = "1"
                    options_array["shards_count"] = \
                        str(self.all_shards_count)

                    # Get all the pointers
                    shard_pointer = self.get_shard_pointers(
                        bucket_id=bucket_id,
                        file_id=file_id,
                        num_of_shards=str(self.all_shards_count))
                except storj.exception.StorjBridgeApiError as e:
                    logger.debug('Bridge error')
                    logger.debug('Error while resolving file pointers \
to download  with ID :%s ...' % file_id)
                    # Emit Storj Bridge Exception
                    self.emit(QtCore.SIGNAL("showStorjBridgeException"),
                              str(e))
                    continue
                except Exception as e:
                    continue
                else:
                    break

            threads = [threading.Thread(
                target=self.shard_download,
                args=(p,
                      self.destination_file_path,
                      options_array)) for p in shard_pointer]
            for t in threads:
                self.already_started_shard_downloads_count += 1
                t.start()
                self.rowposition2 += 1
                time.sleep(1)

    def update_shard_download_progess(self, row_position_index, value):
        self.download_queue_progressbar_list[row_position_index].setValue(value)
        return 1

    def increment_shards_download_progress_counters(self):
        # self.shards_already_downloaded += 1
        self.ui_single_file_download.downloaded_shards.setText(
            "%s%s%s" % (html_format_begin,
                        str(self.shards_already_downloaded),
                        html_format_end))

    def set_current_status(self, current_status):
        self.ui_single_file_download.current_state.setText(str(current_status))

    def select_tmp_directory(self):
        self.selected_tmp_dir = QtGui.QFileDialog.getExistingDirectory(
            None, 'Select a folder:', '', QtGui.QFileDialog.ShowDirsOnly)
        self.ui_single_file_download.tmp_dir.setText(
            str(self.selected_tmp_dir).decode("utf-8"))

    def select_file_save_path(self):
        file_save_path = QtGui.QFileDialog.getSaveFileName(
            self, 'Save file to...',
            str(self.ui_single_file_download.file_save_path.text()).decode(
                'utf-8'))
        self.ui_single_file_download.file_save_path.setText(file_save_path)

    def calculate_final_hmac(self):
        return 1

    def create_download_connection(self, url, path_to_save, options_chain, rowposition, shard_index):
        local_filename = str(path_to_save).decode('utf-8')
        downloaded = False
        farmer_tries = 0

        logger.debug('Downloading shard at index %s from farmer. %s' % (
            shard_index, url))

        tries_download_from_same_farmer = 0
        while self.max_retries_download_from_same_farmer > tries_download_from_same_farmer:
            tries_download_from_same_farmer += 1
            farmer_tries += 1
            print str(rowposition) + " pozycja"
            try:
                self.current_active_connections += 1
                self.emit(QtCore.SIGNAL('setCurrentActiveConnections'))
                self.emit(QtCore.SIGNAL("updateDownloadTaskState"), rowposition,
                          "Downloading...")  # update shard downloading state
                if options_chain["handle_progressbars"] != "1":
                    r = requests.get(url)
                    # requests
                    with open(local_filename, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=1024):
                            if chunk:  # filter out keep-alive new chunks
                                f.write(chunk)
                else:
                    r = requests.get(url, stream=True)
                    if options_chain["file_size_is_given"] == "1":
                        file_size = options_chain["shard_file_size"]
                    else:
                        file_size = int(r.headers['Content-Length'])

                    chunk = 1
                    num_bars = file_size / chunk
                    t1 = float(file_size) / float((32 * 1024))
                    logger.debug(t1)

                    if file_size <= (32 * 1024):
                        t1 = 1

                    i = 0
                    logger.debug(file_size)
                    logger.debug(str(t1) + " kotek")
                    f = open(local_filename, 'wb')
                    for chunk in r.iter_content(32 * 1024):
                        i += 1
                        f.write(chunk)
                        if int(round((100.0 * i) / t1)) > 100:
                            percent_downloaded = 100
                        else:
                            percent_downloaded = int(round((100.0 * i) / t1))
                        # Update progress bar in upload queue table
                        self.emit(
                            QtCore.SIGNAL("updateShardDownloadProgress"),
                            int(rowposition),
                            percent_downloaded)
                        self.shard_download_percent_list[shard_index] = \
                            percent_downloaded
                        # Update progress bar in upload queue table
                        self.emit(QtCore.SIGNAL("refreshOverallDownloadProgress"),
                                  0.1)

                    f.close()
                logger.debug('%s rowposition started' % rowposition)
                logger.debug('%s status http' % r.status_code)
                if r.status_code != 200 and r.status_code != 304:
                    raise storj.exception.StorjFarmerError()
                downloaded = True

            except storj.exception.StorjFarmerError as e:
                # Update shard download state
                self.emit(QtCore.SIGNAL("updateDownloadTaskState"),
                          rowposition,
                          'First try failed. Retrying... (%s)' % farmer_tries)
                continue

            except Exception as e:
                logger.error(e)
                logger.debug('Unhandled error while transfering data to farmer')
                logger.debug('Error occured while downloading\
                             shard at index %s. Retrying ...(%s)' %
                             (shard_index, farmer_tries))
                # Update shard download state
                self.emit(QtCore.SIGNAL("updateDownloadTaskState"),
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
            self.emit(QtCore.SIGNAL("updateDownloadTaskState"),
                      rowposition,
                      "Error while downloading from this farmer. \
Getting another farmer pointer...")
            time.sleep(1)
            # Retry download with new download pointer
            logger.debug("Retry with new downoad pointer")
            self.emit(QtCore.SIGNAL("retryWithNewDownloadPointer"),
                      shard_index)

        else:
            self.current_active_connections -= 1
            self.emit(QtCore.SIGNAL('setCurrentActiveConnections'))
            logger.debug('Shard downloaded')
            logger.debug('Shard at index ' +
                         str(shard_index) +
                         " downloaded successfully.")
            self.shards_already_downloaded += 1
            # Update already downloaded shards count
            self.emit(
                QtCore.SIGNAL("incrementShardsDownloadProgressCounters"))
            # Update already downloaded shards count
            self.emit(QtCore.SIGNAL("updateShardCounters"))
            # Update shard download state
            self.emit(QtCore.SIGNAL("updateDownloadTaskState"),
                      rowposition,
                      "Downloaded!")
            if int(self.all_shards_count) <= int(self.shards_already_downloaded):
                # Send signal to begin file shards join and decryption
                # after all shards are downloaded
                self.emit(QtCore.SIGNAL("finishDownload"))
            return

    def shard_download(self, pointer, file_save_path, options_array):
        logger.debug('Beginning download proccess...')
        options_chain = {}
        file_name = os.path.split(file_save_path)[1]

        try:
            # check ability to write files to selected directories
            if not self.tools.isWritable(os.path.split(file_save_path)[0]):
                raise IOError("13")
            if not self.tools.isWritable(self.tmp_path):
                raise IOError("13")

            if options_array["progressbars_enabled"] == "1":
                options_chain["handle_progressbars"] = "1"

            if options_array["file_size_is_given"] == "1":
                options_chain["file_size_is_given"] = "1"

            shards_count = int(options_array["shards_count"])

            logger.debug('Shard size: %s' % pointer['size'])

            part = pointer['index']
            logger.debug('Shard index %s' % part)

            self.tmp_path = options_array["tmp_path"]

            self.emit(QtCore.SIGNAL("setCurrentState"),
                      "Starting download threads...")
            self.emit(QtCore.SIGNAL("setCurrentState"),
                      "Started download shard at index %s..." % part)

            options_chain["rowposition"] = part
            self.shard_download_percent_list.append(0)

            # logger.debug(pointer)
            options_chain["shard_file_size"] = int(pointer['size'])
            # Generate download URL
            url = 'http://%s:%s/shards/%s?token=%s' % (
                pointer.get('farmer')['address'],
                str(pointer.get('farmer')['port']),
                pointer["hash"],
                pointer["token"])
            logger.debug(url)

            # Add a row to the table
            rowposition = self._add_shard_to_table(pointer,
                                                   part)

            print str(rowposition) + " pozycja2"
            print "TEST: download shard number %s with row number %s" % (
                part, self.rowposition2 - 1)

            if self.combine_tmpdir_name_with_token:
                self.create_download_connection(
                    url,
                    "%s-%s" % (
                        os.path.join(self.tmp_path,
                                     pointer['token'],
                                     file_name),
                        part),
                    options_chain,
                    self.rowposition2 - 1,
                    part)
            else:
                self.create_download_connection(
                    url,
                    '%s-%s' % (os.path.join(self.tmp_path, file_name), part),
                    options_chain,
                    self.rowposition2 - 1,
                    part)

            logger.debug('%s-%s' % (os.path.join(self.tmp_path, file_name), part))

        except IOError as e:
            logger.error('Perm error %s' % e)
            if str(e) == str(13):
                # Emit Storj Bridge Exception
                self.emit(
                    QtCore.SIGNAL('showException'),
                    'Error while saving or reading file or temporary file.\
Probably this is caused by insufficient permisions.Please check if you \
have permissions to write or read from selected directories.')
        except Exception as e:
            logger.debug('Unhandled error')
            logger.error(e)
