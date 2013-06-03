thwackbin
=========

HTTP request/response test service exposing the AppThwack REST API.

## Goals

* Easy to use.
* Allow developers to quickly create, test and integrate AppThwack clients into their environment.

## Usage

thwackbin is currently located at the [thwackbin.herokuapp.com](http://thwackbin.herokuapp.com) domain.

### Authentication

* thwackbin uses HTTP basic auth where the username is the API key and password is empty.
* thwackbin uses the glocal API KEY: **DTOZZNWeCNWFWtuqqJEm14nnonVJMDXA9flmdvzg** to authorize all requests.

### Examples

Get all projects:
```bash
    $ curl -X GET -u "DTOZZNWeCNWFWtuqqJEm14nnonVJMDXA9flmdvzg:" http://thwackbin.herokuapp.com/api/project
    >> [{"url": "my-project", "id": 1, "name": "My Project"}, 
    {"url": "another-project", "id": 2, "name": "Another Project"}, 
    {"url": "thanks-for-all-the-fish", "id": 64, "name": "Thanks for all the fish"}, 
    {"url": "angry-birds", "id": 1023, "name": "Angry Birds"}] 
```

## Documentation

thwackbin documentation can be found [here]().  
AppThwack API documentation can be found [here](https://appthwack.com/docs/api).

## TODO

* HTTPS redirects.
* Tests & Integration (tox/travis/coveralls).
* Complete deployment.
* Add README examples.
* Documentation (sphinx).