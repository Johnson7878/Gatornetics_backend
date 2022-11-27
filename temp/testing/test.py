from __future__ import print_function
import time
import cfbd
from cfbd.rest import ApiException
from pprint import pprint

# Configure API key authorization: ApiKeyAuth
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'uHZyMKEnExs1jxdAWvwmblkR3+vRvnTFT7Ene2/kAMsZefXA3tabMMugpG6hQWh4'
configuration.api_key_prefix['Authorization'] = 'Bearer'

# create an instance of the API class
api_instance = cfbd.PlayersApi(cfbd.ApiClient(configuration))
year = 2022 # int | Year filter
team = 'Florida' # str | Team filter (optional)
conference = 'SEC' # str | Conference abbreviation filter (optional)
start_week = 1 # int | Start week filter (optional)
season_type = 'regular' # str | Season type filter (regular, postseason, or both) (optional)
#category = 'category_example' # str | Stat category filter (e.g. passing) (optional)



####################################################################################


#                                  Player API test


####################################################################################


garbage = []
for temp in range(1,12):
    garbage += [api_instance.get_player_season_stats(year, conference=conference, start_week=start_week, end_week=temp, season_type=season_type)]
    




####################################################################################


#                                  Team API test


####################################################################################


# Create TeamsAPI Call
api_instance = cfbd.TeamsApi(cfbd.ApiClient(configuration))
conference = 'SEC' # str | Conference abbreviation filter (optional)
SEC_Conf = api_instance.get_teams(conference=conference)
year = 2022 # int | Season year (optional)

teams = dict()
for team in SEC_Conf:
    teams[team.id] = team
    


players = dict()
team_ids = teams.keys()
for team in SEC_Conf:
    roster = api_instance.get_roster(team=team.school, year=year)
    for player in roster:
        players[player.id] = player

final = []
         
for twitter in players:
    final += [[twitter, players[twitter].first_name, players[twitter].last_name]]

#apollo = 0
for temp in garbage:
    for bruh in temp:
        apollo = bruh.player_id
print(players[apollo])

temp = [[107494,1],[107494,1],['b',0],['b',0],[107494,1],[107494,1],['b',0],['b',0]]

playa = players
for player in players:
    cook = []
    for iterat in temp:
        if iterat[0] == player:
            cook.append(iterat[1])
    players[player] = cook
print(players[107494])
print(players[3127218])

temp1 = [[107494,2],[107494,2],['b',0],['b',0],[107494,2],[107494,2],['b',0],['b',0]]


for player in playa:
    cook1 = []
    for iterat1 in temp1:
        if iterat1[0] == player:
            cook1.append(iterat1[1])
    playa[player] = cook1
print(playa[107494])
print(playa[3127218])



