from PyQt4 import QtCore, QtGui
import storj
from qt_interfaces.main_menu_ui import Ui_MainMenu
from utilities.account_manager import AccountManager
from engine import StorjEngine

from bucket_create import BucketCreateUI
from bucket_manager import BucketManagerUI
from client_config import ClientConfigurationUI
from file_manager import FileManagerUI
from file_mirror import FileMirrorsListUI
from file_upload import SingleFileUploadUI
from registration import RegisterUI


global html_format_begin, html_format_end
html_format_begin = "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"
html_format_end = "</span></p></body></html>"


# Main UI section
class MainUI(QtGui.QMainWindow):

    def __init__(self, parent=None):
        EXIT_CODE_REBOOT = -123
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        # QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.save_config) # open bucket manager
        self.storj_engine = StorjEngine()  # init StorjEngine
        # self.storj_engine.storj_client.
        # self.sharding_tools = ShardingTools()

        # print self.sharding_tools.get_optimal_shard_parametrs(18888888888)
        # print self.sharding_tools.determine_shard_size(12343446576, 10)
        self.account_manager = AccountManager()  # init AccountManager

        user_email = self.account_manager.get_user_email()
        self.ui.account_label.setText(html_format_begin + str(user_email) + html_format_end)

        # QtCore.QObject.connect(self.ui., QtCore.SIGNAL("clicked()"), self.open_login_window) # open login window
        # QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL("clicked()"), self.open_register_window) # open login window
        QtCore.QObject.connect(self.ui.bucket_menager_bt, QtCore.SIGNAL("clicked()"),
                               self.open_bucket_manager_window)  # open bucket manager window
        QtCore.QObject.connect(self.ui.file_manager_bt, QtCore.SIGNAL("clicked()"),
                               self.open_file_manager_window)  # open file manager window
        QtCore.QObject.connect(self.ui.create_bucket_bt, QtCore.SIGNAL("clicked()"),
                               self.open_bucket_create_window)  # open bucket create window
        QtCore.QObject.connect(self.ui.uploader_bt, QtCore.SIGNAL("clicked()"),
                               self.open_single_file_upload_window)  # open single file upload ui
        QtCore.QObject.connect(self.ui.settings_bt, QtCore.SIGNAL("clicked()"),
                               self.open_settings_window)  # open single file upload ui
        # QtCore.QObject.connect(self.ui.pushButton_7, QtCore.SIGNAL("clicked()"), self.open_file_mirrors_list_window) # open file mirrors list window

    def open_login_window(self):
        self.login_window = LoginUI(self)
        self.login_window.show()

        self.login_window = ClientConfigurationUI(self)
        self.login_window.show()

        # take login action
        print 1

    def open_register_window(self):
        self.register_window = RegisterUI(self)
        self.register_window.show()

    def open_single_file_upload_window(self):
        self.single_file_upload_window = SingleFileUploadUI(self)
        self.single_file_upload_window.show()

    def open_bucket_manager_window(self):
        self.bucket_manager_window = BucketManagerUI(self)
        self.bucket_manager_window.show()

    def open_file_manager_window(self):
        self.file_manager_window = FileManagerUI(self)
        self.file_manager_window.show()

    def open_bucket_create_window(self):
        self.bucket_create_window = BucketCreateUI(self)
        self.bucket_create_window.show()

    def open_file_mirrors_list_window(self):
        self.file_mirrors_list_window = FileMirrorsListUI(self)
        self.file_mirrors_list_window.show()

    def open_settings_window(self):
        self.settings_window = ClientConfigurationUI(self)
        self.settings_window.show()
