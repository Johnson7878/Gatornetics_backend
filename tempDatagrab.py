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


import csv
import cfbd
from cfbd.rest import ApiException
import ast
import urllib.request
import pandas as pd
configuration = cfbd.Configuration()
configuration.api_key['Authorization'] = 'uHZyMKEnExs1jxdAWvwmblkR3+vRvnTFT7Ene2/kAMsZefXA3tabMMugpG6hQWh4'
configuration.api_key_prefix['Authorization'] = 'Bearer'
api_config = cfbd.ApiClient(configuration)
teams_api = cfbd.TeamsApi(api_config)
ratings_api = cfbd.RatingsApi(api_config)
games_api = cfbd.GamesApi(api_config)
stats_api = cfbd.StatsApi(api_config)
betting_api = cfbd.BettingApi(api_config)


# games = []
# lines = []

# for year in range(2015, 2023):
#     response = games_api.get_games(year=year)
#     games = [*games, *response]

#     response = betting_api.get_lines(year=year)
#     lines = [*lines, *response]


# games = [g for g in games if g.home_conference is not None and g.away_conference is not None and g.home_points is not None and g.away_points is not None]
# games = [
#     dict(
#         id = g.id,
#         year = g.season,
#         week = g.week,
#         neutral_site = g.neutral_site,
#         home_team = g.home_team,
#         home_conference = g.home_conference,
#         home_points = g.home_points,
#         home_elo = g.home_pregame_elo,
#         away_team = g.away_team,
#         away_conference = g.away_conference,
#         away_points = g.away_points,
#         away_elo = g.away_pregame_elo
#     ) for g in games]
# for game in games:
#     game_lines = [l for l in lines if l.id == game['id']]

#     if len(game_lines) > 0:
#         game_line = [l for l in game_lines[0].lines if l.provider == 'consensus']

#         if len(game_line) > 0 and game_line[0].spread is not None:
#             game['spread'] = float(game_line[0].spread)
# games = [g for g in games if 'spread' in g and g['spread'] is not None]
# for game in games:
#     game['margin'] = game['away_points'] - game['home_points']
# df = pd.DataFrame.from_records(games).dropna()
# for index, row in df.iterrows():
#     #print (index,row["Fee"], row["Courses"])
#     sql1 = "INSERT INTO data(id, year, week, neutral_site, home_team, home_conference, home_points, home_elo, away_team, away_conference, away_points, away_elo, spread, margin) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
#     val1 = (row["id"], row["year"], row["week"], row["neutral_site"], row["home_team"], row["home_conference"], row["home_points"], row["home_elo"], row["away_team"], row["away_conference"], row["away_points"], row["away_elo"], row["spread"], row["margin"])
#     cursor.execute(sql1,val1)
#     connection.commit() 

sql = "SELECT * FROM data WHERE year = 2020"
cursor.execute(sql)
#data = cursor.fetchall()
from pandas import DataFrame
df = DataFrame(cursor.fetchall())
df.columns = ["id", "year" , "week" , "neutral_site", "home_team", "home_conference", "home_points", "home_elo", "away_team", "away_conference", "away_points", "away_elo", "spread", "margin"]
print(df)


connection.close()