"""
    thwackbin.utils
    ~~~~~~~~~~~~~~~

    Contains helper functions for the route handlers.
"""
__author__ = 'Andrew Hawker <andrew@appthwack.com>'

import flask
import json
import os


def jsonify(obj):
    """
    Custom jsonify function to allow returning of lists as the root object.
    """
    return flask.Response(json.dumps(obj), mimetype='application/json')


def valid_ext(filename):
    """
    Validate a file upload is of the correct application type.
    """
    return os.path.splitext(filename)[1] in ['.apk', '.ipa', '.zip']
