from flask import Flask, render_template, redirect, url_for, session, flash, request
from urllib.request import urlopen
import json
from pymongo import MongoClient
from bson.json_util import loads
from flask import render_template

app = Flask(__name__)

# When your flask app launches, it should drop your db on your default mongo server and rebuild it.
client = MongoClient()
db = client["test"]
# opioids_col = db["opioids"] #collection storing data from opioids dataset
senators_col = db["senators"] #collection storing data from senators dataset

# def setup_opioids():
#     #col.remove({})
#     if opioids_col.count_documents({}) == 0:
#         with open('opioids_data.json','r') as file:
#             data = json.load(file)
#             #print(type(data))
#             lis = data["data"]
#             for item in lis:
#                 opioids_col.insert_one({"date": item[9], "datetype": item[10], "age": item[11], "sex": item[12], "race": item[13], "residencecity": item[14], "residencecounty": item[15], "residencestate": item[16], "deathcity": item[17], "deathcounty": item[18], "location": item[19], "locationifother": item[20], "descriptionofinjury": item[21], "injuryplace": item[22], "injurycity": item[23], "injurycounty": item[24], "injurystate": item[25], "cod": item[26], "othersignifican": item[27], "heroin": item[28], "cocaine": item[29], "fentanyl": item[30], "fentanylanalogue": item[31], "oxycodone": item[32], "oxymorphone": item[33],  "ethanol": item[34], "hydrocodone": item[35], "benzodiazepine": item[36], "methadone": item[37], "amphet": item[38], "tramad": item[39], "morphine_notheroin": item[40], "hydromorphone": item[41], "other": item[42], "opiatenos": item[43], "anyopioid": item[44], "mannerofdeath": item[45]})

def setup_senators():
    # read the data
    if(senators_col.count_documents({})==0):
        file = open("senators_data.json", "r")
        content = loads(file.read())["objects"]
        for line in content:
            senators_col.insert_one(line)

# gets US senators of specified gender
def gender(gender):
    return collection.find({"person.gender" : gender}, {"person.name" : 1})

# gets US senators from specified state
def state(state):
    return collection.find({"state" : state}, {"person.name" : 1})

# gets US senators from specified party
def party(party):
    return collection.find({"party" : party}, {"person.name" : 1})

# gets the website of a specific US senator
def website(fname):
    return collection.find({"person.firstname" : fname}, {"person.name" : 1, "website" : 1})

# gets all related information of a specific US senator
def description(lname):
    return collection.find({"person.lastname" : lname}, {"person.name" : 1, "description" : 1})

# helper method
def printer(data):
    for item in data:
        print(item["person"])

@app.route("/form_data",methods=["POST"])
def form():
    return request.form
# setup_opioids()
setup_senators()

@app.route("/")
def root():
    return render_template("index.html")

if __name__ == "__main__":
    app.debug = True
    app.run()
