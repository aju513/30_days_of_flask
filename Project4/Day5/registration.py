from flask_wtf import FlaskForm
from flask_wtf.recaptcha import validators
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Length

class RegistrationForm(FlaskForm):
	username = StringField('Usernmae',validators=[DataRequired(), Length(min=2,max=20)])
	email =StringField('Email',validators=[DataRequired()])
	password1 =PasswordField('Password',validators=[DataRequired()])
	password2 =PasswordField('Password',validators=[DataRequired()])
	
	submit =SubmitField('Go')