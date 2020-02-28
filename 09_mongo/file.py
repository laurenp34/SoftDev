from pymongo import MongoClient
client = MongoClient(port=27017)
import json
from bson.json_util import loads

db = client.restaurants # creates if doesn't already exist

def get_data():
    json_file = open('data2.json')
    stuff = json_file.readlines()
    for line in stuff:
        restaurants.insert_one(loads(line))
# json_string = json_file.read()
# json_string.replace("$date", "date")
   # data = json.load(json_file)
