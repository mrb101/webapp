from flask import render_template
from . import notifications


@notifications.route('/notifications')
def notifications():
    return render_template('pages/index.html')
