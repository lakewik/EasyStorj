# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login_new.ui'
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

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName(_fromUtf8("Login"))
        Login.resize(327, 454)
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
        Login.setPalette(palette)
        Login.setAutoFillBackground(False)
        Login.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.login_bt = QtGui.QPushButton(Login)
        self.login_bt.setGeometry(QtCore.QRect(185, 400, 121, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.login_bt.setFont(font)
        self.login_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.login_bt.setObjectName(_fromUtf8("login_bt"))
        self.label_3 = QtGui.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(90, 5, 141, 141))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/resources/Storj_io-logo.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(0, 170, 326, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.cancel_bt = QtGui.QPushButton(Login)
        self.cancel_bt.setGeometry(QtCore.QRect(20, 400, 106, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(16)
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
        self.email = QtGui.QLineEdit(Login)
        self.email.setGeometry(QtCore.QRect(20, 200, 286, 31))
        self.email.setStyleSheet(_fromUtf8("QLineEdit{\n"
"  padding: 3px;\n"
"  color: #2683ff;\n"
"  font-size: 15px;\n"
"  border: 1px solid #2683ff;\n"
"}"))
        self.email.setText(_fromUtf8(""))
        self.email.setObjectName(_fromUtf8("email"))
        self.label_2 = QtGui.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(0, 245, 326, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.password = QtGui.QLineEdit(Login)
        self.password.setGeometry(QtCore.QRect(20, 275, 286, 31))
        self.password.setStyleSheet(_fromUtf8("QLineEdit{\n"
"  padding: 3px;\n"
"  color: #2683ff;\n"
"  font-size: 15px;\n"
"  border: 1px solid #2683ff;\n"
"}"))
        self.password.setText(_fromUtf8(""))
        self.password.setEchoMode(QtGui.QLineEdit.Password)
        self.password.setObjectName(_fromUtf8("password"))
        self.label_5 = QtGui.QLabel(Login)
        self.label_5.setGeometry(QtCore.QRect(20, 320, 286, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.bridge_url = QtGui.QLineEdit(Login)
        self.bridge_url.setGeometry(QtCore.QRect(20, 350, 286, 31))
        self.bridge_url.setStyleSheet(_fromUtf8("QLineEdit{\n"
"  padding: 3px;\n"
"  color: #2683ff;\n"
"  font-size: 15px;\n"
"  border: 1px solid #2683ff;\n"
"}"))
        self.bridge_url.setObjectName(_fromUtf8("bridge_url"))

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)
        Login.setTabOrder(self.email, self.password)
        Login.setTabOrder(self.password, self.cancel_bt)
        Login.setTabOrder(self.cancel_bt, self.login_bt)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Login - Storj GUI", None))
        self.login_bt.setText(_translate("Login", "LOGIN", None))
        self.label.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" color:#555555;\">Email Address</span></p></body></html>", None))
        self.cancel_bt.setText(_translate("Login", "CANCEL", None))
        self.label_2.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" color:#555555;\">Password</span></p></body></html>", None))
        self.label_5.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" color:#555555;\">Bridge URL</span></p></body></html>", None))
        self.bridge_url.setText(_translate("Login", "https://api.storj.io", None))

import resources_rc
