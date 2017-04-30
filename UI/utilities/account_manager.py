# -*- coding: utf-8 -*-

import hashlib
import logging

import xml.etree.cElementTree as ET


ACCOUNT_FILE = 'storj_account_conf.xml'


class AccountManager:

    __logger = logging.getLogger('%s.AccountManager' % __name__)

    def __init__(self, login_email=None, password=None):
        self.login_email = login_email
        self.password = password

    def save_account_credentials(self):
        root = ET.Element('account')
        doc = ET.SubElement(root, 'credentials')

        ET.SubElement(doc, 'login_email').text = str(self.login_email)
        ET.SubElement(doc, 'password').text = \
            str(hashlib.sha256(self.password.encode('ascii')).hexdigest())
        ET.SubElement(doc, 'logged_in').text = '1'
        tree = ET.ElementTree(root)
        tree.write('storj_account_conf.xml')

    def if_logged_in(self):
        """Return True if user has already logged in with these credentials"""

        logged_in = '0'
        try:
            et = ET.parse('storj_account_conf.xml')
            for tags in et.iter('logged_in'):
                logged_in = tags.text

        except IOError:
            self.__logger.error('Error in Account Manager login')
            self.__logger.error('Function: if_logged_in')
            self.__logger.error('Credentials file not existing')
            return False

        return logged_in == '1'

    def logout(self):
        self.__logger.debug('TODO')
        self.__logger.debug('1')

    def get_user_password(self):
        password = ""
        try:
            et = ET.parse('storj_account_conf.xml')
            for tags in et.iter('password'):
                password = str(tags.text.encode('ascii'))
                self.__logger.debug('zpliku %s' % tags.text)
        except IOError as e:
            self.__logger.error(e)
            self.__logger.error('Error in Account Manager get password')
            self.__logger.error('Credentials file not existing')
        return password

    def get_user_email(self):
        email = ''
        try:
            et = ET.parse('storj_account_conf.xml')
            for tags in et.iter('login_email'):
                email = tags.text

        except IOError as e:
            self.__logger.error(e)
            self.__logger.error('Error in Account Manager get email')
            self.__logger.error('Credentials file not existing')

        return email
