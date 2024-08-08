from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///matches.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Team(db.Model):
    __tablename__ = 'teams'
    id = db.Column(db.Integer, primary_key=True)
    team = db.Column(db.String(30), nullable=False, unique=True)
    state = db.Column(db.String(30), nullable=False)

    def __repr__(self):
        return f"Team('{self.team}', '{self.state}')"
    
class Player(db.Model):
    __tablename__ = 'players'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(30), nullable=False)
    nationality = db.Column(db.String(30), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey('teams.id'), nullable=False)
    team = db.relationship('Team', backref='players')

    def __repr__(self):
        return f"Player('{self.name}', '{self.nationality}', '{self.team}')"

if __name__ == '__main__':
    app.app_context().push()
    db.create_all()
    db.session.commit()
    app.run(debug=True)