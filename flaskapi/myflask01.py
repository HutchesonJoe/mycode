#!/usr/bin/python3
"""First Flask Script"""

from flask import Flask 

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "Hello World"

@app.route("/tgif")
def tgif():
    return "T.G.I.F"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=2224)
