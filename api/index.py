import os
from flask import Flask, jsonify
# from .jobTracker import jobTrackerBP
from api.auth import authBP
from dotenv import load_dotenv
from database import db
from auth import login_manager
from werkzeug.exceptions import HTTPException

# Load environment variables
load_dotenv()

# App setup
app = Flask(__name__)
# app.register_blueprint(jobTrackerBP)
app.register_blueprint(authBP)

# Database setup
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
db.init_app(app)

# Login manager setup
app.config['SECURITY_PASSWORD_SALT'] = os.getenv('SECURITY_PASSWORD_SALT')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
login_manager.init_app(app)


# Error handling
@app.errorhandler(Exception)
def handle_error(error):
    code = 500
    message = 'Server internal error'

    if isinstance(error, HTTPException):
        code = error.code
        message = error.description

    response = jsonify({'message': message})
    response.status_code = code
    return response
