#!/usr/bin/env python
# -*- coding: utf-8 -*-
import inspect

from flask import session, request
from flask.ext.cache import Cache
from common.config import CACHE_CONFIG, APP_PATH


def sort_dict(undecorated, sort_on, desc=False):
    decorated = [(dict_[sort_on], dict_) for dict_ in undecorated]
    decorated.sort()

    if desc:
        decorated = reversed(decorated)

    return [dict_ for (key, dict_) in decorated]


cache = Cache(config=CACHE_CONFIG)

__path = {}

def get_fingerprint():
    try:
        fingerprint = request.args['fingerprint']
    except:
        try:
            fingerprint = request.form['fingerprint']
        except:
            return False

    return fingerprint


def set_url_path(url_path):
    __path["url"] = url_path


def get_app_path():
    return APP_PATH

def map_object(source, destination, routines=False):
    attributes = inspect.getmembers(source, lambda a: not (inspect.isroutine(a)))
    attributes = [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]

    for attribute in attributes:
        setattr(destination, attribute[0], getattr(source, attribute[0]))

    if routines:
        attributes = inspect.getmembers(source, lambda a: inspect.isroutine(a))
        attributes = [a for a in attributes if not (a[0].startswith('__') and a[0].endswith('__'))]

    for attribute in attributes:
        setattr(destination, attribute[0], getattr(source, attribute[0]))

    return destination


def props(obj):
    pr = {}
    for name in dir(obj):
        value = getattr(obj, name)
        if not name.startswith('__') and not inspect.ismethod(value):
            pr[name] = value
    return pr


def str2js(string, as_array=False):
    lines = string.split("\n")

    if as_array:
        return "[\"{0}\"].join(' ')".format("\",\"".join(lines))

    return " ".join(lines)

def indexed_dict(dict_object=None, index_name=None):
    if not dict_object is None and not index_name is None:
        indexed_obj = dict()
        for obj_row in dict_object:
            indexed_obj[obj_row[index_name]] = obj_row
        return indexed_obj
    return None


def dict_not_empty(dictionary):
    for k in dictionary:
        return True
    return False


def str_to_bool(string=None):
    if not string is None:
        if string.lower() == 'true':
            return True
        elif string.lower() == 'false':
            return False


def get_insert_into_from_dict(data=None):
    sql_indexes = ""
    sql_values = ""
    sql_params = []
    if not data is None:
        for field_index, field_value in data.iteritems():
            sql_indexes += str(field_index) + ", "
            sql_values += "%s, "
            sql_params.append(field_value)
            #delete ", " for the last field
        sql_indexes = sql_indexes.rstrip(', ')
        sql_values = sql_values.rstrip(', ')

        sql_query = "INSERT INTO #table# (" + sql_indexes + ") VALUES (" + sql_values + ")"
        return sql_query, sql_params


def get_update_from_dict(data=None, id_for_where=None, id_index='id'):
    sql_query = "UPDATE #table# SET "
    sql_params = []

    for field_index, field_value in data.iteritems():
        sql_query += str(field_index) + "=%s, "
        sql_params.append(field_value)
        #delete ", " for the last field
    sql_query = sql_query.rstrip(', ')
    sql_query += " WHERE {0}=%s".format(id_index)
    sql_params.append(id_for_where)

    return sql_query, sql_params

