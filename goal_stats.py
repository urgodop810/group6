import json
import pandas as pd

with open('../Statsbomb/data/competitions.json') as file:
    #print(file)
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

Team_required ="Barcelona"

#Find ID for the match
matchIDs = []
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    if (home_team_name==Team_required) or (away_team_name==Team_required):
        matchIDs.append(match['match_id'])

#print(matchIDs)

#with open('../Statsbomb/data/events/'+str(matchIDs[-1])+'.json') as file:
    #match_data = json.load(file)

df = pd.read_json('../Statsbomb/data/events/'+str(matchIDs[-1])+'.json')
df.info()
print(df.shot())
