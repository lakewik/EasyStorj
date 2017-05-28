# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_sync_options.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_FileSyncOptions(object):
    def setupUi(self, FileSyncOptions):
        FileSyncOptions.setObjectName(_fromUtf8("FileSyncOptions"))
        FileSyncOptions.resize(687, 514)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.ToolTipText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Light, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Midlight, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Dark, brush)
        brush = QtGui.QBrush(QtGui.QColor(170, 170, 170))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Mid, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Text, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.BrightText, brush)
        brush = QtGui.QBrush(QtGui.QColor(127, 127, 127))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ButtonText, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Shadow, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.AlternateBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 220))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipBase, brush)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.ToolTipText, brush)
        FileSyncOptions.setPalette(palette)
        self.label_3 = QtGui.QLabel(FileSyncOptions)
        self.label_3.setGeometry(QtCore.QRect(30, 10, 181, 81))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/resources/storj-logo-horizontal.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.file_name = QtGui.QLabel(FileSyncOptions)
        self.file_name.setGeometry(QtCore.QRect(260, 20, 411, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.file_name.setFont(font)
        self.file_name.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.file_name.setObjectName(_fromUtf8("file_name"))
        self.save_bt = QtGui.QPushButton(FileSyncOptions)
        self.save_bt.setGeometry(QtCore.QRect(410, 470, 271, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.save_bt.setFont(font)
        self.save_bt.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
"  background-color: #83bf20;\n"
"  border-color: #83bf20;\n"
"}\n"
"QPushButton:active {\n"
"  background-color: #93cc36;\n"
"  border-color: #93cc36;\n"
"}\n"
"QPushButton{\n"
"  background-color: #88c425;\n"
"    border: 1px solid #88c425;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}"))
        self.save_bt.setObjectName(_fromUtf8("save_bt"))
        self.restore_defaults_bt = QtGui.QPushButton(FileSyncOptions)
        self.restore_defaults_bt.setGeometry(QtCore.QRect(130, 470, 271, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.restore_defaults_bt.setFont(font)
        self.restore_defaults_bt.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
"  background-color: #83bf20;\n"
"  border-color: #83bf20;\n"
"}\n"
"QPushButton:active {\n"
"  background-color: #93cc36;\n"
"  border-color: #93cc36;\n"
"}\n"
"QPushButton{\n"
"  background-color: #88c425;\n"
"    border: 1px solid #88c425;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}"))
        self.restore_defaults_bt.setObjectName(_fromUtf8("restore_defaults_bt"))
        self.cancel_bt = QtGui.QPushButton(FileSyncOptions)
        self.cancel_bt.setGeometry(QtCore.QRect(10, 470, 111, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_bt.setFont(font)
        self.cancel_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #fa6e50;\n"
"    border: 1px solid #fa6e50;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #fa6e50;\n"
"    border-color: #fa6e50;\n"
"}\n"
"QPushButton:active {\n"
"    background-color: #fa6e50;\n"
"    border-color: #fa6e50\n"
"}"))
        self.cancel_bt.setObjectName(_fromUtf8("cancel_bt"))
        self.tabWidget = QtGui.QTabWidget(FileSyncOptions)
        self.tabWidget.setGeometry(QtCore.QRect(10, 120, 671, 331))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.start_sync_on_boot_checkBox = QtGui.QCheckBox(self.tab)
        self.start_sync_on_boot_checkBox.setGeometry(QtCore.QRect(20, 20, 611, 21))
        self.start_sync_on_boot_checkBox.setStyleSheet(_fromUtf8("QCheckBox {\n"
"font-size: 20px;\n"
"}"))
        self.start_sync_on_boot_checkBox.setObjectName(_fromUtf8("start_sync_on_boot_checkBox"))
        self.connections_onetime = QtGui.QSpinBox(self.tab)
        self.connections_onetime.setGeometry(QtCore.QRect(270, 60, 161, 32))
        self.connections_onetime.setObjectName(_fromUtf8("connections_onetime"))
        self.label = QtGui.QLabel(self.tab)
        self.label.setGeometry(QtCore.QRect(20, 60, 241, 31))
        self.label.setStyleSheet(_fromUtf8("QLabel {\n"
"font-size: 20px;\n"
"}"))
        self.label.setObjectName(_fromUtf8("label"))
        self.connections_onetime_2 = QtGui.QSpinBox(self.tab)
        self.connections_onetime_2.setGeometry(QtCore.QRect(290, 100, 141, 32))
        self.connections_onetime_2.setObjectName(_fromUtf8("connections_onetime_2"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(20, 100, 271, 31))
        self.label_2.setStyleSheet(_fromUtf8("QLabel {\n"
"font-size: 20px;\n"
"}"))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.start_sync_on_boot_checkBox_2 = QtGui.QCheckBox(self.tab)
        self.start_sync_on_boot_checkBox_2.setGeometry(QtCore.QRect(20, 150, 361, 21))
        self.start_sync_on_boot_checkBox_2.setStyleSheet(_fromUtf8("QCheckBox {\n"
"font-size: 20px;\n"
"}"))
        self.start_sync_on_boot_checkBox_2.setObjectName(_fromUtf8("start_sync_on_boot_checkBox_2"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.file_name_2 = QtGui.QLabel(self.tab_2)
        self.file_name_2.setGeometry(QtCore.QRect(10, 20, 671, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.file_name_2.setFont(font)
        self.file_name_2.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.file_name_2.setObjectName(_fromUtf8("file_name_2"))
        self.remove_sync_dir = QtGui.QPushButton(self.tab_2)
        self.remove_sync_dir.setGeometry(QtCore.QRect(570, 190, 91, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.remove_sync_dir.setFont(font)
        self.remove_sync_dir.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #fa6e50;\n"
"    border: 1px solid #fa6e50;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #fa6e50;\n"
"    border-color: #fa6e50;\n"
"}\n"
"QPushButton:active {\n"
"    background-color: #fa6e50;\n"
"    border-color: #fa6e50\n"
"}"))
        self.remove_sync_dir.setObjectName(_fromUtf8("remove_sync_dir"))
        self.sync_directories_tableWidget = QtGui.QTableWidget(self.tab_2)
        self.sync_directories_tableWidget.setGeometry(QtCore.QRect(10, 60, 551, 171))
        self.sync_directories_tableWidget.setObjectName(_fromUtf8("sync_directories_tableWidget"))
        self.sync_directories_tableWidget.setColumnCount(0)
        self.sync_directories_tableWidget.setRowCount(0)
        self.add_sync_dir_bt = QtGui.QPushButton(self.tab_2)
        self.add_sync_dir_bt.setGeometry(QtCore.QRect(570, 60, 91, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.add_sync_dir_bt.setFont(font)
        self.add_sync_dir_bt.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
"  background-color: #83bf20;\n"
"  border-color: #83bf20;\n"
"}\n"
"QPushButton:active {\n"
"  background-color: #93cc36;\n"
"  border-color: #93cc36;\n"
"}\n"
"QPushButton{\n"
"  background-color: #88c425;\n"
"    border: 1px solid #88c425;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}"))
        self.add_sync_dir_bt.setObjectName(_fromUtf8("add_sync_dir_bt"))
        self.edit_sync_dir = QtGui.QPushButton(self.tab_2)
        self.edit_sync_dir.setGeometry(QtCore.QRect(570, 130, 91, 51))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.edit_sync_dir.setFont(font)
        self.edit_sync_dir.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2683ff;\n"
"    border: 1px solid #2683ff;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #2274e2;\n"
"  border-color: #2274e2;\n"
"}\n"
"QPushButton:active{\n"
"  background-color: #4393ff;\n"
"  border-color: #4393ff;\n"
"}"))
        self.edit_sync_dir.setObjectName(_fromUtf8("edit_sync_dir"))
        self.manage_excluded_file_types = QtGui.QPushButton(self.tab_2)
        self.manage_excluded_file_types.setGeometry(QtCore.QRect(10, 250, 641, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.manage_excluded_file_types.setFont(font)
        self.manage_excluded_file_types.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2683ff;\n"
"    border: 1px solid #2683ff;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #2274e2;\n"
"  border-color: #2274e2;\n"
"}\n"
"QPushButton:active{\n"
"  background-color: #4393ff;\n"
"  border-color: #4393ff;\n"
"}"))
        self.manage_excluded_file_types.setObjectName(_fromUtf8("manage_excluded_file_types"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.sync_enabled_checkBox = QtGui.QCheckBox(FileSyncOptions)
        self.sync_enabled_checkBox.setGeometry(QtCore.QRect(170, 70, 361, 41))
        self.sync_enabled_checkBox.setStyleSheet(_fromUtf8("QCheckBox {\n"
"font-size: 20px;\n"
"}"))
        self.sync_enabled_checkBox.setObjectName(_fromUtf8("sync_enabled_checkBox"))

        self.retranslateUi(FileSyncOptions)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(FileSyncOptions)

    def retranslateUi(self, FileSyncOptions):
        FileSyncOptions.setWindowTitle(_translate("FileSyncOptions", "File synchronization options", None))
        self.file_name.setText(_translate("FileSyncOptions", "<html><head/><body><p><span style=\" font-size:18pt;\">File synchronization options</span></p></body></html>", None))
        self.save_bt.setText(_translate("FileSyncOptions", "SAVE SETTINGS", None))
        self.restore_defaults_bt.setText(_translate("FileSyncOptions", "RESTORE DEFAULTS", None))
        self.cancel_bt.setText(_translate("FileSyncOptions", "CANCEL", None))
        self.start_sync_on_boot_checkBox.setText(_translate("FileSyncOptions", "Start file synchronization module at system start", None))
        self.label.setText(_translate("FileSyncOptions", "Max upload concurrency:", None))
        self.label_2.setText(_translate("FileSyncOptions", "Max download concurrency:", None))
        self.start_sync_on_boot_checkBox_2.setText(_translate("FileSyncOptions", "Show Tray icon for synchronization", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("FileSyncOptions", "General", None))
        self.file_name_2.setText(_translate("FileSyncOptions", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt;\">Directories with enabled synchronization</span></p></body></html>", None))
        self.remove_sync_dir.setText(_translate("FileSyncOptions", "-", None))
        self.add_sync_dir_bt.setText(_translate("FileSyncOptions", "+", None))
        self.edit_sync_dir.setText(_translate("FileSyncOptions", "EDIT", None))
        self.manage_excluded_file_types.setText(_translate("FileSyncOptions", "MANAGE EXCLUDED FILE TYPES", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("FileSyncOptions", "Synchronized data", None))
        self.sync_enabled_checkBox.setText(_translate("FileSyncOptions", "Enable file synchronization module", None))

import resources_rc
