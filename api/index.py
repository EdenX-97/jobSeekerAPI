import os
from flask import Flask
from .jobTrackerApi import jobTrackerApi
from dotenv import load_dotenv
from database import db

# Load environment variables
load_dotenv()

# Create Flask app
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/about')
def about():
    return 'About'
# app.register_blueprint(jobTrackerApi, url_prefix='/api/jobTrackerApi')

# # Connect to database
# app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
# db.init_app(app)
# with app.app_context():
#     db.create_all()
