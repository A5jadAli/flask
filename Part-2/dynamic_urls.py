from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "<h1>Welcome to our Home Page!</h1>"

# path parameter
# here we are handling name dynamically
@app.route('/welcome/<name>')
def welcome(name):
    return f"<h1>Hello {name.title()}, Welcome to our Webpage!</h2>"

if __name__ == "__main__":
    app.run(debug=True)