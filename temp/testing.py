#this file will test the college football data API
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint
import numpy as np
import csv

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'uHZyMKEnExs1jxdAWvwmblkR3+vRvnTFT7Ene2/kAMsZefXA3tabMMugpG6hQWh4'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# Create TeamsAPI Call
api_instance = cfbd.TeamsApi(cfbd.ApiClient(configuration))
conference = 'SEC' # str | Conference abbreviation filter (optional)

try:
    # Gather SEC information
    SEC_Conf = api_instance.get_teams(conference=conference)
    #pprint(SEC_Conf[0])
except ApiException as e:
    print("Exception when calling TeamsApi->get_teams: %s\n" % e)

teams = []
i = 0
for _ in SEC_Conf:
    temp = []
    temp.append(SEC_Conf[i].id)
    temp.append(SEC_Conf[i].school)
    temp.append(SEC_Conf[i].conference)
    temp.append(SEC_Conf[i].color)
    temp.append(SEC_Conf[i].logos)
    teams.append(temp)
    i += 1


#now lets get player information
api_instance = cfbd.TeamsApi(cfbd.ApiClient(configuration))
#team = 'Florida' # str | Team name (optional)
year = 2022 # int | Season year (optional)
SEC_rosters = []
try:
    i=0
    # Team rosters
    for _ in teams:
        SEC_temp = api_instance.get_roster(team=teams[i][1], year=year)
        for iter in SEC_temp:
            temp = []
            temp.append(iter.id)
            temp.append(iter.first_name)
            temp.append(iter.last_name)
            temp.append(iter.team)
            temp.append(iter.year)
            temp.append(iter.position)
            temp.append(iter.jersey)
            temp.append(iter.height)
            temp.append(iter.weight)
            temp.append(iter.home_city)
            temp.append(iter.home_state)
            SEC_rosters.append(temp)
        
        i+=1
except ApiException as e:
    print("Exception when calling TeamsApi->get_roster: %s\n" % e)




#now we'll print out to csv so that we can import to SQL and then host database.


header1 = ['id', 'school', 'conference', 'color', 'logos']
with open('teamInfo.csv', 'w', encoding='UTF8', newline='') as f:
    writer1 = csv.writer(f)
    writer1.writerow(header1)
    writer1.writerows(teams)

header2 = ['id','first_name', 'last_name','team', 'year', 'position', 'jersey', 'height',
'weight', 'home_city', 'home_state']
with open('playerInfo.csv','w', encoding='UTF8', newline='') as f1:
    writer2 = csv.writer(f1)
    writer2.writerow(header2)
    writer2.writerows(SEC_rosters)