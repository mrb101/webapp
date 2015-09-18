from flask.ext.wtf import Form
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email


class LoginForm(Form):
    email = StringField('Email', validators=[Required(), Length(1, 255), Email()])
    password = PasswordField('Password', validators=[Required()])
    submit = SubmitField('Sign In')
