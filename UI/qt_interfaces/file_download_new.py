# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'download_new.ui'
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

class Ui_SingleFileDownload(object):
    def setupUi(self, SingleFileDownload):
        SingleFileDownload.setObjectName(_fromUtf8("SingleFileDownload"))
        SingleFileDownload.resize(622, 557)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        SingleFileDownload.setPalette(palette)
        SingleFileDownload.setAutoFillBackground(False)
        SingleFileDownload.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.start_download_bt = QtGui.QPushButton(SingleFileDownload)
        self.start_download_bt.setGeometry(QtCore.QRect(490, 515, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.start_download_bt.setFont(font)
        self.start_download_bt.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
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
        self.start_download_bt.setObjectName(_fromUtf8("start_download_bt"))
        self.cancel_bt = QtGui.QPushButton(SingleFileDownload)
        self.cancel_bt.setGeometry(QtCore.QRect(10, 515, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_bt.setFont(font)
        self.cancel_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #CC0000;\n"
"    border: 1px solid #CC0000;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #bb0a0a;\n"
"    border-color: #bb0a0a;\n"
"}\n"
"QPushButton:active {\n"
"    background-color: #ce0e0e;\n"
"    border-color: #ce0e0e;\n"
"}"))
        self.cancel_bt.setObjectName(_fromUtf8("cancel_bt"))
        self.shard_queue_table = QtGui.QTableWidget(SingleFileDownload)
        self.shard_queue_table.setGeometry(QtCore.QRect(10, 235, 601, 231))
        self.shard_queue_table.setObjectName(_fromUtf8("shard_queue_table"))
        self.shard_queue_table.setColumnCount(0)
        self.shard_queue_table.setRowCount(0)
        self.overall_progress = QtGui.QProgressBar(SingleFileDownload)
        self.overall_progress.setGeometry(QtCore.QRect(10, 475, 601, 31))
        self.overall_progress.setProperty("value", 0)
        self.overall_progress.setObjectName(_fromUtf8("overall_progress"))
        self.file_save_path = QtGui.QLineEdit(SingleFileDownload)
        self.file_save_path.setGeometry(QtCore.QRect(170, 82, 401, 31))
        self.file_save_path.setObjectName(_fromUtf8("file_save_path"))
        self.file_path_select_bt = QtGui.QPushButton(SingleFileDownload)
        self.file_path_select_bt.setGeometry(QtCore.QRect(580, 82, 31, 31))
        self.file_path_select_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #555555;\n"
"    border: 1px solid #555555;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"  padding: 100px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #403f3f;\n"
"    border-color: #403f3f;\n"
"}\n"
"QPushButton:active {\n"
"    background-color: #505050;\n"
"    border-color: #505050;\n"
"}"))
        self.file_path_select_bt.setObjectName(_fromUtf8("file_path_select_bt"))
        self.label_6 = QtGui.QLabel(SingleFileDownload)
        self.label_6.setGeometry(QtCore.QRect(20, 20, 141, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.file_name = QtGui.QLabel(SingleFileDownload)
        self.file_name.setGeometry(QtCore.QRect(170, 20, 441, 21))
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
        self.label_5 = QtGui.QLabel(SingleFileDownload)
        self.label_5.setGeometry(QtCore.QRect(20, 89, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_8 = QtGui.QLabel(SingleFileDownload)
        self.label_8.setGeometry(QtCore.QRect(20, 127, 111, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.tmp_dir_bt = QtGui.QPushButton(SingleFileDownload)
        self.tmp_dir_bt.setGeometry(QtCore.QRect(580, 120, 31, 31))
        self.tmp_dir_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #555555;\n"
"    border: 1px solid #555555;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"  padding: 100px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #403f3f;\n"
"    border-color: #403f3f;\n"
"}\n"
"QPushButton:active {\n"
"    background-color: #505050;\n"
"    border-color: #505050;\n"
"}"))
        self.tmp_dir_bt.setObjectName(_fromUtf8("tmp_dir_bt"))
        self.tmp_dir = QtGui.QLineEdit(SingleFileDownload)
        self.tmp_dir.setGeometry(QtCore.QRect(170, 120, 401, 31))
        self.tmp_dir.setObjectName(_fromUtf8("tmp_dir"))
        self.label_15 = QtGui.QLabel(SingleFileDownload)
        self.label_15.setGeometry(QtCore.QRect(20, 210, 211, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.downloaded_shards = QtGui.QLabel(SingleFileDownload)
        self.downloaded_shards.setGeometry(QtCore.QRect(230, 210, 381, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.downloaded_shards.setFont(font)
        self.downloaded_shards.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.downloaded_shards.setObjectName(_fromUtf8("downloaded_shards"))
        self.connections_onetime = QtGui.QSpinBox(SingleFileDownload)
        self.connections_onetime.setGeometry(QtCore.QRect(170, 160, 61, 32))
        self.connections_onetime.setObjectName(_fromUtf8("connections_onetime"))
        self.label_19 = QtGui.QLabel(SingleFileDownload)
        self.label_19.setGeometry(QtCore.QRect(20, 170, 121, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.label_9 = QtGui.QLabel(SingleFileDownload)
        self.label_9.setGeometry(QtCore.QRect(20, 50, 141, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.file_id = QtGui.QLabel(SingleFileDownload)
        self.file_id.setGeometry(QtCore.QRect(170, 50, 441, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.file_id.setFont(font)
        self.file_id.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.file_id.setObjectName(_fromUtf8("file_id"))
        self.current_state = QtGui.QLabel(SingleFileDownload)
        self.current_state.setGeometry(QtCore.QRect(120, 520, 351, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.current_state.setFont(font)
        self.current_state.setStyleSheet(_fromUtf8("QLabel {\n"
"text-align: center;\n"
"}"))
        self.current_state.setObjectName(_fromUtf8("current_state"))
        self.label_16 = QtGui.QLabel(SingleFileDownload)
        self.label_16.setGeometry(QtCore.QRect(250, 169, 281, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.current_active_connections = QtGui.QLabel(SingleFileDownload)
        self.current_active_connections.setGeometry(QtCore.QRect(540, 170, 71, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.current_active_connections.setFont(font)
        self.current_active_connections.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.current_active_connections.setObjectName(_fromUtf8("current_active_connections"))

        self.retranslateUi(SingleFileDownload)
        QtCore.QMetaObject.connectSlotsByName(SingleFileDownload)
        SingleFileDownload.setTabOrder(self.file_save_path, self.file_path_select_bt)
        SingleFileDownload.setTabOrder(self.file_path_select_bt, self.tmp_dir)
        SingleFileDownload.setTabOrder(self.tmp_dir, self.tmp_dir_bt)
        SingleFileDownload.setTabOrder(self.tmp_dir_bt, self.connections_onetime)
        SingleFileDownload.setTabOrder(self.connections_onetime, self.shard_queue_table)
        SingleFileDownload.setTabOrder(self.shard_queue_table, self.cancel_bt)
        SingleFileDownload.setTabOrder(self.cancel_bt, self.start_download_bt)

    def retranslateUi(self, SingleFileDownload):
        SingleFileDownload.setWindowTitle(_translate("SingleFileDownload", "Download file - Storj GUI", None))
        self.start_download_bt.setText(_translate("SingleFileDownload", "DOWNLOAD", None))
        self.cancel_bt.setText(_translate("SingleFileDownload", "CANCEL", None))
        self.file_path_select_bt.setText(_translate("SingleFileDownload", "...", None))
        self.label_6.setText(_translate("SingleFileDownload", "<html><head/><body><p><span style=\" color:#555555;\">DOWNLOAD FILE:</span></p></body></html>", None))
        self.file_name.setText(_translate("SingleFileDownload", "<html><head/><body><p><span style=\" color:#2683ff;\">SOME_FILE.MP4</span></p></body></html>", None))
        self.label_5.setText(_translate("SingleFileDownload", "<html><head/><body><p><span style=\" color:#555555;\">FILE:</span></p></body></html>", None))
        self.label_8.setText(_translate("SingleFileDownload", "<html><head/><body><p><span style=\" color:#555555;\">TEMP PATH:</span></p></body></html>", None))
        self.tmp_dir_bt.setText(_translate("SingleFileDownload", "...", None))
        self.label_15.setText(_translate("SingleFileDownload", "<html><head/><body><p><span style=\" color:#555555;\">DOWNLOADED SHARDS:</span></p></body></html>", None))
        self.downloaded_shards.setText(_translate("SingleFileDownload", "<html><head/><body><p><span style=\" color:#2683ff;\">256/2015594</span></p></body></html>", None))
        self.label_19.setText(_translate("SingleFileDownload", "<html><head/><body><p><span style=\" color:#555555;\">CONNECTIONS:</span></p></body></html>", None))
        self.label_9.setText(_translate("SingleFileDownload", "<html><head/><body><p><span style=\" color:#555555;\">FILE ID:</span></p></body></html>", None))
        self.file_id.setText(_translate("SingleFileDownload", "<html><head/><body><p><span style=\" color:#2683ff;\">SOME_FILE_ID</span></p></body></html>", None))
        self.current_state.setText(_translate("SingleFileDownload", "<html><head/><body><p><span style=\" color:#555555;\">WAITING TO START DOWNLOAD</span></p></body></html>", None))
        self.label_16.setText(_translate("SingleFileDownload", "<html><head/><body><p>CURRENT ACTIVE CONNECTIONS:</p></body></html>", None))
        self.current_active_connections.setText(_translate("SingleFileDownload", "<html><head/><body><p><span style=\" color:#2683ff;\">0</span></p></body></html>", None))

