#!/usr/bin/python3
"""
This modules defines simple API Security
and Authentication techniques.
"""
from flask import Flask, request, jsonify
from flask_httpauth import HTTPBasicAuth
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import create_access_token, jwt_required, get_jwt
from flask_jwt_extended import JWTManager

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['JWT_SECRET_KEY'] = 'your_super_secret_key'
jwt = JWTManager(app)

users = {"user1":
         {"username": "user1",
          "password": generate_password_hash("password"),
          "role": "user"}, "admin1":
         {"username": "admin1",
          "password": generate_password_hash("password"),
          "role": "admin"}}


@auth.verify_password
def verify_password(username, password):
    """
    Verify username and password for basic auth
    """
    if username in users and check_password_hash(
       users.get(username).get("password"), password):
        return username
    else:
        return None


@app.route('/basic-protected', methods=["GET"])
@auth.login_required
def auth_basic():
    """
    Protected route with basic auth
    """
    return ("Basic Auth: Access Granted")


@app.route('/login', methods=["POST"])
def user_login():
    """
    Login route, returns JWT on success
    """
    username = request.json.get("username")
    password = request.json.get("password")
    log = verify_password(username, password)

    if log is None:
        return jsonify({"error": "invalid credentials"}), 401
    else:
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": users[username]["role"]})
        return jsonify(access_token=access_token)


@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def jwt_protected():
    """
    Protected route with JWT auth
    """
    return ("JWT Auth: Access Granted")


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    """
    Admin-only route, check user role from JWT
    """
    identity = get_jwt()
    user_role = identity.get("role")
    if user_role != "admin":
        return jsonify({"error": "Admin access required"}), 403
    else:
        return ("Admin Access: Granted")


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle missing or invalid token error
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle invalid token error
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    """
    Handle expired token error
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    """
    Handle revoked token error
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    """
    Handle fresh token required error
    """
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == '__main__':
    app.run()
