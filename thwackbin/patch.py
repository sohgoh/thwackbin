"""
    thwackbin.patch
    ~~~~~~~~~~~~~~~

    Contains helper methods for patching functionality of the default Flask env.
"""
__author__ = 'Andrew Hawker <andrew@appthwack.com>'

from thwackbin import utils
from werkzeug.exceptions import default_exceptions


def patch_exception_handlers(app):
    """
    Patch the global werkzeug exception handlers to always return JSON responses.
    """
    def jsonify_unhandled_exceptions(e):
        response = utils.jsonify(dict(message=str(e)))
        response.status_code = getattr(e, 'code', 500)
        return response

    for status_code in default_exceptions.keys():
        app.error_handler_spec[None][status_code] = jsonify_unhandled_exceptions

    return app