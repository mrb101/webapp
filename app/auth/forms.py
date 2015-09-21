from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 255), Email()])
    password = PasswordField('Password', validators=[Required()])
    remember_me = BooleanField('Keep me logged in')
    submit = SubmitField('Sign In')


class RegisterForm(Form):
    name = StringField('Name', validators=[Required(), Length(1, 255)])
    email = StringField('Email', validators=[Required(), Length(1, 255), Email()])
    password = PasswordField('Password', validators=[Required()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Sign In')


class ProfileForm(Form):
    name = StringField('Name', validators=[Required(), Length(1, 255)])
    user_name = StringField('UserName', validators=[Required(), Length(1, 255)])
    email = StringField('Email', validators=[Required(), Length(1, 255), Email()])
    bio = StringField('Bio', validators=[Length(1, 255)])
    submit = SubmitField('Update')
