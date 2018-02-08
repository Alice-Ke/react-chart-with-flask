from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route("/honey")
def hello():
    return "Have a good day, honey!"