import json
# import logging
import os
from sys import platform
import requests
from PyQt4 import QtCore, QtGui

from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QProgressBar
from PyQt4.QtGui import QTableWidgetItem

from utilities.sharder import ShardingTools
from utilities.tools import Tools
from qt_interfaces.file_download_new import Ui_SingleFileDownload
from crypto.file_crypto_tools import FileCrypto
from engine import StorjEngine
import storj
# import storj.exception
import threading
import storj.exception as stjex

# from logs_backend import LogsUI
# from logs_backend import LogHandler, logger
from utilities.log_manager import logger

from resources.html_strings import html_format_begin, html_format_end
from utilities.account_manager import AccountManager
import time

"""
######################### Logging ####################
def get_global_logger(handler):
    class GlobalLogger(logging.getLoggerClass()):
        def __init__(self, name):
            logging.getLoggerClass().__init__(self, name)
            self.addHandler(handler)
    return GlobalLogger

######################################################
"""


class SingleFileDownloadUI(QtGui.QMainWindow):
    def __init__(self, parent=None, bucketid=None, fileid=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui_single_file_download = Ui_SingleFileDownload()
        self.ui_single_file_download.setupUi(self)
        # QtCore.QObject.connect(self.ui_single_file_download., QtCore.SIGNAL("clicked()"), self.save_config) # open bucket manager
        self.storj_engine = StorjEngine()  # init StorjEngine
        self.filename_from_bridge = ""
        self.tools = Tools()

        self.bucket_id = bucketid
        self.file_id = fileid

        # init loggers
        # self.log_handler = LogHandler()
        # logging.setLoggerClass(get_global_logger(self.log_handler))
        # logger.addHandler(self.log_handler)

        # self.initialize_shard_queue_table(file_pointers)

        self.account_manager = AccountManager()  # init AccountManager

        self.user_password = self.account_manager.get_user_password()

        ########3

        QtCore.QObject.connect(self.ui_single_file_download.file_path_select_bt, QtCore.SIGNAL("clicked()"),
                               self.select_file_save_path)  # open file select dialog
        QtCore.QObject.connect(self.ui_single_file_download.tmp_dir_bt, QtCore.SIGNAL("clicked()"),
                               self.select_tmp_directory)  # open tmp directory select dialog
        QtCore.QObject.connect(self.ui_single_file_download.start_download_bt, QtCore.SIGNAL("clicked()"),
                               lambda: self.createNewDownloadInitThread(bucketid,
                                                                        fileid))  # begin file downloading process

        #print fileid + " id pliku"
        # QtCore.QObject.connect(self.ui_single_file_download.open_log_bt, QtCore.SIGNAL("clicked()"),
        #                        self.open_logs_window)  # open logs window

        self.connect(self, QtCore.SIGNAL("incrementShardsDownloadProgressCounters"),
                     self.increment_shards_download_progress_counters)
        self.connect(self, QtCore.SIGNAL("updateShardDownloadProgress"), self.update_shard_download_progess)
        self.connect(self, QtCore.SIGNAL("beginShardDownloadProccess"), self.shard_download)
        self.connect(self, QtCore.SIGNAL("refreshOverallDownloadProgress"), self.refresh_overall_download_progress)
        self.connect(self, QtCore.SIGNAL("showDestinationFileNotSelectedError"), self.show_error_not_selected_file)
        self.connect(self, QtCore.SIGNAL("showInvalidDestinationPathError"), self.show_error_invalid_file_path)
        self.connect(self, QtCore.SIGNAL("showInvalidTemporaryDownloadPathError"),
                     self.show_error_invalid_temporary_path)
        self.connect(self, QtCore.SIGNAL("updateDownloadTaskState"), self.update_download_task_state)
        self.connect(self, QtCore.SIGNAL("showStorjBridgeException"), self.show_storj_bridge_exception)
        self.connect(self, QtCore.SIGNAL("showUnhandledException"), self.show_unhandled_exception)
        self.connect(self, QtCore.SIGNAL("showFileDownloadedSuccessfully"), self.show_download_finished_message)
        self.connect(self, QtCore.SIGNAL("showException"), self.show_unhandled_exception)
        self.connect(self, QtCore.SIGNAL("addRowToDownloadQueueTable"), self.add_row_download_queue_table)
        self.connect(self, QtCore.SIGNAL("getNextSetOfPointers"), self.request_and_download_next_set_of_pointers)

        self.connect(self, QtCore.SIGNAL("finishDownload"), lambda: self.create_download_finish_thread(os.path.split(str(self.ui_single_file_download.file_save_path.text()))[1]))
        #print "polaczono"

        self.shards_already_downloaded = 0

        self.createNewInitializationThread(bucketid, fileid)

        self.shard_download_percent_list = []

        # init limit variables
        self.max_retries_download_from_same_farmer = 3
        self.max_retries_get_file_pointers = 10

        # set default paths
        temp_dir = ""
        if platform == "linux" or platform == "linux2":
            # linux
            temp_dir = "/tmp/"
        elif platform == "darwin":
            # OS X
            temp_dir = "/tmp/"
        elif platform == "win32":
            # Windows
            temp_dir = "C:/Windows/temp/"

        self.ui_single_file_download.tmp_dir.setText(str(temp_dir))

        # set config variables

        self.combine_tmpdir_name_with_token = False

        # set overall progress to 0
        self.ui_single_file_download.overall_progress.setValue(0)

        self.current_active_connections = 0

        self.already_started_shard_downloads_count = 0

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

        #print "inijalizacja tabeli"


    def add_row_download_queue_table(self, row_data):
        self.download_queue_progressbar_list.append(QtGui.QProgressBar())

        self.download_queue_table_row_count = self.ui_single_file_download.shard_queue_table.rowCount()

        self.ui_single_file_download.shard_queue_table.setRowCount(self.download_queue_table_row_count + 1)

        self.ui_single_file_download.shard_queue_table.setCellWidget(self.download_queue_table_row_count, 0, self.download_queue_progressbar_list[self.download_queue_table_row_count])
        self.ui_single_file_download.shard_queue_table.setItem(self.download_queue_table_row_count, 1, QtGui.QTableWidgetItem(row_data["hash"]))
        self.ui_single_file_download.shard_queue_table.setItem(self.download_queue_table_row_count, 2, QtGui.QTableWidgetItem(str(row_data["farmer_address"]) + ":" + str(row_data["farmer_port"])))
        self.ui_single_file_download.shard_queue_table.setItem(self.download_queue_table_row_count, 3, QtGui.QTableWidgetItem(str(row_data["state"])))
        self.ui_single_file_download.shard_queue_table.setItem(self.download_queue_table_row_count, 4, QtGui.QTableWidgetItem(str(row_data["shard_index"])))

        self.download_queue_progressbar_list[self.download_queue_table_row_count].setValue(0)
        #print "dodawanie wiersza 2"


    def _add_shard_to_table(self, pointers_content, shard, chapters):
        """
        Add a row to the shard table and return the row number
        """
        # Add items to shard queue table view
        tablerowdata = {}
        tablerowdata["farmer_address"] = pointers_content["farmer"]["address"]
        tablerowdata["farmer_port"] = pointers_content["farmer"]["port"]
        tablerowdata["hash"] = str(pointers_content["hash"])
        tablerowdata["state"] = "Uploading..."
        tablerowdata["shard_index"] = str(chapters)

        # logger.warning('"log_event_type": "debug"')
        logger.debug('"title": "Contract negotiated"')
        logger.debug('"description": "Storage contract negotiated \
                     with: "' +
                     str(pointers_content["farmer"]["address"]) + ":" +
                     str(pointers_content["farmer"]["port"]))
        # logger.warning(str({"log_event_type": "debug", "title": "Contract negotiated",
        #                     "description": "Storage contract negotiated with: " + str(frame_content["farmer"]["address"] + ":" + str(frame_content["farmer"]["port"]))}))

        self.emit(QtCore.SIGNAL("addRowToDownloadQueueTable"), tablerowdata)  # add row to table

        rowcount = self.ui_single_file_download.shard_queue_table.rowCount()
        #print "dodawanie wiersza"

        return rowcount

    def show_download_finished_message(self):
        QMessageBox.information(self, "Success!", "File downloaded successfully!")

    """
    def open_logs_window(self):
        self.logs_window = LogsUI(self)
        self.logs_window.show()
    """

    def show_unhandled_exception(self, exception_content):
        QMessageBox.critical(self, "Unhandled error", str(exception_content))

    def show_storj_bridge_exception(self, exception_content):
        try:
            j = json.loads(str(exception_content))
            if j.get("error") == "Failed to get retrieval token":
                QMessageBox.critical(self, "Bridge error",
                                     str(j["error"]) +
                                     ". Please wait and try again.")
            else:
                QMessageBox.critical(self, "Bridge error", str(j["error"]))

        except:
            QMessageBox.critical(self, "Bridge error", str(exception_content))

    def update_download_task_state(self, row_position, state):
        self.ui_single_file_download.shard_queue_table.setItem(int(row_position), 3, QtGui.QTableWidgetItem(str(state)))

    def show_error_not_selected_file(self):
        QMessageBox.about(self, "Error", "Please select destination file save path!")

    def show_error_invalid_file_path(self):
        QMessageBox.about(self, "Error", "Destination file save path seems to be invalid!")

    def show_error_invalid_temporary_path(self):
        QMessageBox.about(self, "Error", "Temporary path seems to be invalid!")

    def refresh_overall_download_progress(self, base_percent):
        total_percent_to_download = self.all_shards_count * 100
        total_percent_downloaded = sum(self.shard_download_percent_list) * 100

        actual_percent_downloaded = total_percent_downloaded / total_percent_to_download

        total_percent = (base_percent * 100) + (0.90 * actual_percent_downloaded)

        logger.info(str(actual_percent_downloaded) + str(base_percent) +
                    "total_percent_downloaded")

        # actual_upload_progressbar_value = self.ui_single_file_upload.overall_progress.value()

        self.ui_single_file_download.overall_progress.setValue(int(total_percent))

    def create_download_finish_thread(self, file_name):
        download_finish_thread = threading.Thread(target=self.finish_download(file_name=file_name), args=())
        download_finish_thread.start()

    #### Begin file download finish function ####
    # Wait for signal to do shards joining and encryption
    def finish_download(self, file_name):
        print "konczenie downloadu"
        fileisencrypted = False
        if "[DECRYPTED]" in self.filename_from_bridge:
            fileisencrypted = False
        else:
            fileisencrypted = True


            # Join shards
        sharing_tools = ShardingTools()
        self.set_current_status("Joining shards...")
        # logger.warning(str({"log_event_type": "debug", "title": "Sharding", "description": "Joining shards..."}))
        # logger.warning('"log_event_type": "debug"')
        logger.debug('"title": "Sharding"')
        logger.debug('"description": "Joining shards..."')

        if fileisencrypted:
            sharing_tools.join_shards(self.tmp_path + "/" + str(file_name), "-",
                                      self.destination_file_path + ".encrypted")
        else:
            sharing_tools.join_shards(self.tmp_path + "/" + str(file_name), "-", self.destination_file_path)

        logger.debug(self.tmp_path + "/" + str(file_name) + ".encrypted")

        if fileisencrypted:
            # decrypt file
            self.set_current_status("Decrypting file...")
            # logger.warning(str({"log_event_type": "debug", "title": "Decryption", "description": "Decrypting file..."}))
            # logger.warning('"log_event_type": "debug"')
            logger.debug('"title": "Decryption"')
            logger.debug('"description": "Decrypting file..."')
            # self.set_current_status()
            file_crypto_tools = FileCrypto()
            file_crypto_tools.decrypt_file("AES", str(self.destination_file_path) + ".encrypted",
                                           self.destination_file_path,
                                           str(self.user_password))  # begin file decryption

        logger.debug("pobrano")
        # logger.warning(str({"log_event_type": "success", "title": "Finished", "description": "Downloading completed successfully!"}))
        # logger.warning('"log_event_type": "success"')
        logger.debug('"title": "Finished"')
        logger.debug('"description": "Downloading completed successfully!"')
        self.emit(QtCore.SIGNAL("showFileDownloadedSuccessfully"))

        return True

    def request_and_download_next_set_of_pointers(self):
        print "nowe wskazniki"
        i = self.already_started_shard_downloads_count
        i2 = 1
        while i < self.all_shards_count and self.current_active_connections+i2 < 4:
            i2 += 1
            tries_get_file_pointers = 0
            while self.max_retries_get_file_pointers > tries_get_file_pointers:
                tries_get_file_pointers += 1
                try:
                    options_array = {}
                    options_array["tmp_path"] = self.tmp_path
                    options_array["progressbars_enabled"] = "1"
                    options_array["file_size_is_given"] = "1"
                    options_array["shards_count"] = str(self.all_shards_count)
                    shard_pointer = self.storj_engine.storj_client.file_pointers(str(self.bucket_id), self.file_id, limit="1",
                                                                                 skip=str(i))
                    print shard_pointer[0]
                    options_array["shard_index"] = shard_pointer[0]["index"]

                    options_array["file_size_shard_" + str(i)] = shard_pointer[0]["size"]
                    self.emit(QtCore.SIGNAL("beginShardDownloadProccess"), shard_pointer[0],
                              self.destination_file_path, options_array)
                except stjex.StorjBridgeApiError as e:
                    logger.debug('"title": "Bridge error"')
                    logger.debug('"description": "Error while resolving file pointers \
                                                         to download file with ID: "' +
                                 str(self.file_id) + "...")
                    self.emit(QtCore.SIGNAL("showStorjBridgeException"), str(e))  # emit Storj Bridge Exception
                    continue
                else:
                    break


            self.already_started_shard_downloads_count += 1

            i += 1
        return 1

    def retry_download_with_new_pointer(self, shard_index):
        print "ponowienie"
        tries_get_file_pointers = 0
        while self.max_retries_get_file_pointers > tries_get_file_pointers:
            tries_get_file_pointers += 1
            try:
                options_array = {}
                options_array["tmp_path"] = self.tmp_path
                options_array["progressbars_enabled"] = "1"
                options_array["file_size_is_given"] = "1"
                options_array["shards_count"] = str(self.all_shards_count)
                shard_pointer = self.storj_engine.storj_client.file_pointers(str(self.bucket_id), self.file_id, limit="1",
                                                                             skip=str(shard_index))
                print shard_pointer[0]
                options_array["shard_index"] = shard_pointer[0]["index"]

                options_array["file_size_shard_" + str(shard_index)] = shard_pointer[0]["size"]
                self.emit(QtCore.SIGNAL("beginShardDownloadProccess"), shard_pointer[0],
                          self.destination_file_path, options_array)
            except stjex.StorjBridgeApiError as e:
                logger.debug('"title": "Bridge error"')
                logger.debug('"description": "Error while resolving file pointers \
                                                         to download file"')
                self.emit(QtCore.SIGNAL("showStorjBridgeException"), str(e))  # emit Storj Bridge Exception
                continue
            else:
                break

        return 1

    def download_begin(self, bucket_id, file_id):




        self.all_shards_count = self.get_file_pointers_count(bucket_id, file_id)

        self.destination_file_path = str(self.ui_single_file_download.file_save_path.text())
        self.tmp_path = str(self.ui_single_file_download.tmp_dir.text())
        file_name = os.path.split(self.destination_file_path)[1]


        try:
            # logger.warning("log_event_type": "debug")
            logger.debug('"title": "File pointers"')
            logger.debug('"description": "Resolving file pointers to download\
                         file with ID: "' +
                         str(file_id) + "...")
            # logger.warning(str({"log_event_type": "debug", "title": "File pointers",
            #                     "description": "Resolving file pointers to download file with ID: " + str(
            #                         file_id) + "..."}))
            #get_file_pointers_count(self, bucket_id, file_id)

            i = 0
            #while i < self.all_shards_count:
            while i < 4:
                tries_get_file_pointers = 0
                while self.max_retries_get_file_pointers > tries_get_file_pointers:
                    tries_get_file_pointers += 1
                    time.sleep(1)
                    try:
                        options_array = {}
                        options_array["tmp_path"] = self.tmp_path
                        options_array["progressbars_enabled"] = "1"
                        options_array["file_size_is_given"] = "1"
                        options_array["shards_count"] = str(self.all_shards_count)
                        shard_pointer = self.storj_engine.storj_client.file_pointers(str(bucket_id), file_id, limit="1",
                                                                                     skip=str(i))
                        print shard_pointer[0]
                        options_array["shard_index"] = shard_pointer[0]["index"]

                        options_array["file_size_shard_" + str(i)] = shard_pointer[0]["size"]
                        self.emit(QtCore.SIGNAL("beginShardDownloadProccess"), shard_pointer[0],
                                  self.destination_file_path, options_array)
                    except stjex.StorjBridgeApiError as e:
                        logger.debug('"title": "Bridge error"')
                        logger.debug('"description": "Error while resolving file pointers \
                                                 to download file with ID: "' +
                                     str(file_id) + "...")
                        self.emit(QtCore.SIGNAL("showStorjBridgeException"), str(e))  # emit Storj Bridge Exception
                        continue
                    else:
                        break


                self.already_started_shard_downloads_count += 1

                i += 1


        except storj.exception.StorjBridgeApiError as e:
            # logger.warning("log_event_type": "error")
            logger.debug('"title": "Bridge error"')
            logger.debug('"description": "Error while resolving file pointers \
                         to download file with ID: "' +
                         str(file_id) + "...")
            # logger.warning(str({"log_event_type": "error", "title": "Bridge error",
            #                     "description": "Error while resolving file pointers to download file with ID: " + str(
            #                         file_id) + "..."}))
            self.emit(QtCore.SIGNAL("showStorjBridgeException"), str(e))  # emit Storj Bridge Exception
        #except Exception as e:
            # logger.warning('"log_event_type": "error"')
         #   logger.debug('"title": "Unhandled error"'),
          #  logger.debug('"description": "Unhandled error while resolving file\
            #             pointers to download file with ID: "' +
             #            str(file_id) + "...")
            # logger.warning(str({"log_event_type": "error", "title": "Unhandled error",
            #                     "description": "Unhandled error while resolving file pointers to download file with ID: " + str(
            #                         file_id) + "..."}))
          #  self.emit(QtCore.SIGNAL("showUnhandledException"), str(e))  # emit unhandled Exception
          #  logger.error(e)



        i = 0
        # model = QStandardItemModel(1, 1)  # initialize model for inserting to table






        #options_array["file_pointers"] = file_pointers
        #options_array["file_pointers_is_given"] = "1"
        #options_array["progressbars_enabled"] = "1"
        #options_array["file_size_is_given"] = "1"
        #options_array["shards_count"] = i

        #self.all_shards_count = i

        #self.ui_single_file_download.total_shards.setText(html_format_begin + str(i) + html_format_end)

        # storj_sdk_overrides = StorjSDKImplementationsOverrides()

        # self.file_download(None, None, "/home/lakewik/kotek2", options_array, self.progressbar_list)
        #self.file_download(None, None, self.destination_file_path, options_array, self.progressbar_list)
        # progressbar_list[0].setValue(20)
        # progressbar_list[2].setValue(17)
        #print "koniec"

    def createNewDownloadInitThread(self, bucket_id, file_id):
        self.ui_single_file_download.overall_progress.setValue(0)
        self.initialize_download_queue_table()
        file_name_resolve_thread = threading.Thread(target=self.download_begin, args=(bucket_id, file_id))
        file_name_resolve_thread.start()

    def createNewInitializationThread(self, bucket_id, file_id):
        file_name_resolve_thread = threading.Thread(target=self.set_file_metadata, args=(bucket_id, file_id))
        file_name_resolve_thread.start()

    def get_file_frame_id(self, bucket_id, file_id):
        try:
            file_metadata = self.storj_engine.storj_client.file_metadata(str(bucket_id),
                                                                         str(file_id))
            self.file_frame = file_metadata.frame

        except storj.exception.StorjBridgeApiError as e:
            self.emit(QtCore.SIGNAL("showStorjBridgeException"),
                      "Error while resolving file frame ID. " + str(e))  # emit Storj Bridge Exception
        except Exception as e:
            self.emit(QtCore.SIGNAL("showUnhandledException"),
                      "Unhandled error while resolving file frame ID. " + str(e))  # emit unhandled Exception
        else:
            return self.file_frame

    def set_file_metadata(self, bucket_id, file_id):
        try:
            file_metadata = self.storj_engine.storj_client.file_metadata(str(bucket_id),
                                                                         str(file_id))
            self.ui_single_file_download.file_name.setText(
               str(file_metadata.filename.replace("[DECRYPTED]", "")))

            tools = Tools()
            #self.ui_single_file_download.file_size.setText(
             #   html_format_begin + str(tools.human_size(int(file_metadata.size))) + html_format_end)
            self.ui_single_file_download.file_id.setText(str(file_id))

            self.ui_single_file_download.file_save_path.setText(
                str(tools.get_home_user_directory() + "/" + str(file_metadata.filename.replace("[DECRYPTED]", ""))))

            self.filename_from_bridge = str(file_metadata.filename)

            self.resolved_file_metadata = True

        except storj.exception.StorjBridgeApiError as e:
            self.emit(QtCore.SIGNAL("showStorjBridgeException"),
                      "Error while resolving file metadata. " + str(e))  # emit Storj Bridge Exception
        except Exception as e:
            self.emit(QtCore.SIGNAL("showUnhandledException"),
                      "Unhandled error while resolving file metadata. " + str(e))  # emit unhandled Exception

    def update_shard_download_progess(self, row_position_index, value):
        self.download_queue_progressbar_list[row_position_index].setValue(value)
        return 1

    def increment_shards_download_progress_counters(self):
        #self.shards_already_downloaded += 1
        self.ui_single_file_download.downloaded_shards.setText(
            html_format_begin + str(self.shards_already_downloaded) + html_format_end)

    def set_current_status(self, current_status):
        print 1
        #self.ui_single_file_download.current_state.setText(html_format_begin + current_status + html_format_end)

    def select_tmp_directory(self):
        self.selected_tmp_dir = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', '',
                                                                       QtGui.QFileDialog.ShowDirsOnly)
        self.ui_single_file_download.tmp_dir.setText(str(self.selected_tmp_dir))

    def get_file_pointers_count(self, bucket_id, file_id):
        file_frame = self.get_file_frame_id(bucket_id, file_id)
        frame_data = self.storj_engine.storj_client.frame_get(file_frame.id)
        return len(frame_data.shards)

    def select_file_save_path(self):
        file_save_path = QtGui.QFileDialog.getSaveFileName(self, 'Save file to...', '')
        self.ui_single_file_download.file_save_path.setText(str(file_save_path))

    def calculate_final_hmac(self):
        return 1

    def create_download_connection(self, url, path_to_save, options_chain, rowposition, shard_index):
        local_filename = path_to_save
        downloaded = False
        farmer_tries = 0

        # logger.warning('"log_event_type": "debug"')
        logger.debug('"title": "Downloading"')
        logger.debug('"description": "Downloading shard at index "' +
                     str(shard_index) + " from farmer: " +
                     str(url))
        # logger.warning(str({"log_event_type": "debug", "title": "Downloading",
        #                    "description": "Downloading shard at index " + str(shard_index) + " from farmer: " + str(
        #                        url)}))

        tries_download_from_same_farmer = 0
        while self.max_retries_download_from_same_farmer > tries_download_from_same_farmer:
            tries_download_from_same_farmer += 1
            farmer_tries += 1
            try:
                self.current_active_connections += 1
                self.emit(QtCore.SIGNAL("updateDownloadTaskState"), rowposition,
                          "Downloading...")  # update shard downloading state
                if options_chain["handle_progressbars"] != "1":
                    r = requests.get(url)
                    # requests.
                    with open(local_filename, 'wb') as f:
                        for chunk in r.iter_content(chunk_size=1024):
                            if chunk:  # filter out keep-alive new chunks
                                f.write(chunk)
                else:
                    r = requests.get(url, stream=True)
                    f = open(local_filename, 'wb')
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
                    logger.debug(str(t1) + "kotek")
                    for chunk in r.iter_content(32 * 1024):
                        i += 1
                        f.write(chunk)
                        logger.debug(str(i) + " " + str(t1))
                        logger.debug(round(float(i) / float(t1), 1))
                        logger.debug(str(int(round((100.0 * i) / t1))) + " %")
                        if int(round((100.0 * i) / t1)) > 100:
                            percent_downloaded = 100
                        else:
                            percent_downloaded = int(round((100.0 * i) / t1))
                        self.emit(QtCore.SIGNAL("updateShardDownloadProgress"), int(rowposition),
                                  percent_downloaded)  # update progress bar in upload queue table
                        self.shard_download_percent_list[shard_index] = percent_downloaded
                        self.emit(QtCore.SIGNAL("refreshOverallDownloadProgress"),
                                  0.1)  # update progress bar in upload queue table
                        logger.debug(str(rowposition) + "pozycja")
                        # progress_bar.setValue(percent_downloaded)

                    f.close()
                    downloaded = True
                if r.status_code != 200 and r.status_code != 304:
                    raise stjex.StorjFarmerError()
                
            except stjex.StorjFarmerError as e:
                self.emit(QtCore.SIGNAL("updateDownloadTaskState"), rowposition,
                          "First try failed. Retrying... (" + str(farmer_tries) + ")")  # update shard download state
                continue

            except Exception as e:
                logger.error(e)
                # logger.warning('"log_event_type": "warning"')
                logger.debug('"title": "Unhandled error"')
                logger.debug('"description": "Error occured while downloading\
                             shard at index "' + str(shard_index) +
                             ". Retrying... (" + str(farmer_tries) + ")")
                # logger.warning(str({"log_event_type": "warning", "title": "Unhandled error",
                #                     "description": "Error occured while downloading shard at index " + str(
                #                         shard_index) + ". Retrying... (" + str(farmer_tries) + ")"}))

                self.emit(QtCore.SIGNAL("updateDownloadTaskState"), rowposition,
                          "First try failed. Retrying... (" + str(farmer_tries) + ")")  # update shard download state
                continue
            else:
                downloaded = True
                break

        if not downloaded:
            self.current_active_connections -= 1
            self.emit(QtCore.SIGNAL("updateDownloadTaskState"), rowposition,
                      "Error while downloading from this farmer. Getting another farmer pointer...")  # update shard download state
            self.emit(QtCore.SIGNAL("retryWithNewDownloadPointer"),
                      shard_index)  # retry download with new download pointer

        else:
            self.emit(QtCore.SIGNAL("getNextSetOfPointers"))
            self.current_active_connections -= 1
            # logger.warning(str({"log_event_type": "success", "title": "Shard downloaded", "description": "Shard at index " + str(shard_index) + " downloaded successfully."}))
            # logger.warning('"log_event_type": "success"')
            logger.debug('"title": "Shard downloaded"')
            logger.debug('"description": "Shard at index "' +
                         str(shard_index) +
                         " downloaded successfully.")
            self.shards_already_downloaded += 1
            self.emit(QtCore.SIGNAL("incrementShardsDownloadProgressCounters"))  # update already uploaded shards count
            self.emit(QtCore.SIGNAL("updateDownloadTaskState"), rowposition,
                      "Downloaded!")  # update shard download state
            if int(self.all_shards_count) <= int(self.shards_already_downloaded):
                self.emit(QtCore.SIGNAL(
                    "finishDownload"))  # send signal to begin file shards joind and decryption after all shards are downloaded
                #print "sygnal konca pobierania" + str(self.all_shards_count) + " " + str(self.shards_already_downloaded)


            return

    def createNewDownloadThread(self, url, filelocation, options_chain, rowposition, shard_index):
        # self.download_thread = DownloadTaskQtThread(url, filelocation, options_chain, progress_bars_list)
        # self.download_thread.start()
        # self.download_thread.connect(self.download_thread, SIGNAL('setStatus'), self.test1, Qt.QueuedConnection)
        # self.download_thread.tick.connect(progress_bars_list.setValue)

        # Refactor to QtTrhead
        download_thread = threading.Thread(target=self.create_download_connection,
                                           args=(url, filelocation, options_chain, rowposition,
                                                 shard_index))
        download_thread.start()
        logger.debug(str(options_chain["rowposition"]) + "position")

    def test1(self, value1, value2):
        logger.debug(str(value1) + " aaa " + str(value2))

    def shard_download(self, pointer, file_save_path, options_array):
        # logger.warning(str({"log_event_type": "debug", "title": "Downloading", "description": "Beginning download proccess..."}))
        # logger.warning('"log_event_type": "debug"')
        logger.debug('"title": "Downloading"')
        logger.debug('"description": "Beginning download proccess..."')
        options_chain = {}
        #self.storj_engine.storj_client.logger.info('file_pointers(%s, %s)', bucket_id, file_id)
        file_name = os.path.split(file_save_path)[1]

        ##### End file download finish point #####

        try:
            # check ability to write files to selected directories
            if self.tools.isWritable(os.path.split(file_save_path)[0]) != True:
                raise IOError("13")
            if self.tools.isWritable(self.tmp_path) != True:
                raise IOError("13")

            try:
                if options_array["progressbars_enabled"] == "1":
                    options_chain["handle_progressbars"] = "1"

                if options_array["file_size_is_given"] == "1":
                    options_chain["file_size_is_given"] = "1"



                shards_count = int(options_array["shards_count"])

                shard_size_array = []
                shard_size_array.append(int(options_array["file_size_shard_" + str(options_array["shard_index"])]))
                logger.debug(shard_size_array)

                part = options_array["shard_index"]

                self.tmp_path = options_array["tmp_path"]

                self.set_current_status("Starting download threads...")

                self.set_current_status("Downloading shard at index " + str(part) + "...")
                options_chain["rowposition"] = part
                self.shard_download_percent_list.append(0)

                rowposition = self._add_shard_to_table(pointer,
                                                       0,
                                                       part)  # Add a row to the table

                logger.debug(pointer)
                options_chain["shard_file_size"] = shard_size_array[0]
                url = "http://" + pointer.get('farmer')['address'] + \
                      ":" + \
                      str(pointer.get('farmer')['port']) + \
                      "/shards/" + pointer["hash"] + \
                      "?token=" + pointer["token"]
                logger.debug(url)

                if self.combine_tmpdir_name_with_token:
                    self.createNewDownloadThread(url, self.tmp_path + "/" +
                                                 str(pointer["token"]) +
                                                 "/" +
                                                 str(file_name) +
                                                 "-" + str(part),
                                                 options_chain,
                                                 part, part)
                else:
                    self.createNewDownloadThread(url, self.tmp_path + "/" + str(file_name) + "-" + str(part),
                                                 options_chain, part, part)

                logger.debug(self.tmp_path + "/" + str(file_name) + "-" +
                             str(part) + "zapisane")
                part = part + 1


            except Exception as e:
                logger.error(e)
                # logger.warning('"log_event_type": "warning"')
                logger.debug('"title": "Unhandled error"' + str(e))
                    #except Exception as e:
             #   self.emit(QtCore.SIGNAL("showStorjBridgeException"),
              #            "Unhandled error while resolving file pointers for download. " + str(
               #               e))  # emit unhandled Exception

        except IOError as e:
            print " perm error " + str(e)
            if str(e) == str(13):
                self.emit(QtCore.SIGNAL("showException"),
                    "Error while saving or reading file or temporary file. Probably this is caused by insufficient permisions. Please check if you have permissions to write or read from selected directories.  ")  # emit Storj Bridge Exception

        except Exception as e:
            logger.error(e)
            # logger.warning('"log_event_type": "warning"')
            logger.debug('"title": "Unhandled error"')
        #except Exception as e:
         #   self.emit(QtCore.SIGNAL("showException"),
          #            "Unhandled exception: " + str(e) )

         #   logger.debug("Unhandled exception " + str(e))


