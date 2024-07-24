from flask import (
    Flask,
    render_template
)
from helper import Signup, Login

app = Flask(__name__)
app.config['SECRET_KEY'] = 'abc'

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title='Home')

@app.route('/signup', methods=['GET', 'POST'])
def signup():
    form = Signup()
    return render_template('signup.html', title='Sign Up', form=form)

@app.route('/login')
def login():
    form = Login()
    return render_template('login.html', title='Login', form=form)

if __name__ == "__main__":
    app.run(debug=True)