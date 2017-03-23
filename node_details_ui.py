# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'node_details.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_NodeDetails(object):
    def setupUi(self, NodeDetails):
        NodeDetails.setObjectName(_fromUtf8("NodeDetails"))
        NodeDetails.resize(710, 424)
        self.label = QtGui.QLabel(NodeDetails)
        self.label.setGeometry(QtCore.QRect(290, 10, 131, 31))
        self.label.setObjectName(_fromUtf8("label"))
        self.line_3 = QtGui.QFrame(NodeDetails)
        self.line_3.setGeometry(QtCore.QRect(10, 40, 691, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.label_3 = QtGui.QLabel(NodeDetails)
        self.label_3.setGeometry(QtCore.QRect(10, 70, 71, 21))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.label_4 = QtGui.QLabel(NodeDetails)
        self.label_4.setGeometry(QtCore.QRect(10, 100, 101, 21))
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_5 = QtGui.QLabel(NodeDetails)
        self.label_5.setGeometry(QtCore.QRect(10, 130, 101, 21))
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.label_6 = QtGui.QLabel(NodeDetails)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 121, 21))
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.node_id_label = QtGui.QLabel(NodeDetails)
        self.node_id_label.setGeometry(QtCore.QRect(90, 70, 601, 21))
        self.node_id_label.setObjectName(_fromUtf8("node_id_label"))
        self.timeout_rate_label = QtGui.QLabel(NodeDetails)
        self.timeout_rate_label.setGeometry(QtCore.QRect(120, 100, 571, 21))
        self.timeout_rate_label.setObjectName(_fromUtf8("timeout_rate_label"))
        self.last_timeout_label = QtGui.QLabel(NodeDetails)
        self.last_timeout_label.setGeometry(QtCore.QRect(120, 130, 571, 21))
        self.last_timeout_label.setObjectName(_fromUtf8("last_timeout_label"))
        self.response_time_label = QtGui.QLabel(NodeDetails)
        self.response_time_label.setGeometry(QtCore.QRect(130, 160, 561, 21))
        self.response_time_label.setObjectName(_fromUtf8("response_time_label"))
        self.label_11 = QtGui.QLabel(NodeDetails)
        self.label_11.setGeometry(QtCore.QRect(10, 190, 71, 21))
        self.label_11.setObjectName(_fromUtf8("label_11"))
        self.country_label = QtGui.QLabel(NodeDetails)
        self.country_label.setGeometry(QtCore.QRect(80, 190, 561, 21))
        self.country_label.setObjectName(_fromUtf8("country_label"))
        self.country_graphicsView = QtGui.QGraphicsView(NodeDetails)
        self.country_graphicsView.setGeometry(QtCore.QRect(490, 230, 211, 131))
        self.country_graphicsView.setObjectName(_fromUtf8("country_graphicsView"))
        self.label_13 = QtGui.QLabel(NodeDetails)
        self.label_13.setGeometry(QtCore.QRect(10, 220, 101, 21))
        self.label_13.setObjectName(_fromUtf8("label_13"))
        self.ping_label = QtGui.QLabel(NodeDetails)
        self.ping_label.setGeometry(QtCore.QRect(120, 220, 301, 21))
        self.ping_label.setObjectName(_fromUtf8("ping_label"))
        self.line_4 = QtGui.QFrame(NodeDetails)
        self.line_4.setGeometry(QtCore.QRect(10, 360, 691, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.ok_bt = QtGui.QPushButton(NodeDetails)
        self.ok_bt.setGeometry(QtCore.QRect(10, 380, 691, 26))
        self.ok_bt.setObjectName(_fromUtf8("ok_bt"))
        self.label_15 = QtGui.QLabel(NodeDetails)
        self.label_15.setGeometry(QtCore.QRect(10, 250, 71, 21))
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.address_label = QtGui.QLabel(NodeDetails)
        self.address_label.setGeometry(QtCore.QRect(90, 250, 381, 21))
        self.address_label.setObjectName(_fromUtf8("address_label"))
        self.port_label = QtGui.QLabel(NodeDetails)
        self.port_label.setGeometry(QtCore.QRect(60, 280, 391, 21))
        self.port_label.setObjectName(_fromUtf8("port_label"))
        self.label_18 = QtGui.QLabel(NodeDetails)
        self.label_18.setGeometry(QtCore.QRect(10, 280, 41, 21))
        self.label_18.setObjectName(_fromUtf8("label_18"))
        self.user_agent_label = QtGui.QLabel(NodeDetails)
        self.user_agent_label.setGeometry(QtCore.QRect(110, 310, 341, 21))
        self.user_agent_label.setObjectName(_fromUtf8("user_agent_label"))
        self.label_20 = QtGui.QLabel(NodeDetails)
        self.label_20.setGeometry(QtCore.QRect(10, 340, 131, 21))
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.label_21 = QtGui.QLabel(NodeDetails)
        self.label_21.setGeometry(QtCore.QRect(10, 310, 101, 21))
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.protocol_version_label = QtGui.QLabel(NodeDetails)
        self.protocol_version_label.setGeometry(QtCore.QRect(140, 340, 331, 21))
        self.protocol_version_label.setObjectName(_fromUtf8("protocol_version_label"))

        self.retranslateUi(NodeDetails)
        QtCore.QMetaObject.connectSlotsByName(NodeDetails)

    def retranslateUi(self, NodeDetails):
        NodeDetails.setWindowTitle(_translate("NodeDetails", "Node details - Storj GUI Client", None))
        self.label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Node details</span></p></body></html>", None))
        self.label_3.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt;\">Node ID:</span></p></body></html>", None))
        self.label_4.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt;\">Timeout rate:</span></p></body></html>", None))
        self.label_5.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt;\">Last timeout:</span></p></body></html>", None))
        self.label_6.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt;\">Response time:</span></p></body></html>", None))
        self.node_id_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Initializing...</span></p></body></html>", None))
        self.timeout_rate_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Initializing...</span></p></body></html>", None))
        self.last_timeout_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Initializing...</span></p></body></html>", None))
        self.response_time_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Initializing...</span></p></body></html>", None))
        self.label_11.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt;\">Country:</span></p></body></html>", None))
        self.country_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Initializing...</span></p></body></html>", None))
        self.label_13.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt;\">Current ping:</span></p></body></html>", None))
        self.ping_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Initializing...</span></p></body></html>", None))
        self.ok_bt.setText(_translate("NodeDetails", "OK", None))
        self.label_15.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt;\">Address:</span></p></body></html>", None))
        self.address_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Initializing...</span></p></body></html>", None))
        self.port_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Initializing...</span></p></body></html>", None))
        self.label_18.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt;\">Port:</span></p></body></html>", None))
        self.user_agent_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Initializing...</span></p></body></html>", None))
        self.label_20.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt;\">Protocol version:</span></p></body></html>", None))
        self.label_21.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt;\">User Agent:</span></p></body></html>", None))
        self.protocol_version_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">Initializing...</span></p></body></html>", None))

