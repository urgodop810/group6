import pandas
import numpy
import json

with open('../Statsbomb/data/competitions.json') as file:
    competitions_list = json.load(file)
    file.close()

for competition in competitions_list:
    if competition['competition_name'] == "La Liga":
        if competition['season_name'] == "2020/2021":
            season_id = competition['season_id']
            print("season_id:" , season_id)
            competition_id = competition['competition_id']
            print("competition_id:" , competition_id)

with open('../Statsbomb/data/matches/'+str(competition_id)+'/'+str(season_id)+'.json',encoding='utf') as f:
    matches = json.load(f)
    f.close()

Team_required ="Barcelona"

matchIDs = []
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    if (home_team_name==Team_required) or (away_team_name==Team_required):
        matchIDs.append(match['match_id'])

goalsScored = []
goalsConceded = []
for match in matchIDs:        
    with open('../Statsbomb/data/events/' + str(match) + '.json',encoding='utf') as file:
        events = json.load(file)
        for event in events:
            if event["type"]["name"] == "Shot":
                if event["shot"]['outcome']['name'] == "Goal":
                    if event["possession_team"]["name"] == "Barcelona" :
                        goalsScored.append(event)
                    else :
                        goalsConceded.append(event)         
    file.close()