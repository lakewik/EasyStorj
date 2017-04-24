# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'edit_bucket_new.ui'
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

class Ui_BucketEditing(object):
    def setupUi(self, BucketEditing):
        BucketEditing.setObjectName(_fromUtf8("BucketEditing"))
        BucketEditing.resize(593, 199)
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
        BucketEditing.setPalette(palette)
        BucketEditing.setAutoFillBackground(False)
        BucketEditing.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.create_edit_bucket_bt = QtGui.QPushButton(BucketEditing)
        self.create_edit_bucket_bt.setGeometry(QtCore.QRect(450, 150, 121, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.create_edit_bucket_bt.setFont(font)
        self.create_edit_bucket_bt.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
"  background-color: #83bf20;\n"
"  border-color: #83bf20;\n"
"}\n"
"QPushButton:active {\n"
"  background-color: #93cc36;\n"
"  border-color: #93cc36;\n"
"}\n"
"QPushButton{\n"
"  background-color: #88c425;\n"
"    border: 1px solid #88c425;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}"))
        self.create_edit_bucket_bt.setObjectName(_fromUtf8("create_edit_bucket_bt"))
        self.remove_bucket_bt = QtGui.QPushButton(BucketEditing)
        self.remove_bucket_bt.setGeometry(QtCore.QRect(140, 150, 181, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.remove_bucket_bt.setFont(font)
        self.remove_bucket_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #CC0000;\n"
"    border: 1px solid #CC0000;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #bb0a0a;\n"
"    border-color: #bb0a0a;\n"
"}\n"
"QPushButton:active {\n"
"    background-color: #ce0e0e;\n"
"    border-color: #ce0e0e;\n"
"}"))
        self.remove_bucket_bt.setObjectName(_fromUtf8("remove_bucket_bt"))
        self.bucket_size = QtGui.QLineEdit(BucketEditing)
        self.bucket_size.setGeometry(QtCore.QRect(180, 57, 321, 31))
        self.bucket_size.setObjectName(_fromUtf8("bucket_size"))
        self.label_5 = QtGui.QLabel(BucketEditing)
        self.label_5.setGeometry(QtCore.QRect(30, 64, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_8 = QtGui.QLabel(BucketEditing)
        self.label_8.setGeometry(QtCore.QRect(30, 107, 171, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setObjectName(_fromUtf8("label_8"))
        self.bucket_transfer = QtGui.QLineEdit(BucketEditing)
        self.bucket_transfer.setGeometry(QtCore.QRect(200, 100, 301, 31))
        self.bucket_transfer.setObjectName(_fromUtf8("bucket_transfer"))
        self.bucket_name = QtGui.QLineEdit(BucketEditing)
        self.bucket_name.setGeometry(QtCore.QRect(180, 13, 391, 31))
        self.bucket_name.setObjectName(_fromUtf8("bucket_name"))
        self.label_6 = QtGui.QLabel(BucketEditing)
        self.label_6.setGeometry(QtCore.QRect(30, 20, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.transfer_unit_select = QtGui.QComboBox(BucketEditing)
        self.transfer_unit_select.setGeometry(QtCore.QRect(509, 100, 61, 31))
        self.transfer_unit_select.setObjectName(_fromUtf8("transfer_unit_select"))
        self.transfer_unit_select.addItem(_fromUtf8(""))
        self.transfer_unit_select.addItem(_fromUtf8(""))
        self.transfer_unit_select.addItem(_fromUtf8(""))
        self.transfer_unit_select.addItem(_fromUtf8(""))
        self.storage_unit_select = QtGui.QComboBox(BucketEditing)
        self.storage_unit_select.setGeometry(QtCore.QRect(509, 57, 61, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        self.storage_unit_select.setFont(font)
        self.storage_unit_select.setObjectName(_fromUtf8("storage_unit_select"))
        self.storage_unit_select.addItem(_fromUtf8(""))
        self.storage_unit_select.addItem(_fromUtf8(""))
        self.storage_unit_select.addItem(_fromUtf8(""))
        self.storage_unit_select.addItem(_fromUtf8(""))
        self.cancel_bt = QtGui.QPushButton(BucketEditing)
        self.cancel_bt.setGeometry(QtCore.QRect(30, 150, 101, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.cancel_bt.setFont(font)
        self.cancel_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #CC0000;\n"
"    border: 1px solid #CC0000;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #bb0a0a;\n"
"    border-color: #bb0a0a;\n"
"}\n"
"QPushButton:active {\n"
"    background-color: #ce0e0e;\n"
"    border-color: #ce0e0e;\n"
"}"))
        self.cancel_bt.setObjectName(_fromUtf8("cancel_bt"))

        self.retranslateUi(BucketEditing)
        self.transfer_unit_select.setCurrentIndex(1)
        self.storage_unit_select.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(BucketEditing)
        BucketEditing.setTabOrder(self.bucket_name, self.bucket_size)
        BucketEditing.setTabOrder(self.bucket_size, self.storage_unit_select)
        BucketEditing.setTabOrder(self.storage_unit_select, self.bucket_transfer)
        BucketEditing.setTabOrder(self.bucket_transfer, self.transfer_unit_select)
        BucketEditing.setTabOrder(self.transfer_unit_select, self.remove_bucket_bt)
        BucketEditing.setTabOrder(self.remove_bucket_bt, self.create_edit_bucket_bt)

    def retranslateUi(self, BucketEditing):
        BucketEditing.setWindowTitle(_translate("BucketEditing", "Edit bucket - Storj GUI", None))
        self.create_edit_bucket_bt.setText(_translate("BucketEditing", "SAVE", None))
        self.remove_bucket_bt.setText(_translate("BucketEditing", "REMOVE BUCKET", None))
        self.label_5.setText(_translate("BucketEditing", "<html><head/><body><p><span style=\" color:#555555;\">BUCKET SIZE:</span></p></body></html>", None))
        self.label_8.setText(_translate("BucketEditing", "<html><head/><body><p><span style=\" color:#555555;\">BUCKET TRANSFER:</span></p></body></html>", None))
        self.label_6.setText(_translate("BucketEditing", "<html><head/><body><p><span style=\" color:#555555;\">BUCKET NAME:</span></p></body></html>", None))
        self.transfer_unit_select.setItemText(0, _translate("BucketEditing", "MB", None))
        self.transfer_unit_select.setItemText(1, _translate("BucketEditing", "GB", None))
        self.transfer_unit_select.setItemText(2, _translate("BucketEditing", "TB", None))
        self.transfer_unit_select.setItemText(3, _translate("BucketEditing", "PB", None))
        self.storage_unit_select.setItemText(0, _translate("BucketEditing", "MB", None))
        self.storage_unit_select.setItemText(1, _translate("BucketEditing", "GB", None))
        self.storage_unit_select.setItemText(2, _translate("BucketEditing", "TB", None))
        self.storage_unit_select.setItemText(3, _translate("BucketEditing", "PB", None))
        self.cancel_bt.setText(_translate("BucketEditing", "CANCEL", None))

