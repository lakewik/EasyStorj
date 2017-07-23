# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mirror_node_details_new.ui'
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
        NodeDetails.setEnabled(True)
        NodeDetails.resize(661, 397)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Window, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Base, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Window, brush)
        NodeDetails.setPalette(palette)
        NodeDetails.setContextMenuPolicy(QtCore.Qt.DefaultContextMenu)
        NodeDetails.setAutoFillBackground(False)
        NodeDetails.setLocale(QtCore.QLocale(QtCore.QLocale.English, QtCore.QLocale.UnitedStates))
        self.ok_bt = QtGui.QPushButton(NodeDetails)
        self.ok_bt.setGeometry(QtCore.QRect(550, 350, 91, 31))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ok_bt.setFont(font)
        self.ok_bt.setStyleSheet(_fromUtf8("QPushButton {\n"
"    background-color: #CC0000;\n"
"    border: 1px solid #CC0000;\n"
"    color: #fff;\n"
"    border-radius: 7px;\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: #bb0a0a;\n"
"    border-color: #bb0a0a;\n"
"}\n"
"QPushButton:active {\n"
"    background-color: #ce0e0e;\n"
"    border-color: #ce0e0e;\n"
"}"))
        self.ok_bt.setObjectName(_fromUtf8("ok_bt"))
        self.country_graphicsView = QtGui.QGraphicsView(NodeDetails)
        self.country_graphicsView.setGeometry(QtCore.QRect(460, 210, 181, 121))
        self.country_graphicsView.setObjectName(_fromUtf8("country_graphicsView"))
        self.label_15 = QtGui.QLabel(NodeDetails)
        self.label_15.setGeometry(QtCore.QRect(20, 20, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_15.setFont(font)
        self.label_15.setObjectName(_fromUtf8("label_15"))
        self.timeout_rate_label = QtGui.QLabel(NodeDetails)
        self.timeout_rate_label.setGeometry(QtCore.QRect(210, 50, 361, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.timeout_rate_label.setFont(font)
        self.timeout_rate_label.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.timeout_rate_label.setObjectName(_fromUtf8("timeout_rate_label"))
        self.label_31 = QtGui.QLabel(NodeDetails)
        self.label_31.setGeometry(QtCore.QRect(20, 290, 181, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_31.setFont(font)
        self.label_31.setObjectName(_fromUtf8("label_31"))
        self.address_label = QtGui.QLabel(NodeDetails)
        self.address_label.setGeometry(QtCore.QRect(210, 200, 241, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.address_label.setFont(font)
        self.address_label.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.address_label.setObjectName(_fromUtf8("address_label"))
        self.user_agent_label = QtGui.QLabel(NodeDetails)
        self.user_agent_label.setGeometry(QtCore.QRect(210, 260, 166, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.user_agent_label.setFont(font)
        self.user_agent_label.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.user_agent_label.setObjectName(_fromUtf8("user_agent_label"))
        self.label_25 = QtGui.QLabel(NodeDetails)
        self.label_25.setGeometry(QtCore.QRect(20, 200, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_25.setFont(font)
        self.label_25.setObjectName(_fromUtf8("label_25"))
        self.response_time_label = QtGui.QLabel(NodeDetails)
        self.response_time_label.setGeometry(QtCore.QRect(210, 80, 351, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.response_time_label.setFont(font)
        self.response_time_label.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.response_time_label.setObjectName(_fromUtf8("response_time_label"))
        self.label_27 = QtGui.QLabel(NodeDetails)
        self.label_27.setGeometry(QtCore.QRect(20, 230, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_27.setFont(font)
        self.label_27.setObjectName(_fromUtf8("label_27"))
        self.label_21 = QtGui.QLabel(NodeDetails)
        self.label_21.setGeometry(QtCore.QRect(20, 140, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_21.setFont(font)
        self.label_21.setObjectName(_fromUtf8("label_21"))
        self.label_20 = QtGui.QLabel(NodeDetails)
        self.label_20.setGeometry(QtCore.QRect(20, 80, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_20.setFont(font)
        self.label_20.setObjectName(_fromUtf8("label_20"))
        self.country_label = QtGui.QLabel(NodeDetails)
        self.country_label.setGeometry(QtCore.QRect(210, 140, 351, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.country_label.setFont(font)
        self.country_label.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.country_label.setObjectName(_fromUtf8("country_label"))
        self.port_label = QtGui.QLabel(NodeDetails)
        self.port_label.setGeometry(QtCore.QRect(210, 230, 166, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.port_label.setFont(font)
        self.port_label.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.port_label.setObjectName(_fromUtf8("port_label"))
        self.protocol_version_label = QtGui.QLabel(NodeDetails)
        self.protocol_version_label.setGeometry(QtCore.QRect(210, 290, 171, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.protocol_version_label.setFont(font)
        self.protocol_version_label.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.protocol_version_label.setObjectName(_fromUtf8("protocol_version_label"))
        self.label_33 = QtGui.QLabel(NodeDetails)
        self.label_33.setGeometry(QtCore.QRect(20, 110, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_33.setFont(font)
        self.label_33.setObjectName(_fromUtf8("label_33"))
        self.label_17 = QtGui.QLabel(NodeDetails)
        self.label_17.setGeometry(QtCore.QRect(20, 50, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_17.setFont(font)
        self.label_17.setObjectName(_fromUtf8("label_17"))
        self.label_29 = QtGui.QLabel(NodeDetails)
        self.label_29.setGeometry(QtCore.QRect(20, 260, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_29.setFont(font)
        self.label_29.setObjectName(_fromUtf8("label_29"))
        self.last_timeout_label = QtGui.QLabel(NodeDetails)
        self.last_timeout_label.setGeometry(QtCore.QRect(210, 110, 351, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.last_timeout_label.setFont(font)
        self.last_timeout_label.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.last_timeout_label.setObjectName(_fromUtf8("last_timeout_label"))
        self.node_id_label = QtGui.QLabel(NodeDetails)
        self.node_id_label.setGeometry(QtCore.QRect(210, 20, 431, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.node_id_label.setFont(font)
        self.node_id_label.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.node_id_label.setObjectName(_fromUtf8("node_id_label"))
        self.ping_label = QtGui.QLabel(NodeDetails)
        self.ping_label.setGeometry(QtCore.QRect(210, 170, 351, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.ping_label.setFont(font)
        self.ping_label.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.ping_label.setObjectName(_fromUtf8("ping_label"))
        self.label_23 = QtGui.QLabel(NodeDetails)
        self.label_23.setGeometry(QtCore.QRect(20, 170, 151, 16))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_23.setFont(font)
        self.label_23.setObjectName(_fromUtf8("label_23"))
        self.label_34 = QtGui.QLabel(NodeDetails)
        self.label_34.setGeometry(QtCore.QRect(20, 350, 101, 21))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_34.setFont(font)
        self.label_34.setObjectName(_fromUtf8("label_34"))
        self.last_seen_label = QtGui.QLabel(NodeDetails)
        self.last_seen_label.setGeometry(QtCore.QRect(130, 350, 401, 20))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Lato"))
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.last_seen_label.setFont(font)
        self.last_seen_label.setStyleSheet(_fromUtf8("QLabel{\n"
"color: #2683ff;\n"
"}\n"
""))
        self.last_seen_label.setObjectName(_fromUtf8("last_seen_label"))

        self.retranslateUi(NodeDetails)
        QtCore.QMetaObject.connectSlotsByName(NodeDetails)

    def retranslateUi(self, NodeDetails):
        NodeDetails.setWindowTitle(_translate("NodeDetails", "Farmer node details - Storj GUI", None))
        self.ok_bt.setText(_translate("NodeDetails", "CLOSE", None))
        self.label_15.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#555555;\">NODE ID:</span></p></body></html>", None))
        self.timeout_rate_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#2683ff;\">0.00002</span></p></body></html>", None))
        self.label_31.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#555555;\">PROTOCOL VERSION:</span></p></body></html>", None))
        self.address_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#2683ff;\">0.0.0.0</span></p></body></html>", None))
        self.user_agent_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#2683ff;\">Top Secret Agent</span></p></body></html>", None))
        self.label_25.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#555555;\">ADDRESS:</span></p></body></html>", None))
        self.response_time_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#2683ff;\">12MS</span></p></body></html>", None))
        self.label_27.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#555555;\">PORT:</span></p></body></html>", None))
        self.label_21.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#555555;\">COUNTRY:</span></p></body></html>", None))
        self.label_20.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#555555;\">RESPONSE TIME:</span></p></body></html>", None))
        self.country_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#2683ff;\">Neverland</span></p></body></html>", None))
        self.port_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#2683ff;\">4000</span></p></body></html>", None))
        self.protocol_version_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#2683ff;\">6.1.2</span></p></body></html>", None))
        self.label_33.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#555555;\">LAST TIMEOUT:</span></p></body></html>", None))
        self.label_17.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#555555;\">TIMEOUT RATE:</span></p></body></html>", None))
        self.label_29.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#555555;\">USER AGENT:</span></p></body></html>", None))
        self.last_timeout_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#2683ff;\">01.01.2025T11:11:11.ZZZZ</span></p></body></html>", None))
        self.node_id_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#2683ff;\">489BH9UIREVFNJDV3U84IREKD0OXUFLJ67TY</span></p></body></html>", None))
        self.ping_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#2683ff;\">N/A</span></p></body></html>", None))
        self.label_23.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#555555;\">PING:</span></p></body></html>", None))
        self.label_34.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#555555;\">LAST SEEN:</span></p></body></html>", None))
        self.last_seen_label.setText(_translate("NodeDetails", "<html><head/><body><p><span style=\" color:#2683ff;\">01.01.2025T11:11:11.ZZZZ</span></p></body></html>", None))

