# Klondike -- Nahi Khan, Lauren Pehlivanian and Ahmed Sultan
# SoftDev1 pd 9
# K25 -- Getting more REST
# 2019-11-13

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
import urllib
import random
import json
import time


app = Flask(__name__)

# countries, currency exchange, & studio ghibli


@app.route("/")
def main():
    return render_template("index.html")

@app.route("/randCountry")
def randCountry():
    # accessing countries API
    u = urllib.request.urlopen("https://restcountries.eu/rest/v2")
    response = u.read()
    data = json.loads(response)

    country_list = []
    #add 3 random countries to data to pass to template
    for i in range(3):
        country_list.append(data[random.randint(0,len(data)-1)])

    return render_template("randcountry.html", countries=country_list)

@app.route("/randNHLTeam")
def randnhlteam():
    # accessing NHL API
    u = urllib.request.urlopen("https://statsapi.web.nhl.com/api/v1/teams")
    response = u.read()
    data = json.loads(response)

    # picking random NHL team from API response
    team_name = ""
    team_fyop = ""
    team_venue = ""
    team_vcity = ""
    rand_num = random.randint(1, 54)
    for i in data['teams']:
        if i['id'] == rand_num:
            team_name = i['name']
            team_fyop = i['firstYearOfPlay']
            team_venue = i['venue']['name']
            team_vcity = i['venue']['city']

    if (team_name == "") & (team_fyop == "") & (team_venue == "") & (team_vcity == ""):
        return redirect(url_for('randnhlteam'))
    else:
        return render_template("randnhlteam.html",
                               t_name=team_name,
                               t_fyop=team_fyop,
                               t_venu=team_venue,
                               t_vcty=team_vcity)

@app.route("/randNHLLogo")
def randnhllogo():
    # accessing NHL Logo API
    u = urllib.request.urlopen("https://records.nhl.com/site/api/franchise?include=teams.id&include=teams.active&include=teams.triCode&include=teams.placeName&include=teams.commonName&include=teams.fullName&include=teams.logos&include=teams.conference.name&include=teams.division.name&include=teams.franchiseTeam.firstSeason.id&include=teams.franchiseTeam.lastSeason.id&include=teams.franchiseTeam.teamCommonName")
    response = u.read()
    data = json.loads(response)

    # picking random NHL logo from API response
    lteam_name = ""
    lteam_logo = ""
    rand_num = random.randint(0, 37)
    lteam_name = data.get('data')[rand_num]['teams'][0]['fullName']
    lteam_logo = data.get('data')[rand_num]['teams'][0]['logos'][random.randint(0, len(data.get('data')[rand_num]['teams'][0]['logos']) - 1)]['url']


    if (lteam_name == "") & (lteam_logo == ""):
        return redirect(url_for('randnhllogo'))
    else:
        return render_template("randnhllogo.html",
        l_name=lteam_name,
        l_logo=lteam_logo)

if __name__ == "__main__":
    app.debug = True
    app.run()
