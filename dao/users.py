from util.config import db
import bcrypt as bcrypt
from util.utilities import Utilities

class Users(Utilities,db.Model):
    RELATIONSHIPS_TO_DICT = True

    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(100), nullable=False)
    picture_url = db.Column(db.String(200), nullable=False)
    total_points = db.Column(db.Integer, nullable=True)
    progress = db.relationship("Progress", backref=db.backref('users', lazy='subquery'), lazy=True)


    def __init__(self, **args):
        self.name = args.get('name')
        self.email = args.get('email')
        self.password = args.get('password')
        self.picture_url = args.get('picture_url')
        self.total_points = args.get('total_points')

    @property
    def pk(self):
        return self.user_id

    def create(self):
        self.password = bcrypt.hashpw(self.password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
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
    def getUsers():
        return Users.query.order_by(Users.user_id).all()

    @staticmethod
    def getUserById(uid):
        return Users.query.filter_by(user_id=uid).first()

    @staticmethod
    def getUserByEmail(uemail):
        return Users.query.filter_by(email=uemail).first()

    @staticmethod
    def verifyEmail(uemail):
        return len(Users.query.filter_by(email=uemail).all()) != 0
 