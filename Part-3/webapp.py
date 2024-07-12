from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', title="Home")

@app.route('/evaluate/<int:num>')
def evaluate(num):
    return render_template('evaluate.html', title="Evaluate", number=num)

@app.route('/about')
def about():
    return render_template('about.html', title="About")

if __name__ == '__main__':
    app.run(debug=True)