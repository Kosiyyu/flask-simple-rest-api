from app import db

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    value = db.Column(db.String(255))
    max_points = db.Column(db.Float)
    answer = db.relationship('Answer', backref='question')
    quiz_id = db.Column(db.Integer, db.ForeignKey('quiz.id'))

    def __init__(self, value, quiz_id):
        value.id = value
        quiz_id.id = quiz_id