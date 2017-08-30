
from ownstorj import app
import optparse
from OpenSSL import SSL
from UI.utilities.backend_config import Configuration

storj_gui_config_manager = Configuration()

ownstorj_port_settings = storj_gui_config_manager.get_config_parametr_value("ownstorj_port")

if ownstorj_port_settings == False:
    ownstorj_port_settings = "5000"

def flaskrun(default_host="0.0.0.0",
                  default_port=str(ownstorj_port_settings)):

    parser = optparse.OptionParser()
    parser.add_option("-H", "--host",
                      help="Hostname/IP of OwnStorj " + \
                           "[default %s]" % default_host,
                      default=default_host)
    parser.add_option("-P", "--port",
                      help="Port for the OwnStorj " + \
                           "[default %s]" % default_port,
                      default=default_port)
    parser.add_option("-d", "--debug",
                      action="store_true", dest="debug",
                      help=optparse.SUPPRESS_HELP)

    options, _ = parser.parse_args()

    try:
        context = SSL.Context(SSL.SSLv23_METHOD)
        #context.use_privatekey_file('server.key')
        #context.use_certificate_file('server.crt')
    except BaseException as e:
        print e

    app.run(
        debug=options.debug,
        host=options.host,
        port=int(options.port),
        threaded=True
    )


class OwnStorjFlaskServer():
    def run(self):
        flaskrun()

if __name__ == '__main__':
    flaskrun()
