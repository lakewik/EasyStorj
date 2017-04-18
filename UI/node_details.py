import json
import socket
from PyQt4 import QtCore, QtGui

from PyQt4.QtGui import QMessageBox
from PyQt4.QtGui import QPixmap

from qt_interfaces.node_details_ui import Ui_NodeDetails
from engine import StorjEngine
from utilities.tools import Tools

from ipwhois import IPWhois
import pycountry
import threading
import storj.exception

from resources.html_strings import html_format_begin, html_format_end


# Node details section
class NodeDetailsUI(QtGui.QMainWindow):

    def __init__(self, parent=None, nodeid=None):
        QtGui.QWidget.__init__(self, parent)
        self.storj_engine = StorjEngine()  # init StorjEngine
        # login UI
        self.node_details_ui = Ui_NodeDetails()
        self.node_details_ui.setupUi(self)

        self.nodeid = nodeid
        self.tools = Tools()

        QtCore.QObject.connect(self.node_details_ui.ok_bt, QtCore.SIGNAL("clicked()"), self.close)  # close window
        self.connect(self, QtCore.SIGNAL("showBridgeExceptionMessageBox"), self.show_storj_bridge_exception)

        self.createNewNodeDetailsResolveThread()
        # print nodeid

    def show_storj_bridge_exception(self, exception_content):
        try:
            j = json.loads(str(exception_content))
            QMessageBox.critical(self, "Bridge error", str(j["error"]))

        except:
            QMessageBox.critical(self, "Bridge error", str(exception_content))


    def createNewNodeDetailsResolveThread(self):
        download_thread = threading.Thread(target=self.initialize_node_details, args=())
        download_thread.start()

    def initialize_node_details(self):

        try:
            self.node_details_content = self.storj_engine.storj_client.contact_lookup(str(self.nodeid))

            self.node_details_ui.address_label.setText(
                html_format_begin + str(self.node_details_content.address) + html_format_end)  # get given node address
            self.node_details_ui.last_timeout_label.setText(
                html_format_begin + str(self.node_details_content.lastTimeout) + html_format_end)  # get last timeout
            self.node_details_ui.timeout_rate_label.setText(
                html_format_begin + str(self.node_details_content.timeoutRate) + html_format_end)  # get timeout rate
            self.node_details_ui.user_agent_label.setText(
                html_format_begin + str(self.node_details_content.userAgent) + html_format_end)  # get user agent
            self.node_details_ui.protocol_version_label.setText(
                html_format_begin + str(self.node_details_content.protocol) + html_format_end)  # get protocol version
            self.node_details_ui.response_time_label.setText(html_format_begin + str(
                self.node_details_content.responseTime) + html_format_end)  # get farmer node response time
            self.node_details_ui.port_label.setText(
                html_format_begin + str(self.node_details_content.port) + html_format_end)  # get farmer node port
            self.node_details_ui.node_id_label.setText(
                html_format_begin + str(self.nodeid) + html_format_end)  # get farmer node response time

            # ping_to_node = self.tools.measure_ping_latency(str(self.node_details_content.address))

            ip_addr = socket.gethostbyname(str(self.node_details_content.address))

            obj = IPWhois(ip_addr)
            res = obj.lookup_whois()
            country = res["nets"][0]['country']

            country_parsed = pycountry.countries.get(alpha_2=str(country))

            country_full_name = country_parsed.name

            self.node_details_ui.country_label.setText(
                html_format_begin + str(country_full_name) + html_format_end)  # set full country name

            ### Display country flag ###

            self.scene = QtGui.QGraphicsScene()

            # scene.setSceneRect(-600,-600, 600,600)
            # self.scene.setSceneRect(-600, -600, 1200, 1200)

            # pic = QtGui.QPixmap("PL.png")
            # self.scene.addItem(QtGui.QGraphicsPixmapItem(pic))
            # self.view = self.node_details_ui.country_graphicsView
            # self.view.setScene(self.scene)
            # self.view.setRenderHint(QtGui.QPainter.Antialiasing)
            # self.view.show()

            grview = self.node_details_ui.country_graphicsView()
            scene = QtGui.QGraphicsScene()
            scene.addPixmap(QPixmap('PL.png'))
            grview.setScene(scene)

            grview.show()

            print country_full_name
        except storj.exception.StorjBridgeApiError as e:
            self.emit(QtCore.SIGNAL("showBridgeExceptionMessageBox"), str(e))  # emit signal to show message box with bridge exception
        except Exception as e:
            self.emit(QtCore.SIGNAL("showUnhandledExceptionMessageBox"), str(e))  # emit signal to show message box with unhandled exception





