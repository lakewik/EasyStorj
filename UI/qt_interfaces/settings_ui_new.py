# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'settings_new.ui'
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

class Ui_ClientConfiguration(object):
    def setupUi(self, ClientConfiguration):
        ClientConfiguration.setObjectName(_fromUtf8("ClientConfiguration"))
        ClientConfiguration.resize(512, 580)
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
        ClientConfiguration.setPalette(palette)
        ClientConfiguration.setAutoFillBackground(False)
        ClientConfiguration.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.logout_bt = QtGui.QPushButton(ClientConfiguration)
        self.logout_bt.setGeometry(QtCore.QRect(10, 540, 251, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logout_bt.setFont(font)
        self.logout_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.logout_bt.setObjectName(_fromUtf8("logout_bt"))
        self.label_5 = QtGui.QLabel(ClientConfiguration)
        self.label_5.setGeometry(QtCore.QRect(10, 94, 251, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.connections_onetime = QtGui.QSpinBox(ClientConfiguration)
        self.connections_onetime.setGeometry(QtCore.QRect(280, 130, 221, 32))
        self.connections_onetime.setObjectName(_fromUtf8("connections_onetime"))
        self.label_19 = QtGui.QLabel(ClientConfiguration)
        self.label_19.setGeometry(QtCore.QRect(10, 136, 251, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.clear_logs_bt = QtGui.QPushButton(ClientConfiguration)
        self.clear_logs_bt.setGeometry(QtCore.QRect(270, 540, 231, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clear_logs_bt.setFont(font)
        self.clear_logs_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.clear_logs_bt.setObjectName(_fromUtf8("clear_logs_bt"))
        self.shard_size_unit = QtGui.QComboBox(ClientConfiguration)
        self.shard_size_unit.setGeometry(QtCore.QRect(440, 90, 61, 31))
        self.shard_size_unit.setObjectName(_fromUtf8("shard_size_unit"))
        self.shard_size_unit.addItem(_fromUtf8(""))
        self.shard_size_unit.addItem(_fromUtf8(""))
        self.shard_size_unit.addItem(_fromUtf8(""))
        self.shard_size_unit.addItem(_fromUtf8(""))
        self.shard_size_unit.addItem(_fromUtf8(""))
        self.max_shard_size = QtGui.QSpinBox(ClientConfiguration)
        self.max_shard_size.setGeometry(QtCore.QRect(310, 90, 121, 32))
        self.max_shard_size.setObjectName(_fromUtf8("max_shard_size"))
        self.max_download_bandwidth = QtGui.QLineEdit(ClientConfiguration)
        self.max_download_bandwidth.setEnabled(False)
        self.max_download_bandwidth.setGeometry(QtCore.QRect(280, 170, 221, 31))
        self.max_download_bandwidth.setObjectName(_fromUtf8("max_download_bandwidth"))
        self.label_7 = QtGui.QLabel(ClientConfiguration)
        self.label_7.setEnabled(False)
        self.label_7.setGeometry(QtCore.QRect(10, 180, 211, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.max_upload_bandwidth = QtGui.QLineEdit(ClientConfiguration)
        self.max_upload_bandwidth.setEnabled(False)
        self.max_upload_bandwidth.setGeometry(QtCore.QRect(280, 210, 221, 31))
        self.max_upload_bandwidth.setObjectName(_fromUtf8("max_upload_bandwidth"))
        self.label_8 = QtGui.QLabel(ClientConfiguration)
        self.label_8.setEnabled(False)
        self.label_8.setGeometry(QtCore.QRect(10, 220, 191, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.restore_to_default_bt = QtGui.QPushButton(ClientConfiguration)
        self.restore_to_default_bt.setGeometry(QtCore.QRect(110, 500, 231, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.restore_to_default_bt.setFont(font)
        self.restore_to_default_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.restore_to_default_bt.setObjectName(_fromUtf8("restore_to_default_bt"))
        self.label_9 = QtGui.QLabel(ClientConfiguration)
        self.label_9.setEnabled(False)
        self.label_9.setGeometry(QtCore.QRect(10, 260, 221, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.default_crypto_algorithm = QtGui.QComboBox(ClientConfiguration)
        self.default_crypto_algorithm.setGeometry(QtCore.QRect(280, 250, 221, 31))
        self.default_crypto_algorithm.setObjectName(_fromUtf8("default_crypto_algorithm"))
        self.default_crypto_algorithm.addItem(_fromUtf8(""))
        self.apply_bt = QtGui.QPushButton(ClientConfiguration)
        self.apply_bt.setGeometry(QtCore.QRect(350, 500, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.apply_bt.setFont(font)
        self.apply_bt.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
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
        self.apply_bt.setObjectName(_fromUtf8("apply_bt"))
        self.cancel_bt = QtGui.QPushButton(ClientConfiguration)
        self.cancel_bt.setGeometry(QtCore.QRect(10, 500, 91, 31))
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
        self.bridge_request_timeout = QtGui.QSpinBox(ClientConfiguration)
        self.bridge_request_timeout.setGeometry(QtCore.QRect(280, 290, 201, 32))
        self.bridge_request_timeout.setMinimum(1)
        self.bridge_request_timeout.setMaximum(3600)
        self.bridge_request_timeout.setProperty("value", 5)
        self.bridge_request_timeout.setObjectName(_fromUtf8("bridge_request_timeout"))
        self.label_20 = QtGui.QLabel(ClientConfiguration)
        self.label_20.setGeometry(QtCore.QRect(10, 296, 241, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(ClientConfiguration)
        self.label_21.setGeometry(QtCore.QRect(490, 290, 20, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_10 = QtGui.QLabel(ClientConfiguration)
        self.label_10.setEnabled(False)
        self.label_10.setGeometry(QtCore.QRect(10, 330, 221, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_10.setFont(font)
        self.label_10.setObjectName(_fromUtf8("label_10"))
        self.crypto_keys_location = QtGui.QLineEdit(ClientConfiguration)
        self.crypto_keys_location.setEnabled(False)
        self.crypto_keys_location.setGeometry(QtCore.QRect(280, 330, 181, 31))
        self.crypto_keys_location.setObjectName(_fromUtf8("crypto_keys_location"))
        self.crypto_keys_location_select_bt = QtGui.QPushButton(ClientConfiguration)
        self.crypto_keys_location_select_bt.setGeometry(QtCore.QRect(470, 330, 31, 31))
        self.crypto_keys_location_select_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.crypto_keys_location_select_bt.setObjectName(_fromUtf8("crypto_keys_location_select_bt"))
        self.label_3 = QtGui.QLabel(ClientConfiguration)
        self.label_3.setGeometry(QtCore.QRect(40, 10, 161, 71))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/resources/storj-logo-horizontal.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.file_name = QtGui.QLabel(ClientConfiguration)
        self.file_name.setGeometry(QtCore.QRect(240, 10, 211, 71))
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
        self.max_shard_size_enabled_checkBox = QtGui.QCheckBox(ClientConfiguration)
        self.max_shard_size_enabled_checkBox.setGeometry(QtCore.QRect(280, 90, 21, 31))
        self.max_shard_size_enabled_checkBox.setText(_fromUtf8(""))
        self.max_shard_size_enabled_checkBox.setObjectName(_fromUtf8("max_shard_size_enabled_checkBox"))
        self.label_11 = QtGui.QLabel(ClientConfiguration)
        self.label_11.setEnabled(False)
        self.label_11.setGeometry(QtCore.QRect(40, 370, 291, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.background_uploads_enabled = QtGui.QCheckBox(ClientConfiguration)
        self.background_uploads_enabled.setGeometry(QtCore.QRect(10, 370, 21, 31))
        self.background_uploads_enabled.setText(_fromUtf8(""))
        self.background_uploads_enabled.setObjectName(_fromUtf8("background_uploads_enabled"))
        self.background_downloads_enabled = QtGui.QCheckBox(ClientConfiguration)
        self.background_downloads_enabled.setGeometry(QtCore.QRect(10, 410, 21, 31))
        self.background_downloads_enabled.setText(_fromUtf8(""))
        self.background_downloads_enabled.setObjectName(_fromUtf8("background_downloads_enabled"))
        self.label_12 = QtGui.QLabel(ClientConfiguration)
        self.label_12.setEnabled(False)
        self.label_12.setGeometry(QtCore.QRect(40, 410, 321, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_12.setFont(font)
        self.label_12.setObjectName(_fromUtf8("label_12"))
        self.label_13 = QtGui.QLabel(ClientConfiguration)
        self.label_13.setEnabled(False)
        self.label_13.setGeometry(QtCore.QRect(10, 450, 261, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_13.setFont(font)
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.ownstorj_port = QtGui.QSpinBox(ClientConfiguration)
        self.ownstorj_port.setGeometry(QtCore.QRect(280, 450, 221, 32))
        self.ownstorj_port.setMaximum(66589)
        self.ownstorj_port.setProperty("value", 5000)
        self.ownstorj_port.setObjectName(_fromUtf8("ownstorj_port"))

        self.retranslateUi(ClientConfiguration)
        self.shard_size_unit.setCurrentIndex(0)
        self.default_crypto_algorithm.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ClientConfiguration)
        ClientConfiguration.setTabOrder(self.max_shard_size, self.shard_size_unit)
        ClientConfiguration.setTabOrder(self.shard_size_unit, self.connections_onetime)
        ClientConfiguration.setTabOrder(self.connections_onetime, self.max_download_bandwidth)
        ClientConfiguration.setTabOrder(self.max_download_bandwidth, self.max_upload_bandwidth)
        ClientConfiguration.setTabOrder(self.max_upload_bandwidth, self.default_crypto_algorithm)
        ClientConfiguration.setTabOrder(self.default_crypto_algorithm, self.clear_logs_bt)
        ClientConfiguration.setTabOrder(self.clear_logs_bt, self.restore_to_default_bt)
        ClientConfiguration.setTabOrder(self.restore_to_default_bt, self.logout_bt)
        ClientConfiguration.setTabOrder(self.logout_bt, self.cancel_bt)
        ClientConfiguration.setTabOrder(self.cancel_bt, self.apply_bt)

    def retranslateUi(self, ClientConfiguration):
        ClientConfiguration.setWindowTitle(_translate("ClientConfiguration", "Main settings - Storj GUI", None))
        self.logout_bt.setText(_translate("ClientConfiguration", "LOGOUT", None))
        self.label_5.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">MAX SIZE OF SINGLE SHARD:</span></p></body></html>", None))
        self.label_19.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">MAX ONETIME CONNECTIONS:</span></p></body></html>", None))
        self.clear_logs_bt.setText(_translate("ClientConfiguration", "CLEAR LOGS", None))
        self.shard_size_unit.setItemText(0, _translate("ClientConfiguration", "KB", None))
        self.shard_size_unit.setItemText(1, _translate("ClientConfiguration", "MB", None))
        self.shard_size_unit.setItemText(2, _translate("ClientConfiguration", "GB", None))
        self.shard_size_unit.setItemText(3, _translate("ClientConfiguration", "TB", None))
        self.shard_size_unit.setItemText(4, _translate("ClientConfiguration", "PB", None))
        self.label_7.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">MAX DOWNLOAD SPEED:</span></p></body></html>", None))
        self.label_8.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">MAX UPLOAD SPEED:</span></p></body></html>", None))
        self.restore_to_default_bt.setText(_translate("ClientConfiguration", "RESTORE TO DEFAULTS", None))
        self.label_9.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">ENCRYPTION ALGORITHM:</span></p></body></html>", None))
        self.default_crypto_algorithm.setItemText(0, _translate("ClientConfiguration", "AES", None))
        self.apply_bt.setText(_translate("ClientConfiguration", "SAVE", None))
        self.cancel_bt.setText(_translate("ClientConfiguration", "CANCEL", None))
        self.label_20.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">BRIDGE REQUEST TIMEOUT:</span></p></body></html>", None))
        self.label_21.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">s</span></p></body></html>", None))
        self.label_10.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">CRYPTO KEYS LOCATION:</span></p></body></html>", None))
        self.crypto_keys_location_select_bt.setText(_translate("ClientConfiguration", "...", None))
        self.file_name.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" font-size:18pt;\">Main settings</span></p></body></html>", None))
        self.label_11.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">ENABLE BACKGROUND UPLOADS</span></p></body></html>", None))
        self.label_12.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">ENABLE BACKGROUND DOWNLOADS</span></p></body></html>", None))
        self.label_13.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">PORT FOR OwnStorj:</span></p></body></html>", None))

import resources_rc
