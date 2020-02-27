from pymongo import MongoClient
client = MongoClient()
import json

with open('data.json') as json_file:
    data = json.load(json_file)

print(data)
