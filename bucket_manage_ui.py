# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bucket_manage.ui'
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

class Ui_BucketManager(object):
    def setupUi(self, BucketManager):
        BucketManager.setObjectName(_fromUtf8("BucketManager"))
        BucketManager.resize(883, 290)
        self.bucket_list_tableview = QtGui.QTableView(BucketManager)
        self.bucket_list_tableview.setGeometry(QtCore.QRect(10, 50, 671, 201))
        self.bucket_list_tableview.setObjectName(_fromUtf8("bucket_list_tableview"))
        self.label = QtGui.QLabel(BucketManager)
        self.label.setGeometry(QtCore.QRect(350, 0, 181, 51))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(BucketManager)
        self.line.setGeometry(QtCore.QRect(690, 50, 20, 201))
        self.line.setFrameShape(QtGui.QFrame.VLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.edit_bucket_bt = QtGui.QPushButton(BucketManager)
        self.edit_bucket_bt.setGeometry(QtCore.QRect(710, 50, 161, 51))
        self.edit_bucket_bt.setObjectName(_fromUtf8("edit_bucket_bt"))
        self.delete_bucket_bt = QtGui.QPushButton(BucketManager)
        self.delete_bucket_bt.setGeometry(QtCore.QRect(710, 110, 161, 41))
        self.delete_bucket_bt.setObjectName(_fromUtf8("delete_bucket_bt"))
        self.quit_bt = QtGui.QPushButton(BucketManager)
        self.quit_bt.setGeometry(QtCore.QRect(710, 210, 161, 41))
        self.quit_bt.setObjectName(_fromUtf8("quit_bt"))
        self.label_2 = QtGui.QLabel(BucketManager)
        self.label_2.setGeometry(QtCore.QRect(630, 260, 111, 21))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.total_buckets_label = QtGui.QLabel(BucketManager)
        self.total_buckets_label.setGeometry(QtCore.QRect(750, 260, 121, 21))
        self.total_buckets_label.setObjectName(_fromUtf8("total_buckets_label"))
        self.create_new_bucket_bt = QtGui.QPushButton(BucketManager)
        self.create_new_bucket_bt.setGeometry(QtCore.QRect(710, 160, 161, 41))
        self.create_new_bucket_bt.setObjectName(_fromUtf8("create_new_bucket_bt"))

        self.retranslateUi(BucketManager)
        QtCore.QMetaObject.connectSlotsByName(BucketManager)

    def retranslateUi(self, BucketManager):
        BucketManager.setWindowTitle(_translate("BucketManager", "Bucket Manager - Storj GUI Client", None))
        self.label.setText(_translate("BucketManager", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Bucket manager</span></p></body></html>", None))
        self.edit_bucket_bt.setText(_translate("BucketManager", "Edit selected bucket", None))
        self.delete_bucket_bt.setText(_translate("BucketManager", "Delete selected bucket", None))
        self.quit_bt.setText(_translate("BucketManager", "Quit", None))
        self.label_2.setText(_translate("BucketManager", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">Total buckets:</span></p></body></html>", None))
        self.total_buckets_label.setText(_translate("BucketManager", "<html><head/><body><p><span style=\" font-size:11pt; font-weight:600;\">N/A</span></p></body></html>", None))
        self.create_new_bucket_bt.setText(_translate("BucketManager", "Create new bucket", None))

