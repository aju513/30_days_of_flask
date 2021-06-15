from models import app
from flask import flash,render_template,redirect
from models.forms import LoginForm,RegistrationForm
from models.data import User 
from models import db,bcrypt
from flask_login import current_user,login_user
@app.route("/home")
def hello_world():
	return render_template('homepage.html')
@app.route('/register',methods=['POST','GET'])
def registration():
	if current_user.is_authenticated:
		return redirect('/home')
	form=RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password1.data).decode('utf-8')
		user=User(username=form.username.data,password=hashed_password,email=form.email.data)
		db.session.add(user)
		db.session.commit()
		print("use")
		flash(f'Account created succesfully','success')
		return redirect('/home')
	else:
		return render_template('registration.html',form=form)
@app.route('/login',methods=['POST','GET'])
def login():
	# if current_user.is_authenticated:
	# 	return redirect('/home')

	form1=LoginForm()
	if form1.validate_on_submit():
		user=User.query.filter_by(email=form1.email.data).first()

		if user and bcrypt.check_password_hash(user.password, form1.password.data) :
			login_user(user,remember=form1.remember.data)
			flash(f' You are logged in as {user.username}!', 'success')
			return redirect('/home')
		else:
			flash('there was an error')	
			
	
	return render_template('login.html',form1=form1)	
