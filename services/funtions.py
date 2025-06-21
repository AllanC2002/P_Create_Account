from flask import jsonify
from conections.mysql import conection_accounts, conection_userprofile
from models.models import User, Profile
import hashlib
from sqlalchemy.exc import IntegrityError
import requests
import os
import traceback

def hash_password(password: str) -> str:
    return hashlib.sha256(password.encode('utf-8')).hexdigest()

def validate_user(data):
    required = ["Name", "Lastname", "User_mail", "Password", "Id_type", "Id_preferences"]
    missing = [field for field in required if field not in data]
    if missing:
        return jsonify({"error": f"Missing field(s): {', '.join(missing)}"}), 400
    return True

def create_user(data):
    validation = validate_user(data)
    if validation is not True:
        return validation

    hashed_password = hash_password(data["Password"])
    session_accounts = conection_accounts()
    session_userprofile = conection_userprofile()

    try:
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

        new_profile = Profile(
            Id_User=user_id,
            User_mail=data["User_mail"],
            Name=data["Name"],
            Lastname=data["Lastname"],
            Description="",
            Id_type=data["Id_type"],
            Id_preferences=data["Id_preferences"],
            Status_account=1
        )
        session_userprofile.add(new_profile)
        session_userprofile.commit()

        # Microservice defalut-photo
        photo_url = os.getenv("DEFAULT_PHOTO_URL", "http://localhost:8081/default-photo")

        
        try:
            response = requests.post(photo_url, json={"Id_User": user_id}, timeout=5)
            
            if response.status_code == 201:
                print("Default photo assigned successfully.")
            else:
                print("Error to asign default photo:", response.text)
        except Exception as e:
            print("Error to conect whit default-photo:", str(e))

    except IntegrityError as e:
        session_accounts.rollback()
        session_userprofile.rollback()
        return jsonify({"error": "Email already exists or database integrity error."}), 409
    except Exception as e:
        session_accounts.rollback()
        session_userprofile.rollback()
        print("Intern Error\n", traceback.format_exc())
        return jsonify({"error": "Unexpected error: " + str(e)}), 500

    return jsonify({
        "message": "User created successfully",
        "user_id": user_id,
        "user_mail": data["User_mail"]
    }), 201
