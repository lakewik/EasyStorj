# -*- coding: utf-8 -*-

import logging
import xml.etree.cElementTree as ET


CONFIG_FILE = "storj_client_config.xml"


# Configuration backend section
class Configuration:

    __logger = logging.getLogger('%s.Configuration' % __name__)

    def __init__(self, sameFileNamePrompt=None, sameFileHashPrompt=None,
                 load_config=False):
        if load_config:

            et = None

            try:
                et = ET.parse(CONFIG_FILE)
            except BaseException:
                self.__logger.error("Unspecified XML parse error")

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
        except BaseException:
            self.__logger.error("Unspecified error")

        return output

    def load_config_from_xml(self):
        try:
            et = ET.parse(CONFIG_FILE)
            for tags in et.iter('password'):
                output = tags.text
        except BaseException:
            self.__logger.error("Unspecified error")

    def paint_config_to_ui(self, settings_ui):
        et = None

        try:
            et = ET.parse(CONFIG_FILE)

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

        except Exception as e:
            self.__logger.error("Unspecified XML parse error" + str(e))

    def save_client_configuration(self, settings_ui):
        root = ET.Element("configuration")
        doc = ET.SubElement(root, "client")

        # settings_ui = Ui_
        ET.SubElement(doc, "max_shard_size").text = str(settings_ui.max_shard_size.text())
        ET.SubElement(doc, "max_connections_onetime").text = str(settings_ui.connections_onetime.text())
        ET.SubElement(doc, "shard_size_unit").text = str(settings_ui.shard_size_unit.currentIndex())
        ET.SubElement(doc, "max_download_bandwidth").text = str(settings_ui.max_download_bandwidth.text())
        ET.SubElement(doc, "max_upload_bandwidth").text = str(settings_ui.max_upload_bandwidth.text())
        ET.SubElement(doc, "default_file_encryption_algorithm").text = str(
            settings_ui.default_crypto_algorithm.currentIndex())
        ET.SubElement(doc, "bridge_request_timeout").text = str(settings_ui.bridge_request_timeout.text())
        ET.SubElement(doc, "crypto_keys_location").text = str(settings_ui.crypto_keys_location.text())
        tree = ET.ElementTree(root)
        tree.write(CONFIG_FILE)
