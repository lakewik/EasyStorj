from storj_gui_client.UI.utilities import account_manager
from storj_gui_client.UI.engine import StorjEngine

# Module for buckets for OwnStorj

storj_engine = StorjEngine()  # init StorjEngine

def get_buckets_array():
    buckets_array = storj_engine.storj_client.bucket_list()
    return buckets_array

def calculate_bucket_stats(buckets_array):
    buckets_details_array = {}
    i = 0
    for bucket in buckets_array:
        total_bucket_files_size = 0
        total_bucket_files_count = 0

        for file in storj_engine.storj_client.bucket_files(bucket_id=bucket.id):
            total_bucket_files_size += int(file['size'])
            total_bucket_files_count += 1

        buckets_details_array[i, "size"] = total_bucket_files_size
        buckets_details_array[i, "count"] = total_bucket_files_count
        i += 1

        return buckets_details_array
