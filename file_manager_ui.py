# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_manager.ui'
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

class Ui_FileManager(object):
    def setupUi(self, FileManager):
        FileManager.setObjectName(_fromUtf8("FileManager"))
        FileManager.resize(977, 313)
        self.label = QtGui.QLabel(FileManager)
        self.label.setGeometry(QtCore.QRect(290, 0, 141, 61))
        self.label.setObjectName(_fromUtf8("label"))
        self.file_delete_bt = QtGui.QPushButton(FileManager)
        self.file_delete_bt.setGeometry(QtCore.QRect(760, 100, 211, 31))
        self.file_delete_bt.setObjectName(_fromUtf8("file_delete_bt"))
        self.file_mirrors_bt = QtGui.QPushButton(FileManager)
        self.file_mirrors_bt.setGeometry(QtCore.QRect(760, 60, 211, 31))
        self.file_mirrors_bt.setObjectName(_fromUtf8("file_mirrors_bt"))
        self.line = QtGui.QFrame(FileManager)
        self.line.setGeometry(QtCore.QRect(740, 60, 20, 241))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.quit_bt = QtGui.QPushButton(FileManager)
        self.quit_bt.setGeometry(QtCore.QRect(760, 240, 211, 61))
        self.quit_bt.setObjectName(_fromUtf8("quit_bt"))
        self.files_list_tableview = QtGui.QTableView(FileManager)
        self.files_list_tableview.setGeometry(QtCore.QRect(10, 60, 731, 241))
        self.files_list_tableview.setObjectName(_fromUtf8("files_list_tableview"))
        self.file_download_bt = QtGui.QPushButton(FileManager)
        self.file_download_bt.setGeometry(QtCore.QRect(760, 140, 211, 31))
        self.file_download_bt.setObjectName(_fromUtf8("file_download_bt"))
        self.new_file_upload_bt = QtGui.QPushButton(FileManager)
        self.new_file_upload_bt.setGeometry(QtCore.QRect(760, 180, 211, 51))
        self.new_file_upload_bt.setObjectName(_fromUtf8("new_file_upload_bt"))
        self.label_2 = QtGui.QLabel(FileManager)
        self.label_2.setGeometry(QtCore.QRect(600, 20, 131, 31))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.bucket_select_combo_box = QtGui.QComboBox(FileManager)
        self.bucket_select_combo_box.setGeometry(QtCore.QRect(740, 20, 231, 31))
        self.bucket_select_combo_box.setObjectName(_fromUtf8("bucket_select_combo_box"))

        self.retranslateUi(FileManager)
        QtCore.QMetaObject.connectSlotsByName(FileManager)

    def retranslateUi(self, FileManager):
        FileManager.setWindowTitle(_translate("FileManager", "File manager - Storj GUI Client", None))
        self.label.setText(_translate("FileManager", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">File manager</span></p></body></html>", None))
        self.file_delete_bt.setText(_translate("FileManager", "Delete selected file", None))
        self.file_mirrors_bt.setText(_translate("FileManager", "List mirrors of selected file/files", None))
        self.quit_bt.setText(_translate("FileManager", "Quit", None))
        self.file_download_bt.setText(_translate("FileManager", "Download selected file", None))
        self.new_file_upload_bt.setText(_translate("FileManager", "Upload new file", None))
        self.label_2.setText(_translate("FileManager", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Select bucket:</span></p></body></html>", None))

