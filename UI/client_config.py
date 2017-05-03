from PyQt4 import QtCore, QtGui
from .utilities.backend_config import Configuration
from .qt_interfaces.settings_ui_new import Ui_ClientConfiguration
from .utilities.log_manager import logger


# Configuration Ui section
class ClientConfigurationUI(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # register UI
        self.client_configuration_ui = Ui_ClientConfiguration()
        self.client_configuration_ui.setupUi(self)

        self.configuration_manager = Configuration()

        QtCore.QObject.connect(self.client_configuration_ui.apply_bt, QtCore.SIGNAL('clicked()'),
                               self.save_settings)  # save settings action

        QtCore.QObject.connect(self.client_configuration_ui.cancel_bt, QtCore.SIGNAL('clicked()'),
                               self.close)  # close form

        QtCore.QObject.connect(self.client_configuration_ui.crypto_keys_location_select_bt, QtCore.SIGNAL('clicked()'),
                               self.select_crypto_keys_path)  # open path select

        self.configuration_manager.paint_config_to_ui(self.client_configuration_ui)


    def select_crypto_keys_path(self):
        self.client_configuration_ui.crypto_keys_location.setText(str(QtGui.QFileDialog.getSaveFileName(
          self, 'Save file to...', 'storj_client_keyring.sjkr')))

    def save_settings(self):
        # validate settings

        self.configuration_manager.save_client_configuration(self.client_configuration_ui)  # save configuration
        QtGui.QMessageBox.about(self, 'Success', 'Configuration saved successfully!')



    def reset_settings_to_default(self):
        logger.debug(1)
