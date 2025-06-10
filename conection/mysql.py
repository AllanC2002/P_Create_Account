# database Accounts
from dotenv import load_dotenv
import os
import mysql.connector

load_dotenv()

# Conection to accounts
def conection_accounts():
    con = mysql.connector.connect(
        host=os.getenv('Dba_hostip'),
        port=os.getenv('Dba_port'),
        database=os.getenv('Dba_namedb'),
        user=os.getenv('Dba_user'),
        password=os.getenv('Dba_password')
    )
    return con

# Conection to userprofile
def conection_userprofile():
    con = mysql.connector.connect(
        host=os.getenv('Dbu_hostip'),
        port=os.getenv('Dbu_port'),
        database=os.getenv('Dbu_namedb'),
        user=os.getenv('Dbu_user'),
        password=os.getenv('Dbu_password')
    )
    return con


