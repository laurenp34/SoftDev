# Klondike -- Nahi Khan, Lauren Pehlivanian and Ahmed Sultan
# SoftDev1 pd 9
# K25 -- Getting more REST
# 2019-11-13

from flask import Flask, render_template
import urllib
import json
import random

app = Flask(__name__)

# countries, currency exchange, & studio ghibli

@app.route("/")
def main():
    u = urllib.request.urlopen("https://restcountries.eu/rest/v2")
    response = u.read()
    data = json.loads(response)

    country_list = []
    #add 3 random countries to data to pass to template
    for i in range(3):
        country_list.append(data[random.randint(0,len(data)-1)])

    u1 = urllib.request.urlopen("https://api.exchangerate-api.com/v4/latest/CAD")
    response1 = u1.read()
    data1 = json.loads(response)

    return render_template("index.html", countries=country_list)
    #return render_template("index.html", header=data[95]['name'], info=data[95]['capital'], pic=data[95]['flag'], currency=data[95]['currencies'][0]['name'], info2=data1['rates']['CNY'])


if __name__ == "__main__":
    app.debug = True
    app.run()
