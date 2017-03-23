# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_menu.ui'
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

class Ui_MainMenu(object):
    def setupUi(self, MainMenu):
        MainMenu.setObjectName(_fromUtf8("MainMenu"))
        MainMenu.resize(715, 257)
        self.label = QtGui.QLabel(MainMenu)
        self.label.setGeometry(QtCore.QRect(230, 10, 241, 41))
        self.label.setObjectName(_fromUtf8("label"))
        self.bucket_menager_bt = QtGui.QPushButton(MainMenu)
        self.bucket_menager_bt.setGeometry(QtCore.QRect(30, 70, 211, 31))
        self.bucket_menager_bt.setObjectName(_fromUtf8("bucket_menager_bt"))
        self.settings_bt = QtGui.QPushButton(MainMenu)
        self.settings_bt.setGeometry(QtCore.QRect(30, 110, 211, 31))
        self.settings_bt.setObjectName(_fromUtf8("settings_bt"))
        self.uploader_bt = QtGui.QPushButton(MainMenu)
        self.uploader_bt.setGeometry(QtCore.QRect(30, 150, 331, 41))
        self.uploader_bt.setObjectName(_fromUtf8("uploader_bt"))
        self.file_manager_bt = QtGui.QPushButton(MainMenu)
        self.file_manager_bt.setGeometry(QtCore.QRect(480, 70, 211, 71))
        self.file_manager_bt.setObjectName(_fromUtf8("file_manager_bt"))
        self.about_bt = QtGui.QPushButton(MainMenu)
        self.about_bt.setGeometry(QtCore.QRect(480, 210, 211, 31))
        self.about_bt.setObjectName(_fromUtf8("about_bt"))
        self.label_2 = QtGui.QLabel(MainMenu)
        self.label_2.setGeometry(QtCore.QRect(40, 210, 91, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.account_label = QtGui.QLabel(MainMenu)
        self.account_label.setGeometry(QtCore.QRect(150, 210, 311, 31))
        self.account_label.setObjectName(_fromUtf8("account_label"))
        self.create_bucket_bt = QtGui.QPushButton(MainMenu)
        self.create_bucket_bt.setGeometry(QtCore.QRect(260, 70, 211, 71))
        self.create_bucket_bt.setObjectName(_fromUtf8("create_bucket_bt"))
        self.downloader_bt = QtGui.QPushButton(MainMenu)
        self.downloader_bt.setGeometry(QtCore.QRect(370, 150, 321, 41))
        self.downloader_bt.setObjectName(_fromUtf8("downloader_bt"))

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(_translate("MainMenu", "Main menu - Storj GUI Client", None))
        self.label.setText(_translate("MainMenu", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Storj GUI Client - Menu</span></p></body></html>", None))
        self.bucket_menager_bt.setText(_translate("MainMenu", "Bucekts manager", None))
        self.settings_bt.setText(_translate("MainMenu", "Settings", None))
        self.uploader_bt.setText(_translate("MainMenu", "File uploader [UNFINISHED]", None))
        self.file_manager_bt.setText(_translate("MainMenu", "File manager", None))
        self.about_bt.setText(_translate("MainMenu", "About", None))
        self.label_2.setText(_translate("MainMenu", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Account:</span></p></body></html>", None))
        self.account_label.setText(_translate("MainMenu", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">abc@def.pl</span></p></body></html>", None))
        self.create_bucket_bt.setText(_translate("MainMenu", "Create bucket", None))
        self.downloader_bt.setText(_translate("MainMenu", "File downloader [UNFINISHED]", None))

