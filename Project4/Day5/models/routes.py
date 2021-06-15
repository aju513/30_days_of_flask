from models import app
from flask import flash,render_template,redirect
from models.forms import LoginForm,RegistrationForm
from models.data import User
from models import db,bcrypt
@app.route("/")
def hello_world():
	return render_template('homepage.html')
@app.route('/register1',methods=['POST','GET'])
def registration():
	form=RegistrationForm()
	if form.validate_on_submit():
		hashed_password = bcrypt.generate_password_hash(form.password1.data).decode('utf-8')
		user=User(username=form.username.data,password=hashed_password,email=form.email.data)
		db.session.add(user)
		db.session.commit()
		print("use")
		flash(f'Account created succesfully','success')
		return redirect('/')
	else:
		return render_template('registration.html',form=form)
@app.route('/login',methods=['POST','GET'])
def login():
	form1=LoginForm()
	if form1.validate_on_submit():
		user=User.query.filter_by(email=form1.email.data)

		if user and bcrypt.check_password_hash(user.password, form1.password.data) :
			flash(f' You are logged in as {form1.email.data}!', 'success')
			return redirect('/')
		else:
			flash('there was an error')	
			return redirect('/login')
	else:
		return render_template('login.html',form1=form1)	
