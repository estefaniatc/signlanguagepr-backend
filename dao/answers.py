from util.config import db
from util.utilities import Utilities

class Answers(Utilities,db.Model):
    RELATIONSHIPS_TO_DICT = True

    __tablename__ = 'answers'
    answer_id = db.Column(db.Integer, primary_key=True)
    question_id = db.Column(db.Integer, db.ForeignKey('questions.question_id'), nullable=False)
    answer = db.Column(db.String(500), nullable=False)

    def __init__(self, **args):
        self.question_id = args.get('question_id')
        self.answer = args.get('answer')

    @property
    def pk(self):
        return self.answer_id

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
    def getAnswers():
        return Answers.query.all()

    @staticmethod
    def getAnswerById(aid):
        return Answers.query.filter_by(answer_id=aid).first()

    @staticmethod
    def getAnswerByQuestionId(qid):
        return Answers.query.filter_by(question_id=qid).all()
 