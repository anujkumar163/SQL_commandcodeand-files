import mysql.connector
from mysql.connect import Error
import pandas as pd

def create_server_connection(host_name, user_name, user_password):
    connection = None
    try:
        connection = mysql.connector.connect(
            localhost = host_name
            root = user_name
            "" = user_password
        )
        print("mysql Database connection succesful")
    except Error as err:
        print("f*Error: '{err}'")    
    return connection

