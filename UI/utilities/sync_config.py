from PyQt4 import QtCore, QtGui
import xml.etree.cElementTree as ET
from log_manager import logger
import csv


SYNC_CONFIG_FILE = "storj_sync_config.xml"
SYNC_DIRECTORIES_FILE = "storj_sync_dirs.csv"


# Configuration backend section
class SyncConfiguration():

    def __init__(self, load_config=False):
        if load_config:

            et = None

            try:
                et = ET.parse(CONFIG_FILE)
            except:
                logger.error("Unspecified XML parse error")

            for tags in et.iter(str("same_file_name_prompt")):
                if tags.text == "1":
                    self.sameFileNamePrompt = True
                elif tags.text == "0":
                    self.sameFileNamePrompt = False
                else:
                    self.sameFileNamePrompt = True
            for tags in et.iter(str("same_file_hash_prompt")):
                if tags.text == "1":
                    self.sameFileHashPrompt = True
                elif tags.text == "0":
                    self.sameFileHashPrompt = False
                else:
                    self.sameFileHashPrompt = True
            for tags in et.iter(str("max_chunk_size_for_download")):
                if tags.text is not None:
                    self.maxDownloadChunkSize = int(tags.text)
                else:
                    self.maxDownloadChunkSize = 1024

    def get_config_parametr_value(self, parametr):
        output = ""
        try:
            et = ET.parse(CONFIG_FILE)
            for tags in et.iter(str(parametr)):
                output = tags.text
        except:
            logger.error("Unspecified error")

        return output

    def load_config_from_xml(self):
        try:
            et = ET.parse(SYNC_CONFIG_FILE)
            for tags in et.iter('password'):
                output = tags.text
        except:
            logger.error("Unspecified error")

    def paint_config_to_ui(self, settings_ui):

        self.load_sync_directories(settings_ui.sync_directories_tableWidget)

        et = None

        try:
            et = ET.parse(SYNC_CONFIG_FILE)

            for tags in et.iter(str("max_shard_size")):
                settings_ui.max_shard_size.setValue(int(tags.text))
            for tags in et.iter(str("max_connections_onetime")):
                settings_ui.connections_onetime.setValue(int(tags.text))
            for tags in et.iter(str("bridge_request_timeout")):
                settings_ui.bridge_request_timeout.setValue(int(tags.text))
            for tags in et.iter(str("crypto_keys_location")):
                settings_ui.crypto_keys_location.setText(str(tags.text))
            for tags in et.iter(str("max_download_bandwidth")):
                settings_ui.max_download_bandwidth.setText(str(tags.text))
            for tags in et.iter(str("max_upload_bandwidth")):
                settings_ui.max_upload_bandwidth.setText(str(tags.text))
            for tags in et.iter(str("default_file_encryption_algorithm")):
                settings_ui.default_crypto_algorithm.setCurrentIndex(int(tags.text))
            for tags in et.iter(str("shard_size_unit")):
                settings_ui.shard_size_unit.setCurrentIndex(int(tags.text))
            for tags in et.iter(str("custom_max_shard_size_enabled")):
                if int(tags.text) == 1:
                    settings_ui.max_shard_size_enabled_checkBox.setChecked(True)
                else:
                    settings_ui.max_shard_size_enabled_checkBox.setChecked(False)

        except Exception as e:
            logger.error("Unspecified XML parse error" + str(e))

    def save_sync_configuration(self, settings_ui):

        self.save_sync_directories(settings_ui.sync_directories_tableWidget)

        with open(SYNC_CONFIG_FILE, 'r') as conf_file:
            XML_conf_data = conf_file.read().replace('\n', '')

        tree = ET.parse(SYNC_CONFIG_FILE)

        #root = ET.Element("configuration")
        #doc = ET.SubElement(root, "client")

        # settings_ui = Ui_
        if settings_ui.sync_enabled_checkBox.isChecked():
            sync_enabled_checkbox = '1'
        else:
            sync_enabled_checkbox = '0'

        if settings_ui.start_sync_on_boot_checkBox.isChecked():
            start_sync_on_boot_checkbox = '1'
        else:
            start_sync_on_boot_checkbox = '0'

        if settings_ui.show_sync_tray_icon_checkBox.isChecked():
            show_sync_tray_icon_checkbox = '1'
        else:
            show_sync_tray_icon_checkbox = '0'


        tree.write(SYNC_CONFIG_FILE)


    def load_sync_directories(self, sync_directories_table):
        with open(unicode(SYNC_DIRECTORIES_FILE), 'rb') as stream:
            sync_directories_table.setRowCount(0)
            sync_directories_table.setColumnCount(0)
            for rowdata in csv.reader(stream):
                row = sync_directories_table.rowCount()
                sync_directories_table.insertRow(row)
                sync_directories_table.setColumnCount(len(rowdata))
                for column, data in enumerate(rowdata):
                    item = QtGui.QTableWidgetItem(data.decode('utf8'))
                    sync_directories_table.setItem(row, column, item)


    def save_sync_directories(self, sync_directories_table):
        with open(unicode(SYNC_DIRECTORIES_FILE), 'wb') as stream:
            writer = csv.writer(stream)
            for row in range(sync_directories_table.rowCount()):
                rowdata = []
                for column in range(sync_directories_table.columnCount()):
                    item = sync_directories_table.item(row, column)
                    if item is not None:
                        rowdata.append(
                            unicode(item.text()).encode('utf8'))
                    else:
                        rowdata.append('')
                writer.writerow(rowdata)


