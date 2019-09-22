from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
def hello_world():
    print(__name__)
    return "no hablo queso!"

data = coll = [0,1,1,2,3,5,8]

@app.route("/my_foist_template")
def createpage():
    print(__name__) #where will this go?
    return render_template("template.html", header_text="DATA", title="Lauren!", seq=data)

if __name__ == "__main__":
    app.debug = True
    app.run()
