"""
    thwackbin.data
    ~~~~~~~~~~~~~~

    Package which contains mock results data stored on the file system.
"""
__author__ = 'Andrew Hawker <andrew@appthwack.com>'

import json
import os

RESULTS = None
ROOT = os.path.dirname(__file__)

def init():
    """
    Load and cache our results.json data on startup.
    """
    global RESULTS
    RESULTS = json.load(open(os.path.join(ROOT, 'results.json')))
