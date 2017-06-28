# -*- coding: utf-8 -*-

from PyQt4 import QtCore, QtGui
from qt_interfaces.crypto_keys_manager_ui import Ui_KeyManager


# Synchronization menu section #
class CryptoKeysManagerUI(QtGui.QMainWindow):

    def __init__(self, parent=None,):
        QtGui.QWidget.__init__(self, parent)
        self.crypto_key_manager_ui = Ui_KeyManager()
        self.crypto_key_manager_ui.setupUi(self)
