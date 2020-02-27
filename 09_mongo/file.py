from pymongo import MongoClient
client = MongoClient()
import json

with open('data.json') as json_file:
    for line in json_file:
        line.replace("$date", "date")
    data = json.load(json_file)

print(data)
