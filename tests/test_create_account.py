# tests/test_create_account.py
import pytest
from unittest.mock import patch, MagicMock
from main import app  # Asegúrate de que este import funcione

@pytest.fixture
def client():
    app.config['TESTING'] = True
    with app.test_client() as client:
        yield client

@patch("services.functions.conection_accounts")
@patch("services.functions.conection_userprofile")
def test_create_account_success(mock_userprofile, mock_accounts, client):
    # Simulate the database session
    mock_session_account = MagicMock()
    mock_session_userprofile = MagicMock()
    mock_accounts.return_value = mock_session_account
    mock_userprofile.return_value = mock_session_userprofile

    # Simulate the creation of a user and profile
    fake_user = MagicMock()
    fake_user.Id_User = 123
    mock_session_account.add.return_value = None
    mock_session_account.commit.return_value = None
    mock_session_account.refresh.side_effect = lambda user: setattr(user, "Id_User", 123)

    mock_session_userprofile.add.return_value = None
    mock_session_userprofile.commit.return_value = None

    # Test data
    data = {
        "Name": "Juan",
        "Lastname": "Pérez",
        "User_mail": "juan.perez@example.com",
        "Password": "123456",
        "Id_type": 1,
        "Id_preferences": 2
    }

    # Call to endpoint
    response = client.post("/create_account", json=data)

    # Validaciones
    assert response.status_code == 201
    json_data = response.get_json()
    assert json_data["message"] == "User created successfully"
    assert json_data["user_id"] == 123
    assert json_data["user_mail"] == data["User_mail"]
