from threading import local
from flask import Flask,render_template,request
from todo import Todo

app = Flask(__name__)


cryto=Todo()
@app.route('/',methods=['POST','GET'])
def homepage():
    if request.method=="POST":
        get_country=request.form["code"]
        fe=cryto.get_5(get_country)
        id=int(fe['main']['temp'])

        return render_template('homepage.html',**locals())
    else:
        return render_template('homepage.html')

if __name__=="__main__":
    app.run(debug=True)