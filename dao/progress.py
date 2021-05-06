from util.config import db
from util.utilities import Utilities


class Progress(Utilities, db.Model):
    RELATIONSHIPS_TO_DICT = True

    __tablename__ = 'progress'
    progress_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.user_id'), nullable=False)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.lesson_id'), nullable=False)
    type = db.Column(db.String(10), nullable=True)
    isCompleted = db.Column(db.Boolean, nullable=True)

    def __init__(self, **args):
        self.user_id = args.get('user_id')
        self.lesson_id = args.get('lesson_id')
        self.type = args.get('type')
        self.isCompleted = args.get('isCompleted')


    @property
    def pk(self):
        return self.progress_id

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
    def getProgress():
        return Progress.query.all()

    @staticmethod
    def getProgressById(pid):
        return Progress.query.filter_by(progress_id=pid).first()

    @staticmethod
    def getProgressByUserId(uid):
        return Progress.query.filter_by(user_id=uid).all()

    @staticmethod
    def getProgressByLessonIdAndUserId(lid, uid):
        return Progress.query.filter_by(lesson_id=lid, user_id=uid).all()

    @staticmethod
    def checkIfRepeated(lid, uid, tpe):
        return len(Progress.query.filter_by(lesson_id=lid, user_id=uid, type=tpe).all()) == 0
