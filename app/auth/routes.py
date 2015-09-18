from flask import render_template, request, redirect, url_for, flash
from . import auth
from .forms import LoginForm
from ..models import User
from flask.ext.login import login_user

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user is None or not user.verify_passowrd(form.password.data):
            flash('Invalid email or password.')
            return redirect(url_for('auth.login'))
        login_user(user, form.remember_me.data)
        return redirect(request.args.get('next') or url_for('auth.register'))
    return render_template('auth/login.html', form=form)


@auth.route('/register')
def register):
    from = RegisterForm()
    if form.validate_on_submit():
        user = User(
                name = form.name.data,
                user_name = form.user_name.data,
                email = form.email.data,
                password = form.password.data,
                )
        return 'gotcha ya'
    return render_template('auth/register.html')
