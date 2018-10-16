import os
import json
from flask import request, Response, abort

from . import app
from .datastore import DataStore

app.logger.debug('LOAD_FROM is %s', app.config.get('LOAD_FROM'))
app.logger.debug('STORE_TO is %s', app.config.get('STORE_TO'))

ds = DataStore(app.config.get('LOAD_FROM'), app.config.get('STORE_TO'))

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

@app.route('/', defaults={'path': ''}, methods=['DELETE'])
@app.route('/<path:path>', methods=['DELETE'])
def delete_data(path):
    try:
        ds.delete(path)
        return 'OK'
    except KeyError:
        abort(404)
