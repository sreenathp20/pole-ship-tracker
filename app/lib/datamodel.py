import sqlite3
import csv

class DbCon:
    def __init__(self):
        self.conn = sqlite3.connect('pole.db')

    def createTable(self):
        self.conn.execute('''DROP TABLE IF EXISTS SHIPS;''')
        self.conn.execute('''CREATE TABLE SHIPS
         (ID INTEGER PRIMARY KEY AUTOINCREMENT  NOT NULL,
         NAME           TEXT    NOT NULL,
         IMO            INT     NOT NULL);''')
        self.conn.execute('''DROP TABLE IF EXISTS POSITION;''')
        self.conn.execute('''CREATE TABLE POSITION
         (ID INTEGER PRIMARY KEY  NOT NULL,
         IMO           TEXT    NOT NULL,
         TIMESTAMP            DATETIME     NOT NULL,
         LATITUDE            TEXT     NOT NULL,
         LONGITUDE            TEXT     NOT NULL);''')
        print ("Tables created successfully")

    def insertShips(self, ships):
        self.conn.executemany("INSERT INTO SHIPS(NAME, IMO) VALUES (?, ?)", ships)
        self.conn.commit()
        print ("Ships inserted successfully")

    def importCsv(self):        
        with open('data/positions.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            datas = []
            for row in csvreader:
                #print (row)
                data = (row[0], row[1], row[2], row[3])
                datas.append(data)
                #examples = [(2, "def"), (3, "ghi"), (4, "jkl")]
            self.conn.executemany("INSERT INTO POSITION(IMO, TIMESTAMP, LATITUDE, LONGITUDE) VALUES (?, ?, ?, ?)", datas)
            self.conn.commit()
            print ("Positions inserted successfully")

    def getShips(self):
        print("hi getShips" )
        cursor = self.conn.execute("SELECT IMO, NAME FROM SHIPS;")
        ships = []
        for row in cursor:
            print(row, " row")
            data = {"name": row[1], "imo": row[0]}
            ships.append(data)
        return ships

    def getPositions(self, imo):
        cursor = self.conn.execute("SELECT TIMESTAMP, LATITUDE, LONGITUDE FROM POSITION WHERE IMO = '"+imo+"' ORDER BY  TIMESTAMP DESC;")
        positions = []
        for row in cursor:
            print(row, " row")
            data = {"timestamp": row[0], "latitude": row[1], "longitude": row[2]}
            positions.append(data)
        return positions

    def getAllPositions(self):
        cursor = self.conn.execute("SELECT TIMESTAMP, LATITUDE, LONGITUDE FROM POSITION ORDER BY  TIMESTAMP DESC;")
        positions = []
        for row in cursor:
            data = {"timestamp": row[0], "latitude": row[1], "longitude": row[2]}
            positions.append(data)
        return positions
