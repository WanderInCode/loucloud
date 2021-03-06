# -*- coding: utf-8 -*-

import os

class DefaultConfig(object):

    # PROJECT = "loucloud"

    # DEBUG = False
    # TESTING = False

    # http://flask.pocoo.org/docs/quickstart/#sessions
    SECRET_KEY = "~!@@#@WERW"

    # Flask-Sqlalchemy: http://packages.python.org/Flask-SQLAlchemy/config.html
    SQLALCHEMY_ECHO = True
    # MYSQL for production.
    #SQLALCHEMY_DATABASE_URI = 'mysql://username:password@server/db?charset=utf8'
    SQLALCHEMY_DATABASE_URI = "mysql://lc:1qaz@localhost/lc"

    # Flask-cache: http://pythonhosted.org/Flask-Cache/
    CACHE_TYPE = 'simple'
    CACHE_DEFAULT_TIMEOUT = 60
 