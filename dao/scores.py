from util.config import db
from util.utilities import Utilities


class Scores(Utilities, db.Model):
    RELATIONSHIPS_TO_DICT = True

    __tablename__ = 'scores'
    score_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.lesson_id'), nullable=False)
    numberOfQuestions = db.Column(db.Integer, nullable=True)
    numberOfCorrectAnswers = db.Column(db.Integer, nullable=True)
    numberOfIncorrectAnswers = db.Column(db.Integer, nullable=True)
    totalPoints = db.Column(db.Integer, nullable=True)
    correctPoints = db.Column(db.Integer, nullable=True)
    userInput = db.relationship("UserInputs", backref="scores", lazy=True)

    def __init__(self, **args):
        self.user_id = args.get('user_id')
        self.quiz_id = args.get('quiz_id')
        self.lesson_id = args.get('lesson_id')
        self.numberOfQuestions = args.get('numberOfQuestions')
        self.numberOfCorrectAnswers = args.get('numberOfCorrectAnswers')
        self.numberOfIncorrectAnswers = args.get('numberOfIncorrectAnswers')
        self.totalPoints = args.get('totalPoints')
        self.correctPoints = args.get('correctPoints')

    @property
    def pk(self):
        return self.score_id

    def create(self):
        db.session.add(self)
        db.session.commit()
        return self

    def update(self):
        db.session.add(self)
        db.session.commit()
        return self

    def delete(self):
        db.session.delete(self)
        db.session.commit()

    @staticmethod
    def getScores():
        return Scores.query.all()

    @staticmethod
    def getScoresById(sid):
        return Scores.query.filter_by(score_id=sid).first()

    @staticmethod
    def getScoresByUserId(uid):
        return Scores.query.filter_by(user_id=uid).all()

    @staticmethod
    def getScoresByLessonIdAndUserId(lid, uid):
        return Scores.query.filter_by(lesson_id=lid, user_id=uid).all()
