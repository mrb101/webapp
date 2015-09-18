#!/usr/bin/env python
import os
from app import create_app, db
from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand


app = create_app(os.getenv('FLASK_CONFIG') or 'default')
migrate = Migrate(app, db)
manager = Manager(app)


manager.add_command('db', MigrateCommand)

@manager.command
def adduser(email, username, admin=False):
    """Register a new User"""
    from getpass import getpass
    password = getpass()
    password2 = getpass(prompt='Confirm: ')
    if password != password2:
        import sys
        sys.exit('Error: Password do not match')
    db.create_all()
    user = User(email=email, password=password, admin=admin)
    db.session.add(user)
    db.session.commit()
    print('User {0} was successfully created'.formate(username))


if __name__ == '__main__':
    manager.run()
