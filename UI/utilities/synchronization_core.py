# -*- coding: utf-8 -*-
# Synchronization core module for Storj GUI Client #

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import threading

HANDLE_ON_MOVE_EVENT = True
HANDLE_ON_DELETE_EVENT = True

class StorjFileSynchronization():

    def start_sync_thread(self):
        return 1

    def reload_sync_configuration(self):
        return 1

    def add_file_to_sync_queue(self, file_path):
        return 1

class FileChangesHandler(PatternMatchingEventHandler):
    #patterns = ["*.xml", "*.lxml"]

    def __init__(self):
        self.storj_file_synchronization_core = StorjFileSynchronization()


    def process(self, event):
        """
        event.event_type
            'modified' | 'created' | 'moved' | 'deleted'
        event.is_directory
            True | False
        event.src_path
            path/to/observed/file
        """
        # the file will be processed there
        self.storj_file_synchronization_core.add_file_to_sync_queue(file_path=str(event.src_path))
        print str(event)
        #print str(event.src_path) +  str(event.event_type)  + "event" # print now only for degug

    def on_deleted(self, event):
        if HANDLE_ON_DELETE_EVENT:
            self.process(event)

    def on_moved(self, event):
        if HANDLE_ON_MOVE_EVENT:
            self.process(event)

    def on_modified(self, event):
        self.process(event)

    def on_created(self, event):
        self.process(event)

class SyncObserverWorker():
    def start_observing_thread(self):
        observing_main_thread = threading.Thread(
            target=self.start_observing)
        observing_main_thread.start()

    def start_observing(self):
        paths_to_observe = []
        paths_to_observe.append("/home/lakewik/storjsync")
        self.observer = Observer()
        for path in paths_to_observe:
            self.observer.schedule(FileChangesHandler(), path=str(path))
        self.observer.start()
        print "Synchronization directories observing started!"

    def stop_observers(self):
        self.observer.stop()
        return 1
        #try:
         #   while True:
          #      time.sleep(1)
        #except KeyboardInterrupt:
         #   observer.stop()

        #observer.join()

