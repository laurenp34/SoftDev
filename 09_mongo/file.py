from pymongo import MongoClient
client = MongoClient(port=27017)
import json
from bson.json_util import loads

#create test database
db = client['test'] # creates if doesn't already exist
#create restaurants collection
restaurants = db['restaurants']

def get_data():
    json_file = open('data2.json')
    stuff = json_file.readlines()
    for line in stuff:
        line.replace("$data","date")
        restaurants.insert_one(loads(line))

get_data()
len = restaurants.count()
# json_string = json_file.read()
# json_string.replace("$date", "date")
   # data = json.load(json_file)
