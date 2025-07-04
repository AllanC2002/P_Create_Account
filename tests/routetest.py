import requests

url = "http://3.212.156.160:8080/create_account"

#url = "http://localhost:8080/create_account"

data = {
    "Name": "ec2",
    "Lastname": "ec2",
    "User_mail": "allan2",
    "Password": "1234",
    "Id_type": 1,
    "Id_preferences": 1
}

response = requests.post(url, json=data)

print(response.status_code)
print(response.json())