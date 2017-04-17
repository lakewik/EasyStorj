from PyQt4.QtCore import Qt
from PyQt4 import QtGui


class ImageWidget(QtGui.QLabel):

    def __init__(self, imagePath, parent):
        super(ImageWidget, self).__init__(parent)
        self.picture = QtGui.QPixmap(imagePath).scaled(30, 20, Qt.KeepAspectRatio,Qt.SmoothTransformation)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(3, 3, self.picture)
