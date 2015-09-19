from flask import render_template, request, redirect, url_for, flash
from . import auth
from .forms import LoginForm
from ..models import User
from flask.ext.login import login_user, logout_user, login_required

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_passowrd(form.password.data):
            flash('Invalid email or password.')
            return redirect(url_for('auth.login'))
        login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('auth.login'))
    return render_template('auth/login.html', form=form)


@auth.route('/logout')
@login_required
def logout():
    logout_user()
    flash('You have successfully logged out!')
    return redirect(url_for('auth.login'))


@auth.route('/register')
def register():
    return render_template('auth/register.html')


@auth.route('/settings')
def settings():
    return render_template('auth/settings.html')


@auth.route('/profile')
def profile():
    return render_template('auth/profile.html')
