# Storj GUI Client
GUI Client for Storj Distributed Storage Network written in Python and PyQt4. This app finally will work on most desktop platforms: Linux, Windows, Mac OS X. Very early alpha dev version, we are working on download and uploads, but others functions like buckets, file managing, mirrors listing have been implemented

# How to run (Alpha version)
- Clone newest version of python-sdk: `git clone https://github.com/Storj/storj-python-sdk.git`
- `cd storj-python-sdk`
- `python setup.py install`
- `cd ..`
- `git clone https://github.com/lakewik/storj-gui-client.git`
- `cd storj-gui-client`
- install PyQt4 (`sudo apt-get install python-qt4` for Debian and Ubuntu). In
  case you want to use a Virtual Environment, [a few more steps are
  required](https://gist.github.com/marcorosa/73c72f0315fa7098315c8b0774414ad6)
- install python requirements: `pip install -r requirements.txt`
- execute: `python main.py`

# Software features:
- [x] list buckets
- [x] create buckets
- [x] register user 
- [x] list files in buckets
- [ ] upload file &nbsp; &nbsp; ![test](http://progressed.io/bar/95)
- [ ] download file &nbsp; &nbsp; ![test](http://progressed.io/bar/95)
- [x] list file pointers
- [x] list file mirrors
- [x] manage buckets
- [ ] advanced configuration and bandwidth limiting &nbsp; &nbsp; ![test](http://progressed.io/bar/10)
- [x] specified farmer node details

# Planned features:
- multilipe file upload
- analyzing geodistribution of nodes, mirrors
- file syncing

# Support
You can submit issue (feature request), if you want implementation of a feature that haven't been yet implemented or planned. If you find any bugs in this app, please submit issue or a pull request containing a fix. Please note that this software is currently in Alpha Version. Also I accept donations in SJCX, BTC: 1LWMe1AuQSNQq6zUEtC8vMaV3LhS8r1uFw , Monero (XMR): 42VP4x4CRtwf9PXD3J73ntQHb2f2BYHVR75ovjeSNWzRF4X34mdf367VWD74kD4zDT3ReY6t5uQxAC9FWCPnMQjpQ3xFsV9.  
# Thank you very much for your support!

