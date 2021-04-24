from util.config import db

class Models(db.Model):
    __tablename__ = 'models'
    model_id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey('lessons.lesson_id'), nullable=False)
    model_url = db.Column(db.String(500), nullable=True)
    question = db.Column(db.String(500), nullable=False)
    answer = db.Column(db.String(100), nullable=False)
    xp = db.Column(db.Integer, nullable=True)
    model_name = db.Column(db.String(50), nullable=True)

    def __init__(self, **args):
        self.lesson_id = args.get('lesson_id')
        self.model_url = args.get('model_url')
        self.question = args.get('question')
        self.answer = args.get('answer')
        self.xp = args.get('xp')
        self.model_name = args.get('model_name')

    @property
    def pk(self):
        return self.model_id

    @staticmethod
    def getModels():
        return Models().query.all()

    @staticmethod
    def getModelById(mid):
        return Models().query.filter_by(model_id=mid).first()

    @staticmethod
    def getModelsByLessonId(lid):
        return Models().query.filter_by(lesson_id=lid).all()
