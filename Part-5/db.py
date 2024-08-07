from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class employees(db.Model):
    id = db.column(db.Integer, primary_key=True)
    name = db.column(db.String(30), nullable=False)
    age = db.column(db.Integer, nullable=False)
    email = db.column(db.String(50), nullable=False, unique=True)


if __name__ == '__main__':
    app.run(debug=True)