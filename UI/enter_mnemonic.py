from qt_interfaces.enter_mnemonic_key_ui import Ui_EnterMnemonic
from generated_mnemonic import MnemonicGeneratedUI
from mainUI import MainUI
from PyQt4 import QtCore, QtGui

# Mnemonic key enter window section #
class EnterMnemonicUI(QtGui.QMainWindow):

    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.enter_mnemonic_ui = Ui_EnterMnemonic()
        self.enter_mnemonic_ui.setupUi(self)

        self.enter_mnemonic_ui.apply_bt.clicked.connect(self.apply_given_mnemonic)
        self.enter_mnemonic_ui.skip_bt.clicked.connect(self.apply_given_mnemonic)

        self.enter_mnemonic_ui.generate_key_bt.clicked.connect(self.open_key_generate_window)



    def open_key_generate_window(self):
        mnemonic_generate_window = MnemonicGeneratedUI(enter_mnemonic_ui=self.enter_mnemonic_ui)
        print "show"
        mnemonic_generate_window.show()
        mnemonic_generate_window.exec_()

    def apply_given_mnemonic(self):
        main_dashboard = MainUI()
        main_dashboard.show()
        self.close()
