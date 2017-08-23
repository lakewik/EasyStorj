import collections
import socket
from threading import Thread

from ipwhois import IPWhois

from ...ownstorj import app
# from ...ownstorj import socketio

from ...ownstorj.models.buckets import OwnStorjBuckets
from ...ownstorj.models.files import OwnStorjFilesManager
from ...ownstorj.models.download import OwnStorjDownloadEngine
from ...ownstorj.models.public_sharing_manager import OwnStorjPublicFileSharingManager
from ...ownstorj.models.node import OwnStorjNodeDetails
from ...ownstorj.models.mirrors import OwnStorjMirrors
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


def initSession():
    try:
        session['counter'] += 1
    except KeyError:
        session['counter'] = 1
    try:
        a = session['logged_in']
    except BaseException:
        session['logged_in'] = False


def generate_menus_data():
    user_email = storj_account_manager.get_user_email()
    menus_data = {}
    menus_data["account_name"] = user_email
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
    if session['logged_in']:
        return render_template('dashboard.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/buckets_list', defaults={'reinfo': None})
@app.route('/buckets_list/<reinfo>')
def buckets_list_view(reinfo):
    initSession()
    if session['logged_in']:
        if reinfo is None:
            reinfo = ""

        if reinfo == "bucket_created":
            reinfo = "bucket_created"

        return render_template('buckets_list_manager.html', menu_data=generate_menus_data(), reinfo=reinfo)
    else:
        return make_response(redirect("/login"))


@app.route('/buckets_list_table')
def buckets_list_table():
    initSession()

    if session['logged_in']:
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

    if session['logged_in']:
        if reinfo is None:
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
def files_manager_view(bucket_id):
    initSession()

    if session['logged_in']:
        if bucket_id is not None:
            bucket_name = OwnStorjBucketsManager.get_bucket_name(bucket_id=bucket_id)
            return render_template('files_manager.html', menu_data=generate_menus_data(), bucket_id=bucket_id,
                                   bucket_name=bucket_name)
        else:
            return redirect("/buckets_list", 301)
    else:
        return make_response(redirect("/login"))


@app.route('/files_table/<bucket_id>')
def files_table_view(bucket_id):
    initSession()

    if session['logged_in']:
        files_manager = OwnStorjFilesManager(str(bucket_id))
        files_list = files_manager.get_files_list()
        # for file in files_list:
        # print file["size"]
        return render_template('files_table.html', files_list=files_list, bucket_id=bucket_id)
    else:
        return make_response(redirect("/login"))


@app.route('/settings')
def settings_view():
    initSession()

    if session['logged_in']:
        return render_template('settings.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/sync_settings')
def sync_settings_view():
    initSession()

    if session['logged_in']:
        return render_template('sync_settings.html',
                               menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/sync_statistics')
def sync_statistics_view():
    initSession()

    if session['logged_in']:
        return render_template('sync_statistics.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/tags_labels_manager')
def tags_labels_manager_view():
    initSession()

    if session['logged_in']:
        return render_template('tags_labels_manager.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/single_file_upload')
def upload_view():
    initSession()

    if session['logged_in']:
        return render_template('single_file_upload.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/single_file_download')
def download_view():
    initSession()

    if session['logged_in']:
        return render_template('single_file_download.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/favorites')
def favorites_view():
    initSession()

    if session['logged_in']:
        return render_template('favorites.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/file_mirrors/<filebucket_id>')
def file_mirrors_view(filebucket_id):
    initSession()

    if session['logged_in']:
        return render_template('file_mirrors.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/established_file_mirrors/<filebucket_id>')
def established_mirrors_view(filebucket_id):
    initSession()

    if session['logged_in']:
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
        i = 0

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
        print i
        print ownstorj_mirrors.calculate_geodistribution(countries_array=countries_codes_list)

        return render_template('established_mirrors_data.html',
                               table_break_positions=table_break_positions,
                               established_mirrors_shards_count=established_mirrors_shards_count,
                               mirrors_data=mirrors_data,
                               mirrors_data_2=mirrors_data_2,
                               established_mirrors_total_nodes_count=established_mirrors_total_nodes_count,
                               country_codes_array=country_codes_array)
    else:
        return make_response(redirect("/login"))


@app.route('/available_file_mirrors/<filebucket_id>')
def available_mirrors_view(filebucket_id):
    initSession()

    if session['logged_in']:
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
        i = 0

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

        return render_template('available_mirrors_data.html',
                               table_break_positions=table_break_positions,
                               available_mirrors_shards_count=available_mirrors_shards_count,
                               mirrors_data=mirrors_data,
                               mirrors_data_2=mirrors_data_2,
                               available_mirrors_total_nodes_count=available_mirrors_total_nodes_count,
                               country_codes_array=country_codes_array)
    else:
        return make_response(redirect("/login"))


@app.route('/mirrors_geodistribution/<filebucket_id>')
def mirrors_geodistribution_view(filebucket_id):
    initSession()

    if session['logged_in']:
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


def whois_lookup_country(address):
    IP_addr = socket.gethostbyname(str(address))
    obj = IPWhois(IP_addr)
    res = obj.lookup_whois()
    country = res["nets"][0]['country']

    return country


@app.route('/node_details', methods=['GET'])
# @app.route('/node_details?nodeID=<nodeID>')
def node_details_view():
    initSession()

    if session['logged_in']:
        return render_template('node_details.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/node_details_data/<nodeID>')
def node_details_data_view(nodeID):
    initSession()

    if session['logged_in']:
        ownstorj_node_details = OwnStorjNodeDetails()
        node_details_array = ownstorj_node_details.node_details(nodeID)
        return render_template('node_details_data.html', node_details_array=node_details_array)
    else:
        return make_response(redirect("/login"))


@app.route('/contract_details')
def contract_details_view():
    initSession()

    if session['logged_in']:
        return render_template('contract_details.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/billing')
def billing_view():
    initSession()

    if session['logged_in']:
        return render_template('billing.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


@app.route('/account_stats')
def account_stats_view():
    initSession()

    if session['logged_in']:
        return render_template('account_stats.html', menu_data=generate_menus_data())
    else:
        return make_response(redirect("/login"))


# Public Download Gateway
@app.route('/public_download_gateway/<download_id>')
def public_download_gateway_endpoint(download_id):
    public_file_sharing_manager = OwnStorjPublicFileSharingManager()
    download_indicators = public_file_sharing_manager.get_public_download_indicators(public_download_hash_url=download_id)

    pointer = OwnStorjDownloadEngine.get_pointer_for_single_shard_download(
        bucket_id="ef92512a30fab77facaf334a", file_id="3deb3890a445279c648d17a0")
    ready_farmer_url = 'http://%s:%s/shards/%s?token=%s' % (
        pointer.get('farmer')['address'],
        str(pointer.get('farmer')['port']),
        pointer['hash'],
        pointer['token'])

    return redirect(ready_farmer_url)


# actions handling
@app.route('/buckets/new', methods=['POST'])
def add_bucket():
    initSession()

    if session['logged_in']:
        bucket_name = None
        success = False
        if request.method == 'POST':
            bucket_name = request.form['bucket_name']
        print bucket_name

        if bucket_name is not None:
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


@app.route('/synchronization/settings/save', methods=['POST'])
def save_sync_settings():
    initSession()

    if session['logged_in']:
        if request.method == 'POST':
            bucket_name = request.form['bucket_name']

        response = make_response(redirect("/bucket_add"))

        return response
    else:
        return make_response(redirect("/login"))



# SOCKET.IO HANDLERS
#
#@socketio.on('connect')
#def handle_message():
#    print('received message: ' )

#@socketio.on('my event')
#def handle_my_custom_event(json):
#    print('received json: ' + str(json))















