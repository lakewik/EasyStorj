# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_mirrors_list.ui'
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

class Ui_FileMirrorsList(object):
    def setupUi(self, FileMirrorsList):
        FileMirrorsList.setObjectName(_fromUtf8("FileMirrorsList"))
        FileMirrorsList.resize(1252, 548)
        self.label = QtGui.QLabel(FileMirrorsList)
        self.label.setGeometry(QtCore.QRect(530, 0, 171, 61))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(FileMirrorsList)
        self.line.setGeometry(QtCore.QRect(10, 50, 1231, 21))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.established_mirrors_tree = QtGui.QTreeView(FileMirrorsList)
        self.established_mirrors_tree.setGeometry(QtCore.QRect(10, 100, 611, 341))
        self.established_mirrors_tree.setObjectName(_fromUtf8("established_mirrors_tree"))
        self.available_mirrors_tree = QtGui.QTreeView(FileMirrorsList)
        self.available_mirrors_tree.setGeometry(QtCore.QRect(630, 100, 611, 341))
        self.available_mirrors_tree.setObjectName(_fromUtf8("available_mirrors_tree"))
        self.line_2 = QtGui.QFrame(FileMirrorsList)
        self.line_2.setGeometry(QtCore.QRect(10, 480, 1231, 31))
        self.line_2.setFrameShape(QtGui.QFrame.HLine)
        self.line_2.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_2.setObjectName(_fromUtf8("line_2"))
        self.mirror_details_bt = QtGui.QPushButton(FileMirrorsList)
        self.mirror_details_bt.setGeometry(QtCore.QRect(20, 450, 601, 31))
        self.mirror_details_bt.setObjectName(_fromUtf8("mirror_details_bt"))
        self.quit_bt = QtGui.QPushButton(FileMirrorsList)
        self.quit_bt.setGeometry(QtCore.QRect(10, 510, 1231, 31))
        self.quit_bt.setObjectName(_fromUtf8("quit_bt"))
        self.label_2 = QtGui.QLabel(FileMirrorsList)
        self.label_2.setGeometry(QtCore.QRect(910, 0, 71, 61))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.file_id_label = QtGui.QLabel(FileMirrorsList)
        self.file_id_label.setGeometry(QtCore.QRect(990, 0, 251, 61))
        self.file_id_label.setObjectName(_fromUtf8("file_id_label"))
        self.label_3 = QtGui.QLabel(FileMirrorsList)
        self.label_3.setGeometry(QtCore.QRect(900, 50, 101, 61))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(FileMirrorsList)
        self.label_4.setGeometry(QtCore.QRect(260, 50, 171, 61))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.line_3 = QtGui.QFrame(FileMirrorsList)
        self.line_3.setGeometry(QtCore.QRect(599, 60, 61, 31))
        self.line_3.setFrameShape(QtGui.QFrame.VLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_5 = QtGui.QLabel(FileMirrorsList)
        self.label_5.setGeometry(QtCore.QRect(430, 50, 71, 61))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.established_mirrors_count = QtGui.QLabel(FileMirrorsList)
        self.established_mirrors_count.setGeometry(QtCore.QRect(500, 50, 111, 61))
        self.established_mirrors_count.setObjectName(_fromUtf8("established_mirrors_count"))
        self.label_6 = QtGui.QLabel(FileMirrorsList)
        self.label_6.setGeometry(QtCore.QRect(1060, 50, 71, 61))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.available_mirrors_count = QtGui.QLabel(FileMirrorsList)
        self.available_mirrors_count.setGeometry(QtCore.QRect(1130, 50, 111, 61))
        self.available_mirrors_count.setObjectName(_fromUtf8("available_mirrors_count"))
        self.mirror_details_bt_2 = QtGui.QPushButton(FileMirrorsList)
        self.mirror_details_bt_2.setGeometry(QtCore.QRect(630, 450, 611, 31))
        self.mirror_details_bt_2.setObjectName(_fromUtf8("mirror_details_bt_2"))
        self.loading_label_mirrors_established = QtGui.QLabel(FileMirrorsList)
        self.loading_label_mirrors_established.setGeometry(QtCore.QRect(20, 50, 171, 61))
        self.loading_label_mirrors_established.setObjectName(_fromUtf8("loading_label_mirrors_established"))
        self.loading_label_mirrors_available = QtGui.QLabel(FileMirrorsList)
        self.loading_label_mirrors_available.setGeometry(QtCore.QRect(640, 50, 171, 61))
        self.loading_label_mirrors_available.setObjectName(_fromUtf8("loading_label_mirrors_available"))

        self.retranslateUi(FileMirrorsList)
        QtCore.QMetaObject.connectSlotsByName(FileMirrorsList)

    def retranslateUi(self, FileMirrorsList):
        FileMirrorsList.setWindowTitle(_translate("FileMirrorsList", "File mirrors list - Storj GUI Client", None))
        self.label.setText(_translate("FileMirrorsList", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">File mirrors list</span></p></body></html>", None))
        self.mirror_details_bt.setText(_translate("FileMirrorsList", "Selected mirror details", None))
        self.quit_bt.setText(_translate("FileMirrorsList", "Quit", None))
        self.label_2.setText(_translate("FileMirrorsList", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">File ID:</span></p></body></html>", None))
        self.file_id_label.setText(_translate("FileMirrorsList", "<html><head/><body><p><span style=\" font-size:14pt;\">abcdefghijk</span></p></body></html>", None))
        self.label_3.setText(_translate("FileMirrorsList", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Available</span></p></body></html>", None))
        self.label_4.setText(_translate("FileMirrorsList", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Established</span></p></body></html>", None))
        self.label_5.setText(_translate("FileMirrorsList", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Count:</span></p></body></html>", None))
        self.established_mirrors_count.setText(_translate("FileMirrorsList", "<html><head/><body><p><span style=\" font-size:14pt;\">abcdefghijk</span></p></body></html>", None))
        self.label_6.setText(_translate("FileMirrorsList", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Count:</span></p></body></html>", None))
        self.available_mirrors_count.setText(_translate("FileMirrorsList", "<html><head/><body><p><span style=\" font-size:14pt;\">abcdefghijk</span></p></body></html>", None))
        self.mirror_details_bt_2.setText(_translate("FileMirrorsList", "Selected mirror details", None))
        self.loading_label_mirrors_established.setText(_translate("FileMirrorsList", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Loading...</span></p></body></html>", None))
        self.loading_label_mirrors_available.setText(_translate("FileMirrorsList", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Loading...</span></p></body></html>", None))

