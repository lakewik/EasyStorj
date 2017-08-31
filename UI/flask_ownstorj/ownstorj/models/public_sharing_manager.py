from UI.utilities import account_manager
from UI.engine import StorjEngine
from UI.utilities.tools import Tools
from tinydb import TinyDB, Query, where
import hashlib, time


# Module for managing public file sharing in OwnStorj

storj_engine = StorjEngine()  # init StorjEngine
tools = Tools()  # init StorjGUI Tools

class OwnStorjPublicFileSharingManager:
    def __init__(self):
        self.node_details_content = None
        self.public_files_db = TinyDB('public_files.json')
        self.table = self.public_files_db.table('public_files')

    def save_public_file_to_db(self, bucket_id, file_id, public_download_hash, public_download_hash_url, config_array, file_size, file_name, file_upload_date):
        file_size_human = tools.human_size(int(file_size))
        self.table.insert({'public_download_hash_url': public_download_hash_url, 'public_download_hash': public_download_hash, 'bucket_id': bucket_id, 'file_id': file_id, 'file_name': file_name, 'file_size': file_size, 'file_size_human': file_size_human, 'file_upload_date': file_upload_date, 'config': {'wait_time': config_array["wait_time"], 'max_allowed_from_one_ip': config_array["max_allowed_from_one_ip"], 'mode': config_array["mode"]}})

    def get_public_download_indicators(self, public_download_hash_url):
        query = Query()
        public_download_indicators = self.table.search(query.public_download_hash_url.search(public_download_hash_url))

        return public_download_indicators

    def is_file_public(self, bucket_id, file_id):
        if len(self.table.search((where('bucket_id') == str(bucket_id)) & (where('file_id') == str(file_id)))) > 0:
            return True
        else:
            return False

    def get_public_file_hash(self, bucket_id, file_id):
        public_file_data = self.table.search((where('bucket_id') == str(bucket_id)) & (where('file_id') == str(file_id)))
        return public_file_data[0]["public_download_hash"]

    def get_public_file_details_by_local_hash(self, local_file_hash):
        query = Query()
        public_download_indicators = self.table.search(query.public_download_hash.search(local_file_hash))

        return public_download_indicators

    def generate_public_file_hash(self, input_string):
        return hashlib.sha256(hashlib.md5(input_string.encode('ascii')).hexdigest()+str(time.time())).hexdigest()



config_array = {}
config_array["wait_time"] = 1
config_array["max_allowed_from_one_ip"] = 1
config_array["mode"] = 1

#owfsm = OwnStorjPublicFileSharingManager()
#owfsm.save_public_file_to_db(bucket_id="dsf", file_id="Sdfsd", public_download_hash="kotek1", public_download_hash_url="kotek1",config_array=config_array, file_name="rudi1", file_size=20000, file_upload_date="7:44")





