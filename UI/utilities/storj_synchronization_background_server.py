# !/usr/bin/env python
"""
HTTP C&C server for synchronization management for Storj GUI
"""
from BaseHTTPServer import BaseHTTPRequestHandler, HTTPServer
from synchronization_core import SyncObserverWorker
import threading


SYNC_SERVER_PORT = 8234
sync_observer_worker = SyncObserverWorker()

class StorjSyncServerHandler(BaseHTTPRequestHandler):
    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'text/html')
        self.end_headers()

    def do_GET(self):
        self._set_headers()
        self.wfile.write("Sync C&C server for Storj GUI")

    def do_HEAD(self):
        self._set_headers()

    def do_POST(self):

        # Doesn't do anything with posted data
        content_length = int(self.headers['Content-Length'])  # <--- Gets the size of data
        post_data = self.rfile.read(content_length)  # <--- Gets the data itself

        self._set_headers()

        if post_data == "start_sync_observer":
            sync_observer_worker.start_observing_thread()
            self.wfile.write("OK")
        elif post_data == "stop_sync_observer":
            sync_observer_worker.stop_observers()
            self.wfile.write("OK")
        elif post_data == "is_sync_active":
            is_sync_active = sync_observer_worker.is_sync_active
            if is_sync_active:
                self.wfile.write("1")
            else:
                self.wfile.write("0")

        print post_data
        print sync_observer_worker.is_sync_active


def start_storj_sync_server_thread():

    storj_sync_server_thread = threading.Thread(
        target=run_storj_sync_server)

    storj_sync_server_thread.start()

def run_storj_sync_server(server_class=HTTPServer, handler_class=StorjSyncServerHandler, port=SYNC_SERVER_PORT):
    server_address = ('', port)
    httpd = server_class(server_address, handler_class)
    print 'Starting httpd...'
    httpd.serve_forever()

