# -*- coding: utf-8 -*-

import xml.etree.cElementTree as ET
from log_manager import logger

CONFIG_FILE = "storj_client_config.xml"


# Configuration backend section
class Configuration:

    def __init__(self, sameFileNamePrompt=None, sameFileHashPrompt=None,
                 load_config=False):
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
            et = ET.parse(CONFIG_FILE)
            for tags in et.iter('password'):
                output = tags.text
        except:
            logger.error("Unspecified error")

    def save_client_configuration(self, settings_ui):
        root = ET.Element("configuration")
        doc = ET.SubElement(root, "client")

        # settings_ui = Ui_
        ET.SubElement(doc, "max_shard_size").text = str("")
        ET.SubElement(doc, "max_connections_onetime").text = str("test")
        ET.SubElement(doc, "advanced_view_enabled").text = str("test")
        ET.SubElement(doc, "max_download_bandwith").text = str("test")
        ET.SubElement(doc, "max_upload_bandwith").text = str("test")
        ET.SubElement(doc, "default_file_encryption_algorithm").text = str("AES")
        tree = ET.ElementTree(root)
        tree.write(CONFIG_FILE)
