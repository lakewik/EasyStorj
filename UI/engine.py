from utilities.account_manager import AccountManager


# StorjEngine section
class StorjEngine():

    def __init__(self):
        account_manager = AccountManager()
        self.password = None
        if account_manager.if_logged_in():
            self.password = account_manager.get_user_password()
            self.email = account_manager.get_user_email()
            # initialize Storj
            self.storj_client = storj.Client(email=str(self.email), password=str(self.password))
            print "zalogowano"
        print "testlogin"
        print str(self.password)
