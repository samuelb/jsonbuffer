import os
from flask import Flask

app = Flask(__name__, instance_relative_config=True)

# ensure the instance folder exists
try:
    os.makedirs(app.instance_path)
except OSError:
    pass

app.config.from_object('config')
app.config.from_pyfile('config.py')

from . import controller
