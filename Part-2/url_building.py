import time
from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to our Home Page!</h1>"

@app.route('/pass/<sname>/<int:smarks>')
def passed(sname, smarks):
    return f"<h1>Congratulation {sname.title()}, you've passed with {smarks} marks.</h1>"

@app.route('/fail/<sname>/<int:smarks>')
def failed(sname, smarks):
    return f"<h1>Sorry {sname.title()}, you've failed with {smarks} marks.</h1>"

@app.route('/score/<name>/<int:marks>')
def score(name, marks):
    if marks < 30:
        time.sleep(1)
        # redirect to failed page
        return redirect(url_for('failed', sname=name, smarks=marks))
    else:
        time.sleep(1)
        # redirect to passed page
        return redirect(url_for('passed', sname=name, smarks=marks))

if __name__ == "__main__":
    app.run(debug=True)