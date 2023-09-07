from flask import Blueprint, request, jsonify
from app.models import User, Role
from app.db import db_session
from flask_security import Security, SQLAlchemySessionUserDatastore, auth_required
from flask_security.utils import hash_password, verify_password, login_user, logout_user
import http


authBP = Blueprint('auth', __name__, url_prefix='/api/auth')

user_datastore = SQLAlchemySessionUserDatastore(db_session, User, Role)
security = Security(datastore=user_datastore)


def init_auth(app):
    security.init_app(app)


# # Handle unauthorized access
# @security.unauthn_handler
# def unauthorized():
#     raise AuthException()


@authBP.route('/register', methods=['POST'])
def register():
    # Get email and password from request body
    email = request.json.get('email')
    password = request.json.get('password')

    if not email and not password:
        # Return error if email and password are not provided
        return jsonify({'message': 'Email and password are required'}), 400
    elif user_datastore.find_user(email=email):
        # Return error if email already exists
        return jsonify({'message': 'Email already exists'}), 400
    else:
        user_datastore.find_or_create_role(name='free_user', permissions=[
                                           'free_user_read', 'free_user_write'])
        db_session.commit()
        user_datastore.create_user(
            email=email, password=hash_password(password), roles=['free_user'])
        db_session.commit()
        return jsonify({'message': 'User created successfully'})


@authBP.route('/login', methods=['GET'])
def login():
    # Get email and password from request body
    email = request.json.get('email')
    password = request.json.get('password')

    # Get user from database
    user = user_datastore.find_user(email=email)

    # Check if user exists and password is correct
    if user and verify_password(password, user.password):
        # Log user in and remember user, through session cookie
        login_user(user, remember=True)
        return jsonify({'message': 'Logged in successfully'})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


@authBP.route('/logout', methods=['POST'])
@auth_required()
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'})




# @authBP.route('/register', methods=['POST'])
# def register():
#     # Get email and password from request body
#     email = request.json.get('email')
#     password = request.json.get('password')

#     if not email and not password:
#         # Return error if email and password are not provided
#         return jsonify({'message': 'Email and password are required'}), 400
#     elif User.query.filter_by(email=email).first():
#         # Return error if email already exists
#         return jsonify({'message': 'Email already exists'}), 400
#     else:
#         # Encrypt password, create new user
#         password_hash = bcrypt.hashpw(
#             password.encode('utf-8'), bcrypt.gensalt())
#         new_user = User(email=email, password=password_hash)

#         # Add new user to database
#         db_session.add(new_user)
#         db_session.commit()
#         return jsonify({'message': 'User created successfully'})


# @authBP.route('/login', methods=['POST'])
# def login():
#     # Get email and password from request body
#     email = request.json.get('email')
#     password = request.json.get('password')
#     password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

#     # Get user from database
#     user = User.query.filter_by(email=email).first()

#     # Check if user exists and password is correct
#     if user and user.password == password_hash:
#         # Log user in and remember user, through session cookie
#         login_user(user, remember=True)
#         return jsonify({'message': 'Logged in successfully'})
#     else:
#         return jsonify({'message': 'Invalid credentials'}), 401


# @authBP.route('/logout')
# @login_required
# def logout():
#     logout_user()
#     return jsonify({'message': 'Logged out successfully'})
