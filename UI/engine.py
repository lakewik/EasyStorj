from utilities.account_manager import AccountManager
from utilities.backend_config import Configuration
import logging
import storj


class StorjEngine:

    __logger = logging.getLogger('%s.StorjEngine' % __name__)

    def __init__(self):
        self.conf_manager = Configuration()
        self.account_manager = AccountManager()
        self.password = None
        if self.account_manager.if_logged_in():
            self.password = self.account_manager.get_user_password()
            self.email = self.account_manager.get_user_email()
            # initialize Storj
            max_bridge_request_timeout = \
                self.conf_manager.get_max_bridge_request_timeout()
            self.__logger.info('Using Bridge timeout: %s' %
                               max_bridge_request_timeout)
            self.storj_client = storj.Client(email=self.email,
                                             password=self.password,
                                             do_hashing=False,
                                             timeout=max_bridge_request_timeout)
            self.__logger.debug('Login from credentials xml file')
        self.__logger.debug('testlogin, StorjEngine')
