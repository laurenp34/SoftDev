from flask import Flask, render_template
import randomOccupation as randOcc

app = Flask(__name__)

@app.route("/occupyflasks")
def index():
    return randOcc.main()

if __name__ == "__main__":
    app.debug = True
    app.run()
