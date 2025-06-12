#!/usr/bin/python3
"""
It contains the function:
home
data
status
get_users
add_user
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    Create a function home.
    """
    return ("Welcome to the Flask API!")


@app.route("/data")
def data():
    """
    Create a function that give the data.
    """
    return jsonify(sorted(users.keys()))


@app.route("/status")
def status():
    """
    Create a function that give the status.
    """
    return ('OK')


@app.route("/users/<username>")
def get_users(username):
    """
    Create a function that search a user.
    """
    if username in users:
        return jsonify(users[username])
    return jsonify({"error": "Users Not Found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Create a function that add a user.
    """
    data = request.get_json()
    if "username" not in data or not data["username"]:
        return jsonify({"error": "Username is required"}), 400
    username = data["username"]
    users[username] = data
    return jsonify({"message": "User added!", "user": data}), 201


if __name__ == "__main__":
    app.run(debug=True)
