#!/usr/bin/env python
import os
from app import create_app, db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
manager = Manager(app)


manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
