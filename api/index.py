import os
from flask import Flask, jsonify
# from .jobTracker import jobTrackerBP
from app.auth import authBP
from dotenv import load_dotenv
from werkzeug.exceptions import HTTPException
from app.db import init_db
from app.auth import init_auth

# Load environment variables
load_dotenv()

# App setup
app = Flask(__name__)
# app.register_blueprint(jobTrackerBP)
app.register_blueprint(authBP)
app.debug = True

# App configuration
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DB_URI')
app.config['SECURITY_PASSWORD_SALT'] = os.getenv('SECURITY_PASSWORD_SALT')
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')
# app.config['SECURITY_POST_LOGOUT_VIEW'] = None
app.config["REMEMBER_COOKIE_SAMESITE"] = "strict"
app.config["SESSION_COOKIE_SAMESITE"] = "strict"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

# Initialize app
with app.app_context():
    init_auth(app)
    init_db(app)


# # Error handling
# @app.errorhandler(Exception)
# def handle_error(error):
#     code = 500
#     message = 'Server internal error'

#     if isinstance(error, HTTPException):
#         code = error.code
#         message = error.description

#     response = jsonify({'message': message})
#     response.status_code = code
#     return response
