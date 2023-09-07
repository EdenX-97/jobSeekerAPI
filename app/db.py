from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()
db_session = db.session


def init_db(app):
    db.init_app(app)
    db.create_all()
