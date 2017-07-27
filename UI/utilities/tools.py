import re
import os
import platform
import pingparser
from os.path import expanduser
import tempfile
import errno
import hashlib
import requests
import miniupnpc
SYNC_SERVER_URL = "http://localhost:8234"

class Tools:
    def encrypt_file_name(self):
        return 1

    def encrypt_bucket_name(self):
        return 1

    def temp_clean(self, file_name, temp_path):
        return 1

    def clear_all_logs(self):
        return 1

    def isWritable(self, path):
        try:
            testfile = tempfile.TemporaryFile(dir=path)
            testfile.close()
        except OSError as e:
            if e.errno == errno.EACCES:  # 13
                return False
            e.filename = path
            raise
        return True

    def check_email(self, email):
        if not re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$)", email):
            return False
        else:
            return True

    def measure_ping_latency(self, destination_host):
        """
                Measure ping latency of a host
                Args:
                    destination_host (str): the ip of the host
                Returns:
                    ():
        """
        ping_latency = str(os.system(
            "ping " + ("-n 1 " if platform.system().lower() == "windows" else "-c 1 ") + str(destination_host)))

        ping_data_parsed = pingparser.parse(ping_latency)

        return ping_data_parsed

    def human_size(self, size_bytes):
        """
        format a size in bytes into a 'human' file size, e.g. bytes, KB, MB, GB, TB, PB
        Note that bytes/KB will be reported in whole numbers but MB and above will have greater precision
        e.g. 1 byte, 43 bytes, 443 KB, 4.3 MB, 4.43 GB, etc
        From: <http://stackoverflow.com/questions/1094841/reusable-library-to-get-human-readable-version-of-file-size>
        """
        if size_bytes == 1:
            # because I really hate unnecessary plurals
            return "1 byte"

        suffixes_table = [('bytes', 0), ('KB', 0), ('MB', 1), ('GB', 2), ('TB', 2), ('PB', 2)]

        num = float(size_bytes)
        for suffix, precision in suffixes_table:
            if num < 1024.0:
                break
            num /= 1024.0

        if precision == 0:
            formatted_size = "%d" % num
        else:
            formatted_size = str(round(num, ndigits=precision))

        return "%s %s" % (formatted_size, suffix)

    def get_home_user_directory(self):
        """
               Get the path of current user's home folder
               Returns:
                   (str): the extended path of the home
        """
        home = expanduser("~")
        return str(home)

    def count_directory_size(self, directory, include_subdirs):
        """
               Args:
                   directory (str): the directory
                   include_subdirs (bool): include subdirs or not
               Returns:
                   total_size (int): total size of the directory
        """
        if include_subdirs:
            start_path = str(directory)
            total_size = 0
            for dirpath, dirnames, filenames in os.walk(start_path):
                for f in filenames:
                    fp = os.path.join(dirpath, f)
                    total_size += os.path.getsize(fp)
        else:
            total_size = sum(os.path.getsize(f) for f in os.listdir(str(directory)) if os.path.isfile(f))

        return total_size

    def count_files_in_dir(self, directory, include_subdirs=False):
        """
        Get the number of files in a directory
        Args:
            directory (str): the name of the directory
            include_subdirs (bool): include subdirs or not
        Returns:
            files_count (int): number of files in dir
        """
        files_count = len([name for name in os.listdir(str(directory)) if os.path.isfile(os.path.join(str(directory), name))])
        return files_count

    def start_synchronization_observer(self):
        data = "start_sync_observer"

        return requests.post(SYNC_SERVER_URL, data=data).text

    def stop_synchronization_observer(self):
        data = "stop_sync_observer"

        return requests.post(SYNC_SERVER_URL, data=data).text

    def is_sync_observer_active(self):
        data = "is_sync_active"

        return requests.post(SYNC_SERVER_URL, data=data).text

    def generate_max_shard_size(self, max_shard_size_input, shard_size_unit):
        if shard_size_unit == 0:  # KB:
            max_shard_size = (max_shard_size_input * 2048)
        elif shard_size_unit == 1:  # MB:
            max_shard_size = (max_shard_size_input * 1024 * 2048)
        elif shard_size_unit == 2:  # GB:
            max_shard_size = (max_shard_size_input * 1024 * 1024 * 2048)
        elif shard_size_unit == 3:  # TB:
            max_shard_size = (max_shard_size_input * 1024 * 1024 * 1024 * 2048)

        return max_shard_size

    # NETWORK

    def map_port_UPnP(self, port, description):
        upnp = miniupnpc.UPnP()

        upnp.discoverdelay = 10
        upnp.discover()

        upnp.selectigd()

        upnp.addportmapping(port, 'TCP', upnp.lanaddr, port, description, '')


