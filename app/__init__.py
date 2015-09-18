# flask imports
from flask import Flask
from config import config

# Other imports

"""
- to add extension:
    1- Import the extiention
    2- create an instance of it
    3- instantiate the extension
"""

# Bootstrap
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy

# Create the instance of the extension
bootstrap = Bootstrap()
db = SQLAlchemy()

# models file is imported here. "Circuler dependences hell"
from app import models

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # instantiate the extension
    bootstrap.init_app(app)
    db.init_app(app)


    """
    - Register Blueprints
        1- First create the _module folder
        2- Create _module/__init__.py and
        3- Define the the blue prnt in it
        4- Then register bellow

    example:

    from ._module import _module as _module_blueprint
    app.register_blueprint(_module_blueprint, url_prefix='/_module')
    """

    from ._module import _module as _module_blueprint
    app.register_blueprint(_module_blueprint, url_prefix='/_module')

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix='/auth')

    return app
