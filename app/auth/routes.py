from flask import render_template, request, redirect, url_for, flash
from . import auth
from .forms import LoginForm, ProfileForm
from ..models import User
from flask.ext.login import login_user, logout_user, login_required, current_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_passowrd(form.password.data):
            flash('Invalid email or password.')
            return redirect(url_for('auth.login'))
        login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('auth.profile'))
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


@auth.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = ProfileForm()
    if form.validate_on_submit():
        current_user.name = form.name.data
        current_user.user_name = form.name.data
        current_user.email = form.email.data
        current_user.bio = form.bio.data
        db.session.add(current_user._get_current_object())
        db.session.commit()
        flash('Your profile has been updated successfully!')
        return redirect(url_for('auth.profile', user_name=current_user.user_name))
    form.name.data = current_user.name
    form.user_name.data = current_user.user_name
    form.email.data = current_user.email
    form.bio.data = current_user.bio
    return render_template('auth/profile.html', form=form)
