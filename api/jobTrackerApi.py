from flask import Blueprint
from database.models import User
from database import db

jobTrackerApi = Blueprint('jobTrackerApi', __name__,
                          url_prefix='/api/jobTrackerApi')


@jobTrackerApi.route('/get')
def get():

    # new_user = User(username='admin', email='asd@qq.com')

    # db.session.add(new_user)
    # db.session.commit()

    return 'hello world'


@jobTrackerApi.route('/get')
def gett():

    return 'hello world1'
