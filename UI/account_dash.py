# -*- coding: utf-8 -*-
import threading
from PyQt4 import QtCore, QtGui
from qt_interfaces.account_dash_ui import Ui_AccountDash
from engine import StorjEngine
from utilities.tools import Tools


# Synchronization menu section #
class AccountDashUI(QtGui.QMainWindow):

    def __init__(self, parent=None,):
        QtGui.QWidget.__init__(self, parent)
        self.account_dash_ui = Ui_AccountDash()
        self.account_dash_ui.setupUi(self)

        self.storj_engine = StorjEngine()  # init StorjEngine
        self.tools = Tools()

        self.initialize_buckets_stats_table()

        self.createNewBucketsStatsGetThread()


    def createNewBucketsStatsGetThread(self):
        thread = threading.Thread(target=self.fill_buckets_stats_table, args=())
        thread.start()


    def initialize_buckets_stats_table(self):
        self.table_header = ['Bucket name', 'Files count', 'Total used space']
        self.account_dash_ui.buckets_stats_table.setColumnCount(3)
        self.account_dash_ui.buckets_stats_table.setRowCount(0)
        horHeaders = self.table_header
        self.account_dash_ui.buckets_stats_table.setHorizontalHeaderLabels(horHeaders)
        self.account_dash_ui.buckets_stats_table.resizeColumnsToContents()
        self.account_dash_ui.buckets_stats_table.resizeRowsToContents()

        self.account_dash_ui.buckets_stats_table.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

    def fill_buckets_stats_table(self):
        total_files_size = 0
        total_files_count = 0
        for bucket in self.storj_engine.storj_client.bucket_list():
            total_bucket_files_size = 0
            total_bucket_files_count = 0
            # fill table
            table_row_count = self.account_dash_ui.buckets_stats_table.rowCount()

            self.account_dash_ui.buckets_stats_table.setRowCount(
                table_row_count + 1)

            for file in self.storj_engine.storj_client.bucket_files(bucket_id=bucket.id):
                total_bucket_files_size += int(file['size'])
                total_bucket_files_count += 1

            self.account_dash_ui.buckets_stats_table.setItem(
                table_row_count, 0, QtGui.QTableWidgetItem(bucket.name))

            self.account_dash_ui.buckets_stats_table.setItem(
                table_row_count, 1, QtGui.QTableWidgetItem(str(total_bucket_files_count)))

            self.account_dash_ui.buckets_stats_table.setItem(
                table_row_count, 2, QtGui.QTableWidgetItem(str(self.tools.human_size(total_bucket_files_size))))

            total_files_count += total_bucket_files_count
            total_files_size += total_bucket_files_size

        self.account_dash_ui.files_total_count.setText(str(total_files_count))
        self.account_dash_ui.total_used_space.setText(str(self.tools.human_size(total_files_size)))




