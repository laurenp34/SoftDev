from flask import Flask, render_template
import randomOccupation as randOcc
from collections import OrderedDict
import jinja2

app = Flask(__name__)

test_dict = {
    'Gardner': 20,
    'Firefighter':10
}

@app.route("/")
def home():
    return "Go to: /occupyflaskst"

@app.route("/occupyflaskst")
def index():
    return render_template(
    "template.html",
    title="SCHUMER - 10_occ",
    header="Fields of occupation, and their percentages",
    subheader="by TEAM CHUCK SCHUMER (Lauren Pehlivanian and Ahmed Sultan, pd 9)",
    random_occupation=randOcc.main(),
    tblHeading1="Occupation",
    tblHeading2="Percent",
    dict=randOcc.dictGenerate("occupations.csv")
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
