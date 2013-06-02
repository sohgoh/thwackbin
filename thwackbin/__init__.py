"""
    thwackbin
    ~~~~~~~~~

    Thwackbin is an HTTP request/response test service which exposes the AppThwack REST API.
    This service should be used to test/validate clients which wish to consume the actual API endpoint.
"""
__name__ = 'thwackbin'
__version__ = '0.0.1'
__author__ = 'Andrew Hawker <andrew@appthwack.com>'

import flask


def create_app():
    """
    Create the thwackbin WSGI application.
    """
    app = flask.Flask(__name__)

    #Initialize mock data.
    from thwackbin import data
    data.init()

    #Register blueprints.
    from thwackbin import appthwack
    app.register_blueprint(appthwack.api)

    #Patch exc handlers to always return JSON.
    from thwackbin import patch
    app = patch.patch_exception_handlers(app)

    app.config['DOWNLOAD_FOLDER'] = data.ROOT
    return app
