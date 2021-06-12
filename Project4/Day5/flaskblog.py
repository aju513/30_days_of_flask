from flask import Flask,render_template,redirect
from registration import RegistrationForm 

app = Flask(__name__)
app.config['SECRET_KEY']='aju'

@app.route("/")
def hello_world():
	return render_template('homepage.html')
@app.route('/register',methods=['POST','GET'])
def registration():
	form=RegistrationForm()
	if form.validate_on_submit():
		return redirect('/')
	else:
		return render_template('registration.html',form=form)

if __name__=="__main__":
	app.run(debug=True)
