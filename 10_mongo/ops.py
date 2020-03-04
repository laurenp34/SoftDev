import json
#from bson.json_util import loads

from pymongo import MongoClient
client = MongoClient()
db = client["opioids"]
col = db["inventory"]

def total_female():
    count_female = 0
    rows = col.find({},{"data":1})
    row = rows[0]
    for i in range(len(row["data"])):
        #print("-----------\n\n",row["data"][i][12])
        if row["data"][i][12] == "Female":
            count_female = count_female + 1 
    return count_female

def total_male():
    count_male = 0
    rows = col.find({},{"data":1})
    row = rows[0]
    for i in range(len(row["data"])):
        #print("-----------\n\n",row["data"][i][12])
        if row["data"][i][12] == "Male":
            count_male = count_male + 1
    return count_male



if col.count_documents({}) == 0:
    print("populating")
    with open('ct_od_deaths.json','r') as file:
        data = json.load(file)
    #    print(type(data["meta"]))
    #    print(type(data["data"]))
        col.insert_one(data)
    #    col.insert_many(data["data"])


col.find()
print("docs: ",col.count_documents({"data.0.0":"row-khjz_tsvj-hrgp"}))
print(col.count_documents({'meta.view.name':"Accidental Drug Related Deaths 2012-2018"}))
data = col.find({'meta.view.name':"Accidental Drug Related Deaths 2012-2018"},{"data.0.0":1})

# printjson(data)
print(col.estimated_document_count())
print(total_female())
print(total_male())
