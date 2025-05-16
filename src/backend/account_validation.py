


def validate_account(username: str, password: str) -> bool:
    if not username or not password:
        return False
    if len(password) < 8:
        return False
    return True

def validate_red():
    return True