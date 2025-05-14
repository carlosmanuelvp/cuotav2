import re
import requests


class User:
    def __init__(self, username, current_password, new_password, confirm_password):
        self.username = username
        self.current_password = current_password
        self.new_password = new_password
        self.confirm_password = confirm_password


def validate_password(password):
    if len(password) < 8:
        return False, "Password must be at least 8 characters long."
    if not re.search(r"[a-z]", password):
        return False, "Password must contain at least one lowercase letter."
    if not re.search(r"[A-Z]", password):
        return False, "Password must contain at least one uppercase letter."
    if not re.search(r"\d", password):
        return False, "Password must contain at least one number."
    if not re.search(r"[^\w\s]", password):
        return False, "Password must contain at least one special character."
    return True, ""


def change_password(user):
    if user.new_password != user.confirm_password:
        return {"success": False, "message": "New passwords do not match."}

    is_valid, message = validate_password(user.new_password)
    if not is_valid:
        return {"success": False, "message": message}

    # If all validations pass, send the request
    url = "https://drst.uci.cu/change-password"
    data = {
        "user": user.username,
        "old": user.current_password,
        "new": user.new_password,
        "confirm": user.confirm_password,
    }

    try:
        response = requests.post(url, data=data)
        return {
            "success": response.status_code == 200,
            "status_code": response.status_code,
            "message": response.text,
        }
    except requests.RequestException as e:
        return {
            "success": False,
            "message": f"Failed to connect to the server: {str(e)}",
        }
