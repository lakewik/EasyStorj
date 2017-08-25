from UI.utilities import account_manager
from UI.engine import StorjEngine

# Module for buckets for OwnStorj

storj_engine = StorjEngine()  # init StorjEngine

class OwnStorjBuckets:
    def __init__(self):
        print 1

    def get_bucket_name(self, bucket_id):
        bucket_data = storj_engine.storj_client.bucket_get(bucket_id=str(bucket_id))
        bucket_name = str(bucket_data.name)
        return bucket_name

    def get_buckets_array(self):
        buckets_array = storj_engine.storj_client.bucket_list()
        return buckets_array

    def calculate_bucket_stats(self, buckets_array):
        buckets_details_array = {}
        i = 0

        for bucket in buckets_array:
            total_bucket_files_size = 0
            total_bucket_files_count = 0

            for file in storj_engine.storj_client.bucket_files(bucket_id=bucket.id):
                total_bucket_files_size += int(file['size'])
                total_bucket_files_count += 1

            buckets_details_array[str(i) + "_size"] = total_bucket_files_size
            buckets_details_array[str(i) + "_count"] = total_bucket_files_count
            buckets_details_array[str(i) + "_create_date"] = bucket.created
            i += 1
            #print i

        return buckets_details_array


