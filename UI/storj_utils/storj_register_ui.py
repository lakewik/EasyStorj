# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'storj_register.ui'
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

class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName(_fromUtf8("Register"))
        Register.resize(394, 517)
        self.label = QtGui.QLabel(Register)
        self.label.setGeometry(QtCore.QRect(20, 10, 371, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(Register)
        self.label_2.setGeometry(QtCore.QRect(30, 80, 101, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.line = QtGui.QFrame(Register)
        self.line.setGeometry(QtCore.QRect(40, 50, 311, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.bridge_url = QtGui.QLineEdit(Register)
        self.bridge_url.setGeometry(QtCore.QRect(130, 70, 231, 41))
        self.bridge_url.setObjectName(_fromUtf8("bridge_url"))
        self.label_3 = QtGui.QLabel(Register)
        self.label_3.setGeometry(QtCore.QRect(30, 220, 101, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.password = QtGui.QLineEdit(Register)
        self.password.setGeometry(QtCore.QRect(40, 250, 311, 41))
        self.password.setText(_fromUtf8(""))
        self.password.setObjectName(_fromUtf8("password"))
        self.password_2 = QtGui.QLineEdit(Register)
        self.password_2.setGeometry(QtCore.QRect(40, 340, 311, 41))
        self.password_2.setText(_fromUtf8(""))
        self.password_2.setObjectName(_fromUtf8("password_2"))
        self.label_4 = QtGui.QLabel(Register)
        self.label_4.setGeometry(QtCore.QRect(30, 310, 151, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.email = QtGui.QLineEdit(Register)
        self.email.setGeometry(QtCore.QRect(40, 170, 311, 41))
        self.email.setText(_fromUtf8(""))
        self.email.setObjectName(_fromUtf8("email"))
        self.label_5 = QtGui.QLabel(Register)
        self.label_5.setGeometry(QtCore.QRect(30, 140, 101, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.line_2 = QtGui.QFrame(Register)
        self.line_2.setGeometry(QtCore.QRect(40, 110, 311, 20))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.register_bt = QtGui.QPushButton(Register)
        self.register_bt.setGeometry(QtCore.QRect(20, 400, 361, 61))
        self.register_bt.setObjectName(_fromUtf8("register_bt"))
        self.cancel_bt = QtGui.QPushButton(Register)
        self.cancel_bt.setGeometry(QtCore.QRect(20, 470, 361, 31))
        self.cancel_bt.setObjectName(_fromUtf8("cancel_bt"))

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        Register.setWindowTitle(_translate("Register", "Register account in Storj Network - Storj GUI Client", None))
        self.label.setText(_translate("Register", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Register account in Storj Network</span></p></body></html>", None))
        self.label_2.setText(_translate("Register", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Bridge URL:</span></p></body></html>", None))
        self.bridge_url.setText(_translate("Register", "http://api.storj.io", None))
        self.label_3.setText(_translate("Register", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Password:</span></p></body></html>", None))
        self.label_4.setText(_translate("Register", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Repeat password:</span></p></body></html>", None))
        self.label_5.setText(_translate("Register", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">E-mail:</span></p></body></html>", None))
        self.register_bt.setText(_translate("Register", "Register!", None))
        self.cancel_bt.setText(_translate("Register", "Cancel", None))

