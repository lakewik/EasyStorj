# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'sync_menu.ui'
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

class Ui_SyncMenu(object):
    def setupUi(self, SyncMenu):
        SyncMenu.setObjectName(_fromUtf8("SyncMenu"))
        SyncMenu.resize(581, 457)
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
        SyncMenu.setPalette(palette)
        self.label_3 = QtGui.QLabel(SyncMenu)
        self.label_3.setGeometry(QtCore.QRect(50, 10, 161, 71))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/resources/storj-logo-horizontal.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.file_name = QtGui.QLabel(SyncMenu)
        self.file_name.setGeometry(QtCore.QRect(250, 10, 401, 41))
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
        self.sync_settings_bt = QtGui.QPushButton(SyncMenu)
        self.sync_settings_bt.setGeometry(QtCore.QRect(10, 170, 561, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sync_settings_bt.setFont(font)
        self.sync_settings_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.sync_settings_bt.setObjectName(_fromUtf8("sync_settings_bt"))
        self.stop_sync_bt = QtGui.QPushButton(SyncMenu)
        self.stop_sync_bt.setGeometry(QtCore.QRect(300, 100, 271, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.stop_sync_bt.setFont(font)
        self.stop_sync_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.stop_sync_bt.setObjectName(_fromUtf8("stop_sync_bt"))
        self.start_sync_bt = QtGui.QPushButton(SyncMenu)
        self.start_sync_bt.setGeometry(QtCore.QRect(10, 100, 281, 61))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.start_sync_bt.setFont(font)
        self.start_sync_bt.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
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
        self.start_sync_bt.setObjectName(_fromUtf8("start_sync_bt"))
        self.file_name_2 = QtGui.QLabel(SyncMenu)
        self.file_name_2.setGeometry(QtCore.QRect(140, 210, 311, 31))
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
        self.detailied_sync_stats_bt = QtGui.QPushButton(SyncMenu)
        self.detailied_sync_stats_bt.setGeometry(QtCore.QRect(10, 420, 281, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.detailied_sync_stats_bt.setFont(font)
        self.detailied_sync_stats_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color:  #2683ff;\n"
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
        self.detailied_sync_stats_bt.setObjectName(_fromUtf8("detailied_sync_stats_bt"))
        self.file_name_3 = QtGui.QLabel(SyncMenu)
        self.file_name_3.setGeometry(QtCore.QRect(20, 250, 351, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.file_name_3.setFont(font)
        self.file_name_3.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.file_name_3.setObjectName(_fromUtf8("file_name_3"))
        self.file_name_4 = QtGui.QLabel(SyncMenu)
        self.file_name_4.setGeometry(QtCore.QRect(20, 280, 231, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.file_name_4.setFont(font)
        self.file_name_4.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.file_name_4.setObjectName(_fromUtf8("file_name_4"))
        self.file_name_5 = QtGui.QLabel(SyncMenu)
        self.file_name_5.setGeometry(QtCore.QRect(20, 310, 381, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.file_name_5.setFont(font)
        self.file_name_5.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.file_name_5.setObjectName(_fromUtf8("file_name_5"))
        self.file_name_6 = QtGui.QLabel(SyncMenu)
        self.file_name_6.setGeometry(QtCore.QRect(20, 340, 341, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.file_name_6.setFont(font)
        self.file_name_6.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.file_name_6.setObjectName(_fromUtf8("file_name_6"))
        self.file_name_7 = QtGui.QLabel(SyncMenu)
        self.file_name_7.setGeometry(QtCore.QRect(20, 380, 341, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.file_name_7.setFont(font)
        self.file_name_7.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.file_name_7.setObjectName(_fromUtf8("file_name_7"))
        self.successfully_synced_files_count = QtGui.QLabel(SyncMenu)
        self.successfully_synced_files_count.setGeometry(QtCore.QRect(370, 250, 201, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.successfully_synced_files_count.setFont(font)
        self.successfully_synced_files_count.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.successfully_synced_files_count.setObjectName(_fromUtf8("successfully_synced_files_count"))
        self.files_to_sync = QtGui.QLabel(SyncMenu)
        self.files_to_sync.setGeometry(QtCore.QRect(250, 280, 201, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.files_to_sync.setFont(font)
        self.files_to_sync.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.files_to_sync.setObjectName(_fromUtf8("files_to_sync"))
        self.file_sync_in_progress_count = QtGui.QLabel(SyncMenu)
        self.file_sync_in_progress_count.setGeometry(QtCore.QRect(400, 310, 141, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.file_sync_in_progress_count.setFont(font)
        self.file_sync_in_progress_count.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.file_sync_in_progress_count.setObjectName(_fromUtf8("file_sync_in_progress_count"))
        self.summary_synced_files_size = QtGui.QLabel(SyncMenu)
        self.summary_synced_files_size.setGeometry(QtCore.QRect(360, 340, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.summary_synced_files_size.setFont(font)
        self.summary_synced_files_size.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.summary_synced_files_size.setObjectName(_fromUtf8("summary_synced_files_size"))
        self.current_sync_status = QtGui.QLabel(SyncMenu)
        self.current_sync_status.setGeometry(QtCore.QRect(370, 380, 151, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.current_sync_status.setFont(font)
        self.current_sync_status.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.current_sync_status.setObjectName(_fromUtf8("current_sync_status"))
        self.file_name_8 = QtGui.QLabel(SyncMenu)
        self.file_name_8.setGeometry(QtCore.QRect(280, 40, 131, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.file_name_8.setFont(font)
        self.file_name_8.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.file_name_8.setObjectName(_fromUtf8("file_name_8"))
        self.sync_status = QtGui.QLabel(SyncMenu)
        self.sync_status.setGeometry(QtCore.QRect(420, 40, 111, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.sync_status.setFont(font)
        self.sync_status.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.sync_status.setObjectName(_fromUtf8("sync_status"))
        self.sync_logs_bt = QtGui.QPushButton(SyncMenu)
        self.sync_logs_bt.setGeometry(QtCore.QRect(300, 420, 271, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.sync_logs_bt.setFont(font)
        self.sync_logs_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color:  #2683ff;\n"
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
        self.sync_logs_bt.setObjectName(_fromUtf8("sync_logs_bt"))

        self.retranslateUi(SyncMenu)
        QtCore.QMetaObject.connectSlotsByName(SyncMenu)

    def retranslateUi(self, SyncMenu):
        SyncMenu.setWindowTitle(_translate("SyncMenu", "File synchronization menu", None))
        self.file_name.setText(_translate("SyncMenu", "<html><head/><body><p><span style=\" font-size:18pt;\">Synchronization menu</span></p></body></html>", None))
        self.sync_settings_bt.setText(_translate("SyncMenu", "SYNCHRONIZATION SETTINGS", None))
        self.stop_sync_bt.setText(_translate("SyncMenu", "STOP SYNCHRONIZATION", None))
        self.start_sync_bt.setText(_translate("SyncMenu", "START SYNCHRONIZATION", None))
        self.file_name_2.setText(_translate("SyncMenu", "<html><head/><body><p><span style=\" font-size:16pt;\">Synchronization statistics</span></p></body></html>", None))
        self.detailied_sync_stats_bt.setText(_translate("SyncMenu", "DETAILED FILES SYNC STATS", None))
        self.file_name_3.setText(_translate("SyncMenu", "<html><head/><body><p><span style=\" font-size:14pt;\">Files synchronized successfully:</span></p></body></html>", None))
        self.file_name_4.setText(_translate("SyncMenu", "<html><head/><body><p><span style=\" font-size:14pt;\">Files to synchronize:</span></p></body></html>", None))
        self.file_name_5.setText(_translate("SyncMenu", "<html><head/><body><p><span style=\" font-size:14pt;\">Files synchronizations in progress:</span></p></body></html>", None))
        self.file_name_6.setText(_translate("SyncMenu", "<html><head/><body><p><span style=\" font-size:14pt;\">Total size of synchronized files:</span></p></body></html>", None))
        self.file_name_7.setText(_translate("SyncMenu", "<html><head/><body><p><span style=\" font-size:14pt;\">Current synchronization status:</span></p></body></html>", None))
        self.successfully_synced_files_count.setText(_translate("SyncMenu", "<html><head/><body><p><span style=\" font-size:14pt;\">0</span></p></body></html>", None))
        self.files_to_sync.setText(_translate("SyncMenu", "<html><head/><body><p><span style=\" font-size:14pt;\">0</span></p></body></html>", None))
        self.file_sync_in_progress_count.setText(_translate("SyncMenu", "<html><head/><body><p><span style=\" font-size:14pt;\">0</span></p></body></html>", None))
        self.summary_synced_files_size.setText(_translate("SyncMenu", "<html><head/><body><p><span style=\" font-size:14pt;\">0</span></p></body></html>", None))
        self.current_sync_status.setText(_translate("SyncMenu", "<html><head/><body><p><span style=\" font-size:14pt;\">0</span></p></body></html>", None))
        self.file_name_8.setText(_translate("SyncMenu", "<html><head/><body><p><span style=\" font-size:14pt;\">Sync status:</span></p></body></html>", None))
        self.sync_status.setText(_translate("SyncMenu", "<html><head/><body><p><span style=\" font-size:14pt; color:#ff0000;\">DISABLED</span></p></body></html>", None))
        self.sync_logs_bt.setText(_translate("SyncMenu", "SYNC LOGS", None))

import resources_rc
