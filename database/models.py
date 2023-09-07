from database import db
from enum import Enum
from flask_security import UserMixin


class UserRole(Enum):
    ADMIN = 'admin'
    FREE_USER = 'free_user'
    BASIC_USER = 'basic_user'
    PRO_USER = 'pro_user'


class User(db.Model, UserMixin):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=True)
    password = db.Column(db.String(80), nullable=True)
    role = db.Column(db.Enum(UserRole), nullable=True,
                     default=UserRole.FREE_USER)
    jobs = db.relationship('Job', backref='user', lazy=True)

    def get_id(self):
        return str(self.user_id)


class Job(db.Model):
    __tablename__ = 'jobs'
    job_id = db.Column(db.Integer, primary_key=True)
    status = db.Column(db.Enum('Applied', 'Interviewing',
                       'Offered', 'Failed'), nullable=True)
    company_name = db.Column(db.String(80), nullable=True)
    role = db.Column(db.String(80), nullable=True)
    apply_date = db.Column(db.Date, nullable=True)
    last_updated_date = db.Column(db.Date, nullable=False)
    important_info = db.Column(db.String(500), nullable=False)
    url = db.Column(db.String(255), nullable=True)
    salary_expectation = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'users.user_id'), nullable=True)
