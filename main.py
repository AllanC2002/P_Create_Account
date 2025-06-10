from flask import Flask, request, jsonify
from conection.mysql import conection_accounts, conection_userprofile

app = Flask(__name__)

@app.route("/create_account", methods=["GET", "POST"])
def create_account():
    con = conection_accounts()
    cursor = con.cursor()

    sql = "INSERT INTO Users (Name, Lastname, User_mail, Password, Status) VALUES (%s, %s, %s, %s, %s)"
    valores = ("Allan", "Correa", "AllanC2002", "1234", 1)

    cursor.execute(sql, valores)
    con.commit()

    rowcount = cursor.rowcount  # Guarda antes de cerrar
    print(f"{rowcount} accounts registered.")
    
    cursor.close()
    con.close()

    return jsonify({"accounts": rowcount})



if __name__=="__main__":
    app.run(debug=True, host="0.0.0.0", port=8080)
