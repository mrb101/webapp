from flask import Blueprint


# Define Blueprint
_module = Blueprint('_module', __name__)


# Import routes at the bottom to avoid circuler dependinces 
from . import routes
