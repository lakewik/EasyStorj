from UI.utilities import account_manager
from UI.engine import StorjEngine
from UI.utilities.tools import Tools

# Module for files managing for OwnStorj

storj_engine = StorjEngine()  # init StorjEngine


class OwnStorjFilesManager:
    def __init__(self, bucket_id=None):
        self.bucket_id = bucket_id
        self.tools = Tools()

    def get_files_list(self):
        files_array = []
        for file in storj_engine.storj_client.bucket_files(bucket_id=self.bucket_id):
            file['created'] = file['created'].replace('Z', '').replace('T', ' ')
            file['filename'] = file['filename'].replace('[DECRYPTED]', '')
            #file['size'] = file['size']
            file['size_human_formatted'] = self.tools.human_size(int(file['size']))
            files_array.append(file)

        #print files_array

        return files_array
