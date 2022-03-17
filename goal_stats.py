import json

with open('../Statsbomb/data/competitions.json') as file:
    competitions_list = json.load(file)

for competition in competitions_list:
    if competition['competition_name'] == "La Liga":
        if competition['season_name'] == "2020/2021":
            season_id = competition['season_id']
            print("season_id:" , season_id)
            competition_id = competition['competition_id']
            print("competition_id:" , competition_id)

#with open('Statsbomb/data/')
#with open('../Statsbomb/data/matches/'+str(competition_id)+'/90.json') as f:
#    print(type(f))
#    print(f)
file = open('../Statsbomb/data/matches/'+str(competition_id)+'/90.json', encoding="utf8")
    #matches = json.load(f)
print(file)    
'''

Team_required ="Atlético Madrid"

matchIDs = []

#Find ID for the match
for match in matches:
    home_team_name=match['home_team']['home_team_name']
    away_team_name=match['away_team']['away_team_name']
    if (home_team_name==Team_required) or (away_team_name==Team_required):
        matchIDs.append(match['match_id'])

print(matchIDs)

#print(home_team_required + ' vs ' + away_team_required + ' has id:' + str(match_id_required))
'''