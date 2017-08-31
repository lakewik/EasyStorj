import collections
import json
import socket
from threading import Thread

from ipwhois import IPWhois

from ...ownstorj import app
#from ...ownstorj import socketio

from ...ownstorj.models.buckets import OwnStorjBuckets
from ...ownstorj.models.files import OwnStorjFilesManager
from ...ownstorj.models.download import OwnStorjDownloadEngine
from ...ownstorj.models.public_sharing_manager import OwnStorjPublicFileSharingManager
from ...ownstorj.models.node import OwnStorjNodeDetails
from ...ownstorj.models.mirrors import OwnStorjMirrors
from ...ownstorj.models.playlist_manager import OwnStorjPlaylistManager
from UI.engine import StorjEngine
from UI.utilities.account_manager import AccountManager
import base64
import itertools
import copy
from bs4 import BeautifulSoup

from flask import session, render_template, request, make_response, redirect

from decimal import *
import configparser
import hashlib

storj_engine = StorjEngine()  # init StorjEngine
storj_account_manager = AccountManager()

OwnStorjBucketsManager = OwnStorjBuckets()
OwnStorjDownloadEngine = OwnStorjDownloadEngine()

def can_login_local_without_auth():
    return True

def initSession():
  try:
    session['counter'] += 1
  except KeyError:
    session['counter'] = 1

  try:
    a = session['logged_in']
  except KeyError:
    session['logged_in'] = False


def generate_menus_data():
    user_email = storj_account_manager.get_user_email()
    menus_data = {}
    menus_data["account_name"] = user_email
    menus_data["display_logout_button"] = True
    return menus_data


@app.route('/logout', methods=['GET'])
def logout_backend():
    if request.method == 'GET':
        session['logged_in'] = False
        return make_response(redirect("/login"))


@app.route('/login', methods=['POST', 'GET'])
def login_view():
    initSession()

    if session['logged_in']:
        return make_response(redirect("/dashboard"))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if storj_account_manager.validate_password_local(password=str(password)):
            session['logged_in'] = True
            return make_response(redirect("/dashboard"))
        else:
            return render_template('login.html', login_message="failed")
    else:
        return render_template('login.html')




@app.route('/')
@app.route('/dashboard')
def dashboard_view():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('dashboard.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/buckets_list', defaults={'reinfo': None})
@app.route('/buckets_list/<reinfo>')
def buckets_list_view(reinfo):
    initSession()
    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        if reinfo == None:
            reinfo = ""

        if reinfo == "bucket_created":
            reinfo = "bucket_created"

        return render_template('buckets_list_manager.html', menu_data=generate_menus_data(), reinfo=reinfo)
    else:
        return make_response(redirect("/login"))


@app.route('/buckets_list_table')
def buckets_list_table():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        buckets_array = OwnStorjBucketsManager.get_buckets_array()
        buckets_array2 = buckets_array
        # buckets_details_array = OwnStorjBucketsManager.calculate_bucket_stats(buckets_array2)

        buckets_details_array = 1

        print buckets_array
        print buckets_details_array
        return render_template('buckets_list_table.html', buckets=buckets_array2, bucket_details=buckets_details_array)
    else:
        return make_response(redirect("/login"))


@app.route('/bucket_add', defaults={'reinfo': None})
@app.route('/bucket_add/<reinfo>')
def bucket_add_view(reinfo):
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        if reinfo == None:
            reinfo = ""

        if reinfo == "bucket_created":
            reinfo = "bucket_created"
        elif reinfo == "failed":
            reinfo = "failed"

        return render_template('bucket_add.html', menu_data=generate_menus_data(), reinfo=reinfo)
    else:
        return make_response(redirect("/login"))


@app.route('/files_manager/', defaults={'bucket_id': None})
@app.route('/files_manager/<bucket_id>')
@app.route('/files_manager/<bucket_id>/<extra_params>')
def files_manager_view(bucket_id, extra_params=""):
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        if bucket_id != None:
            bucket_name = OwnStorjBucketsManager.get_bucket_name(bucket_id=bucket_id)
            return render_template('files_manager.html', menu_data=generate_menus_data(), bucket_id=bucket_id,
                                   bucket_name=bucket_name)
        else:
            return redirect("/buckets_list", 301)
    else:
        return make_response(redirect("/login"))

@app.route('/files_table/<bucket_id>', defaults={'extra_params': None})
@app.route('/files_table/<bucket_id>/<extra_params>')
def files_table_view(bucket_id, extra_params):
    initSession()
    ownstorj_public_file_sharing_manager = OwnStorjPublicFileSharingManager()
    if extra_params == "3": # public features and playlist features
        are_public_features_enabled = True
        are_playlist_features_enabled = True
    elif extra_params == "4": # public features
        are_public_features_enabled = True
        are_playlist_features_enabled = False
    else:
        are_public_features_enabled = False
        are_playlist_features_enabled = False


    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        files_manager = OwnStorjFilesManager(str(bucket_id))
        files_list = files_manager.get_files_list()
        # for file in files_list:
        # print file["size"]
        return render_template('files_table.html', files_list=files_list, bucket_id=bucket_id,
                               public_features_enabled=are_public_features_enabled,
                               public_file_sharing_manager=ownstorj_public_file_sharing_manager,
                               playlist_features_enabled=are_playlist_features_enabled)
    else:
        return make_response(redirect("/login"))


@app.route('/settings')
def settings_view():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('settings.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))

@app.route('/sync_settings')
def sync_settings_view():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('sync_settings.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))

@app.route('/sync_statistics')
def sync_statistics_view():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('sync_statistics.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))

@app.route('/tags_labels_manager')
def tags_labels_manager_view():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('tags_labels_manager.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))

@app.route('/single_file_upload')
def upload_view():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('single_file_upload.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/single_file_download')
def download_view():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('single_file_download.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))

@app.route('/favorites')
def favorites_view():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('favorites.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/file_mirrors/<filebucket_id>')
def file_mirrors_view(filebucket_id):
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('file_mirrors.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))

@app.route('/established_file_mirrors/<filebucket_id>')
def established_mirrors_view(filebucket_id):
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        splitted_ids = filebucket_id.split("_")
        ownstorj_mirrors = OwnStorjMirrors(bucket_id=splitted_ids[0], file_id=splitted_ids[1])
        mirrors_data = ownstorj_mirrors.get_mirrors_array()
        mirrors_data, mirrors_data_2 = itertools.tee(mirrors_data)
        mirrors_data_2, temp = itertools.tee(mirrors_data_2)

        recent_shard_hash = ""
        current_shard_hash = ""
        established_mirrors_shards_count = 0
        established_mirrors_total_nodes_count = 0
        table_break_positions = []
        countries_codes_list = []
        country_codes_array = {}
        i = 0;

        for file_mirror in temp:
            for mirror in file_mirror.established:
                i += 1
                if mirror['shardHash'] != current_shard_hash:
                    if i != 1:
                        table_break_positions.append(i - 1)
                if mirror['shardHash'] != recent_shard_hash:
                    current_shard_hash = mirror['shardHash']
                    established_mirrors_shards_count += 1

                try:
                    IP_addr = socket.gethostbyname(str(mirror['contact']['address']))
                    country = whois_lookup_country(IP_addr)
                    established_mirrors_total_nodes_count += 1
                    country_codes_array[mirror['contact']['address']] = country
                    countries_codes_list.append(country)
                except BaseException as e:
                    print e

                recent_shard_hash = mirror['shardHash']

        return render_template('established_mirrors_data.html', table_break_positions=table_break_positions,
                               established_mirrors_shards_count=established_mirrors_shards_count
                               , mirrors_data=mirrors_data, mirrors_data_2=mirrors_data_2,
                               established_mirrors_total_nodes_count=established_mirrors_total_nodes_count,
                               country_codes_array=country_codes_array)
    else:
        return make_response(redirect("/login"))


@app.route('/available_file_mirrors/<filebucket_id>')
def available_mirrors_view(filebucket_id):
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        splitted_ids = filebucket_id.split("_")
        ownstorj_mirrors = OwnStorjMirrors(bucket_id=splitted_ids[0], file_id=splitted_ids[1])
        mirrors_data = ownstorj_mirrors.get_mirrors_array()
        mirrors_data, mirrors_data_2 = itertools.tee(mirrors_data)
        mirrors_data_2, temp = itertools.tee(mirrors_data_2)

        recent_shard_hash = ""
        current_shard_hash = ""
        available_mirrors_shards_count = 0
        available_mirrors_total_nodes_count = 0
        table_break_positions = []
        country_codes_array = {}
        i = 0;

        for file_mirror in temp:
            for mirror in file_mirror.available:
                i += 1
                if mirror['shardHash'] != current_shard_hash:
                    if i != 1:
                        table_break_positions.append(i - 1)
                if mirror['shardHash'] != recent_shard_hash:
                    current_shard_hash = mirror['shardHash']
                    available_mirrors_shards_count += 1

                try:
                    # t1 = Thread(target=whois_lookup_country, args=(mirror['contact']['address']))
                    IP_addr = socket.gethostbyname(str(mirror['contact']['address']))
                    obj = IPWhois(IP_addr)
                    res = obj.lookup_whois()
                    country = res["nets"][0]['country']
                    available_mirrors_total_nodes_count += 1
                    country_codes_array[mirror['contact']['address']] = country
                except BaseException as e:
                    print e

                recent_shard_hash = mirror['shardHash']
        print i

        return render_template('available_mirrors_data.html', table_break_positions=table_break_positions,
                               available_mirrors_shards_count=available_mirrors_shards_count
                               , mirrors_data=mirrors_data, mirrors_data_2=mirrors_data_2,
                               available_mirrors_total_nodes_count=available_mirrors_total_nodes_count,
                               country_codes_array=country_codes_array)
    else:
        return make_response(redirect("/login"))


@app.route('/mirrors_geodistribution/<filebucket_id>')
def mirrors_geodistribution_view(filebucket_id):
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        splitted_ids = filebucket_id.split("_")
        ownstorj_mirrors = OwnStorjMirrors(bucket_id=splitted_ids[0], file_id=splitted_ids[1])
        mirrors_data = ownstorj_mirrors.get_mirrors_array()
        mirrors_data, mirrors_data_2 = itertools.tee(mirrors_data)
        mirrors_data_2, temp = itertools.tee(mirrors_data_2)

        countries_codes_list = []
        countries_codes_list_available = []
        country_codes_array = {}
        i = 0

        for file_mirror in temp:
            for mirror in file_mirror.established:
                i += 1
                try:
                    country = whois_lookup_country(str(mirror['contact']['address']))
                    country_codes_array[mirror['contact']['address']] = country
                    countries_codes_list.append(country)
                except BaseException as e:
                    print e

        for file_mirror in mirrors_data_2:
            for mirror in file_mirror.available:
                i += 1
                try:
                    country = whois_lookup_country(str(mirror['contact']['address']))
                    country_codes_array[mirror['contact']['address']] = country
                    countries_codes_list_available.append(country)
                except BaseException as e:
                    print e

        established_mirrors_geodistribution_countarray = ownstorj_mirrors.calculate_geodistribution(
            countries_array=countries_codes_list)
        available_mirrors_geodistribution_countarray = ownstorj_mirrors.calculate_geodistribution(
            countries_array=countries_codes_list_available)

        return render_template('nodes_geodistribution.html',
                               established_mirrors_geodistribution_countarray=established_mirrors_geodistribution_countarray,
                               available_mirrors_geodistribution_countarray=available_mirrors_geodistribution_countarray)
    else:
        return make_response(redirect("/login"))


def whois_lookup_country (address):

    IP_addr = socket.gethostbyname(str(address))
    obj = IPWhois(IP_addr)
    res = obj.lookup_whois()
    country = res["nets"][0]['country']

    return country

@app.route('/node_details', methods=['GET'])
#@app.route('/node_details?nodeID=<nodeID>')
def node_details_view():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('node_details.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))

@app.route('/node_details_data/<nodeID>')
def node_details_data_view(nodeID):
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        ownstorj_node_details = OwnStorjNodeDetails()
        node_details_array = ownstorj_node_details.node_details(nodeID)
        return render_template('node_details_data.html', node_details_array=node_details_array)
    else:
        return make_response(redirect("/login"))


@app.route('/contract_details')
def contract_details_view():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('contract_details.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/billing')
def billing_view():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('billing.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))

@app.route('/account_stats')
def account_stats_view():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('account_stats.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))

@app.route('/playlist_manager')
def playlist_manager_view():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('playlist_manager.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))

@app.route('/playlist_table_data')
def playlist_table_data_view():
    initSession()
    ownstorj_playlist_manager = OwnStorjPlaylistManager()
    playlists_array = ownstorj_playlist_manager.get_playlists_list()
    playlist_tracks_count = []

    # Now we need to count tracks in each playlist
    for playlist in playlists_array:
        playlist_tracks_count.append(ownstorj_playlist_manager.count_tracks_in_playlist(playlist.eid))

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('playlist_table_data.html', playlists_array=playlists_array, playlist_tracks_count=playlist_tracks_count)
    else:
        return make_response(redirect("/login"))


# Public Download Gateway

@app.route('/public_download_gateway/<download_id>', defaults={'download_type': None})
@app.route('/public_download_gateway/<download_id>/<download_type>')
def public_download_gateway_endpoint(download_id, download_type):

    ready_download_id = download_id

    print download_type

    if download_type != None:
        public_download_type = int(download_type)
    else:
        public_download_type = 2

    if public_download_type == 1:
        public_file_sharing_manager = OwnStorjPublicFileSharingManager()
        download_indicators = public_file_sharing_manager.get_public_download_indicators(
            public_download_hash_url=ready_download_id)

        pointer = OwnStorjDownloadEngine.get_pointer_for_single_shard_download(bucket_id=download_indicators[0]['bucket_id'],
                                                                               file_id=download_indicators[0]['file_id'])
        ready_farmer_url = 'http://%s:%s/shards/%s?token=%s' % (
            pointer.get('farmer')['address'],
            str(pointer.get('farmer')['port']),
            pointer['hash'],
            pointer['token'])

        return redirect(ready_farmer_url)
    else:
        return render_template('public_download_gateway.html')

@app.route('/public_download_get_farmers/<download_id>')
def public_download_get_farmers(download_id):
    public_file_sharing_manager = OwnStorjPublicFileSharingManager()
    download_indicators = public_file_sharing_manager.get_public_download_indicators(
        public_download_hash_url=download_id)

    pointer = OwnStorjDownloadEngine.get_pointer_for_single_shard_download(
        bucket_id=download_indicators[0]['bucket_id'],
        file_id=download_indicators[0]['file_id'])

    ready_farmer_url = 'http://%s:%s/shards/%s?token=%s' % (
        pointer.get('farmer')['address'],
        str(pointer.get('farmer')['port']),
        pointer['hash'],
        pointer['token'])

    return ready_farmer_url

@app.route('/public_download_get_shard/<download_id>/<shard_number>')
def public_download_get_shard(download_id, shard_number):
    public_file_sharing_manager = OwnStorjPublicFileSharingManager()
    download_indicators = public_file_sharing_manager.get_public_download_indicators(
        public_download_hash_url=download_id)

    pointer = OwnStorjDownloadEngine.get_pointer_for_single_shard_download(
        bucket_id=download_indicators[0]['bucket_id'],
        file_id=download_indicators[0]['file_id'])

    ready_farmer_url = 'http://%s:%s/shards/%s?token=%s' % (
        pointer.get('farmer')['address'],
        str(pointer.get('farmer')['port']),
        pointer['hash'],
        pointer['token'])

    return ready_farmer_url


@app.route('/get_public_file_properties/<download_id>')
def get_public_file_properties(download_id):
    public_file_sharing_manager = OwnStorjPublicFileSharingManager()
    download_indicators = public_file_sharing_manager.get_public_download_indicators(
        public_download_hash_url=download_id)
    #print download_indicators

    download_indicators_json = json.dumps(download_indicators).replace("[", "").replace("]", "")

    return download_indicators_json


# Playlists tracks section #
@app.route('/playlist_tracks_manager/<playlist_id>')
def playlist_tracks_manager_view(playlist_id):
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('playlist_tracks_manager.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))

@app.route('/playlist_tracks_table_data/<playlist_id>')
def playlist_tracks_table_data_view(playlist_id):
    initSession()
    ownstorj_playlist_manager = OwnStorjPlaylistManager()
    playlist_tracks_array = ownstorj_playlist_manager.get_playlist_tracks_list(playlist_id=playlist_id)
    playlist_tracks_count = len(playlist_tracks_array)


    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        return render_template('playlist_tracks_table_data.html', playlist_tracks_array=playlist_tracks_array, playlist_tracks_count=playlist_tracks_count)
    else:
        return make_response(redirect("/login"))


@app.route('/buckets_optionlist')
def buckets_optionlist_view():
    initSession()


    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        buckets_array = OwnStorjBucketsManager.get_buckets_array()
        return render_template('buckets_optionlist.html', buckets=buckets_array)
    else:
        return make_response(redirect("/login"))

@app.route('/make_all_files_public/<bucket_id>')
def make_all_files_public(bucket_id):
    initSession()

    config_array = {}
    config_array["wait_time"] = 1
    config_array["max_allowed_from_one_ip"] = 1
    config_array["mode"] = 1

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        public_file_sharing_manager = OwnStorjPublicFileSharingManager()
        files_manager = OwnStorjFilesManager(str(bucket_id))
        files_list = files_manager.get_files_list()

        for file in files_list:
            if not public_file_sharing_manager.is_file_public(bucket_id=bucket_id, file_id=file["id"]):
                public_file_hash = public_file_sharing_manager.generate_public_file_hash(
                    input_string=bucket_id + "_" + file["id"] + file["filename"] + str(file["size"]) + file["created"])

                public_file_sharing_manager.save_public_file_to_db(bucket_id,  file["id"], public_file_hash,
                                                                   public_file_hash,
                                                                   config_array, file["size"], file["filename"],
                                                                   file["created"])
        return "SUCCESS", 200
    else:
        return make_response(redirect("/login"))

@app.route('/insert_all_files_to_playlist/<bucket_id>/<playlist_id>')
def insert_all_files_to_playlist(bucket_id, playlist_id):
    initSession()

    config_array = {}
    config_array["wait_time"] = 1
    config_array["max_allowed_from_one_ip"] = 1
    config_array["mode"] = 1

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        public_file_sharing_manager = OwnStorjPublicFileSharingManager()
        playlist_manager = OwnStorjPlaylistManager()
        make_all_files_public(bucket_id)
        files_manager = OwnStorjFilesManager(str(bucket_id))
        files_list = files_manager.get_files_list()

        for file in files_list:
            local_file_id_hash = public_file_sharing_manager.get_public_file_hash(bucket_id=bucket_id, file_id=file["id"])
            if not playlist_manager.is_file_in_playlist(local_file_id=local_file_id_hash):
                public_file_details = public_file_sharing_manager.get_public_file_details_by_local_hash(
                    local_file_id_hash)

                playlist_manager.insert_track(track_name=public_file_details[0]["file_name"]
                                             ,track_local_file_id=local_file_id_hash
                                              ,playlist_id=playlist_id)
        return "SUCCESS", 200
    else:
        return make_response(redirect("/login"))


# actions handling

@app.route('/buckets/new', methods=['POST'])
def add_bucket():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        bucket_name = None
        success = False
        if request.method == 'POST':
            bucket_name = request.form['bucket_name']
        print bucket_name

        if bucket_name != None:
            try:
                storj_engine.storj_client.bucket_create(name=bucket_name, transfer=1, storage=1)
                success = True
            except BaseException as e:
                success = False
                print e

        if success:
            result_info = "bucket_created"
            response = make_response(redirect("/bucket_add/" + result_info))
        else:
            result_info = 'failed'
            response = make_response(redirect("/bucket_add/" + result_info))

        return response
    else:
        return make_response(redirect("/login"))


@app.route('/playlist/new', methods=['GET'])
def add_playlist():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        playlist_name = None
        playlist_category = None
        playlist_description = None
        success = False
        if request.method == 'GET':
            playlist_name = request.args.get('playlist_name')
            playlist_category = request.args.get('playlist_category')
            playlist_description = request.args.get('playlist_description')


        if playlist_name != None:
            ownstorj_playlist_manager = OwnStorjPlaylistManager()
            ownstorj_playlist_manager.add_new_playlist(playlist_name=playlist_name,
                                                       playlist_description=playlist_description,
                                                       playlist_category=playlist_category)

        return "SUCCESS", 200
    else:
        return make_response(redirect("/login"))

@app.route('/playlist/delete/<playlist_id>', methods=['GET'])
def delete_playlist(playlist_id):
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        if playlist_id != None:
            ownstorj_playlist_manager = OwnStorjPlaylistManager()
            ownstorj_playlist_manager.remove_playlist(playlist_id=playlist_id)

        return "SUCCESS", 200
    else:
        return make_response(redirect("/login"))


@app.route('/synchronization/settings/save', methods=['POST'])
def save_sync_settings():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        if request.method == 'POST':
            bucket_name = request.form['bucket_name']

        response = make_response(redirect("/bucket_add"))

        return response
    else:
        return make_response(redirect("/login"))

@app.route('/make_file_public')
def make_file_public():
    initSession()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        ownstorj_public_file_sharing_manager = OwnStorjPublicFileSharingManager()

        bucket_id = request.args.get('bucket_id')
        file_id = request.args.get('file_id')
        file_name = request.args.get('file_name')
        file_size = request.args.get('file_size')
        file_upload_date = request.args.get('file_upload_date')

        config_array = {}
        config_array["wait_time"] = 1
        config_array["max_allowed_from_one_ip"] = 1
        config_array["mode"] = 1

        public_file_hash = ownstorj_public_file_sharing_manager.generate_public_file_hash(
            input_string=bucket_id+"_"+file_id+file_name+file_size+file_upload_date)

        ownstorj_public_file_sharing_manager.save_public_file_to_db(bucket_id, file_id, public_file_hash, public_file_hash,
                                                                    config_array, file_size, file_name, file_upload_date)

        return '{result: "success"}', 200  # return the HTTP 200 statuss code - OK
    else:
        return '{result: "unauthorized"}', 401

@app.route('/insert_file_to_playlist/<file_local_public_hash>/<playlist_id>')
def insert_file_to_playlist_endpoint(file_local_public_hash, playlist_id):
    initSession()

    ownstorj_playlist_manager = OwnStorjPlaylistManager()
    ownstorj_public_file_sharing_manager = OwnStorjPublicFileSharingManager()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        if file_local_public_hash != "":
            public_file_details = ownstorj_public_file_sharing_manager.get_public_file_details_by_local_hash(file_local_public_hash)
            ownstorj_playlist_manager.insert_track(track_name=public_file_details[0]["file_name"]
                                                   , track_local_file_id=file_local_public_hash
                                                   , playlist_id=playlist_id)

        return '{result: "success"}', 200  # return the HTTP 200 statuss code - OK
    else:
        return '{result: "unauthorized"}', 401

@app.route('/download_playlist_export_file/<playlist_id>/<export_file_type>')
def download_playlist_export_file_endpoint(playlist_id, export_file_type):
    initSession()

    ownstorj_playlist_manager = OwnStorjPlaylistManager()

    if session['logged_in'] or (request.remote_addr == "127.0.0.1" and can_login_local_without_auth()):
        if playlist_id != "" and export_file_type != "":
            playlist_export_file_content = ownstorj_playlist_manager.generate_playlist_export_file(
                file_type=export_file_type,
                playlist_id=playlist_id,
                ownstorj_source_address="http://localhost:5000")

            playlist_data = ownstorj_playlist_manager.get_playlist_details(playlist_id)

            response = make_response(playlist_export_file_content)
            response.headers["Content-Disposition"] = "attachment; filename=" + playlist_data['name'] + "." + str(export_file_type)

            return response, 200  # return the HTTP 200 statuss code - OK

        else:
            return '{result: "missing_arguments"}', 503

    else:
        return '{result: "unauthorized"}', 401

# SOCKET.IO HANDLERS
#
#@socketio.on('connect')
#def handle_message():
#    print('received message: ' )

#@socketio.on('my event')
#def handle_my_custom_event(json):
#    print('received json: ' + str(json))















