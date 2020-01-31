from flask import Flask, render_template, request
import random
app = Flask(__name__)

@app.route("/auth")
def route():
    print("\n\n\n")
    print("***DIAG: this Flask obj ***")
    print(app)
    print("***DIAG: request obj***")
    print(request)
    print("***DIAG: request.args***")
    print(request.args)
    # print("***DIAG: request.args['firstname']***")
    # print(request.args['firstname'])
    print("***DIAG: request.args['username']***")
    print(request.args['username'])
    print("***DIAG: request.headers***")
    print(request.headers)
    return render_template(
        "authpage.html",
        username=request.args['username']
    )
###@app.route("/")
##def render_static(page_name):
#    return render_template('%s.html' % page_name)

@app.route("/foo")
def occupy():
    print("foo")
    return render_template("foo.html")
@app.route("/")
def occupy2():
    print("foo2")
    return render_template("foo2.html")
if __name__ == "__main__":
    app.debug = True
    app.run()
