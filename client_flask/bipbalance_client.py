#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, render_template
from flask.ext.compress import Compress
from werkzeug.routing import BaseConverter
from blueprints import home_blueprint
from common import config
from common.utils import cache
import common.log as log


bipbalance_client = Flask(__name__)
bipbalance_client.secret_key = config.SECRET_KEY

class RegexConverter(BaseConverter):
    def __init__(self, url_map, *items):
        super(RegexConverter, self).__init__(url_map)
        self.regex = items[0]

# Use the RegexConverter function as a converter
# method for mapped urls
bipbalance_client.url_map.converters['regex'] = RegexConverter

bipbalance_client.register_blueprint(home_blueprint.page)

Compress(bipbalance_client)
cache.init_app(bipbalance_client)

@bipbalance_client.errorhandler(404)
def page_not_found(e):
    g.config = config
    return render_template('404.html'), 404

@bipbalance_client.errorhandler(500)
def page_not_found(e):
    g.config = config
    return render_template('500.html'), 500


def gevent():
    from gevent.wsgi import WSGIServer

    bipbalance_client.logger.info("Running Gevent on port %s", config.port)

    http_server = WSGIServer(('', config.port), bipbalance_client)
    http_server.serve_forever()


def tornado():
    from tornado.wsgi import WSGIContainer
    from tornado.httpserver import HTTPServer
    from tornado.ioloop import IOLoop

    bipbalance_client.logger.info("Running Tornado on port %s", config.port)

    http_server = HTTPServer(WSGIContainer(bipbalance_client))
    http_server.listen(config.port)
    IOLoop.instance().start()


def builtin():
    bipbalance_client.logger.info("Running Built-in development server on port %s", config.port)
    bipbalance_client.run(host="0.0.0.0", port=config.port, debug=config.debug)


def start_server():
    bipbalance_client.logger.info("Parsing options ...")
    #Command Arguments parser and help generator
    from optparse import OptionParser

    _cmd_parser = OptionParser(usage="usage: %prog [options]", version="BIP Balance Client {0}".format("0.1"))
    _opt = _cmd_parser.add_option
    _opt("--debug", action="store_true", help="Debug Mode.")
    _opt("--tornado", action="store_true", help="Tornado non-blocking web server.")
    _opt("--gevent", action="store_true", help="Gevent non-blocking web server.")
    _opt("--gunicorn", action="store_true", help="Gevent non-blocking web server.")
    _opt("--builtin", action="store_true", help="Built-in Flask web development server.")
    _opt("--port", help="Port to run")
    _opt("--daemon", action="store_true", help="Daemonize")
    _opt("--start", action="store_true", help="Daemonize")
    _opt("--stop", action="store_true", help="Daemonize")
    _opt("--restart", action="store_true", help="Daemonize")

    _cmd_options, _cmd_args = _cmd_parser.parse_args()

    opt, args, parser = _cmd_options, _cmd_args, _cmd_parser

    if opt.debug:
        config.debug = opt.debug

    if config.debug:
        bipbalance_client.logger.info("DEBUG MODE ON!")

    log.set_logging(bipbalance_client)

    if opt.port:
        config.port = opt.port

    bipbalance_client.logger.info("Starting on port %s", config.port)

    if opt.daemon:
        from daemon import Daemon

        class ServerDaemon(Daemon):
            def run(self):
                if opt.tornado:
                    bipbalance_client.logger.info("WEB SERVER: Using Tornado")
                    tornado()
                elif opt.gevent:
                    bipbalance_client.logger.info("WEB SERVER: Using Gevent")
                    gevent()
                else:
                    bipbalance_client.logger.info("WEB SERVER: Using builtin")
                    builtin()

        daemon = ServerDaemon('/tmp/server-daemon.pid')

        if opt.start:
            daemon.start()
        elif opt.stop:
            daemon.stop()
        elif opt.restart:
            daemon.restart()

    elif opt.tornado:
        bipbalance_client.logger.info("WEB SERVER: Using Tornado")
        tornado()
    elif opt.gunicorn:
        bipbalance_client.logger.info("WEB SERVER: Using gunicorn")
        #gunicorn()
    elif opt.gevent:
        bipbalance_client.logger.info("WEB SERVER: Using Gevent")
        gevent()
    else:
        bipbalance_client.logger.info("WEB SERVER: Using builtin")
        builtin()


if __name__ == "__main__":
    start_server()
