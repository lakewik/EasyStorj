# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from qt_interfaces.sync_menu_ui import Ui_SyncMenu

# Synchronization menu section #


class SyncMenuUI(QtGui.QMainWindow):

    def __init__(self, parent=None,):
        QtGui.QWidget.__init__(self, parent)
        self.sync_menu_ui = Ui_SyncMenu()
        self.sync_menu_ui.setupUi(self)

        # start synchronization action
        QtCore.QObject.connect(
            self.sync_menu_ui.start_sync_bt,
            QtCore.SIGNAL('clicked()'),
            self.start_sync_action)

    def start_sync_action(self):
        return 1

    def stop_sync_action(self):
        return 1

    def update_current_main_sync_stats(self, stats_array):
        self.sync_menu_ui.successfully_synced_files_count.setText(stats_array["successfully_synced_files_count"])
        return 1
