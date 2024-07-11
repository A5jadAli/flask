from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to our Home Page!</h1>"

@app.route('/score/<string:name>/<int:marks>')
def score(name, marks):
    if marks < 0:
        pass
    elif marks < 40:
        pass

if __name__ == "__main__":
    app.run(debug=True)