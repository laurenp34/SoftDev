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
        line.replace("$date","date")
        restaurants.insert_one(loads(line,strict=False))

def ingest(f):
    with open(f) as _f:
        return loads(f'[{",".join(map(lambda s: s[:-1], _f))}]')

#get_data()
data = ingest("data.json")
restaurants.insert(data)
len = restaurants.count()
# json_string = json_file.read()
# json_string.replace("$date", "date")
   # data = json.load(json_file)
