from flask import Blueprint, request, jsonify
from database.models import User
from flask_login import login_user, login_required, logout_user
from database import db
from auth import login_manager
import bcrypt


authBP = Blueprint('auth', __name__, url_prefix='/api/auth')


# Handle unauthorized access
@login_manager.unauthorized_handler
def unauthorized():
    return jsonify({'message': 'Invalid credentials'}), 401


# Load user from database
@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@authBP.route('/register', methods=['POST'])
def register():
    # Get email and password from request body
    email = request.json.get('email')
    password = request.json.get('password')

    if not email and not password:
        # Return error if email and password are not provided
        return jsonify({'message': 'Email and password are required'}), 400
    elif User.query.filter_by(email=email).first():
        # Return error if email already exists
        return jsonify({'message': 'Email already exists'}), 400
    else:
        # Encrypt password, create new user
        password_hash = bcrypt.hashpw(
            password.encode('utf-8'), bcrypt.gensalt())
        new_user = User(email=email, password=password_hash)

        # Add new user to database
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'})


@authBP.route('/login', methods=['POST'])
def login():
    # Get email and password from request body
    email = request.json.get('email')
    password = request.json.get('password')
    password_hash = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())

    # Get user from database
    user = User.query.filter_by(email=email).first()

    # Check if user exists and password is correct
    if user and user.password == password_hash:
        # Log user in and remember user, through session cookie
        login_user(user, remember=True)
        return jsonify({'message': 'Logged in successfully'})
    else:
        return jsonify({'message': 'Invalid credentials'}), 401


@authBP.route('/logout')
@login_required
def logout():
    logout_user()
    return jsonify({'message': 'Logged out successfully'})
