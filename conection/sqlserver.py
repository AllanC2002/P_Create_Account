# database Accounts
from dotenv import load_dotenv
import os
import pyodbc

load_dotenv()

# database Accounts
def conection_accounts():
    con=pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('Dba_hostip')},{os.getenv('Dba_port')};"
        f"DATABASE={os.getenv('Dba_namedb')};"
        f"UID={os.getenv('Dba_user')};"
        f"PWD={os.getenv('Dba_password')}"
    )
    return con

# database Userprofile
def conection_userprofile():
    con=pyodbc.connect(
        f"DRIVER={{ODBC Driver 17 for SQL Server}};"
        f"SERVER={os.getenv('Dbu_hostip')},{os.getenv('Dbu_port')};"
        f"DATABASE={os.getenv('Dbu_namedb')};"
        f"UID={os.getenv('Dbu_user')};"
        f"PWD={os.getenv('Dbu_password')}"
    )
    return con

