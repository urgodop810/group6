import json

with open('../Statsbomb/data/competitions.json') as file:
    competitions_list = json.load(file)

for competition in competitions_list:
    if competition['competition_name'] == "La Liga":
        if competition['season_name'] == "2020/2021":
            season_id = competition['season_id']
            #print("season_id:" , season_id)
            competiton_id = competition['competition_id']
            #print("competition_id:" , competiton_id)

with open('Statsbomb/data/')
