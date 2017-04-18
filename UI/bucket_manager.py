from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QStandardItem, QStandardItemModel
from qt_interfaces.bucket_manager_ui import Ui_BucketManager
from engine import StorjEngine
import storj.exception as sjexc
import threading


# Buckets section
class BucketManagerUI(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.bucket_manager_ui = Ui_BucketManager()
        self.bucket_manager_ui.setupUi(self)
        self.createNewBucketGetThread()

        QtCore.QObject.connect(self.bucket_manager_ui.quit_bt, QtCore.SIGNAL("clicked()"),
                               self.quit)  # open login window
        QtCore.QObject.connect(self.bucket_manager_ui.delete_bucket_bt, QtCore.SIGNAL("clicked()"),
                               self.delete_bucket)  # delete bucket
        QtCore.QObject.connect(self.bucket_manager_ui.edit_bucket_bt, QtCore.SIGNAL("clicked()"),
                               self.open_bucket_edit_window)  # open bucket edit window
        # QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL("clicked()"), self.open_register_window) # open login window

    def createNewBucketGetThread(self):
        download_thread = threading.Thread(target=self.initialize_buckets_table, args=())
        download_thread.start()

    def quit(self):
        self.close()

    def delete_bucket(self):
        # initialize variables
        bucket_id = ""
        bucket_name = ""

        tablemodel = self.bucket_manager_ui.bucket_list_tableview.model()
        rows = sorted(set(index.row() for index in self.bucket_manager_ui.bucket_list_tableview.selectedIndexes()))
        i = 0
        for row in rows:
            index = tablemodel.index(row, 3)  # get bucket ID
            index2 = tablemodel.index(row, 2)  # get bucket name
            # We suppose data are strings
            bucket_id = str(tablemodel.data(index).toString())
            bucket_name = str(tablemodel.data(index2).toString())
            i = i + 1
            break

        if i != 0:
            msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Question, "Are you sure?",
                                       "Are you sure to delete this bucket? Bucket name: '" + bucket_name + "'",
                                       (QtGui.QMessageBox.Yes | QtGui.QMessageBox.No))
            result = msgBox.exec_()
            if result == QtGui.QMessageBox.Ok:
                success = False
                try:
                    self.storj_engine.storj_client.bucket_delete(str(bucket_id))
                    success = True
                except sjexc.StorjBridgeApiError as e:
                    QtGui.QMessageBox.about(self, "Unhandled exception deleting bucket", "Exception: " + str(e))
                    success = False

                if success:
                    QtGui.QMessageBox.about(self, "Success", "Bucket was deleted successfully!")
        else:
            QtGui.QMessageBox.about(self, "Warning", "Please select bucket which you want to delete.")

    def open_bucket_edit_window(self):
        print 1

    def initialize_buckets_table(self):
        self.storj_engine = StorjEngine()  # init StorjEngine
        print "resolving buckets"
        model = QStandardItemModel(1, 1)  # initialize model for inserting to table

        model.setHorizontalHeaderLabels(['Name', 'Storage', 'Transfer', 'ID'])

        i = 0
        try:
            for bucket in self.storj_engine.storj_client.bucket_list():
                item = QStandardItem(bucket.name)
                model.setItem(i, 0, item)  # row, column, item (QStandardItem)

                item = QStandardItem(str(bucket.storage))
                model.setItem(i, 1, item)  # row, column, item (QStandardItem)

                item = QStandardItem(str(bucket.transfer))
                model.setItem(i, 2, item)  # row, column, item (QStandardItem)

                item = QStandardItem(bucket.id)
                model.setItem(i, 3, item)  # row, column, item (QStandardItem)

                i = i + 1
        except sjexc.StorjBridgeApiError as e:
            QtGui.QMessageBox.about(self, "Unhandled bucket resolving exception", "Exception: " + str(e))

        self.bucket_manager_ui.total_buckets_label.setText(str(i))  # set label of user buckets number
        self.bucket_manager_ui.bucket_list_tableview.setModel(model)
        self.bucket_manager_ui.bucket_list_tableview.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
