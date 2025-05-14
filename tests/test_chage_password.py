import pytest
from src.backend.change_password import User , change_password

# ---------- UNIT TESTS ----------

def test_passwords_do_not_match():
    user = User("user", "Old123!", "Newpass123!", "WrongConfirm123!")
    result = change_password(user)
    assert result["success"] is False
    assert "do not match" in result["message"].lower()

def test_password_too_short():
    user = User("user", "Old123!", "Aa1!", "Aa1!")
    result = change_password(user)
    assert result["success"] is False
    assert "at least 8 characters" in result["message"]

def test_missing_lowercase():
    user = User("user", "Old123!", "PASSWORD123!", "PASSWORD123!")
    result = change_password(user)
    assert result["success"] is False
    assert "lowercase" in result["message"]

def test_missing_uppercase():
    user = User("user", "Old123!", "password123!", "password123!")
    result = change_password(user)
    assert result["success"] is False
    assert "uppercase" in result["message"]

def test_missing_number():
    user = User("user", "Old123!", "Password!", "Password!")
    result = change_password(user)
    assert result["success"] is False
    assert "number" in result["message"]

def test_missing_special_char():
    user = User("user", "Old123!", "Password123", "Password123")
    result = change_password(user)
    assert result["success"] is False
    assert "special character" in result["message"]

# ---------- INTEGRATION TEST ----------

def test_valid_password(monkeypatch):
    """Simulate a successful request to the server."""

    class MockResponse:
        status_code = 200
        text = "Password successfully changed."

    def mock_post(*args, **kwargs):
        return MockResponse()

    monkeypatch.setattr("requests.post", mock_post)

    user = User("user", "Old123!", "ValidPass123!", "ValidPass123!")
    result = change_password(user)

    assert result["success"] is True
    assert result["status_code"] == 200
    assert "successfully" in result["message"].lower()
