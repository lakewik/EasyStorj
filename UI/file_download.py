from PyQt4 import QtCore, QtGui
from qt_interfaces.single_file_downloader_ui import Ui_SingleFileDownload
from crypto.file_crypto_tools import FileCrypto
from engine import StorjEngine
import storj
import threading


global html_format_begin, html_format_end
html_format_begin = "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"
html_format_end = "</span></p></body></html>"


class SingleFileDownloadUI(QtGui.QMainWindow):

    def __init__(self, parent=None, bucketid=None, fileid=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui_single_file_download = Ui_SingleFileDownload()
        self.ui_single_file_download.setupUi(self)
        # QtCore.QObject.connect(self.ui_single_file_download., QtCore.SIGNAL("clicked()"), self.save_config) # open bucket manager
        self.storj_engine = StorjEngine()  # init StorjEngine

        # self.initialize_shard_queue_table(file_pointers)

        QtCore.QObject.connect(self.ui_single_file_download.file_save_path_bt, QtCore.SIGNAL("clicked()"),
                               self.select_file_save_path)  # open file select dialog
        QtCore.QObject.connect(self.ui_single_file_download.tmp_dir_bt, QtCore.SIGNAL("clicked()"),
                               self.select_tmp_directory)  # open tmp directory select dialog
        QtCore.QObject.connect(self.ui_single_file_download.start_download_bt, QtCore.SIGNAL("clicked()"),
                               lambda: self.createNewDownloadInitThread(bucketid, fileid))  # begin file downloading process

        self.connect(self, QtCore.SIGNAL("incrementShardsDownloadProgressCounters"), self.increment_shards_download_progress_counters)
        self.connect(self, QtCore.SIGNAL("updateShardDownloadProgress"), self.update_shard_download_progess)
        self.connect(self, QtCore.SIGNAL("beginDownloadProccess"), self.download_begin)

        self.shards_already_downloaded = 0

        self.createNewInitializationThread(bucketid, fileid)

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

        self.file_download(None, None, "/home/lakewik/rudasek2", options_array, self.progressbar_list)
        # progressbar_list[0].setValue(20)
        # progressbar_list[2].setValue(17)

    def createNewDownloadInitThread(self, bucket_id, file_id):
        file_name_resolve_thread = threading.Thread(target=self.init_download_file_pointers, args=(bucket_id, file_id))
        file_name_resolve_thread.start()

    def createNewInitializationThread(self, bucket_id, file_id):
        file_name_resolve_thread = threading.Thread(target=self.set_file_metadata, args=(bucket_id, file_id))
        file_name_resolve_thread.start()

    def set_file_metadata(self, bucket_id, file_id):
        file_metadata = self.storj_engine.storj_client.file_metadata("dc4778cc186192af49475b49", "07a2a9ebff6b7785b4bb18fd")
        self.ui_single_file_download.file_name.setText(html_format_begin + str(file_metadata.filename) + html_format_end)

        tools = Tools()
        self.ui_single_file_download.file_size.setText(html_format_begin + str(tools.human_size(int(file_metadata.size))) + html_format_end)
        self.ui_single_file_download.file_id.setText(html_format_begin + str(file_id) + html_format_end)

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
        file_pointers = self.storj_engine.storj_client.file_pointers("dc4778cc186192af49475b49", "9af4e2f80e7f334ae651464a")
        self.emit(QtCore.SIGNAL("beginDownloadProccess"), file_pointers)

    def select_file_save_path(self):
        file_save_path = QtGui.QFileDialog.getSaveFileName(self, 'Save file to...', '')
        self.ui_single_file_download.file_save_path.setText(str(file_save_path))

    def calculate_final_hmac(self):
        return 1

    def create_download_connection(self, url, path_to_save, options_chain, progress_bar, rowposition):
        local_filename = path_to_save
        downloaded = False

        while True:
            try:
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
                    print t1

                    if file_size <= (32 * 1024):
                        t1 = 1

                    i = 0
                    print file_size
                    print str(t1) + "kotek"
                    for chunk in r.iter_content(32 * 1024):
                        i += 1
                        f.write(chunk)
                        print str(i) + " " + str(t1)
                        print round(float(i) / float(t1), 1)
                        print str(int(round((100.0 * i) / t1))) + " %"
                        if int(round((100.0 * i) / t1)) > 100:
                            percent_downloaded = 100
                        else:
                            percent_downloaded = int(round((100.0 * i) / t1))
                        self.emit(QtCore.SIGNAL("updateShardDownloadProgress"), int(rowposition), percent_downloaded)  # update progress bar in upload queue table
                        print str(rowposition) + "pozycja"

                        # progress_bar.setValue(percent_downloaded)

                    f.close()
                    downloaded = True
            except Exception, e:
                print str(e)
                continue
            else:
                downloaded = True
                break

        if not downloaded:
            self.emit(QtCore.SIGNAL("retryWithNewDownloadPointer"), options_chain["shard_index"])  # retry download with new download pointer
        else:
            self.emit(QtCore.SIGNAL("incrementShardsDownloadProgressCounters"))  # update already uploaded shards count
            self.emit(QtCore.SIGNAL("updateDownloadTaskState"), options_chain["rowposition"], "Downloaded!")  # update shard upload state
            if int(self.all_shards_count) <= int(self.shards_already_downloaded + 1):
                self.emit(QtCore.SIGNAL("finishDownload"))  # send signal to begin file shards joind and decryption after all shards are downloaded

            return

    def createNewDownloadThread(self, url, filelocation, options_chain, progress_bars_list, rowposition):
        # self.download_thread = DownloadTaskQtThread(url, filelocation, options_chain, progress_bars_list)
        # self.download_thread.start()
        # self.download_thread.connect(self.download_thread, SIGNAL('setStatus'), self.test1, Qt.QueuedConnection)
        # self.download_thread.tick.connect(progress_bars_list.setValue)

        # Refactor to QtTrhead
        download_thread = threading.Thread(target=self.create_download_connection,
                                           args=(url, filelocation, options_chain, progress_bars_list, rowposition))
        download_thread.start()
        print str(options_chain["rowposition"]) + "position"

    def test1(self, value1, value2):
        print str(value1) + " aaa " + str(value2)

    def upload_file(self):
        print 1

    def file_download(self, bucket_id, file_id, file_save_path, options_array, progress_bars_list):

        #### Begin file download finish function ####
        # Wait for signal to do shards joining and encryption
        def finish_download(self):

            fileisencrypted = False

            # Join shards
            sharing_tools = ShardingTools()
            self.set_current_status("Joining shards...")
            if fileisencrypted:
                sharing_tools.join_shards(self.tmp_path + "/" + str(file_name), "-", file_save_path + ".encrypted")
            else:
                sharing_tools.join_shards(self.tmp_path + "/" + str(file_name), "-", file_save_path)

            print file_save_path + ".encrypted"

            if fileisencrypted:
                # decrypt file
                self.set_current_status("Decrypting file...")
                # self.set_current_status()
                file_crypto_tools = FileCrypto()
                # file_crypto_tools.decrypt_file("AES", str(self.tmp_path + "/" + str(file_name)) + ".encrypted", file_save_path,
                #                                "kotecze57")  # begin file decryption

            print "pobrano"

            return True

        self.connect(self, QtCore.SIGNAL("finishDownload"), lambda: finish_download(self))

        ##### End file download finish point #####

        options_chain = {}
        self.storj_engine.storj_client.logger.info('file_pointers(%s, %s)', bucket_id, file_id)
        file_name = os.path.split(file_save_path)[1]
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
        print shard_size_array
        part = 0

        self.tmp_path = options_array["tmp_path"]

        self.set_current_status("Starting download threads...")
        for pointer in pointers:
            self.set_current_status("Downloading shard at index " + str(part) + "...")
            options_chain["rowposition"] = part

            print pointer
            options_chain["shard_file_size"] = shard_size_array[part]
            url = "http://" + pointer.get('farmer')['address'] + ":" + str(pointer.get('farmer')['port']) + "/shards/" + \
                  pointer["hash"] + "?token=" + pointer["token"]
            print url
            self.createNewDownloadThread(url, self.tmp_path + "/" + str(file_name) + "-" + str(part), options_chain, progress_bars_list[part], part)
            part = part + 1
