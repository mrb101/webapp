from flask import render_template
from . import notifications


@notifications.route('/notification')
def index():
    return render_template('pages/index.html')
