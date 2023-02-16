#######################################################################################
#
#
#       In this file, we test the accuracy of our information
#
#
#######################################################################################

import os
from dotenv import load_dotenv
from mysql.connector import Error
import mysql.connector
from pandas import DataFrame
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'uHZyMKEnExs1jxdAWvwmblkR3+vRvnTFT7Ene2/kAMsZefXA3tabMMugpG6hQWh4'
configuration.api_key_prefix['Authorization'] = 'Bearer'


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


sql = "SELECT school, wins, losses, conference FROM teams"
cursor.execute(sql)
df = DataFrame(cursor.fetchall())
df.columns = ["school", "wins", "losses", "conference"]


inp = input("Please Input an FBS team: ")
data = df.loc[df['school'] == inp].values.flatten().tolist()

#data grab
api_instance = cfbd.TeamsApi(cfbd.ApiClient(configuration))
api_response = api_instance.get_teams()
api_instance1 = cfbd.GamesApi(cfbd.ApiClient(configuration))
api_response1 = api_instance1.get_team_records(year=2022, team=inp)




check = 0
for team in api_response:
    if(team.school == data[0] and team.conference == data[3] and api_response1[0].total.wins == data[1] and api_response1[0].total.losses == data[2]):
        check=1

if check == 1:
    print("CONGRATULATIONS THE INFORMATION IS CORRECT \n")
else:
    print("oh my gawd bruh...........ahhh heeelll nah\n")


connection.close()