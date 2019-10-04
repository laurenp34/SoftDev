#Derek Leung and Lauren Pehlivanian
#SoftDev1 pd 9
#K#15 -- Do I Know You?
#2019-10-04

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def something():
    return redirect("/login")

@app.route("/login")
def something2():
    # print(url_for("something2"))
    # print(url_for("something"))
    # print(url_for("something3"))
    # print(url_for("something4"))
    return render_template("login.html", uMatch=True, pMatch=True)

@app.route("/error")
def something3():
    return render_template("error.html")

@app.route("/welcome")
def something4():
    return render_template("welcome.html")

username = "hi"
password = "hi"

@app.route("/auth")
def something5():
    #print(request.headers)
    #print(request.args)
    userPassed = request.args['user']==username
    passPassed = request.args['pass']==password
    if (userPassed and passPassed):
        return render_template("welcome.html",username=username)
    return render_template("login.html", uMatch=userPassed, pMatch=passPassed)

if __name__ == "__main__":
    app.debug = True;
    app.run()
