import pandas
import json

with open('../Statsbomb/data/events/15946.json') as file:
    events = json.load(file)
    file.close()


for event in events:
    if event["type"]["name"] == "Shot":
        if event["shot"]['outcome']['name'] == "Goal":
            print(event["id"])

