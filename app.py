from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "rajiv Udacity Final project Blue Deployment Version 1 after rolling update"
app.run(host="0.0.0.0", port=8080, debug=True)
