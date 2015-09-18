# Flask Imports
from flask import render_template


# Blueprint imports
from . import _module


# Define routes
@_module.route('/')
def index():
    return render_template('_module/index.html')
