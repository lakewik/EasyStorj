import xml.etree.cElementTree as ET
from log_manager import logger
from BeautifulSoup import BeautifulStoneSoup as Soup
from UI.resources.constants import DEFAULT_SHARD_SIZE, DEFAULT_MAX_BRIDGE_REQUEST_TIMEOUT

CONFIG_FILE = 'storj_client_config.xml'


class Configuration:

    def __init__(self, sameFileNamePrompt=None, sameFileHashPrompt=None,
                 load_config=False):
        if load_config:
            et = None
            try:
                et = ET.parse(CONFIG_FILE)
            except:
                logger.error('Unspecified XML parse error')

            for tags in et.iter(str('same_file_name_prompt')):
                if tags.text == '1':
                    self.sameFileNamePrompt = True
                elif tags.text == '0':
                    self.sameFileNamePrompt = False
                else:
                    self.sameFileNamePrompt = True
            for tags in et.iter(str('same_file_hash_prompt')):
                if tags.text == '1':
                    self.sameFileHashPrompt = True
                elif tags.text == '0':
                    self.sameFileHashPrompt = False
                else:
                    self.sameFileHashPrompt = True
            for tags in et.iter(str('max_chunk_size_for_download')):
                if tags.text is not None:
                    self.maxDownloadChunkSize = int(tags.text)
                else:
                    self.maxDownloadChunkSize = 1024

    def get_config_parametr_value(self, parametr):
        output = ''
        try:
            et = ET.parse(CONFIG_FILE)
            for tags in et.iter(str(parametr)):
                output = tags.text
        except:
            logger.error('Unspecified error')

        return output

    def load_config_from_xml(self):
        try:
            et = ET.parse(CONFIG_FILE)
            for tags in et.iter('password'):
                output = tags.text
        except:
            logger.error('Unspecified error')

    def paint_config_to_ui(self, settings_ui):
        et = None

        try:
            et = ET.parse(CONFIG_FILE)

            for tags in et.iter(str('max_shard_size')):
                settings_ui.max_shard_size.setValue(int(tags.text))
            for tags in et.iter(str('max_connections_onetime')):
                settings_ui.connections_onetime.setValue(int(tags.text))
            for tags in et.iter(str('bridge_request_timeout')):
                settings_ui.bridge_request_timeout.setValue(int(tags.text))
            for tags in et.iter(str('crypto_keys_location')):
                settings_ui.crypto_keys_location.setText(str(tags.text))
            for tags in et.iter(str('max_download_bandwidth')):
                settings_ui.max_download_bandwidth.setText(str(tags.text))
            for tags in et.iter(str('max_upload_bandwidth')):
                settings_ui.max_upload_bandwidth.setText(str(tags.text))
            for tags in et.iter(str('default_file_encryption_algorithm')):
                settings_ui.default_crypto_algorithm.setCurrentIndex(int(tags.text))
            for tags in et.iter(str('shard_size_unit')):
                settings_ui.shard_size_unit.setCurrentIndex(int(tags.text))
            for tags in et.iter(str('custom_max_shard_size_enabled')):
                if int(tags.text) == 1:
                    settings_ui.max_shard_size_enabled_checkBox.setChecked(True)
                else:
                    settings_ui.max_shard_size_enabled_checkBox.setChecked(False)

        except Exception as e:
            logger.error('Unspecified XML parse error' + str(e))

    def save_client_configuration(self, settings_ui):
        root = ET.Element('configuration')
        doc = ET.SubElement(root, 'client')

        # settings_ui = Ui_
        if settings_ui.max_shard_size_enabled_checkBox.isChecked():
            custom_max_shard_size_enabled_checkbox = '1'
        else:
            custom_max_shard_size_enabled_checkbox = '0'

        ET.SubElement(doc, 'custom_max_shard_size_enabled').text = \
            str(custom_max_shard_size_enabled_checkbox)
        ET.SubElement(doc, 'max_shard_size').text = \
            str(settings_ui.max_shard_size.text())
        ET.SubElement(doc, 'max_connections_onetime').text = \
            str(settings_ui.connections_onetime.text())
        ET.SubElement(doc, 'shard_size_unit').text = \
            str(settings_ui.shard_size_unit.currentIndex())
        ET.SubElement(doc, 'max_download_bandwidth').text = \
            str(settings_ui.max_download_bandwidth.text())
        ET.SubElement(doc, 'max_upload_bandwidth').text = \
            str(settings_ui.max_upload_bandwidth.text())
        ET.SubElement(doc, 'default_file_encryption_algorithm').text = \
            str(settings_ui.default_crypto_algorithm.currentIndex())
        ET.SubElement(doc, 'bridge_request_timeout').text = \
            str(settings_ui.bridge_request_timeout.text())
        ET.SubElement(doc, 'crypto_keys_location').text = \
            str(settings_ui.crypto_keys_location.text())
        ET.SubElement(doc, 'custom_tmp_path').set('path', 'ABC')
        tree = ET.ElementTree(root)
        tree.write(CONFIG_FILE)

        custom_tmp_path = self.get_custom_temp_path()
        logger.debug(custom_tmp_path)

    def max_shard_size(self):
        et = None
        max_shard_size = DEFAULT_SHARD_SIZE

        try:
            et = ET.parse(CONFIG_FILE)
            shard_size_unit = 2
            max_shard_size_sterile = None
            for tags in et.iter(str('custom_max_shard_size_enabled')):
                if int(tags.text) == 1:
                    for tags2 in et.iter(str('max_shard_size')):
                        max_shard_size_sterile = int(tags2.text)
                    for tags3 in et.iter(str('shard_size_unit')):
                        shard_size_unit = int(tags3.text)

                    if shard_size_unit == 0:  # KB:
                        max_shard_size = max_shard_size_sterile * 2 * 1024
                    elif shard_size_unit == 1:  # MB:
                        max_shard_size = max_shard_size_sterile * 2 * 1024 ** 2
                    elif shard_size_unit == 2:  # GB:
                        max_shard_size = max_shard_size_sterile * 2 * 1024 ** 3
                    elif shard_size_unit == 3:  # TB:
                        max_shard_size = max_shard_size_sterile * 2 * 1024 ** 4
                else:
                    max_shard_size = DEFAULT_SHARD_SIZE

        except Exception as e:
            logger.error('Unspecified XML parse error %s' % str(e))

        return max_shard_size / 2

    def get_max_bridge_request_timeout(self):
        max_bridge_request_timeout = DEFAULT_MAX_BRIDGE_REQUEST_TIMEOUT
        et = None
        try:
            et = ET.parse(CONFIG_FILE)
            for tags in et.iter('bridge_request_timeout'):
                max_bridge_request_timeout = int(tags.text)

        except Exception as e:
            logger.error('Unspecified XML parse error %s' % str(e))

        return max_bridge_request_timeout

    def get_custom_temp_path(self):
        et = ET.parse(CONFIG_FILE)
        custom_temp_path = ''
        for tags in et.iter(str('custom_tmp_path')):
            custom_temp_path = str(tags.get('path'))

        return custom_temp_path

    def save_custom_temp_path(self, custom_path):

        with open(CONFIG_FILE, 'r') as conf_file:
            XML_conf_data = conf_file.read().replace('\n', '')
        soup = Soup(XML_conf_data)
        custom_tmp_path_tag = soup.configuration.client.custom_temp_path
        custom_tmp_path_tag['path'] = 'Updated'

        return True
