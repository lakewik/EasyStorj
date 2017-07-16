from qt_interfaces.storage_contract_details_ui import Ui_StorageContractDetails
from PyQt4 import QtCore, QtGui

# Node details section
class StorageContractDetailsUI(QtGui.QMainWindow):

    def __init__(self, parent=None, storage_contract=None):
        QtGui.QWidget.__init__(self, parent)
        self.storage_contract_details_ui = Ui_StorageContractDetails()
        self.storage_contract_details_ui.setupUi(self)

        self.storage_contract_details_ui.copy_to_clipboard.clicked.connect(self.copy_contract_details_to_clipboard)
        #self.storage_contract_details_ui.file_delete_bt.clicked.connect(self.close)

        self.storage_contract_details_ui.contract_details_tableWidget.setColumnCount(1)
        self.storage_contract_details_ui.contract_details_tableWidget.setRowCount(15)

        self.contract_table_vertical_header = ['Payment destination', 'Renter ID', 'Data hash'
            , 'Payment storage price', 'Store end', 'Renter hd index', 'Renter signature', 'Store begin', 'Data size'
            , 'Farmer ID', 'Payment download price', 'Version', 'Renter hd key', 'Farmer signature'
            , 'Audit count']
        self.contract_table_horizontal_header = ['Value']

        self.storage_contract_details_ui.contract_details_tableWidget.verticalHeader().setVisible(True)
        self.storage_contract_details_ui.contract_details_tableWidget.setVerticalHeaderLabels(self.contract_table_vertical_header)
        self.storage_contract_details_ui.contract_details_tableWidget.setHorizontalHeaderLabels(self.contract_table_horizontal_header)
        self.storage_contract_details_ui.contract_details_tableWidget.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.storage_contract_details_ui.contract_details_tableWidget.setItem(
                0, 0, QtGui.QTableWidgetItem(storage_contract['payment_destination']))
        self.storage_contract_details_ui.contract_details_tableWidget.setItem(
            1, 0, QtGui.QTableWidgetItem(storage_contract['renter_id']))
        self.storage_contract_details_ui.contract_details_tableWidget.setItem(
            2, 0, QtGui.QTableWidgetItem(storage_contract['data_hash']))
        self.storage_contract_details_ui.contract_details_tableWidget.setItem(
            3, 0, QtGui.QTableWidgetItem(str(storage_contract['payment_storage_price'])))
        self.storage_contract_details_ui.contract_details_tableWidget.setItem(
            4, 0, QtGui.QTableWidgetItem(str(storage_contract['store_end'])))
        self.storage_contract_details_ui.contract_details_tableWidget.setItem(
            5, 0, QtGui.QTableWidgetItem(str(storage_contract['renter_hd_index'])))
        self.storage_contract_details_ui.contract_details_tableWidget.setItem(
            6, 0, QtGui.QTableWidgetItem(storage_contract['renter_signature']))
        self.storage_contract_details_ui.contract_details_tableWidget.setItem(
            7, 0, QtGui.QTableWidgetItem(str(storage_contract['store_begin'])))
        self.storage_contract_details_ui.contract_details_tableWidget.setItem(
            8, 0, QtGui.QTableWidgetItem(str(storage_contract['data_size'])))
        self.storage_contract_details_ui.contract_details_tableWidget.setItem(
            9, 0, QtGui.QTableWidgetItem(storage_contract['farmer_id']))
        self.storage_contract_details_ui.contract_details_tableWidget.setItem(
            10, 0, QtGui.QTableWidgetItem(str(storage_contract['payment_download_price'])))
        self.storage_contract_details_ui.contract_details_tableWidget.setItem(
            11, 0, QtGui.QTableWidgetItem(str(storage_contract['version'])))
        self.storage_contract_details_ui.contract_details_tableWidget.setItem(
            12, 0, QtGui.QTableWidgetItem(storage_contract['renter_hd_key']))
        self.storage_contract_details_ui.contract_details_tableWidget.setItem(
            13, 0, QtGui.QTableWidgetItem(storage_contract['farmer_signature']))
        self.storage_contract_details_ui.contract_details_tableWidget.setItem(
            14, 0, QtGui.QTableWidgetItem(str(storage_contract['audit_count'])))


    def copy_contract_details_to_clipboard(self):
        return True
