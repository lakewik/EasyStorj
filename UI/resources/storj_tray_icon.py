import sys
from PyQt4 import QtGui

class StorjTrayIcon(QtGui.QSystemTrayIcon):

    def __init__(self, icon, parent=None):
        QtGui.QSystemTrayIcon.__init__(self, icon, parent)
        menu = QtGui.QMenu(parent)

    def update_tray_sync_stats(self):
        return True


