from lib import datamodel

ships = [("Mathilde Maersk", "9632179"), ("Australian Spirit", "9247455"), ("MSC Preziosa", "9595321")]

class Test():
    def __init__(self):
        dbmodel = datamodel.DbCon()
        dbmodel.createTable()
        dbmodel.insertShips(ships)
        dbmodel.importCsv()
        

