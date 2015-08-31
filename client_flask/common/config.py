#!/usr/bin/env python
# -*- coding: utf-8 -*-

from os.path import dirname, realpath

APP_PATH = dirname(realpath(__file__)).rstrip("/common")
CACHE_CONFIG={'CACHE_TYPE': 'simple'}
COOKIE_DOMAIN = "127.0.0.1"
SECRET_KEY = 'zMZ9AXr6R6qXs6ifl8MZE66ha6ITheHY'

JS_COMPONENTS = {

}

port = 8888
debug = True
log_filename = "bipbalance_client.log"
