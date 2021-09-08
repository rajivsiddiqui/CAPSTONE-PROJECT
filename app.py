from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Welcome, My name is Sivakumar KS , This is Udacity final project Green Deployment Version 2 after rolling update"
app.run(host="0.0.0.0", port=8080, debug=True)
