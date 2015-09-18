from flask import render_template
from . import auth
from .forms import LoginForm

@auth.route('/signin', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        pass
    return render_template('auth/signin.html', form=form)


@auth.route('/signup')
def sugnup():
    return render_template('auth/signup.html')
