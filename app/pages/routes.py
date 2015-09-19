from flask import render_template
from . import pages


@pages.route('/webstore')
def webstore():
    return render_template('pages/webstore.html')


@pages.route('/marketplacesync')
def marketplacesync():
    return render_template('pages/marketplacesync.html')


@pages.route('/pricing')
def pricing():
    return render_template('pages/pricing.html')
