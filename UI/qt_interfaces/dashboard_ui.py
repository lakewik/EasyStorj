# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'dashboard_new.ui'
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
        MainMenu.resize(780, 429)
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
        MainMenu.setPalette(palette)
        MainMenu.setAutoFillBackground(False)
        MainMenu.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.file_download_bt = QtGui.QPushButton(MainMenu)
        self.file_download_bt.setGeometry(QtCore.QRect(510, 390, 261, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.file_download_bt.setFont(font)
        self.file_download_bt.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
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
        self.file_download_bt.setObjectName(_fromUtf8("file_download_bt"))
        self.label_3 = QtGui.QLabel(MainMenu)
        self.label_3.setGeometry(QtCore.QRect(170, 10, 171, 71))
        self.label_3.setText(_fromUtf8(""))
        self.label_3.setPixmap(QtGui.QPixmap(_fromUtf8(":/resources/storj-logo-horizontal.png")))
        self.label_3.setScaledContents(True)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.file_delete_bt = QtGui.QPushButton(MainMenu)
        self.file_delete_bt.setGeometry(QtCore.QRect(10, 390, 41, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.file_delete_bt.setFont(font)
        self.file_delete_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #fa6e50;\n"
"    border: 1px solid #fa6e50;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #fa6e50;\n"
"    border-color: #fa6e50;\n"
"}\n"
"QPushButton:active {\n"
"    background-color: #fa6e50;\n"
"    border-color: #fa6e50\n"
"}"))
        self.file_delete_bt.setObjectName(_fromUtf8("file_delete_bt"))
        self.label_4 = QtGui.QLabel(MainMenu)
        self.label_4.setGeometry(QtCore.QRect(430, 20, 141, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.files_list_tableview = QtGui.QTableView(MainMenu)
        self.files_list_tableview.setGeometry(QtCore.QRect(15, 135, 751, 241))
        self.files_list_tableview.setObjectName(_fromUtf8("files_list_tableview"))
        self.bucket_select_combo_box = QtGui.QComboBox(MainMenu)
        self.bucket_select_combo_box.setGeometry(QtCore.QRect(95, 90, 501, 31))
        self.bucket_select_combo_box.setStyleSheet(_fromUtf8(""))
        self.bucket_select_combo_box.setObjectName(_fromUtf8("bucket_select_combo_box"))
        self.create_bucket_bt = QtGui.QPushButton(MainMenu)
        self.create_bucket_bt.setGeometry(QtCore.QRect(610, 90, 31, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.create_bucket_bt.setFont(font)
        self.create_bucket_bt.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
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
        self.create_bucket_bt.setObjectName(_fromUtf8("create_bucket_bt"))
        self.edit_bucket_bt = QtGui.QPushButton(MainMenu)
        self.edit_bucket_bt.setGeometry(QtCore.QRect(690, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.edit_bucket_bt.setFont(font)
        self.edit_bucket_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.edit_bucket_bt.setObjectName(_fromUtf8("edit_bucket_bt"))
        self.account_label = QtGui.QLabel(MainMenu)
        self.account_label.setGeometry(QtCore.QRect(450, 40, 321, 41))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.account_label.setFont(font)
        self.account_label.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.account_label.setObjectName(_fromUtf8("account_label"))
        self.file_mirrors_bt = QtGui.QPushButton(MainMenu)
        self.file_mirrors_bt.setGeometry(QtCore.QRect(350, 390, 151, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.file_mirrors_bt.setFont(font)
        self.file_mirrors_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
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
        self.file_mirrors_bt.setObjectName(_fromUtf8("file_mirrors_bt"))
        self.new_file_upload_bt = QtGui.QPushButton(MainMenu)
        self.new_file_upload_bt.setGeometry(QtCore.QRect(60, 390, 281, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.new_file_upload_bt.setFont(font)
        self.new_file_upload_bt.setStyleSheet(_fromUtf8("QPushButton:hover{\n"
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
        self.new_file_upload_bt.setObjectName(_fromUtf8("new_file_upload_bt"))
        self.settings_bt = QtGui.QLabel(MainMenu)
        self.settings_bt.setGeometry(QtCore.QRect(740, 10, 31, 31))
        self.settings_bt.setText(_fromUtf8(""))
        self.settings_bt.setPixmap(QtGui.QPixmap(_fromUtf8(":/resources/cog-outline-filled.png")))
        self.settings_bt.setScaledContents(True)
        self.settings_bt.setObjectName(_fromUtf8("settings_bt"))
        self.refresh_bt = QtGui.QLabel(MainMenu)
        self.refresh_bt.setGeometry(QtCore.QRect(650, 90, 31, 31))
        self.refresh_bt.setText(_fromUtf8(""))
        self.refresh_bt.setPixmap(QtGui.QPixmap(_fromUtf8(":/resources/refresh.png")))
        self.refresh_bt.setScaledContents(True)
        self.refresh_bt.setObjectName(_fromUtf8("refresh_bt"))
        self.label_5 = QtGui.QLabel(MainMenu)
        self.label_5.setGeometry(QtCore.QRect(10, 90, 81, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.crypto_keys_manager_bt = QtGui.QLabel(MainMenu)
        self.crypto_keys_manager_bt.setGeometry(QtCore.QRect(700, 10, 31, 31))
        self.crypto_keys_manager_bt.setText(_fromUtf8(""))
        self.crypto_keys_manager_bt.setPixmap(QtGui.QPixmap(_fromUtf8(":/resources/keys.png")))
        self.crypto_keys_manager_bt.setScaledContents(True)
        self.crypto_keys_manager_bt.setObjectName(_fromUtf8("crypto_keys_manager_bt"))
        self.sync_menu_bt = QtGui.QLabel(MainMenu)
        self.sync_menu_bt.setGeometry(QtCore.QRect(660, 10, 31, 31))
        self.sync_menu_bt.setText(_fromUtf8(""))
        self.sync_menu_bt.setPixmap(QtGui.QPixmap(_fromUtf8(":/resources/refresh.png")))
        self.sync_menu_bt.setScaledContents(True)
        self.sync_menu_bt.setObjectName(_fromUtf8("sync_menu_bt"))
        self.account_dash_bt = QtGui.QLabel(MainMenu)
        self.account_dash_bt.setGeometry(QtCore.QRect(620, 10, 31, 31))
        self.account_dash_bt.setText(_fromUtf8(""))
        self.account_dash_bt.setPixmap(QtGui.QPixmap(_fromUtf8(":/resources/account.png")))
        self.account_dash_bt.setScaledContents(True)
        self.account_dash_bt.setObjectName(_fromUtf8("account_dash_bt"))

        self.retranslateUi(MainMenu)
        QtCore.QMetaObject.connectSlotsByName(MainMenu)
        MainMenu.setTabOrder(self.bucket_select_combo_box, self.create_bucket_bt)
        MainMenu.setTabOrder(self.create_bucket_bt, self.edit_bucket_bt)
        MainMenu.setTabOrder(self.edit_bucket_bt, self.files_list_tableview)
        MainMenu.setTabOrder(self.files_list_tableview, self.new_file_upload_bt)
        MainMenu.setTabOrder(self.new_file_upload_bt, self.file_delete_bt)
        MainMenu.setTabOrder(self.file_delete_bt, self.file_mirrors_bt)
        MainMenu.setTabOrder(self.file_mirrors_bt, self.file_download_bt)

    def retranslateUi(self, MainMenu):
        MainMenu.setWindowTitle(_translate("MainMenu", "Storj GUI", None))
        self.file_download_bt.setText(_translate("MainMenu", "DOWNLOAD", None))
        self.file_delete_bt.setText(_translate("MainMenu", "X", None))
        self.label_4.setText(_translate("MainMenu", "<html><head/><body><p align=\"center\"><span style=\" color:#555555;\">LOGGED AS:</span></p></body></html>", None))
        self.create_bucket_bt.setText(_translate("MainMenu", "+", None))
        self.edit_bucket_bt.setText(_translate("MainMenu", "EDIT", None))
        self.account_label.setText(_translate("MainMenu", "<html><head/><body><p><span style=\" color:#2683ff;\">JOHN.SMITH.STORJ.80@GMAIL.COM</span></p></body></html>", None))
        self.file_mirrors_bt.setText(_translate("MainMenu", "MIRRORS", None))
        self.new_file_upload_bt.setText(_translate("MainMenu", "UPLOAD", None))
        self.label_5.setText(_translate("MainMenu", "<html><head/><body><p align=\"center\"><span style=\" color:#555555;\">BUCKET:</span></p></body></html>", None))

import resources_rc
