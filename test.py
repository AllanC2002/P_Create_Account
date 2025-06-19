import requests

url = "http://localhost:8080/create_account"

data = {
    "Name": "asfasfsafdf",
    "Lastname": "asfafd",
    "User_mail": "fdasdfasdfs@example.com",
    "Password": "12asf32423",
    "Description": "asdf m32undo",
    "Id_type": 1,
    "Id_preferences": 1
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())