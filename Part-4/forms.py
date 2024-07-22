from flask import Flask

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return 

@app.route('/signup')
def signup():
    return

@app.route('/login')
def login():
    return

if __name__ == "__main__":
    app.run(debug=True)