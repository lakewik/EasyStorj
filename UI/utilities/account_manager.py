import xml.etree.cElementTree as ET


class AccountManager:

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

    def if_logged_in(self):
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

    def logout(self):
        print 1

    def get_user_password(self):
        password = ""
        try:
            et = etree.parse("storj_account_conf.xml")
            for tags in et.iter('password'):
                password = tags.text
        except:
            print "Unspecified error"
        return password

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
