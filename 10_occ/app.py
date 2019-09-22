from flask import Flask, render_template
import randomOccupation as randOcc
from collections import OrderedDict
import jinja2

app = Flask(__name__)

test_dict = {
    'Gardner': 20,
    'Firefighter':10
}

@app.route("/occupyflasks")
def index():
    return render_template(
    "template.html",
    title="Team Chuck Schumer",
    header="Lauren and Ahmed, pd. 9",
    tblHeading1="Occupation",
    tblHeading2="Percent",
    dict=test_dict
    )

if __name__ == "__main__":
    app.debug = True
    app.run()
