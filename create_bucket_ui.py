# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'create_bucket.ui'
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

class Ui_BucketCreate(object):
    def setupUi(self, BucketCreate):
        BucketCreate.setObjectName(_fromUtf8("BucketCreate"))
        BucketCreate.resize(641, 300)
        self.label = QtGui.QLabel(BucketCreate)
        self.label.setGeometry(QtCore.QRect(150, 0, 351, 51))
        self.label.setObjectName(_fromUtf8("label"))
        self.line = QtGui.QFrame(BucketCreate)
        self.line.setGeometry(QtCore.QRect(20, 50, 601, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.label_5 = QtGui.QLabel(BucketCreate)
        self.label_5.setGeometry(QtCore.QRect(30, 80, 111, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.bucket_name = QtGui.QLineEdit(BucketCreate)
        self.bucket_name.setGeometry(QtCore.QRect(170, 70, 451, 41))
        self.bucket_name.setText(_fromUtf8(""))
        self.bucket_name.setObjectName(_fromUtf8("bucket_name"))
        self.label_6 = QtGui.QLabel(BucketCreate)
        self.label_6.setGeometry(QtCore.QRect(40, 130, 101, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.bucket_storage_size = QtGui.QLineEdit(BucketCreate)
        self.bucket_storage_size.setGeometry(QtCore.QRect(170, 120, 381, 41))
        self.bucket_storage_size.setText(_fromUtf8(""))
        self.bucket_storage_size.setObjectName(_fromUtf8("bucket_storage_size"))
        self.label_7 = QtGui.QLabel(BucketCreate)
        self.label_7.setGeometry(QtCore.QRect(20, 180, 131, 21))
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.bucket_transfer = QtGui.QLineEdit(BucketCreate)
        self.bucket_transfer.setGeometry(QtCore.QRect(170, 170, 381, 41))
        self.bucket_transfer.setText(_fromUtf8(""))
        self.bucket_transfer.setObjectName(_fromUtf8("bucket_transfer"))
        self.storage_unit_select = QtGui.QComboBox(BucketCreate)
        self.storage_unit_select.setGeometry(QtCore.QRect(560, 120, 61, 41))
        self.storage_unit_select.setObjectName(_fromUtf8("storage_unit_select"))
        self.storage_unit_select.addItem(_fromUtf8(""))
        self.storage_unit_select.addItem(_fromUtf8(""))
        self.storage_unit_select.addItem(_fromUtf8(""))
        self.storage_unit_select.addItem(_fromUtf8(""))
        self.transfer_unit_select = QtGui.QComboBox(BucketCreate)
        self.transfer_unit_select.setGeometry(QtCore.QRect(560, 170, 61, 41))
        self.transfer_unit_select.setObjectName(_fromUtf8("transfer_unit_select"))
        self.transfer_unit_select.addItem(_fromUtf8(""))
        self.transfer_unit_select.addItem(_fromUtf8(""))
        self.transfer_unit_select.addItem(_fromUtf8(""))
        self.transfer_unit_select.addItem(_fromUtf8(""))
        self.create_bucket_bt = QtGui.QPushButton(BucketCreate)
        self.create_bucket_bt.setGeometry(QtCore.QRect(140, 230, 481, 61))
        self.create_bucket_bt.setObjectName(_fromUtf8("create_bucket_bt"))
        self.cancel_bt = QtGui.QPushButton(BucketCreate)
        self.cancel_bt.setGeometry(QtCore.QRect(10, 230, 121, 61))
        self.cancel_bt.setObjectName(_fromUtf8("cancel_bt"))

        self.retranslateUi(BucketCreate)
        self.storage_unit_select.setCurrentIndex(1)
        self.transfer_unit_select.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(BucketCreate)

    def retranslateUi(self, BucketCreate):
        BucketCreate.setWindowTitle(_translate("BucketCreate", "Create Bucket - Storj GUI Client", None))
        self.label.setText(_translate("BucketCreate", "<html><head/><body><p><span style=\" font-size:16pt; font-weight:600;\">Create a bucket in Storj Network</span></p></body></html>", None))
        self.label_5.setText(_translate("BucketCreate", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Bucket name:</span></p></body></html>", None))
        self.label_6.setText(_translate("BucketCreate", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Bucket size:</span></p></body></html>", None))
        self.label_7.setText(_translate("BucketCreate", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Bucket transfer:</span></p></body></html>", None))
        self.storage_unit_select.setItemText(0, _translate("BucketCreate", "MB", None))
        self.storage_unit_select.setItemText(1, _translate("BucketCreate", "GB", None))
        self.storage_unit_select.setItemText(2, _translate("BucketCreate", "TB", None))
        self.storage_unit_select.setItemText(3, _translate("BucketCreate", "PB", None))
        self.transfer_unit_select.setItemText(0, _translate("BucketCreate", "MB", None))
        self.transfer_unit_select.setItemText(1, _translate("BucketCreate", "GB", None))
        self.transfer_unit_select.setItemText(2, _translate("BucketCreate", "TB", None))
        self.transfer_unit_select.setItemText(3, _translate("BucketCreate", "PB", None))
        self.create_bucket_bt.setText(_translate("BucketCreate", "Create bucket", None))
        self.cancel_bt.setText(_translate("BucketCreate", "Cancel", None))

