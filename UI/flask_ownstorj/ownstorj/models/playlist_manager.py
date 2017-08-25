from UI.utilities import account_manager
from UI.engine import StorjEngine
from UI.utilities.tools import Tools
from tinydb import TinyDB, Query, where

#import soundfile as sf


# Module for managing public file sharing in OwnStorj

storj_engine = StorjEngine()  # init StorjEngine
tools = Tools()  # init StorjGUI Tools

class OwnStorjPlaylistManager:
    def __init__(self):
        self.ownstorj_playlists_db = TinyDB('ownstorj_playlists.json')
        self.playlists_table = self.ownstorj_playlists_db.table('playlists')
        self.tracks_table = self.ownstorj_playlists_db.table('tracks')

    def get_sound_file_length(self, file_path):
        #f = sf.SoundFile(file_path)

        #sound_file_length = int (round(len(f) / f.samplerate))
        #return sound_file_length
        return False

    def add_new_playlist(self, playlist_name, playlist_category, playlist_description):
        added_playlist = self.playlists_table.insert({'name': playlist_name, 'category': playlist_category, 'description': playlist_description})

        return added_playlist

    def remove_playlist(self, playlist_id):
        self.playlists_table.remove(eids=[int(playlist_id)])
        return True

    def remove_track(self, track_id):
        self.tracks_table.remove(eids=[int(track_id)])
        return True

    def insert_track(self, track_name, track_local_file_id, playlist_id, track_author="",
                     track_description="", track_length="", track_album=""):
        inserted_track = self.tracks_table.insert({'name': track_name, 'author': track_author,
                                                   'description': track_description,
                                                   'length': track_length, 'album': track_album,
                                                   'local_file_id': track_local_file_id,
                                                   'playlist_id': playlist_id})

        return inserted_track

    def get_playlist_tracks_list(self, playlist_id):
        playlist_tracks_list = self.tracks_table.search(where('playlist_id') == str(playlist_id))
        return playlist_tracks_list

    def get_playlists_list(self):
        playlists_list = self.playlists_table.all()
        return playlists_list

    def get_playlist_details(self, playlist_id):
        playlist_details = self.tracks_table.get(eid=playlist_id)
        return playlist_details

    def count_tracks_in_playlist(self, playlist_id):
        playlist_tracks_list = self.tracks_table.search(where('playlist_id') == str(playlist_id))
        #i = 0
        #for track in playlist_tracks_list:
        #    i += 1

        return len(playlist_tracks_list)

    def generate_playlist_export_file(self, file_type, playlist_id, ownstorj_source_address):
        playlist_tracks_list = self.get_playlist_tracks_list(playlist_id=playlist_id)
        tracks_count = len(playlist_tracks_list)
        output_playlist_file_content = "" # init variable

        if file_type == "PLS":
            output_playlist_file_content = '[playlist] \n' \
                          'NumberOfEntries='+str(tracks_count)+'\n'

            i = 0
            for track in playlist_tracks_list:
                i += 1
                output_playlist_file_content += "File"+str(i)+"="+str(ownstorj_source_address)+"/public_download_gateway/"+str(track['local_file_id'])+"/1"+'\n'
                output_playlist_file_content += "Title"+str(i)+"="+str(track["name"])+'\n'
                output_playlist_file_content += "Length"+str(i)+"="+str(track["length"])+'\n'
                output_playlist_file_content += 'Version=2\n'

        elif file_type == "M3U":
            for track in playlist_tracks_list:
                output_playlist_file_content += str(ownstorj_source_address)+"/public_download_gateway/"+str(track['local_file_id'])+"/1"+'\n'

        elif file_type == "XSPF":
            output_playlist_file_content = '<?xml version="1.0" encoding="UTF-8"?>'
            output_playlist_file_content += '<playlist version="1" xmlns="http://xspf.org/ns/0/">'
            output_playlist_file_content += '<trackList>'

            for track in playlist_tracks_list:
                output_playlist_file_content += '<track>'
                output_playlist_file_content += '<title>'+track["name"]+'</title>'
                output_playlist_file_content += '<location>'+str(ownstorj_source_address)+"/public_download_gateway/"+str(track['local_file_id'])+"/1"+'</location>'
                output_playlist_file_content += '</track>'

            output_playlist_file_content += '</trackList>'
            output_playlist_file_content += '</playlist>'

        elif file_type == "ASX":
            output_playlist_file_content = '<asx version="3.0">'
            output_playlist_file_content += '<title>OwnStorj Playlist</title>'

            for track in playlist_tracks_list:
                output_playlist_file_content += '<entry>'
                output_playlist_file_content += '<title>'+track["name"]+'</title>'
                output_playlist_file_content += '<ref href="'+str(ownstorj_source_address)+"/public_download_gateway/"+str(track['local_file_id'])+"/1"+'" />'
                output_playlist_file_content += '<author>' + track["author"] + '</author>'
                output_playlist_file_content += '</entry>'

            output_playlist_file_content += '</asx>'
        else:
            return False

        return output_playlist_file_content

    def is_file_in_playlist(self, local_file_id):
        if len(self.tracks_table.search(where('local_file_id') == str(local_file_id))) > 0:
            return True
        else:
            return False



ownstorj_playlist_manager = OwnStorjPlaylistManager()
#own_storj_playlist_manager.add_new_playlist(playlist_category="b", playlist_description="bb", playlist_name="ff")
#ownstorj_playlist_manager.get_playlist_details("sff")

