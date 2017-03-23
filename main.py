import sys
from PyQt4 import QtCore, QtGui

from PyQt4.QtCore import *
from PyQt4.QtGui import *

import re # for regex

import  threading

import json
import storj
from storj import  model
from storj import  exception

import string

from xml.dom import minidom
from xml.etree import ElementTree
import lxml
from lxml import etree
import xml.etree.cElementTree as ET

import os, platform
from main_menu_ui import Ui_MainMenu
from storj_login_ui import Ui_Login
from storj_register_ui import Ui_Register
from bucket_manage_ui import Ui_BucketManager
from file_manager_ui import Ui_FileManager
from create_bucket_ui import Ui_BucketCreate
from file_mirrors_list_ui import  Ui_FileMirrorsList
from node_details_ui import  Ui_NodeDetails
from client_configuration_ui import  Ui_ClientConfiguration
from initial_window_ui import  Ui_InitialWindow

import socket

import pingparser

import pycountry

from ipwhois import IPWhois

from io import BytesIO
import requests


# ext libs
from treeview_lib import GroupNode

# Defina CONSTANS
global html_format_begin, html_format_end
html_format_begin = "<html><head/><body><p><span style=\" font-size:12pt; font-weight:600;\">"
html_format_end = "</span></p></body></html>"

class Tools():
    def check_email (self, email):
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return False
        else:
            return True

    def measure_ping_latency (self, destination_host):
        ping_latency = str(os.system("ping " + ("-n 1 " if platform.system().lower() == "windows" else "-c 1 ") + str(destination_host)))

        ping_data_parsed = pingparser.parse(ping_latency)

        return ping_data_parsed



#Configuration backend section
class Configuration ():
    def get_config_parametr_value (self, parametr):
        output = ""
        try:
            et = etree.parse("storj_client_config.xml")
            for tags in et.iter(str(parametr)):
                output = tags.text
        except:
            print "Unspecified error"

        return output


    def load_config_from_xml (self):
        try:
            et = etree.parse("storj_client_config.xml")
            for tags in et.iter('password'):
                output = tags.text
        except:
            print "Unspecified error"

    def save_client_configuration(self, settings_ui):
        root = ET.Element("configuration")
        doc = ET.SubElement(root, "client")
        i = 0

        ET.SubElement(doc, "max_shard_size").text = str("test")
        ET.SubElement(doc, "max_connections_onetime").text = str("test")
        ET.SubElement(doc, "advanced_view_enabled").text = str("test")
        ET.SubElement(doc, "max_download_bandwith").text = str("test")
        ET.SubElement(doc, "max_upload_bandwith").text = str("test")
        tree = ET.ElementTree(root)
        tree.write("storj_client_config.xml")


class AccountManager():
    def __init__(self, login_email=None, password=None):
        self.login_email = login_email
        self.password = password

    def save_account_credentials(self):
        root = ET.Element("account")
        doc = ET.SubElement(root, "credentials")
        i = 0

        ET.SubElement(doc, "login_email").text = str(self.login_email)
        ET.SubElement(doc, "password").text = str(self.password)
        ET.SubElement(doc, "logged_in").text = str("1")
        tree = ET.ElementTree(root)
        tree.write("storj_account_conf.xml")

    def if_logged_in (self):
        logged_in = "0"
        try:
            et = etree.parse("storj_account_conf.xml")
            for tags in et.iter('logged_in'):
                logged_in = tags.text
        except:
            logged_in = "0"
            print "Unspecified error"

        if logged_in == "1":
            return True
        else:
            return False


    def logout (self):
        print  1

    def get_user_password (self):
        password = ""
        try:
            et = etree.parse("storj_account_conf.xml")
            for tags in et.iter('password'):
                password = tags.text
        except:
            print "Unspecified error"
        return  password

    def get_user_email(self):
        email = ""
        try:
            et = etree.parse("storj_account_conf.xml")
            for tags in et.iter('login_email'):
                email = tags.text
        except:
            print "Unspecified error"
        return email
        print 1

# Configuration Ui section
class ClientConfigurationUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # register UI
        self.client_configuration_ui = Ui_ClientConfiguration()
        self.client_configuration_ui.setupUi(self)

        self.configuration_manager = Configuration()

        QtCore.QObject.connect(self.client_configuration_ui.apply_bt, QtCore.SIGNAL("clicked()"),self.save_settings)  # valudate and register user

    def save_settings (self):
        #validate settings

        self.configuration_manager.save_client_configuration(self.client_configuration_ui) #save configuration

    def reset_settings_to_default (self):
        print 1

#Register section
class RegisterUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # register UI
        self.register_ui = Ui_Register()
        self.register_ui.setupUi(self)

        QtCore.QObject.connect(self.register_ui.pushButton, QtCore.SIGNAL("clicked()"), self.register) # valudate and register user

    def register (self):
        #validate fields


        self.email = self.register_ui.lineEdit_4.text()
        self.password = self.register_ui.lineEdit_2.text()
        self.password_repeat = self.register_ui.lineEdit_3.text()

        self.tools = Tools()
        success = False
        if self.email != "" and self.password != "" and self.password_repeat != "":
            if self.password == self.password_repeat:
                if (self.tools.check_email(self.email)):
                    # take login action
                    try:
                        self.storj_client = storj.Client(str(self.email), str(self.password))
                        success = True
                        # self.storj_client.user_create("wiktest15@gmail.com", "kotek1")
                    except storj.exception.StorjBridgeApiError, e:
                        j = json.loads(str(e))
                        if (j["error"] == "Email is already registered"):
                            success = False
                            QMessageBox.about(self, "Warning",
                                          "User with this e-mail is already registered! Please login or try different e-mail!")
                        else:
                            success = False
                            QMessageBox.about(self, "Unhandled exception", "Exception: " + str(e))
                else:
                    success = False
                    QMessageBox.about(self, "Warning",
                                  "Your e-mail seems to be invalid! Please chech e-mail  and try again")
            else:
                success = False
                QMessageBox.about(self, "Warning",
                                  "Given passwords are different! Please check and try again!")
        else:
            success = False
            QMessageBox.about(self, "Warning",
                              "Please fill out all fields!")


        if success:
            msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information, "Success", "Successfully registered in Storj Distributed Storage Network! "
                                                                                 "Now, yo must verify your email by clicking link, that been send to you. "
                                                                                 "Then you can login", QtGui.QMessageBox.Ok)
            result = msgBox.exec_()
            if result == QtGui.QMessageBox.Ok:
                self.login_window = LoginUI(self)
                self.login_window.show()
                self.close()
                initial_window.hide()



        print self.email



#Login section
class LoginUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)

        # login UI
        self.login_ui = Ui_Login()
        self.login_ui.setupUi(self)

        # Account manager



        QtCore.QObject.connect(self.login_ui.login_bt, QtCore.SIGNAL("clicked()"), self.login) # take login action

    def login (self):
        #take login action

        self.email = self.login_ui.email.text() #get login
        self.password = self.login_ui.password.text() #get password

        self.storj_client = storj.Client(email=str(self.email), password=str(self.password))
        success = False
        # take login action - check credentials by listing keys :D
        try:
            self.storj_client.key_list()
            success = True
        except storj.exception.StorjBridgeApiError, e:
            j = json.loads(str(e))
            if (j["error"] == "Invalid email or password"):
                QMessageBox.about(self, "Warning",
                                  "Invalid email or password - access denied. Please check your credentials and try again!")
            else:
                QMessageBox.about(self, "Unhandled exception", "Exception: " + str(e))

        if success:
            self.account_manager = AccountManager(str(self.email), str(self.password)) # init account manager
            self.account_manager.save_account_credentials() # save login credentials and state
            #login_msg_box = QMessageBox.about(self, "Success", "Successfully loged in!")
            msgBox = QtGui.QMessageBox(QtGui.QMessageBox.Information,"Success", "Successfully loged in!", QtGui.QMessageBox.Ok)
            result = msgBox.exec_()
            if result == QtGui.QMessageBox.Ok:
                self.main_ui_window = MainUI(self)
                self.main_ui_window.show()
                self.close()
                initial_window.hide()

            #self.account_manager.get_login_state()

        #print self.storj_client.bucket_list()
        print 1;

#StorjEngine section
class StorjEngine ():
    def __init__(self):
        account_manager = AccountManager()
        if account_manager.if_logged_in():
            self.password = account_manager.get_user_password()
            self.email = account_manager.get_user_email()
            # initialize Storj
            self.storj_client = storj.Client(email=str(self.email), password=str(self.password))

#Node details section
class NodeDetailsUI(QtGui.QMainWindow):
    def __init__(self, parent=None, nodeid=None):
        QtGui.QWidget.__init__(self, parent)

        self.storj_engine = StorjEngine()  # init StorjEngine
        # login UI
        self.node_details_ui = Ui_NodeDetails()
        self.node_details_ui.setupUi(self)

        self.nodeid = nodeid
        self.tools = Tools()

        QtCore.QObject.connect(self.node_details_ui.ok_bt, QtCore.SIGNAL("clicked()"), self.close) # close window


        self.createNewNodeDetailsResolveThread()

        ## print nodeid

    def createNewNodeDetailsResolveThread(self):
        download_thread = threading.Thread(target=self.initialize_node_details, args=())
        download_thread.start()


    def initialize_node_details (self):
        self.node_details_content = self.storj_engine.storj_client.contact_lookup(str(self.nodeid))

        self.node_details_ui.address_label.setText(html_format_begin +  str(self.node_details_content.address ) + html_format_end) #get given node address
        self.node_details_ui.last_timeout_label.setText(html_format_begin + str(self.node_details_content.lastTimeout) + html_format_end) #get last timeout
        self.node_details_ui.timeout_rate_label.setText(html_format_begin + str(self.node_details_content.timeoutRate) + html_format_end) #get timeout rate
        self.node_details_ui.user_agent_label.setText(html_format_begin + str(self.node_details_content.userAgent) + html_format_end) #get user agent
        self.node_details_ui.protocol_version_label.setText(html_format_begin + str(self.node_details_content.protocol) + html_format_end) #get protocol version
        self.node_details_ui.response_time_label.setText(html_format_begin + str(self.node_details_content.responseTime) + html_format_end) #get farmer node response time
        self.node_details_ui.port_label.setText(html_format_begin + str(self.node_details_content.port) + html_format_end) #get farmer node port
        self.node_details_ui.node_id_label.setText(html_format_begin + str(self.nodeid) + html_format_end) #get farmer node response time

        #ping_to_node = self.tools.measure_ping_latency(str(self.node_details_content.address))

        ip_addr = socket.gethostbyname(str(self.node_details_content.address))

        obj = IPWhois(ip_addr)
        res = obj.lookup_whois()
        country = res["nets"][0]['country']

        country_parsed = pycountry.countries.get(alpha_2=str(country))

        country_full_name = country_parsed.name

        self.node_details_ui.country_label.setText(html_format_begin + str(country_full_name) + html_format_end)  # set full country name

        print country_full_name


# Mirrors section
class FileMirrorsListUI(QtGui.QMainWindow):
    def __init__(self, parent=None, bucketid=None, fileid=None):
        QtGui.QWidget.__init__(self, parent)
        self.file_mirrors_list_ui = Ui_FileMirrorsList()
        self.file_mirrors_list_ui.setupUi(self)
        #model = self.file_mirrors_list_ui.established_mirrors_tree.model()


        self.file_mirrors_list_ui.mirror_details_bt.clicked.connect (lambda: self.open_mirror_details_window("established"))
        self.file_mirrors_list_ui.mirror_details_bt_2.clicked.connect (lambda: self.open_mirror_details_window("available"))


        #self.connect(self.file_mirrors_list_ui.established_mirrors_tree, QtCore.SIGNAL("selectionChanged(QItemSelection, QItemSelection)"), self.open_mirror_details_window)

        #self.connect(self.file_mirrors_list_ui.established_mirrors_tree, QtCore.SIGNAL('selectionChanged()'), self.open_mirror_details_window)


        #QtCore.QObject.connect(self.file_mirrors_list_ui.established_mirrors_tree.selectionModel(), QtCore.SIGNAL('selectionChanged(QItemSelection, QItemSelection)'),
                              #self.open_mirror_details_window)


        #self.file_mirrors_list_ui.established_mirrors_tree.

        self.bucketid = bucketid
        self.fileid = fileid

        self.file_mirrors_list_ui.file_id_label.setText(html_format_begin + str(self.fileid) + html_format_end)

        print self.fileid
        self.storj_engine = StorjEngine() #init StorjEngine
        self.createNewMirrorListInitializationThread()

    def open_mirror_details_window (self, mirror_state):
        #self.established_mirrors_tree_view = self.file_mirrors_list_ui.established_mirrors_tree


        #daat = self.file_mirrors_list_ui.established_mirrors_tree.selectedIndexes()
        #model = self.file_mirrors_list_ui.established_mirrors_tree.model()
        #data = []

        #initialize variables
        item = ""
        index = ""
        try:
            if mirror_state == "established":
                index = self.file_mirrors_list_ui.established_mirrors_tree.selectedIndexes()[3]
                item = self.file_mirrors_list_ui.established_mirrors_tree.selectedIndexes()[3]
            elif mirror_state == "available":
                index = self.file_mirrors_list_ui.available_mirrors_tree.selectedIndexes()[3]
                item = self.file_mirrors_list_ui.available_mirrors_tree.selectedIndexes()[3]

            nodeid_to_send = item.model().itemFromIndex(index).text()

            if nodeid_to_send != "":
                self.node_details_window = NodeDetailsUI(self, nodeid_to_send)
                self.node_details_window.show()
            else:
                QMessageBox.about(self, "Warning", "Please select farmer node from list")
                print "Unhandled error"

        except:
            QMessageBox.about(self, "Warning", "Please select farmer node from list")
            print "Unhandled error"


    def createNewMirrorListInitializationThread(self):
        mirror_list_initialization_thread = threading.Thread(target=self.initialize_mirrors_tree, args=())
        mirror_list_initialization_thread.start()

    def initialize_mirrors_tree (self):
        # create model
        #model = QtGui.QFileSystemModel()
        #model.setRootPath(QtCore.QDir.currentPath())

        self.file_mirrors_list_ui.loading_label_mirrors_established.setStyleSheet('color: red') #set loading color
        self.file_mirrors_list_ui.loading_label_mirrors_available.setStyleSheet('color: red') #set loading color

        self.mirror_tree_view_header = ['Shard Hash / Address', 'User agent', 'Last seed', 'Node ID']


        # set the model for established mirrors
        self.established_mirrors_model = QStandardItemModel()
        self.established_mirrors_model.setHorizontalHeaderLabels(self.mirror_tree_view_header)

        self.established_mirrors_tree_view = self.file_mirrors_list_ui.established_mirrors_tree
        self.established_mirrors_tree_view.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.established_mirrors_tree_view.setModel(self.established_mirrors_model)
        self.established_mirrors_tree_view.setUniformRowHeights(True)


        self.file_mirrors_list_ui.available_mirrors_tree.setModel(self.established_mirrors_model)



        divider = 0
        group = 1
        self.established_mirrors_count_for_file = 0
        recent_shard_hash = "";
        parent1 = QStandardItem('')
        for file_mirror in self.storj_engine.storj_client.file_mirrors(str(self.bucketid), str(self.fileid)):
            for mirror in file_mirror.established:
                self.established_mirrors_count_for_file += 1
                print file_mirror.established
                if mirror["shardHash"] != recent_shard_hash:
                    parent1 = QStandardItem('Shard with hash {}'.format(mirror["shardHash"]))
                    divider = divider + 1
                    self.established_mirrors_model.appendRow(parent1)

                child1 = QStandardItem(str(mirror["contact"]["address"] + ":" + str(mirror["contact"]["port"])))
                child2 = QStandardItem(str(mirror["contact"]["userAgent"]))
                child3 = QStandardItem(str(mirror["contact"]["lastSeen"]))
                child4 = QStandardItem(str(mirror["contact"]["nodeID"]))
                parent1.appendRow([child1, child2, child3, child4])


                # span container columns
                #self.established_mirrors_tree_view.setFirstColumnSpanned(1, self.established_mirrors_tree_view.rootIndex(), True)

                recent_shard_hash = mirror["shardHash"]

        self.file_mirrors_list_ui.loading_label_mirrors_established.setText("")

        #dbQueryModel.itemData(treeView.selectedIndexes()[0])

        # set the model for available mirrors
        self.available_mirrors_model = QStandardItemModel()
        self.available_mirrors_model.setHorizontalHeaderLabels(self.mirror_tree_view_header)

        self.available_mirrors_tree_view = self.file_mirrors_list_ui.available_mirrors_tree
        self.available_mirrors_tree_view.setSelectionBehavior(QAbstractItemView.SelectRows)

        self.available_mirrors_tree_view.setModel(self.available_mirrors_model)
        self.available_mirrors_tree_view.setUniformRowHeights(True)


        self.file_mirrors_list_ui.available_mirrors_tree.setModel(self.available_mirrors_model)


        divider = 0
        self.available_mirrors_count_for_file = 0
        recent_shard_hash_2 = "";
        parent2 = QStandardItem('')
        for file_mirror in self.storj_engine.storj_client.file_mirrors(str(self.bucketid), str(self.fileid)):
            for mirror_2 in file_mirror.available:
                self.available_mirrors_count_for_file += 1
                if mirror_2["shardHash"] != recent_shard_hash_2:
                    parent2 = QStandardItem('Shard with hash {}'.format(mirror_2["shardHash"]))
                    divider = divider + 1
                    self.available_mirrors_model.appendRow(parent2)

                child1 = QStandardItem(str(mirror_2["contact"]["address"] + ":" + str(mirror_2["contact"]["port"])))
                child2 = QStandardItem(str(mirror_2["contact"]["userAgent"]))
                child3 = QStandardItem(str(mirror_2["contact"]["lastSeen"]))
                child4 = QStandardItem(str(mirror_2["contact"]["nodeID"]))
                parent2.appendRow([child1, child2, child3, child4])


                # span container columns
                #self.established_mirrors_tree_view.setFirstColumnSpanned(1, self.established_mirrors_tree_view.rootIndex(), True)

                recent_shard_hash_2 = mirror_2["shardHash"]
        self.file_mirrors_list_ui.loading_label_mirrors_available.setText("")

        self.file_mirrors_list_ui.established_mirrors_count.setText(html_format_begin + str(self.established_mirrors_count_for_file) + html_format_end)
        self.file_mirrors_list_ui.available_mirrors_count.setText(html_format_begin + str(self.available_mirrors_count_for_file) + html_format_end)
        print QtCore.QDir.currentPath()


# Bucekts section
class BucketManagerUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.bucket_manager_ui = Ui_BucketManager()
        self.bucket_manager_ui.setupUi(self)
        self.createNewBucketGetThread()

        QtCore.QObject.connect(self.bucket_manager_ui.quit_bt, QtCore.SIGNAL("clicked()"), self.quit) # open login window
        #QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL("clicked()"), self.open_register_window) # open login window

    def createNewBucketGetThread(self):
        download_thread = threading.Thread(target=self.initialize_buckets_table, args=())
        download_thread.start()

    def quit (self):
        self.close()

    def initialize_buckets_table (self):
        self.storj_engine = StorjEngine()  # init StorjEngine
        model = QStandardItemModel(1, 1) # initialize model for inserting to table



        model.setHorizontalHeaderLabels(['Name', 'Storage', 'Transfer', 'ID'])

        i = 0
        try:
            for bucket in self.storj_engine.storj_client.bucket_list():
                item = QStandardItem(bucket.name)
                model.setItem(i, 0, item) # row, column, item (QStandardItem)

                item = QStandardItem(str(bucket.storage))
                model.setItem(i, 1, item)  # row, column, item (QStandardItem)

                item = QStandardItem(str(bucket.transfer))
                model.setItem(i, 2, item)  # row, column, item (QStandardItem)

                item = QStandardItem(bucket.id)
                model.setItem(i, 3, item)  # row, column, item (QStandardItem)

                i = i + 1
        except storj.exception.StorjBridgeApiError, e:
            QMessageBox.about(self, "Unhandled bucket resolving exception", "Exception: " + str(e))



        self.bucket_manager_ui.total_buckets_label.setText(str(i)) #set label of user buckets number
        self.bucket_manager_ui.bucket_list_tableview.setModel(model)
        self.bucket_manager_ui.bucket_list_tableview.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)



class BucketCreateUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.bucket_create_ui = Ui_BucketCreate()
        self.bucket_create_ui.setupUi(self)

        QtCore.QObject.connect(self.bucket_create_ui.create_bucket_bt, QtCore.SIGNAL("clicked()"), self.createNewBucketCreateThread)  #create bucket action

        self.storj_engine = StorjEngine() #init StorjEngine

    def createNewBucketCreateThread(self):
        bucket_create_thread = threading.Thread(target=self.create_bucket, args=())
        bucket_create_thread.start()

    def create_bucket (self):
        self.bucket_name = self.bucket_create_ui.bucket_name.text()
        self.bucket_storage = self.bucket_create_ui.bucket_storage_size.text()
        self.bucket_transfer = self.bucket_create_ui.bucket_transfer.text()

        bucekt_cerated = False # init boolean
        if self.bucket_name != "" and self.bucket_transfer != "" and self.bucket_storage != "":

            try:
                self.storj_engine.storj_client.bucket_create(str(self.bucket_name), int(self.bucket_storage), int(self.bucket_transfer))
                bucekt_cerated = True
            except  storj.exception.StorjBridgeApiError, e:
                bucekt_cerated = False
                QMessageBox.about(self, "Unhandled exception while creating bucket", "Exception: " + str(e))

        else:
            QMessageBox.about(self, "Warning", "Please fill out all fields!")
            bucekt_cerated = False

        if bucekt_cerated:
            QMessageBox.about(self, "Success", "Bucket was created successfully!")


        print 1


#Files section
class FileManagerUI(QtGui.QMainWindow):
    def __init__(self, parent=None, bucketid=None):
        QtGui.QWidget.__init__(self, parent)
        self.file_manager_ui = Ui_FileManager()
        self.file_manager_ui.setupUi(self)

        QtCore.QObject.connect(self.file_manager_ui.bucket_select_combo_box, QtCore.SIGNAL("currentIndexChanged(const QString&)"), self.createNewFileListUpdateThread) #connect ComboBox change listener
        QtCore.QObject.connect(self.file_manager_ui.file_mirrors_bt, QtCore.SIGNAL("clicked()"), self.open_mirrors_list_window)  #create bucket action
        QtCore.QObject.connect(self.file_manager_ui.quit_bt, QtCore.SIGNAL("clicked()"), self.close)  #create bucket action

        self.storj_engine = StorjEngine() #init StorjEngine
        self.createNewBucketResolveThread()

    def open_mirrors_list_window (self):
        self.current_bucket_index = self.file_manager_ui.bucket_select_combo_box.currentIndex()
        self.current_selected_bucket_id = self.bucket_id_list[self.current_bucket_index]

        tablemodel = self.file_manager_ui.files_list_tableview.model()
        rows = sorted(set(index.row() for index in
                          self.file_manager_ui.files_list_tableview.selectedIndexes()))
        for row in rows:
            print('Row %d is selected' % row)
            index = tablemodel.index(row, 3)  #get file ID
            # We suppose data are strings
            selected_file_id = str(tablemodel.data(index).toString())
            self.file_mirrors_list_window = FileMirrorsListUI(self, str(self.current_selected_bucket_id), selected_file_id)
            self.file_mirrors_list_window.show()
        print 1


    def createNewFileListUpdateThread(self):
        download_thread = threading.Thread(target=self.update_files_list, args=())
        download_thread.start()

    def update_files_list (self):
        model = QStandardItemModel(1, 1)  # initialize model for inserting to table

        model.setHorizontalHeaderLabels(['File name', 'File size', 'Mimetype', 'File ID'])

        self.current_bucket_index = self.file_manager_ui.bucket_select_combo_box.currentIndex()
        self.current_selected_bucket_id = self.bucket_id_list[self.current_bucket_index]

        i = 0

        for self.file_details in self.storj_engine.storj_client.bucket_files(str(self.current_selected_bucket_id)):
            item = QStandardItem(str(self.file_details["filename"]))
            model.setItem(i, 0, item)  # row, column, item (QStandardItem)

            item = QStandardItem(str(self.file_details["size"]))
            model.setItem(i, 1, item)  # row, column, item (QStandardItem)

            item = QStandardItem(str(self.file_details["mimetype"]))
            model.setItem(i, 2, item)  # row, column, item (QStandardItem)

            item = QStandardItem(str(self.file_details["id"]))
            model.setItem(i, 3, item)  # row, column, item (QStandardItem)

            i = i + 1

            print self.file_details

        self.file_manager_ui.files_list_tableview.clearFocus()
        self.file_manager_ui.files_list_tableview.setModel(model)
        self.file_manager_ui.files_list_tableview.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

    def createNewBucketResolveThread(self):
        download_thread = threading.Thread(target=self.initialize_bucket_select_combobox, args=())
        download_thread.start()

    def initialize_bucket_select_combobox (self):
        self.buckets_list = []
        self.bucket_id_list = []
        self.storj_engine = StorjEngine()  # init StorjEngine
        i = 0
        try:
            for bucket in self.storj_engine.storj_client.bucket_list():
                self.buckets_list.append(str(bucket.name))  # append buckets to list
                self.bucket_id_list.append(str(bucket.id))  # append buckets to list
                i = i + 1
        except storj.exception.StorjBridgeApiError, e:
            QMessageBox.about(self, "Unhandled bucket resolving exception", "Exception: " + str(e))

        self.file_manager_ui.bucket_select_combo_box.addItems(self.buckets_list)

#Initial window section

class InitialWindowUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui_initial_window = Ui_InitialWindow()
        self.ui_initial_window.setupUi(self)
        #QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.save_config) # open bucket manager
        self.storj_engine = StorjEngine() #init StorjEngine


        QtCore.QObject.connect(self.ui_initial_window.login_bt, QtCore.SIGNAL("clicked()"), self.open_login_window) # open login window
        QtCore.QObject.connect(self.ui_initial_window.register_bt, QtCore.SIGNAL("clicked()"), self.open_register_window) # open login window
        #QtCore.QObject.connect(self.ui_initial_window.about_bt, QtCore.SIGNAL("clicked()"), self.open_about_window) # open login window


        #self.storj_engine.storj_client.

    def open_login_window(self):
        self.login_window = LoginUI(self)
        self.login_window.show()


    def open_register_window(self):
        self.register_window = RegisterUI(self)
        self.register_window.show()

# Main UI section
class MainUI(QtGui.QMainWindow):
    def __init__(self, parent=None):
        QtGui.QWidget.__init__(self, parent)
        self.ui = Ui_MainMenu()
        self.ui.setupUi(self)
        #QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.save_config) # open bucket manager
        self.storj_engine = StorjEngine() #init StorjEngine
        #self.storj_engine.storj_client.



        QtCore.QObject.connect(self.ui.pushButton_3, QtCore.SIGNAL("clicked()"), self.open_login_window) # open login window
        QtCore.QObject.connect(self.ui.pushButton_4, QtCore.SIGNAL("clicked()"), self.open_register_window) # open login window
        QtCore.QObject.connect(self.ui.pushButton_5, QtCore.SIGNAL("clicked()"), self.open_bucket_manager_window) # open bucket manager window
        QtCore.QObject.connect(self.ui.pushButton_6, QtCore.SIGNAL("clicked()"), self.open_file_manager_window) # open file manager window
        QtCore.QObject.connect(self.ui.pushButton_7, QtCore.SIGNAL("clicked()"), self.open_bucket_create_window) # open bucket create window
        QtCore.QObject.connect(self.ui.pushButton_7, QtCore.SIGNAL("clicked()"), self.open_file_mirrors_list_window) # open file mirrors list window

    def open_login_window (self):
        self.login_window = LoginUI(self)
        self.login_window.show()

        self.login_window = ClientConfigurationUI(self)
        self.login_window.show()


        #take login action
        print 1;

    def open_register_window(self):
        self.register_window = RegisterUI(self)
        self.register_window.show()

    def open_bucket_manager_window(self):
        self.bucket_manager_window = BucketManagerUI(self)
        self.bucket_manager_window.show()


    def open_file_manager_window(self):
        self.file_manager_window = FileManagerUI(self)
        self.file_manager_window.show()


    def open_bucket_create_window(self):
        self.bucket_create_window = BucketCreateUI(self)
        self.bucket_create_window.show()


    def open_file_mirrors_list_window(self):
        self.file_mirrors_list_window = FileMirrorsListUI(self)
        self.file_mirrors_list_window.show()



class StorjSDKImplementationsOverrides():
    def __init__(self, parent=None):
        self.storj_engine = StorjEngine()  # init StorjEngine


    def create_download_connection(self, url, path_to_save):
        local_filename = path_to_save
        r = requests.get(url)
        # requests.
        with open(local_filename, 'wb') as f:
            for chunk in r.iter_content(chunk_size=1024):
                if chunk:  # filter out keep-alive new chunks
                    f.write(chunk)

    def createNewDownloadThread(self,  url, filelocation):
        download_thread = threading.Thread(target=self.create_download_connection, args=(url, filelocation))
        download_thread.start()


    def upload_file (self):
        print 1;

    def file_download(self, bucket_id, file_id, file_save_path):
        self.storj_engine.storj_client.logger.info('file_pointers(%s, %s)', bucket_id, file_id)

        pointers = self.storj_engine.storj_client.file_pointers(bucket_id=bucket_id, file_id=file_id)

        #file_contents = BytesIO()

        part = 0
        for pointer in pointers:
            print pointer
            url = "http://" +  pointer.get('farmer')['address'] + ":" + str(pointer.get('farmer')['port']) + "/shards/" + pointer["hash"] + "?token=" + pointer["token"]
            self.createNewDownloadThread(url, file_save_path + "part" + str(part))
            part = part + 1;

        print "pobrano"

        return True


if __name__ == "__main__":
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_X11InitThreads)
    app = QtGui.QApplication(sys.argv)

    myapp = MainUI()
    initial_window = InitialWindowUI()

    account_manager = AccountManager()
    if account_manager.if_logged_in():
        myapp.show()
    else:
        initial_window.show()

    sys.exit(app.exec_())
