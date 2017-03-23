# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'single_file_downloader.ui'
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

class Ui_SingleFileDownload(object):
    def setupUi(self, SingleFileDownload):
        SingleFileDownload.setObjectName(_fromUtf8("SingleFileDownload"))
        SingleFileDownload.resize(955, 459)
        self.line_3 = QtGui.QFrame(SingleFileDownload)
        self.line_3.setGeometry(QtCore.QRect(15, 40, 931, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label = QtGui.QLabel(SingleFileDownload)
        self.label.setGeometry(QtCore.QRect(20, 10, 921, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.shard_queue_table = QtGui.QTableView(SingleFileDownload)
        self.shard_queue_table.setGeometry(QtCore.QRect(415, 110, 531, 211))
        self.shard_queue_table.setObjectName(_fromUtf8("shard_queue_table"))
        self.label_6 = QtGui.QLabel(SingleFileDownload)
        self.label_6.setGeometry(QtCore.QRect(415, 60, 531, 41))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.line = QtGui.QFrame(SingleFileDownload)
        self.line.setGeometry(QtCore.QRect(390, 60, 21, 291))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))

        self.retranslateUi(SingleFileDownload)
        QtCore.QMetaObject.connectSlotsByName(SingleFileDownload)

    def retranslateUi(self, SingleFileDownload):
        SingleFileDownload.setWindowTitle(_translate("SingleFileDownload", "Single file download - Storj GUI Client", None))
        self.label.setText(_translate("SingleFileDownload", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Single file downloading - Storj GUI Client</span></p></body></html>", None))
        self.label_6.setText(_translate("SingleFileDownload", "<html><head/><body><p align=\"center\"><span style=\" font-size:14pt; font-weight:600;\">Shard upload queue progress</span></p></body></html>", None))

