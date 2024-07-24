from flask_wtf import FlaskForm
from wtforms import (StringField, 
                     SelectField,
                     DateField,
                     PasswordField, 
                     SubmitField,
                     BooleanField)

from wtforms.validators import (
    DataRequired,
    Length,
    Email,
    Optional,
    EqualTo
)

class Signup(FlaskForm):
    username = StringField('Username',
                           validators=[DataRequired(), Length(2, 20, 'Username must be between 2 and 20 characters')])
    email = StringField('Email',
                        validators=[DataRequired(), Email('Invalid email')])
    gender = SelectField(
        'gender',
        choices=["Male", "Female", "Other"],
        validators=[Optional()])
    dob = DateField(
        "Date of Birth",
        validators=[Optional()])
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(6, 20, 'Password must be between 6 and 20 characters')])
    confirm_password = PasswordField(
        'Confirm Password',
        validators=[DataRequired(), EqualTo('password', 'Passwords must match')])
    submit = SubmitField('Sign Up')

class Login(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email('Invalid email')])
    password = PasswordField(
        'Password',
        validators=[DataRequired(), Length(6, 20, 'Password must be between 6 and 20 characters')])
    remember_me = BooleanField(
        'Remember Me')
    submit = SubmitField('Log in')
    