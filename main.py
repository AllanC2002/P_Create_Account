from flask import Flask, request, jsonify
from conection.mysql import conection_accounts, conection_userprofile
from models import User, Profile, Type, Preference
import hashlib

app = Flask(__name__)

def hash_password_sha256(password: str) -> str:
    # Function to hash password with SHA-256
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    data = request.json
    if not data:
        return jsonify({"error": "No JSON payload received"}), 400

    # Validate required fields
    required_fields = ["Name", "Lastname", "User_mail", "Password", "Description", "Id_type", "Id_preferences"]
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing field: {field}"}), 400

    # Hash password
    hashed_password = hash_password_sha256(data["Password"])

    # Insert into accounts database
    session_accounts = conection_accounts()
    new_user = User(
        Name=data["Name"],
        Lastname=data["Lastname"],
        User_mail=data["User_mail"],
        Password=hashed_password,
        Status=1
    )
    session_accounts.add(new_user)
    session_accounts.commit()
    session_accounts.refresh(new_user)

    user_id = new_user.Id_User

    # Insert into userprofile database
    session_userprofile = conection_userprofile()

    new_profile = Profile(
        Id_User=user_id,
        User_mail=data["User_mail"],
        Name=data["Name"],
        Lastname=data["Lastname"],
        Description=data["Description"],
        Id_type=data["Id_type"],
        Id_preferences=data["Id_preferences"],
        Status_account=1
    )
    session_userprofile.add(new_profile)
    session_userprofile.commit()

    return jsonify({
        "accounts": {
            "Id_User": new_user.Id_User,
            "Name": new_user.Name,
            "Lastname": new_user.Lastname,
            "User_mail": new_user.User_mail
        },
        "userprofile": {
            "Id_User": new_profile.Id_User,
            "Description": new_profile.Description
        }
    }), 201

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
