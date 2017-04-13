# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'initial_window.ui'
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

class Ui_InitialWindow(object):
    def setupUi(self, InitialWindow):
        InitialWindow.setObjectName(_fromUtf8("InitialWindow"))
        InitialWindow.resize(820, 202)
        self.label = QtGui.QLabel(InitialWindow)
        self.label.setGeometry(QtCore.QRect(10, 0, 801, 61))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(InitialWindow)
        self.line.setGeometry(QtCore.QRect(10, 50, 801, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.login_bt = QtGui.QPushButton(InitialWindow)
        self.login_bt.setGeometry(QtCore.QRect(10, 70, 401, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.login_bt.setFont(font)
        self.login_bt.setObjectName(_fromUtf8("login_bt"))
        self.register_bt = QtGui.QPushButton(InitialWindow)
        self.register_bt.setGeometry(QtCore.QRect(420, 70, 391, 71))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.register_bt.setFont(font)
        self.register_bt.setObjectName(_fromUtf8("register_bt"))
        self.about_bt = QtGui.QPushButton(InitialWindow)
        self.about_bt.setGeometry(QtCore.QRect(10, 150, 801, 41))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.about_bt.setFont(font)
        self.about_bt.setObjectName(_fromUtf8("about_bt"))

        self.retranslateUi(InitialWindow)
        QtCore.QMetaObject.connectSlotsByName(InitialWindow)

    def retranslateUi(self, InitialWindow):
        InitialWindow.setWindowTitle(_translate("InitialWindow", "Welcome! - Storj GUI Client", None))
        self.label.setText(_translate("InitialWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:16pt; font-weight:600;\">Login or register in the Storj Distributed Storage Network</span></p></body></html>", None))
        self.login_bt.setText(_translate("InitialWindow", "Login", None))
        self.register_bt.setText(_translate("InitialWindow", "Register", None))
        self.about_bt.setText(_translate("InitialWindow", "About", None))

