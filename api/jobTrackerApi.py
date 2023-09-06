from database.models import User
from database import db
from flask import Flask

app = Flask(__name__)


@app.route('/get')
def get():

    # new_user = User(username='admin', email='asd@qq.com')

    # db.session.add(new_user)
    # db.session.commit()

    return 'hello world'


@app.route('/get')
def gett():

    return 'hello world1'
