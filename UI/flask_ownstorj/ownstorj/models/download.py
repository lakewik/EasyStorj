from UI.utilities import account_manager
from UI.engine import StorjEngine


# Module for node details displaying for OwnStorj

storj_engine = StorjEngine()  # init StorjEngine

class OwnStorjDownloadEngine:
    def __init__(self):
        self.node_details_content = None

    def get_file_parametrs_from_public_download_hash(self):
        return False

    def get_pointer_for_single_shard_download(self, bucket_id, file_id):
        pointer = storj_engine.storj_client.file_pointers(
            bucket_id,
            file_id,
            limit=1,
            skip=0,
            exclude=[])

        for single_pointer in pointer:
            ready_pointer = single_pointer

        return ready_pointer



