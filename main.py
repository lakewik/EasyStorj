# -*- coding: utf-8 -*-



import sys, collections, threading, os
#sys.path.append("/home/lakewik/PycharmProjects/storjguibeta/4/storj_gui_client")
print(os.path.dirname(os.path.realpath(__file__)))
import requests.packages.urllib3.packages.ordered_dict
from PyQt4 import QtCore, QtGui
from UI.utilities.account_manager import AccountManager
from UI.mainUI import MainUI
from UI.initial_window import InitialWindowUI
import configparser # needed for Windows package builder
from UI.resources.storj_tray_icon import StorjTrayIcon
from UI.resources.constants import SHOW_TRAY_ICON
from UI.resources.sync_constants import SYNC_ENABLED
from UI.utilities.synchronization_core import SyncObserverWorker
from UI.utilities.backend_config import Configuration
#from UI.utilities.storj_synchronization_daemon import StorjSynchronizationDaemon
from UI.utilities.storj_synchronization_background_server import start_storj_sync_server_thread
from UI.utilities.tools import Tools
from UI.resources.constants import RUN_IN_BACKGROUND_AFTER_CLOSE
from UI.enter_mnemonic import EnterMnemonicUI
from UI.generated_mnemonic import MnemonicGeneratedUI
#from UI.flask_ownstorj.runserver import OwnStorjFlaskServer



if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_X11InitThreads)
    app = QtGui.QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False) # app can run in background

    tools = Tools()

    locale = QtCore.QLocale.system().name()
    qtTranslator = QtCore.QTranslator()
    # try to load translation

    if qtTranslator.load("" + locale, ":tra/"):
        app.installTranslator(qtTranslator)

    account_manager = AccountManager()
    if account_manager.if_logged_in():
        #own_storj_init = OwnStorjFlaskServer()
        #own_storj_init.run()
        #myapp = MainUI()
        myapp = EnterMnemonicUI()
        #myapp = MnemonicGeneratedUI()
        #start_storj_sync_server_thread()

        def restore_from_tray(reason):
            if reason == QtGui.QSystemTrayIcon.DoubleClick:  # show main window when user double-clicked tray
                #myapp.destroy(True, True)
                main = MainUI()
                main.show()

        #if SYNC_ENABLED:
            #tools.start_synchronization_observer()


        if SHOW_TRAY_ICON:
            style = app.style()
            icon = QtGui.QIcon(style.standardPixmap(QtGui.QStyle.SP_FileIcon))
            trayIcon = StorjTrayIcon(icon)

            menu = QtGui.QMenu()
            exitAction = menu.addAction("Exit")
            sync_menu_action = menu.addAction("Show synchronization menu")

            trayIcon.setContextMenu(menu)

            trayIcon.setToolTip("test")

            trayIcon.show()

            QtCore.QObject.connect(exitAction, QtCore.SIGNAL('triggered()'), lambda: myapp.close())

            trayIcon.activated.connect(restore_from_tray)


        myapp.show()
    else:
        initial_window = InitialWindowUI()
        initial_window.show()
        # Apply default configuration
        configuration = Configuration()
        configuration.create_genesis_configuration()


    sys.exit(app.exec_())
