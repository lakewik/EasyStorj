# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
import time, os, os.path
from qt_interfaces.file_sync_options_ui import Ui_FileSyncOptions
from utilities.sync_config import SyncConfiguration
from utilities.tools import Tools

# Synchronization menu section #
class SyncOptionsUI(QtGui.QMainWindow):

    def __init__(self, parent=None,):
        QtGui.QWidget.__init__(self, parent)
        self.sync_menu_ui = Ui_FileSyncOptions()
        self.sync_menu_ui.setupUi(self)

        self.sync_configuration_manager = SyncConfiguration()
        self.tools = Tools()

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

        QtCore.QObject.connect(
            self.sync_menu_ui.add_sync_dir_bt,
            QtCore.SIGNAL('clicked()'),
            self.add_new_sync_directory)

        QtCore.QObject.connect(
            self.sync_menu_ui.remove_sync_dir,
            QtCore.SIGNAL('clicked()'),
            self.delete_sync_directory)

        # prepare table
        self.sync_dirs_table_header = ['Directory', 'Add date', 'Files count', 'Actual total size']

        self.sync_menu_ui.sync_directories_tableWidget.setRowCount(0)


        self.sync_menu_ui.sync_directories_tableWidget.resizeColumnsToContents()
        self.sync_menu_ui.sync_directories_tableWidget.resizeRowsToContents()
        self.sync_menu_ui.sync_directories_tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.sync_configuration_manager.paint_config_to_ui(self.sync_menu_ui)

        self.sync_menu_ui.sync_directories_tableWidget.setHorizontalHeaderLabels(self.sync_dirs_table_header)
        self.sync_menu_ui.sync_directories_tableWidget.setColumnCount(4)



    def restore_default_settings(self):
        msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Question, "Question",
                                   "Are you sure that you want to restore sync settings to default?",
                                   (QtGui.QMessageBox.Yes | QtGui.QMessageBox.No))
        result = msgBox.exec_()
        if result == QtGui.QMessageBox.Yes:
            QtGui.QMessageBox.about(self, 'Success', 'Default settings have been restored successfully!')
            return True
        else:
            return False


    def save_sync_options(self):
        # validate settings

        self.sync_configuration_manager.save_sync_configuration(self.sync_menu_ui)  # save configuration
        QtGui.QMessageBox.about(self, 'Success', 'Synchronization configuration saved successfully!')

    def add_new_sync_directory(self):
        self.selected_sync_sirectory = QtGui.QFileDialog.getExistingDirectory(
            None,
            'Select a sync directory: ',
            "",
            QtGui.QFileDialog.ShowDirsOnly)

        if self.selected_sync_sirectory != "":
            self.current_time = time.ctime()
            total_files_count = self.tools.count_files_in_dir(directory=self.selected_sync_sirectory)
            total_files_size = self.tools.human_size(self.tools.count_directory_size(self.selected_sync_sirectory, True))

            table_row_count = self.sync_menu_ui.sync_directories_tableWidget.rowCount()
            self.sync_menu_ui.sync_directories_tableWidget.setRowCount(table_row_count + 1)
            self.sync_menu_ui.sync_directories_tableWidget.setItem(
               table_row_count, 0, QtGui.QTableWidgetItem(str(self.selected_sync_sirectory)))
            self.sync_menu_ui.sync_directories_tableWidget.setItem(
                table_row_count, 1, QtGui.QTableWidgetItem(str(self.current_time)))
            self.sync_menu_ui.sync_directories_tableWidget.setItem(
                table_row_count, 2, QtGui.QTableWidgetItem(str(total_files_count)))
            self.sync_menu_ui.sync_directories_tableWidget.setItem(
                table_row_count, 3, QtGui.QTableWidgetItem(str(total_files_size)))


        return True

    def delete_sync_directory(self):
        tablemodel = self.sync_menu_ui.sync_directories_tableWidget.model()
        rows = sorted(set(index.row() for index in
                          self.sync_menu_ui.sync_directories_tableWidget.selectedIndexes()))

        selected = False
        for row in rows:
            selected = True
            index = tablemodel.index(row, 0)  # get directory index

            # We suppose data are strings
            selected_directory_in_table = str(tablemodel.data(index).toString())
            msgBox = QtGui.QMessageBox(
                QtGui.QMessageBox.Question,
                'Question',
                'Are you sure you want to delete this sync directory from table? Directory which you want to delete from table: %s' % str('"' + selected_directory_in_table + '"').decode('utf-8'),
                (QtGui.QMessageBox.Yes | QtGui.QMessageBox.No))
            result = msgBox.exec_()
            if result == QtGui.QMessageBox.Yes:
                # delete directory from table
                self.sync_menu_ui.sync_directories_tableWidget.removeRow(int(row))
                QtGui.QMessageBox.about(
                    self, 'Information', 'Directory %s have been successfully deleted form table' % str('"' + selected_directory_in_table + '"').decode('utf-8'))

        if not selected:
            QtGui.QMessageBox.about(
                self, 'Information', 'Please select sync directory which you want to delete form table')




        return True

