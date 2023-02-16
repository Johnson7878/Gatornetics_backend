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







# This test will define the upper bound of our connection-timing limit with Planetscale. By requesting large amounts of data,
# we can perform stress testing on the database calls to see how much data we can process in a given time. Although we are going
# to be performing trivial tasks with the data we are requesting 
import time
start_time = time.time()
while(1):
    sql = "SELECT school FROM teams"
    cursor.execute(sql)
    data = cursor.fetchall()
    print(time.time() - start_time, " seconds")

#Upper Bound is 20s


connection.close()