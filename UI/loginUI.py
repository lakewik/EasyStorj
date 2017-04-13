import json
import storj
from PyQt4 import QtCore, QtGui
from mainUI import MainUI
from qt_interfaces.storj_login_ui import Ui_Login
from utilities.account_manager import AccountManager


# Login section
class LoginUI(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # login UI
        self.login_ui = Ui_Login()
        self.login_ui.setupUi(self)

        # Account manager

        self.login_ui.password.setEchoMode(QtGui.QLineEdit.Password)

        QtCore.QObject.connect(self.login_ui.login_bt, QtCore.SIGNAL("clicked()"), self.login)  # take login action

    def login(self):
        # take login action

        self.email = self.login_ui.email.text()  # get login
        self.password = self.login_ui.password.text()  # get password

        self.storj_client = storj.Client(email=str(self.email), password=str(self.password))
        success = False
        # take login action - check credentials by listing keys :D
        try:
            self.storj_client.key_list()
            success = True
        except storj.exception.StorjBridgeApiError as e:
            j = json.loads(str(e))
            if (j["error"] == "Invalid email or password"):
                QMessageBox.about(self, "Warning",
                                  "Invalid email or password - access denied. Please check your credentials and try again!")
            else:
                QMessageBox.about(self, "Unhandled exception", "Exception: " + str(e))

        if success:
            self.account_manager = AccountManager(str(self.email), str(self.password))  # init account manager
            self.account_manager.save_account_credentials()  # save login credentials and state
            # login_msg_box = QMessageBox.about(self, "Success", "Successfully loged in!")
            msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information, "Success", "Successfully loged in!",
                                       QtGui.QMessageBox.Ok)
            result = msgBox.exec_()
            if result == QtGui.QMessageBox.Ok:
                self.main_ui_window = MainUI(self)
                self.main_ui_window.show()
                self.close()
                initial_window.hide()

                # self.account_manager.get_login_state()

        # print self.storj_client.bucket_list()
        print 1
