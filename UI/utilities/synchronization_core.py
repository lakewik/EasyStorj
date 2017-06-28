# -*- coding: utf-8 -*-
# Synchronization core module for Storj GUI Client #

import time
from watchdog.observers import Observer
from watchdog.events import PatternMatchingEventHandler
import threading, csv

HANDLE_ON_MOVE_EVENT = True
HANDLE_ON_DELETE_EVENT = True
SYNC_DIRECTORIES_FILE = "storj_sync_dirs.csv"

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
    def __init__(self):
        self.is_sync_active = False

    def start_observing_thread(self):
        observing_main_thread = threading.Thread(
            target=self.start_observing)
        observing_main_thread.start()

    def start_observing(self):
        paths_to_observe = []

        with open(unicode(SYNC_DIRECTORIES_FILE), 'rb') as stream:
            for rowdata in csv.reader(stream):
                for column, data in enumerate(rowdata):
                    if column == 0:
                        paths_to_observe.append(str(data.decode('utf8')))
                        print data.decode('utf8')

        paths_to_observe.append("/home/lakewik/storjsync")
        self.observer = Observer()
        for path in paths_to_observe:
            self.observer.schedule(FileChangesHandler(), path=str(path))
        self.observer.start()
        print "Synchronization directories observing started!"
        self.is_sync_active = True

    def stop_observers(self):
        self.observer.stop()
        self.is_sync_active = False
        print "Synchronization directories observing stopped!"
        return 1

    def restart_observers(self):
        self.stop_observers()
        self.start_observing_thread()
        return True

    def is_sync_active(self):
        return self.is_sync_active


