from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return "no hablo queso!"

@app.route("/breakfast")
def greeting():
    print("scrambled eggs")
    return "Good morning! Breakfast is important"

@app.route("/lunch")
def lunch():
    print("hamburger")
    return "Do not forget to eat lunch!"

@app.route("/dinner")
def dinner():
    print("lasagna")
    return "Have a good sleep"

if __name__ == "__main__":
    app.debug = True
    app.run()
