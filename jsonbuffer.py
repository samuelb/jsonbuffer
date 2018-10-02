#! /usr/bin/env python

import json
from flask import Flask, request, Response, abort
from dpath import util as dpath

app = Flask(__name__)

data = {
    'fruits': ['Banana', 'Apple'],
    'burger': ['Double Cheese', 'Whopper'],
    'colors': {
        'Banana': 'yellow',
        'Apple': 'green',
    }
}

@app.route('/', defaults={'path': ''}, methods=['GET'])
@app.route('/<path:path>', methods=['GET'])
def get_data(path):
    d = {}
    if path == '':
        d = data
    else:
        try:
            d = dpath.get(data, path)
        except KeyError:
            abort(404)
    return Response(json.dumps(d), mimetype='application/json')


@app.route('/', defaults={'path': ''}, methods=['PUT', 'POST'])
@app.route('/<path:path>', methods=['PUT', 'POST'])
def update_data(path):
    d = request.get_json(force=True)
    if path == '':
        data = d
    else:
        try:
            dpath.set(data, path, d)
        except KeyError:
            abort(404)
    return 'OK'


if __name__ == '__main__':
    app.run()
