# -*- coding: utf-8 -*-
#import base64
#import hashlib
#import hmac
#import json
from PyQt4 import Qt

import magic
import os
import operator
import socket
import sys
import threading
import time
from PyQt4 import QtCore, QtGui

#import pycountry
import requests
import storj
from PyQt4.QtCore import QAbstractTableModel, SIGNAL
from PyQt4.QtCore import QVariant
from PyQt4.QtGui import *
#from ipwhois import IPWhois
from storj import exception
from storj import model

#from bucket_manage_ui import Ui_BucketManager
#from client_configuration_ui import Ui_ClientConfiguration
#from create_bucket_ui import Ui_BucketCreate
#from file_crypto_tools import FileCrypto  # file ancryption and decryption lib
#from file_manager_ui import Ui_FileManager
#from file_mirrors_list_ui import Ui_FileMirrorsList
#from initial_window_ui import Ui_InitialWindow
#from main_menu_ui import Ui_MainMenu
#from node_details_ui import Ui_NodeDetails
#from single_file_downloader_ui import Ui_SingleFileDownload
#from single_file_upload_ui import Ui_SingleFileUpload
#from storj_login_ui import Ui_Login
#from storj_register_ui import Ui_Register
from sharder import ShardingTools
from tools import Tools
#from backend_config import Configuration
from account_manager import AccountManager

# UI
#from UI.login import LoginUI
#from UI.registration import RegisterUI
from UI.mainUI import MainUI
from UI.initial_window import InitialWindowUI

# CONSIDER A BETTER PLACE WHERE TO MOVE THIS
from UI.engine import StorjEngine

# ext libs

# Define CONSTANS


global SHARD_MULTIPLES_BACK, MAX_SHARD_SIZE

MAX_SHARD_SIZE = 4294967296  # 4Gb
SHARD_MULTIPLES_BACK = 4

global html_format_begin, html_format_end
html_format_begin = "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"
html_format_end = "</span></p></body></html>"



class ProgressBar(QProgressBar):

    def __init__(self, value, parent=None):
        QProgressBar.__init__(self)
        self.setMinimum(1)
        self.setMaximum(100)
        self.setValue(value)
        self.setFormat('{0:.5f}'.format(value))
        #style = ''' QProgressBar{max-height: 15px;text-align: center;}'''
        #self.setStyleSheet(style)

class ProgressWidgetItem(QTableWidgetItem):

    def __lt__(self, other):
        return self.data(Qt.UserRole) < other.data(Qt.UserRole)

    def updateValue(self, value):
        self.setData(Qt.UserRole, value)


class MyTableModel(QtCore.QAbstractTableModel):
    def __init__(self,data,parent=None):
        QtCore.QAbstractTableModel.__init__(self,parent)
        self.__data=data     # Initial Data

    def rowCount( self, parent ):
        return len(self.__data)

    def columnCount( self , parent ):
        return len(self.__data)

    def data ( self , index , role ):
        if role == QtCore.Qt.DisplayRole:
            row = index.row()
            column = index.column()
            value = self.__data[row][column]
            return QtCore.QString(str(value))

    def setData(self, index, value):
        self.__data[index.row()][index.column()] = value
        return True

    def flags(self, index):
        return QtCore.Qt.ItemIsEnabled|QtCore.Qt.ItemIsEditable|QtCore.Qt.ItemIsSelectable

    def insertRows(self , position , rows , item , parent=QtCore.QModelIndex()):
        # beginInsertRows (self, QModelIndex parent, int first, int last)
        self.beginInsertRows(QtCore.QModelIndex(),len(self.__data),len(self.__data)+1)
        self.__data.append(item) # Item must be an array
        self.endInsertRows()
        return True


class StorjSDKImplementationsOverrides():
    def __init__(self, parent=None):
        self.storj_engine = StorjEngine()  # init StorjEngine














if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_X11InitThreads)
    app = QtGui.QApplication(sys.argv)

    myapp = MainUI()
    initial_window = InitialWindowUI()

    account_manager = AccountManager()
    if account_manager.if_logged_in():
        myapp.show()
    else:
        initial_window.show()

    sys.exit(app.exec_())
