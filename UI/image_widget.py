# -*- coding: utf-8 -*-

import logging

from PyQt4 import QtGui
from PyQt4.QtCore import Qt


class ImageWidget(QtGui.QLabel):

    __logger = logging.getLogger('%s.ImageWidget' % __name__)

    def __init__(self, imagePath, parent):
        super(ImageWidget, self).__init__(parent)
        self.picture = QtGui.QPixmap(imagePath).scaled(
            30, 20, Qt.KeepAspectRatio, Qt.SmoothTransformation)

    def paintEvent(self, event):
        painter = QtGui.QPainter(self)
        painter.drawPixmap(3, 3, self.picture)
