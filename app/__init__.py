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

# Importing Extensions
from flask.ext.bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.login import LoginManager

# Create the instance of the extension
bootstrap = Bootstrap()
db = SQLAlchemy()
login_manager = LoginManager()
login_manager.login_view = 'auth.login'

# models file is imported here. "Circuler dependences hell"
from app import models

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    # instantiate the extension
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)


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

    from .pages import pages as pages_blueprint
    app.register_blueprint(pages_blueprint, url_prefix='/services')

    from .messages import messages as messages_blueprint
    app.register_blueprint(messages_blueprint, url_prefix='/messages')

    from .notifications import notifications as notifications_blueprint
    app.register_blueprint(notifications_blueprint, url_prefix='/notifications')

    from .inventory import inventory as inventory_blueprint
    app.register_blueprint(inventory_blueprint, url_prefix='/inventory')

    return app
