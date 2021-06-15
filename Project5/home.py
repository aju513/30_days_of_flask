from flask import Flask,render_template
from flask.templating import render_template
from random import randint
app=Flask(__name__)

@app.route('/')
def home():
      value=randint(1,4)
      
      quotes= ["“The purpose of our lives is to be happy.” — Dalai Lama",

" “Life is what happens when you’re busy making other plans.” — John Lennon",

 "“Get busy living or get busy dying.” — Stephen King",

 "“You only live once, but if you do it right, once is enough.” — Mae West",

" “Many of life’s failures are people who did not realize how close they were to success when they gave up.”– Thomas A. Edison"]
      return render_template('home.html',quotes=quotes[value],value=str(value)) 
      
if __name__=="__main__":
       app.run(debug=True)
