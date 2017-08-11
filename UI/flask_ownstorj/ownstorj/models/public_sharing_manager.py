from UI.utilities import account_manager
from UI.engine import StorjEngine
from tinydb import TinyDB, Query


# Module for managing public file sharing in OwnStorj

storj_engine = StorjEngine()  # init StorjEngine

class OwnStorjPublicFileSharingManager:
    def __init__(self):
        self.node_details_content = None
        self.public_files_db = TinyDB('public_files.json')
        self.table = self.public_files_db.table('public_files')

    def save_public_file_to_db(self, bucket_id, file_id, public_download_hash, public_download_hash_url, config_array):
        self.table.insert({'public_download_hash_url': public_download_hash_url, 'public_download_hash': public_download_hash, 'bucket_id': bucket_id, 'file_id': file_id, 'config': {'wait_time': config_array["wait_time"], 'max_allowed_from_one_ip': config_array["max_allowed_from_one_ip"], 'mode': config_array["mode"]}})

    def get_public_download_indicators(self, public_download_hash_url):
        query = Query()
        public_download_indicators = self.table.search(query.public_download_hash_url.search(public_download_hash_url))

        return public_download_indicators



#OwnStorjPublicFileSharingManager.save_public_file_to_db(bucket_id="dsf", file_id="Sdfsd", public_download_hash="adsfasf", public_download_hash_url="sadfasd")





