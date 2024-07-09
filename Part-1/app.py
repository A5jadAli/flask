<<<<<<< HEAD
from flask import Flask

app = Flask(__name__) # here name is a special variable that is passed in any python module

@app.route('/') # this is our first endpoint
@app.route('/home') # for the same endpoint we can have multiple routes
def home():
    return "<h1>Welcome to the Home Page!</h1>"

# path parameter in the URL
@app.route('/welcome/<name>')
def welcome(name):
    return f"<h1> Hi {name.title()}, Welcome to the Welcome Page!</h1>"

# how to get numbers as path parameter
@app.route('/square/<int:num>')
def square(num):
    return f"<h1> The square of {num} is {num**2}</h1>"

# two path parameters
@app.route('/rectangle/<int:length>/<int:breadth>')
def rectangle(length, breadth):
    return f"<h1> The area of rectangle with length {length} and breadth {breadth} is {length*breadth}</h1>"

# this is our second endpoint
@app.route('/about')
def about():
    return "<h1>Welcome to the About Page!</h1>"

if __name__ == '__main__':
=======
from flask import Flask

app = Flask(__name__) # here name is a special variable that is passed in any python module

@app.route('/') # this is our first endpoint
@app.route('/home') # for the same endpoint we can have multiple routes
def home():
    return "<h1>Welcome to the Home Page!</h1>"

# path parameter in the URL
@app.route('/welcome/<name>')
def welcome(name):
    return f"<h1> Hi {name.title()}, Welcome to the Welcome Page!</h1>"

# how to get numbers as path parameter
@app.route('/square/<int:num>')
def square(num):
    return f"<h1> The square of {num} is {num**2}</h1>"

# two path parameters
@app.route('/rectangle/<int:length>/<int:breadth>')
def rectangle(length, breadth):
    return f"<h1> The area of rectangle with length {length} and breadth {breadth} is {length*breadth}</h1>"

# this is our second endpoint
@app.route('/about')
def about():
    return "<h1>Welcome to the About Page!</h1>"

if __name__ == '__main__':
>>>>>>> b139f3dc343eea4464c32cb41f86bef905a67efe
    app.run(debug=True) # here debug=True is used to run the server in debug mode and it will automatically restart the server when we make any changes in the code