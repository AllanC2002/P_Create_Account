from flask import Flask, request, jsonify
from conection.mysql import conection_accounts, conection_userprofile
from models import User, Profile, Type, Preference


app = Flask(__name__)


@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    # 1. Insert Users (DB accounts)
    session_accounts = conection_accounts()

    nuevo_usuario = User(
        Name="Allan",
        Lastname="Correa",
        User_mail="Test15",
        Password=("1234"),  # contraseña encriptada aquí
        Status=1
    )
    session_accounts.add(nuevo_usuario)
    session_accounts.commit()
    session_accounts.refresh(nuevo_usuario)  # obtener el ID

    user_id = nuevo_usuario.Id_User

    # 2. Insertar en Profile (DB userprofile)
    session_userprofile = conection_userprofile()

    # Obtener cualquier tipo y preferencia (ID 1, 2 por ejemplo)
    tipo = session_userprofile.query(Type).first()
    preferencia = session_userprofile.query(Preference).first()

    nuevo_perfil = Profile(
        Id_User=user_id,
        User_mail="Test15",
        Name="Allan",
        Lastname="Correa",
        Description="Hola",
        Id_type=1,
        Id_preferences=1,
        Status_account=1
    )
    session_userprofile.add(nuevo_perfil)
    session_userprofile.commit()

    return jsonify({
        "accounts": {
            "Id_User": nuevo_usuario.Id_User,
            "Name": nuevo_usuario.Name,
            "Lastname": nuevo_usuario.Lastname,
            "User_mail": nuevo_usuario.User_mail
        },
        "userprofile": {
            "Id_User": nuevo_perfil.Id_User,
            "Description": nuevo_perfil.Description
        }
    })

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
