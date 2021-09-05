from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome, My name is Sivakumar kS , This is Udacity final project Blue Deployment Version 1 before rolling update"
app.run(host="0.0.0.0", port=8080, debug=True)
