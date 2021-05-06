from util.config import db
from util.utilities import Utilities


class Lessons(Utilities, db.Model):
    RELATIONSHIPS_TO_DICT = True

    __tablename__ = 'lessons'
    lesson_id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500), nullable=False)
    level_id = db.Column(db.Integer, db.ForeignKey('levels.level_id'), nullable=False)
    video_url = db.Column(db.String(500), nullable=False)
    max_xp = db.Column(db.Integer, nullable=True)
    lesson_img = db.Column(db.String(500), nullable=True)
    quiz_url = db.Column(db.String(150), nullable=True)
    total_activities = db.Column(db.Integer, nullable=False)
    models = db.relationship("Models", backref=db.backref('lessons', lazy='subquery'), lazy=True)
    # questions = db.relationship("dao.questions.Questions", backref=db.backref('lessons', lazy='subquery'), lazy=True)

    def __init__(self, **args):
        self.lname = args.get('lname')
        self.description = args.get('description')
        self.level_id = args.get('level_id')
        self.video_url = args.get('video_url')
        self.max_xp = args.get('max_xp')
        self.lesson_img = args.get('lesson_img')
        self.quiz_url = args.get('quiz_url')
        self.total_activities = args.get('total_activities')

    @property
    def pk(self):
        return self.lesson_id

    @staticmethod
    def getAllLessons():
        return Lessons.query.all()

    @staticmethod
    def getLessonById(lid):
        return Lessons.query.filter_by(lesson_id=lid).first()

    @staticmethod
    def getLessonsByLevelId(levid):
        return Lessons.query.filter_by(level_id=levid).all()
