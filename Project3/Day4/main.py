from flask import Flask,render_template
from api import Crypto
from api2 import GlobalStats
app=Flask(__name__)

globaldata=GlobalStats()
crypto=Crypto()

@app.route('/')
def homepage():
    crypto_data=crypto.get_all()
    global_data = globaldata.getGlobalstats()
    return render_template('homepage.html',global_data=global_data,crypto_data=crypto_data)


if __name__=="__main__":
    app.run(debug=True)
