# -*- coding: utf-8 -*-

from utilities.account_manager import AccountManager
import storj
from utilities.log_manager import logger


class StorjEngine:

    def __init__(self):
        self.account_manager = AccountManager()
        self.password = None
        if self.account_manager.if_logged_in():
            self.password = self.account_manager.get_user_password()
            self.email = self.account_manager.get_user_email()
            # initialize Storj
            self.storj_client = storj.Client(email=self.email,
                                             password=self.password, do_hashing=False)
            logger.debug("Login from credentials xml file")
        logger.debug("testlogin, StorjEngine")
