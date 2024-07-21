"""
constants.py
-------------
Contains constants used throughout the project.
"""

# List of valid country codes
VALID_COUNTRY_LIST = ["91", "45", "67", "56"]

# List of excluded mobile numbers
EXCLUDED_NUMBERS = ["9898989898", "9999999999", "8888888888"]

# List of valid genders
VALID_GENDERS = ["male", "female", "other"]

# List of valid blood groups
VALID_BLOOD_GROUPS = ["A+", "A-", "B+", "B-", "O+", "O-", "AB+", "AB-"]

# Log switch (True to enable logging, False to disable)
LOG_SWITCH = True

# Log messages
LOG_MESSAGES = {
    'invalid_email': "Invalid email format: {}",
    'valid_email': "Valid email: {}",
    'invalid_age': "Invalid age: {}",
    'valid_age': "Valid age: {}",
    'invalid_mobile': "Invalid mobile number: {}",
    'excluded_mobile': "Excluded mobile number: {}",
    'valid_mobile': "Valid mobile number: {}",
    'invalid_gender': "Invalid gender: {}",
    'valid_gender': "Valid gender: {}",
    'invalid_blood_group': "Invalid blood group: {}",
    'valid_blood_group': "Valid blood group: {}",
    'user_info': "User info for {}: {}",
    'unauthorized_access': "Unauthorized access attempt by {} to view {}'s information",
    'user_not_found': "User {} not found",
    'list_all_users': "Admin {} listing all users",
    'unauthorized_list_users': "Unauthorized access attempt by {} to list all users"
}
