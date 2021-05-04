from util.config import db
from util.utilities import Utilities


class Questions(Utilities, db.Model):
    RELATIONSHIPS_TO_DICT = True

    __tablename__ = 'questions'
    question_id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.lesson_id'), nullable=False)
    question = db.Column(db.String(500), nullable=True)
    questionType = db.Column(db.String(500), nullable=True)
    answerSelectionType = db.Column(db.String(50), nullable=True)
    correctAnswer = db.Column(db.String(10), nullable=True)
    messageForCorrectAnswer = db.Column(db.String(400), nullable=True)
    messageForIncorrectAnswer = db.Column(db.String(500), nullable=True)
    explanation = db.Column(db.String(400), nullable=True)
    point = db.Column(db.String(10), nullable=True)
    questionIndex = db.Column(db.Integer, nullable=True)
    questionPic = db.Column(db.String(500), nullable=True)

    answers = db.relationship("dao.answers.Answers", backref=db.backref('questions', lazy='subquery'), lazy=True)

    def __init__(self, **args):
        self.lesson_id = args.get('lesson_id')
        self.question = args.get('question')
        self.questionType = args.get('questionType')
        self.answerSelectionType = args.get('answerSelectionType')
        self.correctAnswer = args.get('correctAnswer')
        self.messageForCorrectAnswer = args.get('messageForCorrectAnswer')
        self.messageForIncorrectAnswer = args.get('messageForIncorrectAnswer')
        self.explanation = args.get('explanation')
        self.point = args.get('point')
        self.questionIndex = args.get('questionIndex')
        self.questionPic = args.get('questionPic')

    @property
    def pk(self):
        return self.question_id

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
    def getQuestions():
        return Questions.query.all()

    @staticmethod
    def getQuestionsById(qid):
        return Questions.query.filter_by(question_id=qid).first()

    @staticmethod
    def getQuestionsByLessonId(lid):
        return Questions.query.filter_by(lesson_id=lid).all()

