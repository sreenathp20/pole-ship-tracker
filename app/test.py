from lib import datamodel

dbmodel = datamodel.DbCon()
dbmodel.createTable()
dbmodel.importCsv()