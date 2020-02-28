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

def get_boro(boro):
    return restaurants.find( {"borough": boro} )

#All restaurants in a specified borough.
def borough(bor):
    num = restaurants.count_documents({"borough": bor})
    print(num," restaurants in borough: ", bor)
    out = restaurants.find({ "borough": bor })
    return out
        #print(res)

#All restaurants in a specified zip code.
def zipcode(zip):
    num = restaurants.count_documents({"address.zipcode": zip})
    print(num," restaurants in zip code ", zip)
    return restaurants.find( {"address.zipcode": zip})

#All restaurants in a specified zip code and with a specified grade.
def zipgrade(zip, grade):
    num = restaurants.count_documents({"address.zipcode": zip, "grades.0.grade": grade})
    print(num, " restaurants in zip code ", zip, " and grade ", grade)
    return restaurants.find( {"address.zipcode": zip, "grades.0.grade": grade})

#All restaurants in a specified zip code with a score below a specified threshold.
def zipscore(zip, thres):
    num = restaurants.count_documents({"address.zipcode": zip, "grades.0.score": {"$lt": int(thres)}})
    print(num, " restaurants in zip code ", zip, " with grade below ", thres)
    return restaurants.find( {"address.zipcode": zip, "grades.0.score": {"$lt": int(thres)}})

#Something more clever.

#only populate restaurants if empty
if restaurants.estimated_document_count() == 0:
    get_data()
# print(restaurants.count_documents({"borough": "Bronx"}))
borough("Bronx")
zipcode("10462")
zipgrade("10462","A")
zipscore("10462",15)




#data = ingest("data.json")
#restaurants.insert(data)
len = restaurants.estimated_document_count()
print(len)
# json_string = json_file.read()
# json_string.replace("$date", "date")
   # data = json.load(json_file)
