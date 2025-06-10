# database Accounts
from dotenv import load_dotenv
import os

load_dotenv()

# database Accounts
def conection_accounts():
    Db_ip=os.getenv("dbu_hostip")
    Db_port=os.getenv("dbu_port")
    Db_user=os.getenv("dbu_user")
    Db_password=os.getenv("dbu_password")
    Db_name=os.getenv("dbu_namedb")

    

    return

# database Userprofile
def conection_userprofile():
    Db_ip=os.getenv("dba_hostip")
    Db_port=os.getenv("dba_port")
    Db_user=os.getenv("dba_user")
    Db_password=os.getenv("dba_password")
    Db_name=os.getenv("dba_namedb")
    return


