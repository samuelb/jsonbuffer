#! /usr/bin/env python

import os
import json
from flask import Flask, request, Response, abort
from .datastore import DataStore


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)

    #app.config.from_mapping(
    #    SECRET_KEY='dev',
    #    DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    #)

    #if test_config is None:
    #    # load the instance config, if it exists, when not testing
    #    app.config.from_pyfile('config.py', silent=True)
    #else:
    #    # load the test config if passed in
    #    app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    ds = DataStore()

    @app.route('/', defaults={'path': ''}, methods=['GET'])
    @app.route('/<path:path>', methods=['GET'])
    def get_data(path):
        try:
            d = ds.get(path)
            return Response(json.dumps(d), mimetype='application/json')
        except KeyError:
            abort(404)

    @app.route('/', defaults={'path': ''}, methods=['PUT', 'POST'])
    @app.route('/<path:path>', methods=['PUT', 'POST'])
    def update_data(path):
        try:
            d = request.get_json(force=True)
            ds.set(d, path)
            return 'OK'
        except KeyError:
            abort(404)

    return app
