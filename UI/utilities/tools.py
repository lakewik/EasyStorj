import re
import os
import platform
import pingparser
from os.path import expanduser
import tempfile
import errno

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
        home = expanduser("~")
        return str(home)

    def count_directory_size(self, directory, include_subdirs):

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
        files_count = len([name for name in os.listdir(str(directory)) if os.path.isfile(os.path.join(str(directory), name))])
        return files_count

