from PyQt4 import QtCore, QtGui
from qt_interfaces.main_menu_ui import Ui_MainMenu
from utilities.account_manager import AccountManager
from engine import StorjEngine

from bucket_create import BucketCreateUI
from bucket_manager import BucketManagerUI
from client_config import ClientConfigurationUI
from file_manager import FileManagerUI
from file_mirror import FileMirrorsListUI
from file_upload import SingleFileUploadUI
# from login import LoginUI
# from registration import RegisterUI
from resources.html_strings import html_format_begin, html_format_end
from utilities.log_manager import logger


# Main UI section
class MainUI(QtGui.QMainWindow):

    def __init__(self, parent=None):
        # EXIT_CODE_REBOOT = -123
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        # QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.save_config) # open bucket manager
        self.storj_engine = StorjEngine()  # init StorjEngine

        self.account_manager = AccountManager()  # init AccountManager

        user_email = self.account_manager.get_user_email()
        self.ui.account_label.setText(html_format_begin +
                                      str(user_email).strip() +
                                      html_format_end)

        # BUTTONS:
        # QtCore.QObject.connect(self.ui., QtCore.SIGNAL("clicked()"), self.open_login_window) # open login window
        # QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL("clicked()"), self.open_register_window) # open login window
        QtCore.QObject.connect(self.ui.create_bucket_bt, QtCore.SIGNAL("clicked()"),
                               self.open_bucket_create_window)  # open bucket create window
        QtCore.QObject.connect(self.ui.bucket_manager_bt, QtCore.SIGNAL("clicked()"),
                               self.open_bucket_manager_window)  # open bucket manager window
        QtCore.QObject.connect(self.ui.settings_bt, QtCore.SIGNAL("clicked()"),
                               self.open_settings_window)  # open settings ui
        QtCore.QObject.connect(self.ui.file_manager_bt, QtCore.SIGNAL("clicked()"),
                               self.open_file_manager_window)  # open file manager window
        QtCore.QObject.connect(self.ui.uploader_bt, QtCore.SIGNAL("clicked()"),
                               self.open_single_file_upload_window)  # open single file upload ui
        QtCore.QObject.connect(self.ui.downloader_bt, QtCore.SIGNAL("clicked()"),
                               self.open_file_mirrors_list_window)  # open single file download ui

    """
    def open_login_window(self):
        self.login_window = LoginUI(self)
        self.login_window.show()

        self.login_window = ClientConfigurationUI(self)
        self.login_window.show()

        # take login action
        print 1
    """

    """
    def open_register_window(self):
        self.register_window = RegisterUI(self)
        self.register_window.show()
    """

    def open_bucket_create_window(self):
        """Create a new bucket"""
        logger.debug("Create a new bucket")
        self.bucket_create_window = BucketCreateUI(self)
        self.bucket_create_window.show()

    def open_bucket_manager_window(self):
        """Bucket manager"""
        logger.debug("Bucket manager")
        self.bucket_manager_window = BucketManagerUI(self)
        self.bucket_manager_window.show()

    def open_file_manager_window(self):
        """File manager"""
        logger.debug("File manager")
        self.file_manager_window = FileManagerUI(self)
        self.file_manager_window.show()

    def open_file_mirrors_list_window(self):
        """File download"""
        logger.debug("Download file")
        self.file_mirrors_list_window = FileMirrorsListUI(self)
        self.file_mirrors_list_window.show()

    def open_single_file_upload_window(self):
        """File upload"""
        logger.debug("Upload file")
        self.single_file_upload_window = SingleFileUploadUI(self)
        self.single_file_upload_window.show()

    def open_settings_window(self):
        """Settings"""
        logger.debug("Open settings")
        self.settings_window = ClientConfigurationUI(self)
        self.settings_window.show()
