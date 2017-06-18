# -*- coding: utf-8 -*-

import logging
import threading

from .engine import StorjEngine
from PyQt4 import QtCore, QtGui
from .qt_interfaces.create_bucket_ui import Ui_BucketCreate

import storj.exception as sjexc


class BucketCreateUI(QtGui.QMainWindow):

    __logger = logging.getLogger('%s.BucketCreateUI' % __name__)

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.bucket_create_ui = Ui_BucketCreate()
        self.bucket_create_ui.setupUi(self)

        # Create bucket action
        QtCore.QObject.connect(self.bucket_create_ui.create_bucket_bt,
                               QtCore.SIGNAL('clicked()'),
                               self.createNewBucketCreateThread)
        # Delete bucket action
        QtCore.QObject.connect(self.bucket_create_ui.cancel_bt,
                               QtCore.SIGNAL('clicked()'),
                               self.close)

        self.connect(self, QtCore.SIGNAL('showBucketCreatingException'),
                     self.show_bucket_creating_exception_dialog)
        self.connect(self, QtCore.SIGNAL('showBucketCreatedSuccessfully'),
                     self.show_bucket_crated_successfully)
        self.connect(self,
                     QtCore.SIGNAL('showBucketCreationMissingFields'),
                     lambda: QtGui.QMessageBox.about(
                         self,
                         'Warning',
                         'Please fill out all fields!'))

        self.storj_engine = StorjEngine()  # init StorjEngine

    def show_bucket_creating_exception_dialog(self, exception):
        QtGui.QMessageBox.about(
            self,
            'Unhandled exception while creating bucket',
            'Exception: %s' % str(exception))

    def show_bucket_crated_successfully(self, bucket_name):
        msgBox = QtGui.QMessageBox(
            QtGui.QMessageBox.Information,
            'Success',
            'Bucket \'%s\' was created successfully!' % bucket_name,
            QtGui.QMessageBox.Ok)
        msgBox.exec_()

    def createNewBucketCreateThread(self):
        bucket_create_thread = threading.Thread(target=self.create_bucket,
                                                args=())
        bucket_create_thread.start()

    def create_bucket(self):
        self.bucket_name = str(self.bucket_create_ui.bucket_name.text())
        self.bucket_storage = self.bucket_create_ui.bucket_storage_size.text()
        self.bucket_transfer = self.bucket_create_ui.bucket_transfer.text()

        bucket_created = False  # init boolean
        if self.bucket_name != '' and \
                self.bucket_transfer != '' and \
                self.bucket_storage != '':

            try:
                self.storj_engine.storj_client.bucket_create(
                    self.bucket_name,
                    int(self.bucket_storage),
                    int(self.bucket_transfer))
                bucket_created = True
            except sjexc.StorjBridgeApiError as e:
                self.__logger.error('Bucket not created')
                self.__logger.error(e)
                bucket_created = False
                self.emit(QtCore.SIGNAL('showBucketCreatingException'), str(e))

        else:
            self.emit(QtCore.SIGNAL('showBucketCreationMissingFields'))
            self.__logger.warning('Bucket not created')
            bucket_created = False

        if bucket_created:
            self.__logger.info('Bucket created')
            self.emit(
                QtCore.SIGNAL('showBucketCreatedSuccessfully'),
                self.bucket_name)  # Show dialog - Bucket created successfully
            self.close()
