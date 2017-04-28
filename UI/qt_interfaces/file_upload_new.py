# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'upload_new.ui'
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

class Ui_SingleFileUpload(object):
    def setupUi(self, SingleFileUpload):
        SingleFileUpload.setObjectName(_fromUtf8("SingleFileUpload"))
        SingleFileUpload.resize(975, 591)
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
        SingleFileUpload.setPalette(palette)
        SingleFileUpload.setAutoFillBackground(False)
        SingleFileUpload.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.start_upload_bt = QtGui.QPushButton(SingleFileUpload)
        self.start_upload_bt.setGeometry(QtCore.QRect(840, 550, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.start_upload_bt.setFont(font)
        self.start_upload_bt.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
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
        self.start_upload_bt.setObjectName(_fromUtf8("start_upload_bt"))
        self.cancel_bt = QtGui.QPushButton(SingleFileUpload)
        self.cancel_bt.setGeometry(QtCore.QRect(10, 550, 91, 31))
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
        self.label_4 = QtGui.QLabel(SingleFileUpload)
        self.label_4.setGeometry(QtCore.QRect(20, 20, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.shard_queue_table_widget = QtGui.QTableWidget(SingleFileUpload)
        self.shard_queue_table_widget.setGeometry(QtCore.QRect(10, 280, 951, 221))
        self.shard_queue_table_widget.setObjectName(_fromUtf8("shard_queue_table_widget"))
        self.shard_queue_table_widget.setColumnCount(0)
        self.shard_queue_table_widget.setRowCount(0)
        self.save_to_bucket_select = QtGui.QComboBox(SingleFileUpload)
        self.save_to_bucket_select.setGeometry(QtCore.QRect(130, 10, 251, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(10)
        self.save_to_bucket_select.setFont(font)
        self.save_to_bucket_select.setObjectName(_fromUtf8("save_to_bucket_select"))
        self.overall_progress = QtGui.QProgressBar(SingleFileUpload)
        self.overall_progress.setGeometry(QtCore.QRect(10, 510, 951, 31))
        self.overall_progress.setProperty("value", 0)
        self.overall_progress.setObjectName(_fromUtf8("overall_progress"))
        self.file_path = QtGui.QLineEdit(SingleFileUpload)
        self.file_path.setGeometry(QtCore.QRect(130, 57, 801, 31))
        self.file_path.setObjectName(_fromUtf8("file_path"))
        self.file_path_select_bt = QtGui.QPushButton(SingleFileUpload)
        self.file_path_select_bt.setGeometry(QtCore.QRect(940, 60, 31, 31))
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
        self.label_6 = QtGui.QLabel(SingleFileUpload)
        self.label_6.setGeometry(QtCore.QRect(15, 180, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.file_size = QtGui.QLabel(SingleFileUpload)
        self.file_size.setGeometry(QtCore.QRect(110, 180, 101, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.file_size.setFont(font)
        self.file_size.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.file_size.setObjectName(_fromUtf8("file_size"))
        self.label_5 = QtGui.QLabel(SingleFileUpload)
        self.label_5.setGeometry(QtCore.QRect(20, 64, 91, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_8 = QtGui.QLabel(SingleFileUpload)
        self.label_8.setGeometry(QtCore.QRect(20, 107, 101, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.tmp_path_select_bt = QtGui.QPushButton(SingleFileUpload)
        self.tmp_path_select_bt.setGeometry(QtCore.QRect(940, 100, 31, 31))
        self.tmp_path_select_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.tmp_path_select_bt.setObjectName(_fromUtf8("tmp_path_select_bt"))
        self.tmp_path = QtGui.QLineEdit(SingleFileUpload)
        self.tmp_path.setGeometry(QtCore.QRect(130, 100, 801, 31))
        self.tmp_path.setObjectName(_fromUtf8("tmp_path"))
        self.encrypt_files_checkbox = QtGui.QCheckBox(SingleFileUpload)
        self.encrypt_files_checkbox.setGeometry(QtCore.QRect(130, 140, 171, 22))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(False)
        font.setItalic(False)
        font.setWeight(50)
        self.encrypt_files_checkbox.setFont(font)
        self.encrypt_files_checkbox.setStyleSheet(_fromUtf8("QCheckBox{\n"
"    color: #555555;\n"
"}"))
        self.encrypt_files_checkbox.setChecked(True)
        self.encrypt_files_checkbox.setTristate(False)
        self.encrypt_files_checkbox.setObjectName(_fromUtf8("encrypt_files_checkbox"))
        self.label_9 = QtGui.QLabel(SingleFileUpload)
        self.label_9.setGeometry(QtCore.QRect(15, 210, 121, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.push_token = QtGui.QLabel(SingleFileUpload)
        self.push_token.setGeometry(QtCore.QRect(140, 210, 821, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.push_token.setFont(font)
        self.push_token.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.push_token.setObjectName(_fromUtf8("push_token"))
        self.label_11 = QtGui.QLabel(SingleFileUpload)
        self.label_11.setGeometry(QtCore.QRect(225, 180, 191, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.shardsize = QtGui.QLabel(SingleFileUpload)
        self.shardsize.setGeometry(QtCore.QRect(410, 180, 101, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.shardsize.setFont(font)
        self.shardsize.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.shardsize.setObjectName(_fromUtf8("shardsize"))
        self.label_13 = QtGui.QLabel(SingleFileUpload)
        self.label_13.setGeometry(QtCore.QRect(520, 180, 131, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.file_frame_id = QtGui.QLabel(SingleFileUpload)
        self.file_frame_id.setGeometry(QtCore.QRect(660, 180, 291, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.file_frame_id.setFont(font)
        self.file_frame_id.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.file_frame_id.setObjectName(_fromUtf8("file_frame_id"))
        self.label_15 = QtGui.QLabel(SingleFileUpload)
        self.label_15.setGeometry(QtCore.QRect(640, 250, 181, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.uploaded_shards = QtGui.QLabel(SingleFileUpload)
        self.uploaded_shards.setGeometry(QtCore.QRect(820, 250, 141, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.uploaded_shards.setFont(font)
        self.uploaded_shards.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.uploaded_shards.setObjectName(_fromUtf8("uploaded_shards"))
        self.label_17 = QtGui.QLabel(SingleFileUpload)
        self.label_17.setGeometry(QtCore.QRect(15, 250, 111, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.avg_bandwidth = QtGui.QLabel(SingleFileUpload)
        self.avg_bandwidth.setGeometry(QtCore.QRect(130, 250, 161, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.avg_bandwidth.setFont(font)
        self.avg_bandwidth.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.avg_bandwidth.setObjectName(_fromUtf8("avg_bandwidth"))
        self.current_state = QtGui.QLabel(SingleFileUpload)
        self.current_state.setGeometry(QtCore.QRect(120, 549, 711, 31))
        font = QtGui.QFont()
        font.setPointSize(-1)
        font.setBold(True)
        font.setWeight(75)
        self.current_state.setFont(font)
        self.current_state.setStyleSheet(_fromUtf8("QLabel{\n"
"    font-size: 12px;\n"
"font-weight: bold;\n"
"}\n"
""))
        self.current_state.setObjectName(_fromUtf8("current_state"))
        self.label_16 = QtGui.QLabel(SingleFileUpload)
        self.label_16.setGeometry(QtCore.QRect(290, 250, 201, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_16.setFont(font)
        self.label_16.setObjectName(_fromUtf8("label_16"))
        self.current_active_connections = QtGui.QLabel(SingleFileUpload)
        self.current_active_connections.setGeometry(QtCore.QRect(490, 250, 91, 20))
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

        self.retranslateUi(SingleFileUpload)
        QtCore.QMetaObject.connectSlotsByName(SingleFileUpload)
        SingleFileUpload.setTabOrder(self.save_to_bucket_select, self.file_path)
        SingleFileUpload.setTabOrder(self.file_path, self.file_path_select_bt)
        SingleFileUpload.setTabOrder(self.file_path_select_bt, self.tmp_path)
        SingleFileUpload.setTabOrder(self.tmp_path, self.tmp_path_select_bt)
        SingleFileUpload.setTabOrder(self.tmp_path_select_bt, self.encrypt_files_checkbox)
        SingleFileUpload.setTabOrder(self.encrypt_files_checkbox, self.shard_queue_table_widget)
        SingleFileUpload.setTabOrder(self.shard_queue_table_widget, self.cancel_bt)
        SingleFileUpload.setTabOrder(self.cancel_bt, self.start_upload_bt)

    def retranslateUi(self, SingleFileUpload):
        SingleFileUpload.setWindowTitle(_translate("SingleFileUpload", "Upload new file - Storj GUI", None))
        self.start_upload_bt.setText(_translate("SingleFileUpload", "UPLOAD", None))
        self.cancel_bt.setText(_translate("SingleFileUpload", "CANCEL", None))
        self.label_4.setText(_translate("SingleFileUpload", "<html><head/><body><p><span style=\" color:#555555;\">BUCKET:</span></p></body></html>", None))
        self.file_path_select_bt.setText(_translate("SingleFileUpload", "...", None))
        self.label_6.setText(_translate("SingleFileUpload", "<html><head/><body><p><span style=\" color:#555555;\">FILE SIZE:</span></p></body></html>", None))
        self.file_size.setText(_translate("SingleFileUpload", "<html><head/><body><p><span style=\" color:#2683ff;\">N/A</span></p></body></html>", None))
        self.label_5.setText(_translate("SingleFileUpload", "<html><head/><body><p><span style=\" color:#555555;\">FILE:</span></p></body></html>", None))
        self.label_8.setText(_translate("SingleFileUpload", "<html><head/><body><p><span style=\" color:#555555;\">TEMP PATH:</span></p></body></html>", None))
        self.tmp_path_select_bt.setText(_translate("SingleFileUpload", "...", None))
        self.encrypt_files_checkbox.setText(_translate("SingleFileUpload", "ENCRYPT FILE", None))
        self.label_9.setText(_translate("SingleFileUpload", "<html><head/><body><p><span style=\" color:#555555;\">PUSH TOKEN:</span></p></body></html>", None))
        self.push_token.setText(_translate("SingleFileUpload", "<html><head/><body><p><span style=\" color:#2683ff;\">5075c00004d06b0de02885f9de1016e4c5bc481b08d980ff6e83a9093ec7110f</span></p></body></html>", None))
        self.label_11.setText(_translate("SingleFileUpload", "<html><head/><body><p><span style=\" color:#555555;\">SINGLE SHARD SIZE:</span></p></body></html>", None))
        self.shardsize.setText(_translate("SingleFileUpload", "<html><head/><body><p><span style=\" color:#2683ff;\">N/A</span></p></body></html>", None))
        self.label_13.setText(_translate("SingleFileUpload", "<html><head/><body><p><span style=\" color:#555555;\">FILE FRAME ID:</span></p></body></html>", None))
        self.file_frame_id.setText(_translate("SingleFileUpload", "<html><head/><body><p><span style=\" color:#2683ff;\">58fa49dfd2720b0fb9d9845f</span></p></body></html>", None))
        self.label_15.setText(_translate("SingleFileUpload", "<html><head/><body><p><span style=\" color:#555555;\">UPLOADED SHARDS:</span></p></body></html>", None))
        self.uploaded_shards.setText(_translate("SingleFileUpload", "<html><head/><body><p align=\"center\"><span style=\" color:#2683ff;\">Waiting...</span></p></body></html>", None))
        self.label_17.setText(_translate("SingleFileUpload", "<html><head/><body><p><span style=\" color:#555555;\">AVG SPEED:</span></p></body></html>", None))
        self.avg_bandwidth.setText(_translate("SingleFileUpload", "<html><head/><body><p align=\"center\"><span style=\" color:#2683ff;\">N/A</span></p></body></html>", None))
        self.current_state.setText(_translate("SingleFileUpload", "<html><head/><body><p><span style=\" color:#555555;\">WAITING TO START UPLOAD</span></p></body></html>", None))
        self.label_16.setText(_translate("SingleFileUpload", "<html><head/><body><p><span style=\" color:#555555;\">ACTIVE CONNECTIONS:</span></p></body></html>", None))
        self.current_active_connections.setText(_translate("SingleFileUpload", "<html><head/><body><p align=\"center\"><span style=\" color:#2683ff;\">0</span></p></body></html>", None))

