import requests

url = "http://localhost:8080/create_account"

data = {
    "Name": "sdasdf",
    "Lastname": "asfasadsdffd",
    "User_mail": "fs@edaxample.com",
    "Password": "12asf32dasdf423",
    "Id_type": 1,
    "Id_preferences": 1
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())