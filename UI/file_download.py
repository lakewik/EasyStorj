import json
# import logging
import os

import requests
from PyQt4 import QtCore, QtGui

from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QProgressBar
from PyQt4.QtGui import QTableWidgetItem

from utilities.sharder import ShardingTools
from utilities.tools import Tools
from qt_interfaces.single_file_downloader_ui import Ui_SingleFileDownload
from crypto.file_crypto_tools import FileCrypto
from engine import StorjEngine
import storj
# import storj.exception
import threading

# from logs_backend import LogsUI
# from logs_backend import LogHandler, logger
from utilities.log_manager import logger

from resources.html_strings import html_format_begin, html_format_end
from utilities.account_manager import AccountManager

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

        self.tools = Tools()

        # init loggers
        # self.log_handler = LogHandler()
        # logging.setLoggerClass(get_global_logger(self.log_handler))
        # logger.addHandler(self.log_handler)

        # self.initialize_shard_queue_table(file_pointers)

        self.account_manager = AccountManager()  # init AccountManager

        self.user_password = self.account_manager.get_user_password()

        ########3

        QtCore.QObject.connect(self.ui_single_file_download.file_save_path_bt, QtCore.SIGNAL("clicked()"),
                               self.select_file_save_path)  # open file select dialog
        QtCore.QObject.connect(self.ui_single_file_download.tmp_dir_bt, QtCore.SIGNAL("clicked()"),
                               self.select_tmp_directory)  # open tmp directory select dialog
        QtCore.QObject.connect(self.ui_single_file_download.start_download_bt, QtCore.SIGNAL("clicked()"),
                               lambda: self.createNewDownloadInitThread(bucketid, fileid))  # begin file downloading process

        # QtCore.QObject.connect(self.ui_single_file_download.open_log_bt, QtCore.SIGNAL("clicked()"),
        #                        self.open_logs_window)  # open logs window

        self.connect(self, QtCore.SIGNAL("incrementShardsDownloadProgressCounters"), self.increment_shards_download_progress_counters)
        self.connect(self, QtCore.SIGNAL("updateShardDownloadProgress"), self.update_shard_download_progess)
        self.connect(self, QtCore.SIGNAL("beginDownloadProccess"), self.download_begin)
        self.connect(self, QtCore.SIGNAL("refreshOverallDownloadProgress"), self.refresh_overall_download_progress)
        self.connect(self, QtCore.SIGNAL("showDestinationFileNotSelectedError"), self.show_error_not_selected_file)
        self.connect(self, QtCore.SIGNAL("showInvalidDestinationPathError"), self.show_error_invalid_file_path)
        self.connect(self, QtCore.SIGNAL("showInvalidTemporaryDownloadPathError"), self.show_error_invalid_temporary_path)
        self.connect(self, QtCore.SIGNAL("updateDownloadTaskState"), self.update_download_task_state)
        self.connect(self, QtCore.SIGNAL("showStorjBridgeException"), self.show_storj_bridge_exception)
        self.connect(self, QtCore.SIGNAL("showUnhandledException"), self.show_unhandled_exception)
        self.connect(self, QtCore.SIGNAL("showFileDownloadedSuccessfully"), self.show_download_finished_message)

        self.shards_already_downloaded = 0

        self.createNewInitializationThread(bucketid, fileid)

        self.shard_download_percent_list = []

        # init limit variables
        self.max_retries_download_from_same_farmer = 3
        self.max_retries_get_file_pointers = 10

        # set default paths
        self.ui_single_file_download.tmp_dir.setText(str("/tmp/"))

        # set config variables

        self.combine_tmpdir_name_with_token = False

        # set overall progress to 0
        self.ui_single_file_download.overall_progress.setValue(0)

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

    def download_begin(self, file_pointers):
        self.destination_file_path = str(self.ui_single_file_download.file_save_path.text())
        self.tmp_path = str(self.ui_single_file_download.tmp_dir.text())

        options_array = {}
        options_array["tmp_path"] = self.tmp_path

        i = 0
        # model = QStandardItemModel(1, 1)  # initialize model for inserting to table

        self.ui_single_file_download.shard_queue_table.setColumnCount(5)
        self.ui_single_file_download.shard_queue_table.setRowCount(len(file_pointers))

        self.ui_single_file_download.shard_queue_table.setHorizontalHeaderLabels(
            ['Progress', 'Hash', 'Farmer addres', 'State', 'Shard index'])
        for pointer in file_pointers:
            item = QTableWidgetItem(str(""))
            self.ui_single_file_download.shard_queue_table.setItem(i, 0, item)  # row, column, item (QStandardItem)

            item = QTableWidgetItem(str(pointer["hash"]))
            self.ui_single_file_download.shard_queue_table.setItem(i, 1, item)  # row, column, item (QStandardItem)

            item = QTableWidgetItem(str(pointer["farmer"]["address"] + ":" + str(pointer["farmer"]["port"])))
            self.ui_single_file_download.shard_queue_table.setItem(i, 2, item)  # row, column, item (QStandardItem)

            item = QTableWidgetItem(str("Waiting..."))
            self.ui_single_file_download.shard_queue_table.setItem(i, 3, item)  # row, column, item (QStandardItem)

            item = QTableWidgetItem(str(pointer["index"]))
            self.ui_single_file_download.shard_queue_table.setItem(i, 4, item)  # row, column, item (QStandardItem)

            options_array["file_size_shard_" + str(i)] = pointer["size"]
            i = i + 1
            # print  str(pointer["index"])+"index"

        self.ui_single_file_download.shard_queue_table.clearFocus()
        self.ui_single_file_download.shard_queue_table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        i2 = 0
        self.progressbar_list = []
        for pointer in file_pointers:
            tablemodel = self.ui_single_file_download.shard_queue_table.model()
            index = tablemodel.index(i2, 0)
            self.progressbar_list.append(QProgressBar())
            self.ui_single_file_download.shard_queue_table.setIndexWidget(index, self.progressbar_list[i2])
            i2 = i2 + 1

        options_array["file_pointers"] = file_pointers
        options_array["file_pointers_is_given"] = "1"
        options_array["progressbars_enabled"] = "1"
        options_array["file_size_is_given"] = "1"
        options_array["shards_count"] = i

        self.all_shards_count = i

        self.ui_single_file_download.total_shards.setText(html_format_begin + str(i) + html_format_end)

        # storj_sdk_overrides = StorjSDKImplementationsOverrides()

        # self.file_download(None, None, "/home/lakewik/kotek2", options_array, self.progressbar_list)
        self.file_download(None, None, self.destination_file_path, options_array, self.progressbar_list)
        # progressbar_list[0].setValue(20)
        # progressbar_list[2].setValue(17)

    def createNewDownloadInitThread(self, bucket_id, file_id):
        self.ui_single_file_download.overall_progress.setValue(0)
        file_name_resolve_thread = threading.Thread(target=self.init_download_file_pointers, args=(bucket_id, file_id))
        file_name_resolve_thread.start()

    def createNewInitializationThread(self, bucket_id, file_id):
        file_name_resolve_thread = threading.Thread(target=self.set_file_metadata, args=(bucket_id, file_id))
        file_name_resolve_thread.start()

    def set_file_metadata(self, bucket_id, file_id):
        try:
            file_metadata = self.storj_engine.storj_client.file_metadata(str(bucket_id),
                                                                         str(file_id))
            self.ui_single_file_download.file_name.setText(
                html_format_begin + str(file_metadata.filename) + html_format_end)

            tools = Tools()
            self.ui_single_file_download.file_size.setText(
                html_format_begin + str(tools.human_size(int(file_metadata.size))) + html_format_end)
            self.ui_single_file_download.file_id.setText(html_format_begin + str(file_id) + html_format_end)

            self.ui_single_file_download.file_save_path.setText(
                str(tools.get_home_user_directory() + "/" + str(file_metadata.filename)))
        except storj.exception.StorjBridgeApiError as e:
            self.emit(QtCore.SIGNAL("showStorjBridgeException"), "Error while resolving file metadata. " + str(e))  # emit Storj Bridge Exception
        except Exception as e:
            self.emit(QtCore.SIGNAL("showUnhandledException"), "Unhandled error while resolving file metadata. " + str(e))  # emit unhandled Exception

    def update_shard_download_progess(self, row_position_index, value):
        self.progressbar_list[row_position_index].setValue(value)
        return 1

    def increment_shards_download_progress_counters(self):
        self.shards_already_downloaded += 1
        self.ui_single_file_download.downloaded_shards.setText(html_format_begin + str(self.shards_already_downloaded) + html_format_end)

    def set_current_status(self, current_status):
        self.ui_single_file_download.current_state.setText(html_format_begin + current_status + html_format_end)

    def select_tmp_directory(self):
        self.selected_tmp_dir = QtGui.QFileDialog.getExistingDirectory(None, 'Select a folder:', '',
                                                                       QtGui.QFileDialog.ShowDirsOnly)
        self.ui_single_file_download.tmp_dir.setText(str(self.selected_tmp_dir))

    def init_download_file_pointers(self, bucket_id, file_id):
        try:
            # logger.warning("log_event_type": "debug")
            logger.debug('"title": "File pointers"')
            logger.debug('"description": "Resolving file pointers to download\
                         file with ID: "' +
                         str(file_id) + "...")
            # logger.warning(str({"log_event_type": "debug", "title": "File pointers",
            #                     "description": "Resolving file pointers to download file with ID: " + str(
            #                         file_id) + "..."}))

            file_pointers = self.storj_engine.storj_client.file_pointers(str(bucket_id), file_id)
            self.emit(QtCore.SIGNAL("beginDownloadProccess"), file_pointers)
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
        except Exception as e:
            # logger.warning('"log_event_type": "error"')
            logger.debug('"title": "Unhandled error"'),
            logger.debug('"description": "Unhandled error while resolving file\
                         pointers to download file with ID: "' +
                         str(file_id) + "...")
            # logger.warning(str({"log_event_type": "error", "title": "Unhandled error",
            #                     "description": "Unhandled error while resolving file pointers to download file with ID: " + str(
            #                         file_id) + "..."}))
            self.emit(QtCore.SIGNAL("showUnhandledException"), str(e))  # emit unhandled Exception
            logger.error(e)

    def select_file_save_path(self):
        file_save_path = QtGui.QFileDialog.getSaveFileName(self, 'Save file to...', '')
        self.ui_single_file_download.file_save_path.setText(str(file_save_path))

    def calculate_final_hmac(self):
        return 1

    def create_download_connection(self, url, path_to_save, options_chain, progress_bar, rowposition, shard_index):
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
                self.emit(QtCore.SIGNAL("updateDownloadTaskState"), rowposition, "Downloading...")  # update shard downloading state
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
                        self.emit(QtCore.SIGNAL("updateShardDownloadProgress"), int(rowposition), percent_downloaded)  # update progress bar in upload queue table
                        self.shard_download_percent_list[shard_index] = percent_downloaded
                        self.emit(QtCore.SIGNAL("refreshOverallDownloadProgress"), 0.1)  # update progress bar in upload queue table
                        logger.debug(str(rowposition) + "pozycja")
                        # progress_bar.setValue(percent_downloaded)

                    f.close()
                    downloaded = True
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
            self.emit(QtCore.SIGNAL("retryWithNewDownloadPointer"), options_chain["shard_index"])  # retry download with new download pointer
        else:
            # logger.warning(str({"log_event_type": "success", "title": "Shard downloaded", "description": "Shard at index " + str(shard_index) + " downloaded successfully."}))
            # logger.warning('"log_event_type": "success"')
            logger.debug('"title": "Shard downloaded"')
            logger.debug('"description": "Shard at index "' +
                         str(shard_index) +
                         " downloaded successfully.")
            self.emit(QtCore.SIGNAL("incrementShardsDownloadProgressCounters"))  # update already uploaded shards count
            self.emit(QtCore.SIGNAL("updateDownloadTaskState"), rowposition,
                      "Downloaded!")  # update shard download state
            if int(self.all_shards_count) <= int(self.shards_already_downloaded + 1):
                self.emit(QtCore.SIGNAL("finishDownload"))  # send signal to begin file shards joind and decryption after all shards are downloaded

            return

    def createNewDownloadThread(self, url, filelocation, options_chain, progress_bars_list, rowposition, shard_index):
        # self.download_thread = DownloadTaskQtThread(url, filelocation, options_chain, progress_bars_list)
        # self.download_thread.start()
        # self.download_thread.connect(self.download_thread, SIGNAL('setStatus'), self.test1, Qt.QueuedConnection)
        # self.download_thread.tick.connect(progress_bars_list.setValue)

        # Refactor to QtTrhead
        download_thread = threading.Thread(target=self.create_download_connection,
                                           args=(url, filelocation, options_chain, progress_bars_list, rowposition, shard_index))
        download_thread.start()
        logger.debug(str(options_chain["rowposition"]) + "position")

    def test1(self, value1, value2):
        logger.debug(str(value1) + " aaa " + str(value2))

    def upload_file(self):
        logger.debug(1)

    def file_download(self, bucket_id, file_id, file_save_path, options_array, progress_bars_list):
        # logger.warning(str({"log_event_type": "debug", "title": "Downloading", "description": "Beginning download proccess..."}))
        # logger.warning('"log_event_type": "debug"')
        logger.debug('"title": "Downloading"')
        logger.debug('"description": "Beginning download proccess..."')
        options_chain = {}
        self.storj_engine.storj_client.logger.info('file_pointers(%s, %s)', bucket_id, file_id)
        file_name = os.path.split(file_save_path)[1]

        #### Begin file download finish function ####
        # Wait for signal to do shards joining and encryption
        def finish_download(self):

            fileisencrypted = False

            # Join shards
            sharing_tools = ShardingTools()
            self.set_current_status("Joining shards...")
            # logger.warning(str({"log_event_type": "debug", "title": "Sharding", "description": "Joining shards..."}))
            # logger.warning('"log_event_type": "debug"')
            logger.debug('"title": "Sharding"')
            logger.debug('"description": "Joining shards..."')

            if fileisencrypted:
                sharing_tools.join_shards(self.tmp_path + "/" + str(file_name), "-", file_save_path + ".encrypted")
            else:
                sharing_tools.join_shards(self.tmp_path + "/" + str(file_name), "-", file_save_path)

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
                file_crypto_tools.decrypt_file("AES", str(file_save_path) + ".encrypted", file_save_path, str(self.user_password))  # begin file decryption

            logger.debug("pobrano")
            # logger.warning(str({"log_event_type": "success", "title": "Finished", "description": "Downloading completed successfully!"}))
            # logger.warning('"log_event_type": "success"')
            logger.debug('"title": "Finished"')
            logger.debug('"description": "Downloading completed successfully!"')
            self.emit(QtCore.SIGNAL("showFileDownloadedSuccessfully"))

            return True

        self.connect(self, QtCore.SIGNAL("finishDownload"), lambda: finish_download(self))

        ##### End file download finish point #####

        get_file_pointers_tries = 0
        while self.max_retries_get_file_pointers > get_file_pointers_tries:
            get_file_pointers_tries += 1
            try:
                # Determine file pointers
                if options_array["file_pointers_is_given"] == "1":
                    pointers = options_array["file_pointers"]
                else:
                    pointers = self.storj_engine.storj_client.file_pointers(bucket_id=bucket_id, file_id=file_id)

                if options_array["progressbars_enabled"] == "1":
                    options_chain["handle_progressbars"] = "1"

                if options_array["file_size_is_given"] == "1":
                    options_chain["file_size_is_given"] = "1"

                shards_count = int(options_array["shards_count"])

                i = 0
                shard_size_array = []
                while i < shards_count:
                    shard_size_array.append(int(options_array["file_size_shard_" + str(i)]))
                    i += 1
                logger.debug(shard_size_array)
                part = 0

                self.tmp_path = options_array["tmp_path"]

                self.set_current_status("Starting download threads...")
                for pointer in pointers:
                    self.set_current_status("Downloading shard at index " + str(part) + "...")
                    options_chain["rowposition"] = part
                    self.shard_download_percent_list.append(0)

                    logger.debug(pointer)
                    options_chain["shard_file_size"] = shard_size_array[part]
                    url = "http://" + pointer.get('farmer')['address'] +\
                          ":" +\
                          str(pointer.get('farmer')['port']) +\
                          "/shards/" + pointer["hash"] +\
                          "?token=" + pointer["token"]
                    logger.debug(url)

                    if self.combine_tmpdir_name_with_token:
                        self.createNewDownloadThread(url, self.tmp_path + "/" +
                                                     str(pointer["token"]) +
                                                     "/" +
                                                     str(file_name) +
                                                     "-" + str(part),
                                                     options_chain,
                                                     progress_bars_list[part],
                                                     part, part)
                    else:
                        self.createNewDownloadThread(url, self.tmp_path + "/" + str(file_name) + "-" + str(part),
                                                     options_chain,
                                                     progress_bars_list[part], part, part)

                    logger.debug(self.tmp_path + "/" + str(file_name) + "-" +
                                 str(part) + "zapisane")
                    part = part + 1

            except storj.exception.StorjBridgeApiError as e:
                self.emit(QtCore.SIGNAL("showStorjBridgeException"),
                          "Error while resolving file pointers for download. " + str(e))  # emit Storj Bridge Exception
                continue
            except Exception as e:
                self.emit(QtCore.SIGNAL("showStorjBridgeException"),
                          "Unhandled error while resolving file pointers for download. " + str(e))  # emit unhandled Exception
                continue
            else:
                break
