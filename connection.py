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
import cfbd
from cfbd.rest import ApiException
import ast
import urllib.request
# with open('temp2.csv') as file_obj:
#     heading = next(file_obj)
#     reader_obj = csv.reader(file_obj)
#     for row in reader_obj:
#         #stats = row[1]
#         temp1 = ast.literal_eval(row[1])
#         temp2 = ast.literal_eval(row[2])

#         sql = "UPDATE players SET posStat1 = JSON_ARRAY(%s) WHERE id = %s"
#         val = (str(temp1),row[0])
#         cursor.execute(sql,val)
#         connection.commit()

#         sql1 = "UPDATE players SET posStat2 = JSON_ARRAY(%s) WHERE id = %s"
#         val1 = (str(temp2),row[0])
#         cursor.execute(sql1,val1)
#         connection.commit()


    



#////////////////////////////////////////////////////////////////////////////
#
#       PULLING STRAIGHT FROM THE CFB AND UPLOADING SECTION BELOW
#
#
#////////////////////////////////////////////////////////////////////////////



configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'uHZyMKEnExs1jxdAWvwmblkR3+vRvnTFT7Ene2/kAMsZefXA3tabMMugpG6hQWh4'
configuration.api_key_prefix['Authorization'] = 'Bearer'
#api_instance = cfbd.TeamsApi(cfbd.ApiClient(configuration))
#conference = 'ACC' # str | Conference abbreviation filter (optional)
#Conf = api_instance.get_teams(conference=conference)

# sql = "SELECT school FROM teams WHERE conference != 'SEC'"
# cursor.execute(sql)
# data = cursor.fetchall()
# Valz=[]
# for valz in data:
#     for temp in valz:
#         Valz += [str(temp)]

# print("\nSchools have been grabbed...\n")
# #I am including garbage time
# api_instance4Rec = cfbd.TeamsApi(cfbd.ApiClient(configuration))
# year=2022
# api_response1 = api_instance4Rec.get_teams(conference='AAC')
# for team in api_response1:
#     sql1 = "UPDATE players SET team_id = %s, Conference = %s WHERE team = %s"
#     valz1 = (team.id, team.conference, team.school)
#     cursor.execute(sql1, valz1)
#     connection.commit()

    #for player in api_response1:
        #sql1 = "INSERT INTO players(id, firstName, lastName, team, year, position, jerseyNumber, height, weight, homeCity, homeState)  VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
        #valz1 = (player.id, player.first_name, player.last_name, player.team, player.year, player.position, player.jersey, player.height, player.weight, player.home_city, player.home_state)
    
        
# sql1 = "UPDATE teams SET playerIDS = JSON_ARRAY(%s) WHERE school = %s"
# valz1 = (str(pValz),'Tennessee')
# cursor.execute(sql1, valz1)
# connection.commit()
# for valz in Conf:
#     sql = "INSERT INTO teams(id, school, conference, color, division, abbr) VALUES(%s, %s, %s, %s, %s, %s)"
#     val = (valz.id, valz.school, valz.conference, valz.color, valz.division, valz.abbreviation)
#     cursor.execute(sql,val)
#     connection.commit()










#########################################################################
#
#
#                   webp image pull
#
#
#
#########################################################################


# sql = "SELECT id FROM players"
# cursor.execute(sql)
# data = cursor.fetchall()
# idTags=[]
# for valz in data:
#     for temp in valz:
#         idTags += [str(temp)]

# udarl = []
# for tag in idTags:
#     udarl.append("https://a.espncdn.com/combiner/i?img=/i/headshots/college-football/players/full/" + str(tag)+ ".png&w=350&h=254")
#     # temp = "https://a.espncdn.com/combiner/i?img=/i/headshots/college-football/players/full/" + str(tag)+ ".png&w=350&h=254"
#     # sql = "UPDATE players SET imgLinx = %s WHERE id = %s"
#     # val = (temp,tag)
#     # cursor.execute(sql,val)
#     # connection.commit()


# i=0
# #get all the images
# for pid in idTags:
#     try:   
#         urllib.request.urlretrieve(udarl[i], f"pps/{str(pid)}.webp")
#     except:
#         pass
    
#     i+=1

sql = "SELECT id FROM teams"
cursor.execute(sql)
data = cursor.fetchall()
schoolTags=[]
for valz in data:
    for temp in valz:
        schoolTags += [str(temp)]


udarl = []
for tag in schoolTags:
    udarl.append("https://a.espncdn.com/i/teamlogos/ncaa/500/" + str(tag)+ ".png")
    # temp1 = "https://a.espncdn.com/i/teamlogos/ncaa/500/" + str(tag)+ ".png"
    # sql = "UPDATE teams SET imgLinx = %s WHERE id = %s"
    # val = (temp1,tag)
    # cursor.execute(sql,val)
    # connection.commit()



i=0
#get all the images
for pid in schoolTags:
    try:   
        urllib.request.urlretrieve(udarl[i], f"logos/{str(pid)}.webp")
    except:
        pass
    
    i+=1

connection.close()