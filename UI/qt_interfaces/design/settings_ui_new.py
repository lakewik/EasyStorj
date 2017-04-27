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
        ClientConfiguration.resize(412, 448)
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
        self.logout_bt.setGeometry(QtCore.QRect(10, 320, 391, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.logout_bt.setFont(font)
        self.logout_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.logout_bt.setObjectName(_fromUtf8("logout_bt"))
        self.label_5 = QtGui.QLabel(ClientConfiguration)
        self.label_5.setGeometry(QtCore.QRect(10, 14, 251, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.connections_onetime = QtGui.QSpinBox(ClientConfiguration)
        self.connections_onetime.setGeometry(QtCore.QRect(260, 50, 141, 32))
        self.connections_onetime.setObjectName(_fromUtf8("connections_onetime"))
        self.label_19 = QtGui.QLabel(ClientConfiguration)
        self.label_19.setGeometry(QtCore.QRect(10, 56, 171, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_19.setFont(font)
        self.label_19.setObjectName(_fromUtf8("label_19"))
        self.clear_logs_bt = QtGui.QPushButton(ClientConfiguration)
        self.clear_logs_bt.setGeometry(QtCore.QRect(10, 220, 391, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.clear_logs_bt.setFont(font)
        self.clear_logs_bt.setStyleSheet(_fromUtf8("QPushButton:pressed {\n"
"\n"
"}\n"
"QPushButton {\n"
"    background-color: #ffa500;\n"
"    border: 1px solid #ffa500;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}\n"
""))
        self.clear_logs_bt.setObjectName(_fromUtf8("clear_logs_bt"))
        self.shard_size_unit = QtGui.QComboBox(ClientConfiguration)
        self.shard_size_unit.setGeometry(QtCore.QRect(340, 8, 61, 31))
        self.shard_size_unit.setObjectName(_fromUtf8("shard_size_unit"))
        self.shard_size_unit.addItem(_fromUtf8(""))
        self.shard_size_unit.addItem(_fromUtf8(""))
        self.shard_size_unit.addItem(_fromUtf8(""))
        self.shard_size_unit.addItem(_fromUtf8(""))
        self.max_shard_size = QtGui.QSpinBox(ClientConfiguration)
        self.max_shard_size.setGeometry(QtCore.QRect(260, 7, 71, 32))
        self.max_shard_size.setObjectName(_fromUtf8("max_shard_size"))
        self.max_download_bandwidth = QtGui.QLineEdit(ClientConfiguration)
        self.max_download_bandwidth.setEnabled(False)
        self.max_download_bandwidth.setGeometry(QtCore.QRect(260, 93, 141, 31))
        self.max_download_bandwidth.setObjectName(_fromUtf8("max_download_bandwidth"))
        self.label_7 = QtGui.QLabel(ClientConfiguration)
        self.label_7.setEnabled(False)
        self.label_7.setGeometry(QtCore.QRect(10, 100, 211, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.max_upload_bandwidth = QtGui.QLineEdit(ClientConfiguration)
        self.max_upload_bandwidth.setEnabled(False)
        self.max_upload_bandwidth.setGeometry(QtCore.QRect(260, 133, 141, 31))
        self.max_upload_bandwidth.setObjectName(_fromUtf8("max_upload_bandwidth"))
        self.label_8 = QtGui.QLabel(ClientConfiguration)
        self.label_8.setEnabled(False)
        self.label_8.setGeometry(QtCore.QRect(10, 140, 191, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.restore_to_default_bt = QtGui.QPushButton(ClientConfiguration)
        self.restore_to_default_bt.setGeometry(QtCore.QRect(10, 270, 391, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.restore_to_default_bt.setFont(font)
        self.restore_to_default_bt.setStyleSheet(_fromUtf8("QPushButton:pressed {\n"
"\n"
"}\n"
"QPushButton {\n"
"    background-color: #ffa500;\n"
"    border: 1px solid #ffa500;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}\n"
""))
        self.restore_to_default_bt.setObjectName(_fromUtf8("restore_to_default_bt"))
        self.label_9 = QtGui.QLabel(ClientConfiguration)
        self.label_9.setEnabled(False)
        self.label_9.setGeometry(QtCore.QRect(10, 180, 221, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setObjectName(_fromUtf8("label_9"))
        self.shard_size_unit_2 = QtGui.QComboBox(ClientConfiguration)
        self.shard_size_unit_2.setGeometry(QtCore.QRect(260, 173, 141, 31))
        self.shard_size_unit_2.setObjectName(_fromUtf8("shard_size_unit_2"))
        self.shard_size_unit_2.addItem(_fromUtf8(""))
        self.apply_bt = QtGui.QPushButton(ClientConfiguration)
        self.apply_bt.setGeometry(QtCore.QRect(280, 400, 121, 31))
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
        self.cancel_bt.setGeometry(QtCore.QRect(10, 400, 91, 31))
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

        self.retranslateUi(ClientConfiguration)
        self.shard_size_unit.setCurrentIndex(1)
        self.shard_size_unit_2.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(ClientConfiguration)
        ClientConfiguration.setTabOrder(self.max_shard_size, self.shard_size_unit)
        ClientConfiguration.setTabOrder(self.shard_size_unit, self.connections_onetime)
        ClientConfiguration.setTabOrder(self.connections_onetime, self.max_download_bandwidth)
        ClientConfiguration.setTabOrder(self.max_download_bandwidth, self.max_upload_bandwidth)
        ClientConfiguration.setTabOrder(self.max_upload_bandwidth, self.shard_size_unit_2)
        ClientConfiguration.setTabOrder(self.shard_size_unit_2, self.clear_logs_bt)
        ClientConfiguration.setTabOrder(self.clear_logs_bt, self.restore_to_default_bt)
        ClientConfiguration.setTabOrder(self.restore_to_default_bt, self.logout_bt)
        ClientConfiguration.setTabOrder(self.logout_bt, self.cancel_bt)
        ClientConfiguration.setTabOrder(self.cancel_bt, self.apply_bt)

    def retranslateUi(self, ClientConfiguration):
        ClientConfiguration.setWindowTitle(_translate("ClientConfiguration", "Main settings - Storj GUI", None))
        self.logout_bt.setText(_translate("ClientConfiguration", "LOGOUT", None))
        self.label_5.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">MAX SIZE OF SINGLE SHARD:</span></p></body></html>", None))
        self.label_19.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">MAX CONNECTIONS:</span></p></body></html>", None))
        self.clear_logs_bt.setText(_translate("ClientConfiguration", "CLEAR LOGS", None))
        self.shard_size_unit.setItemText(0, _translate("ClientConfiguration", "MB", None))
        self.shard_size_unit.setItemText(1, _translate("ClientConfiguration", "GB", None))
        self.shard_size_unit.setItemText(2, _translate("ClientConfiguration", "TB", None))
        self.shard_size_unit.setItemText(3, _translate("ClientConfiguration", "PB", None))
        self.label_7.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">MAX DOWNLOAD SPEED:</span></p></body></html>", None))
        self.label_8.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">MAX UPLOAD SPEED:</span></p></body></html>", None))
        self.restore_to_default_bt.setText(_translate("ClientConfiguration", "RESTORE TO DEFAULTS", None))
        self.label_9.setText(_translate("ClientConfiguration", "<html><head/><body><p><span style=\" color:#555555;\">ENCRYPTION ALGORITHM:</span></p></body></html>", None))
        self.shard_size_unit_2.setItemText(0, _translate("ClientConfiguration", "AES", None))
        self.apply_bt.setText(_translate("ClientConfiguration", "SAVE", None))
        self.cancel_bt.setText(_translate("ClientConfiguration", "CANCEL", None))

