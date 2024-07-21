# main.py
"""
main.py
--------
Defines the Flask application and endpoints for the profile management system.
"""

from flask import Flask, request, jsonify
from utils import get_user_info, list_all_users
from log import log_message

app = Flask(__name__)

@app.route('/user/<username>', methods=['GET'])
def user_info(username):
    """
    Endpoint to get information about a specific user.

    Args:
        username (str): The username of the user whose information is to be retrieved.

    Returns:
        JSON response containing user information or an error message.
    """
    current_user = request.args.get('current_user')
    is_admin = request.args.get('is_admin', 'false').lower() == 'true'

    try:
        user_data = {"email": "radha@example.com", "age": 30, "mobile": "9123456789", "gender": "male", "blood_group": "B+"}
        user_info = get_user_info(username, current_user, is_admin, user_data=user_data)
        return jsonify(user_info), 200
    except (ValueError, PermissionError) as e:
        return jsonify({'error': str(e)}), 403 if isinstance(e, PermissionError) else 404

@app.route('/users', methods=['GET'])
def all_users():
    """
    Endpoint to list all users.

    Returns:
        JSON response containing all users or an error message.
    """
    current_user = request.args.get('current_user')
    is_admin = request.args.get('is_admin', 'false').lower() == 'true'

    try:
        all_users = list_all_users(current_user, is_admin)
        return jsonify(all_users), 200
    except PermissionError as e:
        return jsonify({'error': str(e)}), 403

if __name__ == "__main__":
    app.run(debug=True)
