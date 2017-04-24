# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'first_run_new.ui'
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
        InitialWindow.resize(309, 337)
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
        InitialWindow.setPalette(palette)
        InitialWindow.setAutoFillBackground(False)
        InitialWindow.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.login_bt = QtGui.QPushButton(InitialWindow)
        self.login_bt.setGeometry(QtCore.QRect(90, 270, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.login_bt.setFont(font)
        self.login_bt.setStyleSheet(_fromUtf8("QPushButton:pressed {\n"
"\n"
"}\n"
"QPushButton {\n"
"    background-color: #2683ff;\n"
"    border: 1px solid #2683ff;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}\n"
""))
        self.login_bt.setObjectName(_fromUtf8("login_bt"))
        self.label_3 = QtGui.QLabel(InitialWindow)
        self.label_3.setGeometry(QtCore.QRect(90, 10, 141, 141))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8("Storj_io-logo.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label = QtGui.QLabel(InitialWindow)
        self.label.setGeometry(QtCore.QRect(10, 230, 291, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName(_fromUtf8("label"))
        self.register_bt = QtGui.QPushButton(InitialWindow)
        self.register_bt.setGeometry(QtCore.QRect(90, 170, 141, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.register_bt.setFont(font)
        self.register_bt.setStyleSheet(_fromUtf8("QPushButton:pressed {\n"
"\n"
"}\n"
"QPushButton {\n"
"    background-color: #ffa500;\n"
"    border: 1px solid #ffa500;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}\n"
""))
        self.register_bt.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.register_bt.setObjectName(_fromUtf8("register_bt"))

        self.retranslateUi(InitialWindow)
        QtCore.QMetaObject.connectSlotsByName(InitialWindow)
        InitialWindow.setTabOrder(self.register_bt, self.login_bt)

    def retranslateUi(self, InitialWindow):
        InitialWindow.setWindowTitle(_translate("InitialWindow", "Storj GUI", None))
        self.login_bt.setText(_translate("InitialWindow", "LOGIN", None))
        self.label.setText(_translate("InitialWindow", "<html><head/><body><p align=\"center\"><span style=\" color:#2683ff;\">Already have an account?</span></p></body></html>", None))
        self.register_bt.setText(_translate("InitialWindow", "REGISTER", None))

