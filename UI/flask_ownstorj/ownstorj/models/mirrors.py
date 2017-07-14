from storj_gui_client.UI.utilities import account_manager
from storj_gui_client.UI.engine import StorjEngine

# Module for mirrors for OwnStorj

storj_engine = StorjEngine()  # init StorjEngine

class OwnStorjMirrors:
    def __init__(self, bucket_id, file_id):
        self.mirrors_data  = storj_engine.storj_client.file_mirrors(str(bucket_id), str(file_id))

    def get_established_mirrors_array(self):
        divider = 0
        recent_shard_hash = ''
        established_mirrors_count_for_file = 0
        for file_mirror in self.mirrors_data:
            for mirror in file_mirror.established:
                established_mirrors_count_for_file += 1
                if mirror['shardHash'] != recent_shard_hash:
                    divider = divider + 1

                recent_shard_hash = mirror['shardHash']

    def get_available_mirrors_array(self):
        divider = 0
        recent_shard_hash = ''
        established_mirrors_count_for_file = 0
        for file_mirror in self.mirrors_data:
            for mirror in file_mirror.available:
                established_mirrors_count_for_file += 1
                if mirror['shardHash'] != recent_shard_hash:
                    divider = divider + 1

                recent_shard_hash = mirror['shardHash']
