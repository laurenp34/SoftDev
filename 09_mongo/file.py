from pymongo import MongoClient
client = MongoClient()
import json

json_file = open('data.json')
json_string = json_file.read()
json_string.replace("$date", "date")
   # data = json.load(json_file)

print(len(json_string))
