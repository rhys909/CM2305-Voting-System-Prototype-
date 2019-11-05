from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Booleanfield
from wtforms.validators import DataRequired, Length, Email, EqualTo

class registrationForm(FlaskForm):
	#First name and last name have a max length of 50 as the longest first name is 46 characters
    firstName = StringField('First Name', validators=[DataRequired('Please enter your first name'), Length(min=3, max=50)])
	surname = StringField('Surame', validators=[DataRequired('Please enter your last name'), Length(min=3, max=50)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired(), Regexp('^.{6,15}$', message='Your password needs to be between 6 and 15 characters long')])
    passwordVerify = PasswordField('Confirm Your Password', validators=[DataRequired(), EqualTo('password', message='Passwords must match')])
    submit = SubmitField('Sign Up')

    def validEmail(self, email):
        mail = User.query.filter_by(email=email.data).first()
        if mail:
            raise ValidationError('This email is already being used.')

class loginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')

class SubmitVoteForm(FlaskForm):
