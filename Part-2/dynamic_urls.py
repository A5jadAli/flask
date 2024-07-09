from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return "Welcome to our Home Page!"

@app.route('/welcome/Asjad')
def welcome_asjad():
    return "Welcome Asjad!"

if __name__ == "__main__":
    app.run(debug=True)