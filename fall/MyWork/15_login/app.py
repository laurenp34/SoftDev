#Derek Leung and Lauren Pehlivanian
#SoftDev1 pd 9
#K#15 -- Do I Know You?
#2019-10-04

from flask import Flask, render_template, request, redirect, url_for, session
import os

app = Flask(__name__)

app.secret_key = os.urandom(32)

@app.route("/")
def something():
    print(session)
    return redirect(url_for("login"))

@app.route("/login")
def login():
    # print(url_for("something2"))
    # print(url_for("something"))
    # print(url_for("something3"))
    # print(url_for("something4"))

    print(session)

    if "user" in session and "pass" in session:
        return redirect(url_for("welcomePage"))

    #This represents the first time the login page is reached.
    return render_template("login.html")

@app.route("/error")
def something3():
    return render_template("error.html")

@app.route("/welcome")
def welcomePage():
    return render_template("welcome.html", username=username)

username = "Jorja Smith"
password = "go away"

@app.route("/auth")
def something5():
    #print(request.headers)
    #print(request.args)

    userPassed = request.args['user']==username
    passPassed = request.args['pass']==password


    if (userPassed and passPassed):
        session["user"] = username
        session["pass"] = password
        #print(session)
        return redirect(url_for("welcomePage"))

    # redirect(url_for("/login",userPassed, passPassed))
    return render_template("login.html", uMatch=userPassed, pMatch=passPassed)

@app.route("/logout")
def loggedout():
    session.pop("user")
    session.pop("pass")
    return "Logged out!"

if __name__ == "__main__":
    app.debug = True;
    app.run()
