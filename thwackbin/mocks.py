"""
    thwackbin.mocks
    ~~~~~~~~~~~~~~~

    Module contains static mock data returned by the service.
"""
__author__ = 'Andrew Hawker <andrew@appthwack.com>'

from thwackbin import data

def project():
    return [{ "id": 1, "name": "My Project", "url": "my-project"},
            { "id": 2, "name": "Another Project", "url": "another-project"},
            { "id": 64, "name": "Thanks for all the fish", "url": "thanks-for-all-the-fish"},
            { "id": 1023, "name": "Angry Birds", "url": "angry-birds"}]


def devicepool():
    return [{ "id": 1, "name": "Only the Best"},
            { "id": 2, "name": "The Worst"},
            { "id": 15, "name": "The Usual Suspects"},
            { "id": 49, "name": "Tablets"}]


def file_id():
    return dict(file_id=64)


def run_id():
    return dict(run_id=128)


def results():
    return data.RESULTS

if __name__ == '__main__':
    print results()
