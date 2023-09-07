# from database.models import User
# from database import db
from flask import Blueprint

jobTrackerBP = Blueprint('jobTracker', __name__, url_prefix='/jobTracker')


@jobTrackerBP.route('/get')
def get():
    return 'hello world2'
