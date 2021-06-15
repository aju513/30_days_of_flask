from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField
from wtforms.validators import DataRequired,Length,ValidationError,EqualTo
from models.data import User

class RegistrationForm(FlaskForm):
	username = StringField('Usernmae',validators=[DataRequired(), Length(min=2,max=20)])
	email =StringField('Email',validators=[DataRequired()])
	password1 =PasswordField('Password',validators=[DataRequired(),Length(min=8,max=20)])
	password2 =PasswordField('Password',validators=[DataRequired(),Length(min=8,max=20),EqualTo('password1')],)
	submit =SubmitField('Go')


	def validate_username(self,username):
		user = User.query.filter_by(username=username.data).first()
		if user:
			raise ValidationError('That username is taken. Please choose a different one.')

	def validate_email(self,email):
		user = User.query.filter_by(email=email.data).first()
		if user:
			raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
	email = StringField('Email',validators=[DataRequired(),Length(min=8,max=20)])
	password1 = PasswordField('Password',validators=[DataRequired(),Length(min=8,max=20)])
	submit = SubmitField('Go')