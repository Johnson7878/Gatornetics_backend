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
	

# cursor.execute("CREATE TABLE players(id int NOT NULL PRIMARY KEY, team_id int, KEY teamID (team_id), firstName varchar(255) NOT NULL, \
# lastName varchar(255) NOT NULL, team varchar(255) NOT NULL, year int NOT NULL, position varchar(2) NOT NULL, \
# jerseyNumber varchar(2) NOT NULL, height int, weight int, homeCity varchar(255), \
# homeState varchar(255))")
#INSERT INTO players(posStat1, posStat2) VALUES (%s, %s)


import csv
import ast
with open('./data/teamInfo.csv') as file_obj:
    heading = next(file_obj)
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        #stats = row[1]
        # temp1 = ast.literal_eval(row[1])
        # temp2 = ast.literal_eval(row[2])

        # sql = "UPDATE players SET posStat1 = JSON_ARRAY(%s) WHERE id = %s"
        # val = (temp1,row[0])
        # cursor.execute(sql,val)
        # connection.commit()

        # sql1 = "UPDATE players SET posStat2 = JSON_ARRAY(%s) WHERE id = %s"
        # val1 = (temp2,row[0])
        # cursor.execute(sql1,val1)
        # connection.commit()
        sql = "UPDATE teams SET division = %s WHERE id = %s"
        val = (row[5], row[0])
        cursor.execute(sql,val)
        connection.commit()

        sql = "UPDATE teams SET wins = %s WHERE id = %s"
        val = (row[6], row[0])
        cursor.execute(sql,val)
        connection.commit()

        sql = "UPDATE teams SET expecWins = %s WHERE id = %s"
        val = (row[7], row[0])
        cursor.execute(sql,val)
        connection.commit()

        sql = "UPDATE teams SET recRank = %s WHERE id = %s"
        val = (row[8], row[0])
        cursor.execute(sql,val)
        connection.commit()

        sql = "UPDATE teams SET talentScore = %s WHERE id = %s"
        val = (row[9], row[0])
        cursor.execute(sql,val)
        connection.commit()

        sql = "UPDATE teams SET losses = %s WHERE id = %s"
        val = (row[10], row[0])
        cursor.execute(sql,val)
        connection.commit()

        sql = "UPDATE teams SET overOff = %s WHERE id = %s"
        val = (row[11], row[0])
        cursor.execute(sql,val)
        connection.commit()

        sql = "UPDATE teams SET overDeff = %s WHERE id = %s"
        val = (row[12], row[0])
        cursor.execute(sql,val)
        connection.commit()



connection.close()