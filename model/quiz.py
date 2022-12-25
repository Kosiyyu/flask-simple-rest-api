from app import db

class Quiz(db.Model):
    __tablename__ = 'quiz'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    description = db.Column(db.String(255))
    qusetion_limit = db.Column(db.Integer)
    questions = db.relationship('Question', backref='quiz')

    def __init__(self, name, description, qusetion_limit):
        self.name = name
        self.description = description
        self.qusetion_limit = qusetion_limit