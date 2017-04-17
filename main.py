# -*- coding: utf-8 -*-

import sys
from PyQt4 import QtCore, QtGui
from UI.utilities.account_manager import AccountManager
from UI.mainUI import MainUI
from UI.initial_window import InitialWindowUI


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_X11InitThreads)
    app = QtGui.QApplication(sys.argv)

    locale = QtCore.QLocale.system().name()
    qtTranslator = QtCore.QTranslator()
    # try to load translation
    if qtTranslator.load("" + locale, ":tra/"):
        app.installTranslator(qtTranslator)

    account_manager = AccountManager()
    if account_manager.if_logged_in():
        myapp = MainUI()
        myapp.show()
    else:
        initial_window = InitialWindowUI()
        initial_window.show()

    sys.exit(app.exec_())
