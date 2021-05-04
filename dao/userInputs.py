from util.config import db
from util.utilities import Utilities


class UserInputs(Utilities, db.Model):
    RELATIONSHIPS_TO_DICT = True

    __tablename__ = 'userInput'
    userInput_id = db.Column(db.Integer, primary_key=True)
    score_id = db.Column(db.Integer, db.ForeignKey('scores.score_id'), nullable=False)
    input = db.Column(db.Integer, nullable=False)

    def __init__(self, **args):
        self.score_id = args.get('score_id')
        self.input = args.get('input')

    @property
    def pk(self):
        return self.userInput_id

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
    def getUserInputs():
        return UserInputs.query.all()

    @staticmethod
    def getUserInputById(ui_id):
        return UserInputs.query.filter_by(userInput_id=ui_id).first()

    @staticmethod
    def getUserInputsByScoreId(sid):
        return UserInputs.query.filter_by(score_id=sid).all()

