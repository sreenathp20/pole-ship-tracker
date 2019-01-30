from flask import Flask, render_template
import json
app = Flask(__name__)
from lib import datamodel

#dbmodel.createTable()

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/api/ships/")
def ships():
    print("hi")
    dbmodel = datamodel.DbCon()
    ships = dbmodel.getShips()
    return json.dumps(ships)

@app.route("/api/positions/<imo>/")
def positions(imo):
    print("imo ", imo)
    dbmodel = datamodel.DbCon()
    positions = dbmodel.getPositions(imo)
    return json.dumps(positions)