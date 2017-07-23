from ownstorj import app
import optparse

def flaskrun(default_host="localhost",
                  default_port="5000"):

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

    app.run(
        debug=options.debug,
        host=options.host,
        port=int(options.port),
        threaded=True
    )


if __name__ == '__main__':
    flaskrun()
