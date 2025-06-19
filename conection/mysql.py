# database Accounts
from dotenv import load_dotenv
import os
# import mysql.connector

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


load_dotenv()

def conection_accounts():
    host = os.getenv("DBA_HOST")
    port = os.getenv("DBA_PORT")
    user = os.getenv("DBA_USER")
    password = os.getenv("DBA_PASSWORD")
    dbname = os.getenv("DBA_NAME")

    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}"
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    return Session()

def conection_userprofile():
    host = os.getenv("DBU_HOST")
    port = os.getenv("DBU_PORT")
    user = os.getenv("DBU_USER")
    password = os.getenv("DBU_PASSWORD")
    dbname = os.getenv("DBU_NAME")

    connection_string = f"mysql+pymysql://{user}:{password}@{host}:{port}/{dbname}"
    engine = create_engine(connection_string)
    Session = sessionmaker(bind=engine)
    return Session()


"""
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
"""

