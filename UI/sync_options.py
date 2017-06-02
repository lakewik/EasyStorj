# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from qt_interfaces.file_sync_options_ui import Ui_FileSyncOptions
from utilities.sync_config import SyncConfiguration

# Synchronization menu section #
class SyncOptionsUI(QtGui.QMainWindow):

    def __init__(self, parent=None,):
        QtGui.QWidget.__init__(self, parent)
        self.sync_menu_ui = Ui_FileSyncOptions()
        self.sync_menu_ui.setupUi(self)

        self.sync_configuration_manager = SyncConfiguration()

        QtCore.QObject.connect(
            self.sync_menu_ui.restore_defaults_bt,
            QtCore.SIGNAL('clicked()'),
            self.restore_default_settings)

        QtCore.QObject.connect(
            self.sync_menu_ui.save_bt,
            QtCore.SIGNAL('clicked()'),
            self.save_sync_options)

        QtCore.QObject.connect(
            self.sync_menu_ui.cancel_bt,
            QtCore.SIGNAL('clicked()'),
            self.save_sync_options)

    def restore_default_settings(self):
        return 1

    def save_sync_options(self):
        # validate settings

        self.sync_configuration_manager.save_sync_configuration(self.sync_menu_ui)  # save configuration
        QtGui.QMessageBox.about(self, 'Success', 'Synchronization configuration saved successfully!')

