# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storj_login.ui'
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
        Login.resize(400, 428)
        self.label_2 = QtGui.QLabel(Login)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 101, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.label_3 = QtGui.QLabel(Login)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 101, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.login_bt = QtGui.QPushButton(Login)
        self.login_bt.setGeometry(QtCore.QRect(20, 310, 361, 61))
        self.login_bt.setObjectName(_fromUtf8("login_bt"))
        self.line = QtGui.QFrame(Login)
        self.line.setGeometry(QtCore.QRect(40, 50, 311, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.bridge_url = QtGui.QLineEdit(Login)
        self.bridge_url.setGeometry(QtCore.QRect(130, 70, 231, 41))
        self.bridge_url.setObjectName(_fromUtf8("bridge_url"))
        self.label_5 = QtGui.QLabel(Login)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 101, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.password = QtGui.QLineEdit(Login)
        self.password.setGeometry(QtCore.QRect(40, 250, 311, 41))
        self.password.setText(_fromUtf8(""))
        self.password.setObjectName(_fromUtf8("password"))
        self.email = QtGui.QLineEdit(Login)
        self.email.setGeometry(QtCore.QRect(40, 170, 311, 41))
        self.email.setText(_fromUtf8(""))
        self.email.setObjectName(_fromUtf8("email"))
        self.label = QtGui.QLabel(Login)
        self.label.setGeometry(QtCore.QRect(20, 10, 361, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.line_2 = QtGui.QFrame(Login)
        self.line_2.setGeometry(QtCore.QRect(40, 110, 311, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.cancel_bt = QtGui.QPushButton(Login)
        self.cancel_bt.setGeometry(QtCore.QRect(20, 380, 361, 31))
        self.cancel_bt.setObjectName(_fromUtf8("cancel_bt"))

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        Login.setWindowTitle(_translate("Login", "Login to your Storj Account", None))
        self.label_2.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Bridge URL:</span></p></body></html>", None))
        self.label_3.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Password:</span></p></body></html>", None))
        self.login_bt.setText(_translate("Login", "Login!", None))
        self.bridge_url.setText(_translate("Login", "http://api.storj.io", None))
        self.label_5.setText(_translate("Login", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">E-mail:</span></p></body></html>", None))
        self.label.setText(_translate("Login", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Login to your Storj Account</span></p></body></html>", None))
        self.cancel_bt.setText(_translate("Login", "Cancel", None))

