from flask import Flask
from .jobTracker import jobTrackerBP

app = Flask(__name__)
app.register_blueprint(jobTrackerBP)


@app.route('/get')
def get():

    # new_user = User(username='admin', email='asd@qq.com')

    # db.session.add(new_user)
    # db.session.commit()

    return 'hello world'


@app.route('/get1')
def gett():

    return 'hello world1'
