#######################################################################################
#
#
#       In this file, we test the timeout upper bounds of Planetscale
#
#
#######################################################################################

import os
from dotenv import load_dotenv
from mysql.connector import Error
import mysql.connector

load_dotenv()

connection = mysql.connector.connect(
host=os.getenv("HOST"),
database=os.getenv("DATABASE"),
user=os.getenv("IDENTITY"),
password=os.getenv("PASSWORD"),
ssl_ca=os.getenv("SSL_CERT")
)

try:
    if connection.is_connected():
        cursor = connection.cursor()
    cursor.execute("select @@version ")
    version = cursor.fetchone()
    if version:
        print('Running version: ', version)
    else:
        print('Not connected.')
except Error as e:
    print("Error while connecting to MySQL", e)

#WELCOME ABOARD CAPTAIN .... ALL SYSTEMS ONLINE


while(1):
    print("1")