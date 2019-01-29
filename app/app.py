from flask import Flask
app = Flask(__name__)
from lib import datamodel

dbmodel = datamodel.DbCon()
dbmodel.createTable()

@app.route("/")
def hello():
    return "Hello World!"