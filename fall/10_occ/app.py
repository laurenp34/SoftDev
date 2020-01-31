#   Lauren Pehlivanian, Ahmed Sultan
#   SoftDev1 pd9
#   K10 -- Jinja Tuning
#   2019-09-24

from flask import Flask, render_template
import randomOccupation as randOcc
from collections import OrderedDict
import jinja2

app = Flask(__name__)

links = {
    'Management': 'https://www.thebalancecareers.com/getting-a-first-management-job-2275109',
    "Business and Financial operations": "http://www.careers.org/occupations/field/13/business-and-financial-operations",
    "Computer and Mathematical": "http://www.careers.org/occupations/field/15/computer-and-mathematical",
    "Architecture and Engineering": "http://www.careers.org/occupations/field/17/architecture-and-engineering",
    "Life, Physical and Social Science": "https://collegegrad.com/careers/life-physical-and-social-science",
    "Community and Social Service": "https://www.bls.gov/ooh/community-and-social-service/health-educators.htm#tab-4",
    "Legal": "https://www.bls.gov/ooh/legal/paralegals-and-legal-assistants.htm",
    "Education, training and library": "https://www.bls.gov/ooh/education-training-and-library/home.htm",
    "Arts, design, entertainment, sports and media" : "https://www.bls.gov/ooh/arts-and-design/home.htm",
    "Healthcare practioners and technical": "https://www.bls.gov/ooh/healthcare/home.htm",
    "Healthcare support": "https://www.bls.gov/ooh/healthcare/medical-assistants.htm",
    "Protective service": "https://www.bls.gov/ooh/protective-service/home.htm",
    "Food preparation and serving": "https://www.bls.gov/ooh/food-preparation-and-serving/home.htm",
    "Building and grounds cleaning and maintenance": "https://www.bls.gov/ooh/building-and-grounds-cleaning/home.htm",
    "Personal care and service": "https://www.bls.gov/ooh/personal-care-and-service/home.htm",
    "Sales": "https://www.bls.gov/ooh/sales/home.htm",
    "Office and administrative support": "https://www.bls.gov/ooh/office-and-administrative-support/home.htm",
    "Farming, fishing and forestry": "https://www.bls.gov/ooh/farming-fishing-and-forestry/home.htm",
    "Construction and extraction": "https://www.bls.gov/ooh/construction-and-extraction/home.htm",
    "Installation, maintenance and repair": "https://www.bls.gov/ooh/installation-maintenance-and-repair/home.htm",
    "Production": "https://www.bls.gov/ooh/production/home.htm",
    "Transportation and material moving": "https://www.bls.gov/ooh/transportation-and-material-moving/home.htm",
}

@app.route("/occupyflaskst")

def occ():
    return render_template(
        "template.html",
        title="SCHUMER - 10_occ",
        header="Fields of occupation, and their percentages",
        subheader="by TEAM CHUCK SCHUMER (Lauren Pehlivanian and Ahmed Sultan, pd 9)",
        random_occupation=randOcc.main(),
        tblHeading1="Occupation",
        tblHeading2="Percent",
        tblHeading3="Link",
        occDict=randOcc.dictGenerate("occupations.csv"),
        linkDict=links

    )



@app.route("/")
def root():
    return "Hi! Check out /occupyflaskst for the assignment."



if __name__ == "__main__":
    app.debug = True
    app.run()
