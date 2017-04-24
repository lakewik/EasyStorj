# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'file_mirrors_list_new.ui'
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
        FileMirrorsList.resize(1241, 496)
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
        FileMirrorsList.setPalette(palette)
        FileMirrorsList.setAutoFillBackground(False)
        FileMirrorsList.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.label_6 = QtGui.QLabel(FileMirrorsList)
        self.label_6.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_6.setFont(font)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.file_name = QtGui.QLabel(FileMirrorsList)
        self.file_name.setGeometry(QtCore.QRect(110, 10, 511, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.file_name.setFont(font)
        self.file_name.setStyleSheet(_fromUtf8("QLabel {\n"
"    \n"
"    color:#555555;\n"
"}"))
        self.file_name.setObjectName(_fromUtf8("file_name"))
        self.label_11 = QtGui.QLabel(FileMirrorsList)
        self.label_11.setGeometry(QtCore.QRect(10, 30, 81, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_11.setFont(font)
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.file_id = QtGui.QLabel(FileMirrorsList)
        self.file_id.setGeometry(QtCore.QRect(110, 30, 511, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.file_id.setFont(font)
        self.file_id.setStyleSheet(_fromUtf8("QLabel {\n"
"    \n"
"    color:#555555;\n"
"}"))
        self.file_id.setObjectName(_fromUtf8("file_id"))
        self.available_mirrors_tree = QtGui.QTreeView(FileMirrorsList)
        self.available_mirrors_tree.setGeometry(QtCore.QRect(620, 90, 611, 351))
        self.available_mirrors_tree.setObjectName(_fromUtf8("available_mirrors_tree"))
        self.established_mirrors_tree = QtGui.QTreeView(FileMirrorsList)
        self.established_mirrors_tree.setGeometry(QtCore.QRect(10, 90, 601, 351))
        self.established_mirrors_tree.setObjectName(_fromUtf8("established_mirrors_tree"))
        self.established_mirrors_count = QtGui.QLabel(FileMirrorsList)
        self.established_mirrors_count.setGeometry(QtCore.QRect(160, 50, 301, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.established_mirrors_count.setFont(font)
        self.established_mirrors_count.setObjectName(_fromUtf8("established_mirrors_count"))
        self.available_mirrors_count = QtGui.QLabel(FileMirrorsList)
        self.available_mirrors_count.setGeometry(QtCore.QRect(820, 50, 241, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.available_mirrors_count.setFont(font)
        self.available_mirrors_count.setObjectName(_fromUtf8("available_mirrors_count"))
        self.mirror_details_bt = QtGui.QPushButton(FileMirrorsList)
        self.mirror_details_bt.setGeometry(QtCore.QRect(190, 450, 271, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mirror_details_bt.setFont(font)
        self.mirror_details_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2683ff;\n"
"    border: 1px solid #2683ff;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #2274e2;\n"
"  border-color: #2274e2;\n"
"}\n"
"QPushButton:active{\n"
"  background-color: #4393ff;\n"
"  border-color: #4393ff;\n"
"}"))
        self.mirror_details_bt.setObjectName(_fromUtf8("mirror_details_bt"))
        self.mirror_details_bt_2 = QtGui.QPushButton(FileMirrorsList)
        self.mirror_details_bt_2.setGeometry(QtCore.QRect(790, 450, 291, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.mirror_details_bt_2.setFont(font)
        self.mirror_details_bt_2.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #2683ff;\n"
"    border: 1px solid #2683ff;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"  background-color: #2274e2;\n"
"  border-color: #2274e2;\n"
"}\n"
"QPushButton:active{\n"
"  background-color: #4393ff;\n"
"  border-color: #4393ff;\n"
"}"))
        self.mirror_details_bt_2.setObjectName(_fromUtf8("mirror_details_bt_2"))
        self.quit_bt = QtGui.QPushButton(FileMirrorsList)
        self.quit_bt.setGeometry(QtCore.QRect(10, 450, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.quit_bt.setFont(font)
        self.quit_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.quit_bt.setObjectName(_fromUtf8("quit_bt"))

        self.retranslateUi(FileMirrorsList)
        QtCore.QMetaObject.connectSlotsByName(FileMirrorsList)
        FileMirrorsList.setTabOrder(self.established_mirrors_tree, self.available_mirrors_tree)
        FileMirrorsList.setTabOrder(self.available_mirrors_tree, self.quit_bt)
        FileMirrorsList.setTabOrder(self.quit_bt, self.mirror_details_bt)
        FileMirrorsList.setTabOrder(self.mirror_details_bt, self.mirror_details_bt_2)

    def retranslateUi(self, FileMirrorsList):
        FileMirrorsList.setWindowTitle(_translate("FileMirrorsList", "File mirrors list - Storj GUI", None))
        self.label_6.setText(_translate("FileMirrorsList", "<html><head/><body><p><span style=\" color:#555555;\">FILE NAME:</span></p></body></html>", None))
        self.file_name.setText(_translate("FileMirrorsList", "<html><head/><body><p><span style=\" color:#2683ff;\">N/A</span></p></body></html>", None))
        self.label_11.setText(_translate("FileMirrorsList", "<html><head/><body><p><span style=\" color:#555555;\">FILE ID:</span></p></body></html>", None))
        self.file_id.setText(_translate("FileMirrorsList", "<html><head/><body><p><span style=\" color:#2683ff;\">2000.00MB</span></p></body></html>", None))
        self.established_mirrors_count.setText(_translate("FileMirrorsList", "<html><head/><body><p align=\"center\"><span style=\" color:#555555;\">ESTABLISHED (XXXX)</span></p></body></html>", None))
        self.available_mirrors_count.setText(_translate("FileMirrorsList", "<html><head/><body><p align=\"center\"><span style=\" color:#555555;\">AVAILABLE (XXXX)</span></p></body></html>", None))
        self.mirror_details_bt.setText(_translate("FileMirrorsList", "MORE MIRROR DETAILS", None))
        self.mirror_details_bt_2.setText(_translate("FileMirrorsList", "MORE MIRROR DETAILS", None))
        self.quit_bt.setText(_translate("FileMirrorsList", "CLOSE", None))

