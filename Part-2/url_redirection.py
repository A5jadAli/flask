from flask import Flask, redirect, url_for

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to our Home Page!</h1>"

@app.route('/pass')
def passed():
    return "<h1>Congratulation, you've passed.</h1>"

@app.route('/fail')
def failed():
    return "<h1>Sorry, you've failed.</h1>"

@app.route('/score/<string:name>/<int:marks>')
def score(name, marks):
    if marks < 30:
        # redirect to failed page
        return redirect(url_for('failed'))
    else:
        # redirect to passed page
        return redirect(url_for('passed'))

if __name__ == "__main__":
    app.run(debug=True)