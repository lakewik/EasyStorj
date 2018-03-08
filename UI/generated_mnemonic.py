from qt_interfaces.generated_mnemonic_ui import Ui_MnemonicGenerated
from PyQt4 import QtGui

from crypto.mnemonic import mnemonic


# Mnemonic key enter window section #
class MnemonicGeneratedUI(QtGui.QMainWindow):

    def __init__(self, parent=None, enter_mnemonic_ui=None):
        QtGui.QWidget.__init__(self, parent)
        self.mnemonic_generated_ui = Ui_MnemonicGenerated()
        self.mnemonic_generated_ui.setupUi(self)

        self.enter_mnemonic_ui = enter_mnemonic_ui

        self.mnemonic_generated_ui.generate_new_key.clicked.connect(
            self.generate_new_mnemonic)
        self.mnemonic_generated_ui.apply_bt.clicked.connect(self.finish)

        self.mnemonic_module = mnemonic.Mnemonic("english")
        generated_mnemonic_key = self.mnemonic_module.generate(128)

        # seed = self.mnemonic_module.to_seed(mnemonic=generated_mnemonic_key)

        self.mnemonic_generated_ui.mnemonic_edit.setPlainText(
            generated_mnemonic_key)

    def generate_new_mnemonic(self):
        generated_mnemonic_key = self.mnemonic_module.generate(128)
        self.mnemonic_generated_ui.mnemonic_edit.setPlainText(
            generated_mnemonic_key)

    def finish(self):
        self.enter_mnemonic_ui.encryption_mnemonic_key.setText(
            self.mnemonic_generated_ui.mnemonic_edit.toPlainText())
        self.close()
        return True

    def copy_mnemonic_to_clipborad(self):
        return True
