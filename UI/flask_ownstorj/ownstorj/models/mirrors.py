from UI.utilities import account_manager
from UI.engine import StorjEngine

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

    def get_mirrors_array(self):
        return self.mirrors_data

    def calculate_geodistribution(self, countries_array):

        total_countries = len(countries_array)

        country_counting_array = {}
        country_percent_array = {}
        countries_array_deduplicated = list(set(countries_array))
        for country_code in countries_array_deduplicated:
            country_counting_array[country_code] = countries_array.count(country_code)
            country_percent_array[country_code] = countries_array.count(country_code) / total_countries

        return country_counting_array, country_percent_array




