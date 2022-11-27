#this file will test the college football data API
from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint
import numpy as np
import pandas as pd
import csv
from sklearn.linear_model import LinearRegression
import matplotlib.pyplot as plt
plt.style.use('bmh')

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'uHZyMKEnExs1jxdAWvwmblkR3+vRvnTFT7Ene2/kAMsZefXA3tabMMugpG6hQWh4'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# Create TeamsAPI Call
api_instance = cfbd.TeamsApi(cfbd.ApiClient(configuration))
conference = 'SEC' # str | Conference abbreviation filter (optional)
SEC_Conf = api_instance.get_teams(conference=conference)


teams = dict()
for team in SEC_Conf:
    teams[team.id] = team
    
# Emmanuel's Code (without objects)


############################################################################################

#now lets get player information
#team = 'Florida' # str | Team name (optional)
year = 2022 # int | Season year (optional)

############################################################################################


players = dict()
team_ids = teams.keys()
for team in SEC_Conf:
    roster = api_instance.get_roster(team=team.school, year=year)
    for player in roster:
        players[player.id] = player
            
players2 = dict()
for team in SEC_Conf:
    rasta = api_instance.get_roster(team=team.school,year=year)
    for playa in rasta:
        players2[playa.id] = playa

############################################################################################




############################################################################################


#                              Positional-stat Collection


############################################################################################


start_week = 1
season_type = 'regular'
firstCol = []
secondCol = []

#first we collect all the data
#then we parse through said data, creating custom lists for player positions and appending it based on unique player id.
api_instance1 = cfbd.PlayersApi(cfbd.ApiClient(configuration))

def posGrabber(position):
    
    if position == 'QB':
        category1 = 'passing'
        statType1 = 'YDS'
        category2 = category1
        statType2 = 'TD'

    elif position == 'RB':
        category1 = 'rushing'
        statType1 = 'YDS'
        category2 = category1
        statType2 = 'TD'

    elif position == 'LB':
        category1 = 'defensive'
        statType1 = 'SOLO'
        category2 = category1
        statType2 = 'TOT'

    elif position == 'DL':
        category1 = 'defensive'
        statType1 = 'SOLO'
        category2 = category1
        statType2 = 'TOT'

    elif position == 'DB':
        category1 = 'defensive'
        statType1 = 'SOLO'
        category2 = category1
        statType2 = 'TOT'

    elif position == 'PK':
        category1 = 'kicking'
        statType1 = 'PCT'
        category2 = category1
        statType2 = 'PTS'

    elif position == 'S':
        category1 = 'defensive'
        statType1 = 'SOLO'
        category2 = category1
        statType2 = 'TOT'

    elif position == 'WR':
        category1 = 'receiving'
        statType1 = 'YDS'
        category2 = category1
        statType2 = 'TD'

    elif position == 'TE':
        category1 = 'receiving'
        statType1 = 'YDS'
        category2 = category1
        statType2 = 'REC'

    elif position == 'DE':
        category1 = 'defensive'
        statType1 = 'SOLO'
        category2 = category1
        statType2 = 'SACKS'

    elif position == 'DT':
        category1 = 'defensive'
        statType1 = 'SOLO'
        category2 = category1
        statType2 = 'TOT'

    elif position == 'P':
        category1 = 'punting'
        statType1 = 'YPP'
        category2 = category1
        statType2 = 'YDS'

    elif position == 'CB':
        category1 = 'interceptions'
        statType1 = 'INT'
        category2 = 'defensive'
        statType2 = 'PD'
    else:
        category1 = ''
        statType1 = category1
        category2 = category1
        statType2 = category1
    
    return (category1, statType1, category2, statType2)

garbage = []
for temp in range(1,13):
    garbage += [api_instance1.get_player_season_stats(year, conference=conference, start_week=start_week, end_week=temp, season_type=season_type)]

for tempo in garbage:
    for iter in tempo:
        val = iter.player_id
        if val < 0:
            continue
        cat1, sT1, cat2, sT2 = posGrabber(players[val].position)
        if cat1 == '':
            #add zeros
            #print("uh oh")
            firstCol += [[iter.player_id, 0]]
            secondCol += [[iter.player_id,0]]


        else:
            #add desired to list 1 and 2 and
            if iter.stat_type == sT1 and iter.category == cat1:
                #add to first list
                firstCol += [[iter.player_id, iter.stat]]
            elif iter.stat_type == sT2 and iter.category == cat2:
                #add to second list 
                secondCol += [[iter.player_id,iter.stat]]



for player in players:
    cook = []
    for iterat in firstCol:
        if iterat[0] == player:
            cook.append(iterat[1])
    players[player] = cook

for player1 in players2:
    cook1 = []
    for iterat1 in secondCol:
        if iterat1[0] == player1:
            cook1.append(iterat1[1])
    players2[player1] = cook1


# csv_input = pd.read_csv('input.csv')
# csv_input['Berries'] = csv_input['Name']
# csv_input.to_csv('output.csv', index=False)

#print(players[107494],players2[107494])




header = ['id', 'posStat']
with open('temp.csv','w', encoding='UTF8', newline='') as f:
    writa = csv.writer(f)
    writa.writerow(header)
    for valz in players:
        temp = [valz, players[valz]]
        writa.writerow(temp)
    for valz in players2:
        temp = [valz, players2[valz]]
        writa.writerow(temp)

################################################################################################################################


#                                                   ML EXAMPLE BELOW


##################################################################################################################################


# now lets create a ML starter that will showcase a common example
# Here, we'll load in a players season stats (Anthony Richardson, UF) and plot them on a graph
# Then, we'll take the player's data and put it into a matrix (pre-process) and send it through Linear regression model
# from ScikitLearn.

# # For the example below, we'll focus on total passing yards
# api_instance2 = cfbd.PlayersApi(cfbd.ApiClient(configuration))
# year = 2022 # int | Year filter
# team = 'Florida' # str | Team filter (optional)
# conference = 'SEC' # str | Conference abbreviation filter (optional)
# start_week = 1 # int | Start week filter (optional)
# end_week = 9 # int | Start week filter (optional)
# season_type = 'regular' # str | Season type filter (regular, postseason, or both) (optional)
# category = 'passing' # str | Stat category filter (e.g. passing) (optional)


# totalyards = []
# def getvalz():
#     api_response = api_instance2.get_player_season_stats(year, team=team, conference=conference, start_week=start_week, end_week=end_week, season_type=season_type, category = category)
#     return api_response

# try:
#     # Player stats by season
#     for ___ in range(end_week,0,-1):
#         temp = getvalz()
#         for iter1 in temp:
            
#             if iter1.player == 'Anthony Richardson':
#                 if iter1.stat_type == 'YDS':
#                     totalyards += [iter1.stat]
#         end_week -= 1
# except ApiException as e:
#     print("Exception when calling PlayersApi->get_player_season_stats: %s\n" % e)

# totalyards.sort()
# weeks = np.array(list(range(1,10)))
# weeks = weeks.reshape(len(weeks),1)


# reg = LinearRegression().fit(weeks, totalyards)
# yards_pred = reg.predict(weeks)

# plt.plot(weeks, totalyards, 'o')
# plt.plot(weeks, yards_pred, 'orange')
# plt.xlabel('Weeks',size=15)
# plt.ylabel('Total Yards',size=15)
# plt.title('Total Passing Yards for AR15')
# plt.show()

# #and thats the first example of our ML application done!!! As you can see,
# #we have created a linear regression line of fit for our data on AR15. This line of
# #fit will allow us to measure prediction points for how his passing game COULD improve 
# #over the last couple of games/weeks