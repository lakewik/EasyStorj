import storj
from PyQt4 import QtCore, QtGui
from qt_interfaces.storj_register_ui import Ui_Register
from login import LoginUI
from utilities.tools import Tools


# Register section
class RegisterUI(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # register UI
        self.register_ui = Ui_Register()
        self.register_ui.setupUi(self)

        self.register_ui.password.setEchoMode(QtGui.QLineEdit.Password)
        self.register_ui.password_2.setEchoMode(QtGui.QLineEdit.Password)

        QtCore.QObject.connect(self.register_ui.register_bt, QtCore.SIGNAL("clicked()"),
                               self.register)  # valudate and register user

    def register(self):
        # validate fields
        self.email = self.register_ui.email.text()
        self.password = self.register_ui.password.text()
        self.password_repeat = self.register_ui.password_2.text()

        self.tools = Tools()
        success = False
        if self.email != "" and self.password != "" and self.password_repeat != "":
            if self.password == self.password_repeat:
                if (self.tools.check_email(self.email)):
                    # take login action
                    try:
                        self.storj_client = storj.Client(str(self.email), str(self.password))
                        print self.email
                        success = True
                        # self.storj_client.user_create("wiktest15@gmail.com", "kotek1")
                    except storj.exception.StorjBridgeApiError as e:
                        j = json.loads(str(e))
                        if (j["error"] == "Email is already registered"):
                            success = False
                            QMessageBox.about(self, "Warning",
                                              "User with this e-mail is already registered! Please login or try different e-mail!")
                        else:
                            success = False
                            QMessageBox.about(self, "Unhandled exception", "Exception: " + str(e))
                else:
                    success = False
                    QMessageBox.about(self, "Warning",
                                      "Your e-mail seems to be invalid! Please chech e-mail  and try again")
            else:
                success = False
                QMessageBox.about(self, "Warning",
                                  "Given passwords are different! Please check and try again!")
        else:
            success = False
            QMessageBox.about(self, "Warning",
                              "Please fill out all fields!")

        if success:
            msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information, "Success",
                                       "Successfully registered in Storj Distributed Storage Network! "
                                       "Now, yo must verify your email by clicking link, that been send to you. "
                                       "Then you can login", QtGui.QMessageBox.Ok)
            result = msgBox.exec_()
            if result == QtGui.QMessageBox.Ok:
                self.login_window = LoginUI(self)
                self.login_window.show()
                self.close()
                #initial_window.hide()

        print self.email
