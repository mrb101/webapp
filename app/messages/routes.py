from flask import render_template
from . import messages


@messages.route('/messages')
def inbox():
    return render_template('messages/index.html')
