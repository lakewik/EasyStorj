from PyQt4 import QtCore, QtGui
from qt_interfaces.initial_window_ui_new import Ui_InitialWindow
from login import LoginUI
from registration import RegisterUI
from engine import StorjEngine


# Initial window section
class InitialWindowUI(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui_initial_window = Ui_InitialWindow()
        self.ui_initial_window.setupUi(self)
        # QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.save_config) # open bucket manager
        self.storj_engine = StorjEngine()  # init StorjEngine

        QtCore.QObject.connect(self.ui_initial_window.login_bt, QtCore.SIGNAL("clicked()"),
                               self.open_login_window)  # open login window
        QtCore.QObject.connect(self.ui_initial_window.register_bt, QtCore.SIGNAL("clicked()"),
                               self.open_register_window)  # open login window
        # QtCore.QObject.connect(self.ui_initial_window.about_bt, QtCore.SIGNAL("clicked()"), self.open_about_window) # open login window

    def open_login_window(self):
        self.login_window = LoginUI(self)
        self.login_window.show()
        # initial_window.hide()

    def open_register_window(self):
        self.register_window = RegisterUI(self)
        self.register_window.show()
