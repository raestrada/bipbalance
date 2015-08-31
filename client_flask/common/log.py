#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import logging
from common import config as Config


def set_logging(app):
    ADMINS = ['dev@bipbalance.com']

    if Config.debug:
        from logging import StreamHandler

        file_handler = StreamHandler(sys.stdout)
        file_handler.setLevel(logging.DEBUG)

        from logging import Formatter

        file_handler.setFormatter(Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'
        ))

        app.logger.addHandler(file_handler)
        app.logger.setLevel(logging.DEBUG)

    else:

        from logging.handlers import SMTPHandler

        mail_handler = SMTPHandler('127.0.0.1',
                                   'server-error@example.com',
                                   ADMINS, 'YourApplication Failed')
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)

        file_handler = logging.FileHandler(Config.log_filename, mode='a', encoding=None, delay=False)
        file_handler.setLevel(logging.WARNING)

        from logging import Formatter

        file_handler.setFormatter(Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'
        ))

        app.logger.addHandler(file_handler)

        app.logger.setLevel(logging.ERROR)

__logger = None

def logger():
    global __logger

    if not __logger is None:
        return __logger

    ADMINS = ['dev@bipbalance.com']

    __logger = logging.getLogger('bipbalance')

    if True:
        from logging import StreamHandler

        file_handler = StreamHandler(sys.stdout)
        file_handler.setLevel(logging.DEBUG)

        from logging import Formatter

        file_handler.setFormatter(Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'
        ))

        __logger.addHandler(file_handler)
        __logger.setLevel(logging.DEBUG)

    else:

        from logging.handlers import SMTPHandler

        mail_handler = SMTPHandler('127.0.0.1',
                                   'server-error@example.com',
                                   ADMINS, 'YourApplication Failed')
        mail_handler.setLevel(logging.ERROR)
        __logger.addHandler(mail_handler)

        file_handler = logging.FileHandler(Config.log_filename, mode='a', encoding=None, delay=False)
        file_handler.setLevel(logging.WARNING)

        from logging import Formatter

        file_handler.setFormatter(Formatter(
            '%(asctime)s %(levelname)s: %(message)s '
            '[in %(pathname)s:%(lineno)d]'
        ))

        __logger.addHandler(file_handler)
        __logger.setLevel(logging.ERROR)

    return __logger