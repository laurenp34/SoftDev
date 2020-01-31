#Derek Leung and Lauren Pehlivanian
#SoftDev1 pd 9
#K#15 -- Do I Know You?
#2019-10-04

from flask import Flask, render_template, request, redirect, url_for, session
import os


app = Flask(__name__)

app.secret_key = os.urandom(32)
username = "Obama"
password = "cactus"

@app.route("/")
def something():
    # check session to see if username and password stored
    if("username" in session and "password" in session):
        # check to see if username and password are correct
        if(session['username'] == username and session['password'] == password):
            # automatically go to welcome if they are correct
            return redirect("/welcome")
    # if not correct, redirect to login page.
    else: return redirect("/login")

@app.route("/login")
def something2():
    # print(url_for("something2"))
    # print(url_for("something"))
    # print(url_for("something3"))
    # print(url_for("something4"))

    # true for both because we don't want to print the wrong user/pw statements.
    # this path only runs the first time the login page is called, never after
    # the user submits the form, so these variables don't matter.
    return render_template("login.html", uMatch=True, pMatch=True)

@app.route("/error")
def something3():
    return render_template("error.html")

@app.route("/welcome")
def something4():
    # check to see if username is stored to print to welcome screen.
    if("username" in session):
        ussername = session['username']
    else: ussername = None
    return render_template("welcome.html",username=ussername)


@app.route("/auth")
def something5():
    #print(request.headers)
    #print(request.args)

    #does the username/password inputed match the static user/pass
    userPassed = request.args['user']==username
    passPassed = request.args['pass']==password

    #if they do match:
    if (userPassed and passPassed):
        #save user/pass to session
        session['username'] = username
        session['password'] = password
        #redirect to welcome page
        return render_template("welcome.html",username=username)
    #they did not match. print login screen(not redirected), with statements saying which (user or pass) was wrong
    return render_template("login.html", uMatch=userPassed, pMatch=passPassed)

#the log out page
@app.route("/auth2")
def something6():
    # remove username and password from session
    session.pop('username')
    session.pop('password')
    # go back to login screen
    return redirect("/")

if __name__ == "__main__":
    app.debug = True;
    app.run()
