import pymongo, json
from pymongo import MongoClient
client = MongoClient()
from bson.json_util import loads

#create test database
db = client['test'] # creates if doesn't already exist
#create restaurants collection
restaurants = db['restaurants']

def get_data():
    json_file = open('data3.json')
    stuff = json_file.readlines()
    for line in stuff:
        line.replace("$date","date")
        restaurants.insert_one(loads(line,strict=False))

# def ingest(f):
#     with open(f) as _f:
#         return loads(f'[{",".join(map(lambda s: s[:-1], _f))}]')

if restaurants.estimated_document_count() == 0:
    get_data()
#data = ingest("data.json")
#restaurants.insert(data)
len = restaurants.estimated_document_count()
print(len)
# json_string = json_file.read()
# json_string.replace("$date", "date")
   # data = json.load(json_file)
