import requests

url = "http://127.0.0.1:8080/create_account"

data = {
    "Name": "test1",
    "Lastname": "testeo2",
    "User_mail": "ascorread1",
    "Password": "1234",
    "Id_type": 1,
    "Id_preferences": 1
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())