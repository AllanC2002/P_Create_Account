from flask import Flask, request, jsonify
from conection.mysql import conection_accounts, conection_userprofile

app = Flask(__name__)

@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    cona = conection_accounts()
    cursor = cona.cursor()

    sql = "INSERT INTO Users (Name, Lastname, User_mail, Password, Status) VALUES (%s, %s, %s, %s, %s)"
    valores = ("Allan", "Correa", "Test15", "1234", 1)
    cursor.execute(sql, valores)
    cona.commit()
    # 2. Obtener el ID generado
    user_id = cursor.lastrowid

    # 3. Recuperar el usuario insertado
    cursor.execute("SELECT * FROM Users WHERE Id_User = %s", (user_id,))
    usuario = cursor.fetchone()

    rowcount = cursor.rowcount
    # 4. Mostrar resultados
    print("Datos del usuario insertado en la database accounts:")
    print(usuario)

    cursor.close()
    cona.close()

    conu=conection_userprofile()
    cursoru=conu.cursor()
    sql3= "INSERT INTO Types (Id_user,Description) VALUES (%s, %s)"
    valores3=(f"{user_id}","Test13")

    cursoru.execute(sql3,valores3)
    conu.commit()

    sql4= "INSERT INTO Preferences (Id_user,Description) VALUES (%s, %s)"
    valores4=(f"{user_id}","Test13")

    cursoru.execute(sql4,valores4)
    conu.commit()

    sql2 = "INSERT INTO Profile (Id_user,User_mail,Name,Lastname,Description,Id_preferences,Id_type, Status_account) VALUES (%s, %s, %s, %s, %s,%s,%s,%s)"
    valores2 = (f"{user_id}","Test15","Allan", "Correa", "Hola", 2,2, 1)
    
    cursoru.execute(sql2,valores2)
    conu.commit()

    cursoru.execute("SELECT * FROM Profile WHERE Id_User = %s", (user_id,))
    usuariou = cursor.fetchone()

    return jsonify({"accounts": usuario,"userprofile":usuariou})



if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
