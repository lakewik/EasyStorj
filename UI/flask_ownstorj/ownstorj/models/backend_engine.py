from UI.utilities import account_manager
from UI.engine import StorjEngine
from ownstorj_config_manager import OwnStorjConfigManager

# OwnStorj backend enging

storj_engine = StorjEngine()  # init StorjEngine
ownstorj_config_manager = OwnStorjConfigManager()

class OwnStorjBuckets:
    def __init__(self):
        print 1

    def initialize_public_bucket(self):
        try:
            bucket_create_response = storj_engine.storj_client.bucket_create(name="ownstorj_public", transfer=1, storage=1)
            ownstorj_config_manager.add_public_bucket(bucket_id=bucket_create_response.id,
                                                      bucket_name=bucket_create_response.name)
            return True
        except BaseException as e:
            print e
            return False


