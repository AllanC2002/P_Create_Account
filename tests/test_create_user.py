import requests

BASE_URL = "http:/3.212.156.160/:8080"

def test_missing_fields():
    user_data = {
        "Name": "Testing"
        # intentionally missing other fields
    }

    response = requests.post(f"{BASE_URL}/create_account", json=user_data)

    assert response.status_code == 400
    assert "Missing field" in response.json().get("error", "")