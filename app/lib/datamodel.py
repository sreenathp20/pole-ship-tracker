import sqlite3
import csv

class DbCon:
    def __init__(self):
        self.conn = sqlite3.connect('test.db')

    def createTable(self):
        self.conn.execute('''CREATE TABLE SHIPS
         (ID INT PRIMARY KEY     NOT NULL,
         NAME           TEXT    NOT NULL,
         IMO            INT     NOT NULL);''')
        self.conn.execute('''CREATE TABLE POSITION
         (ID INT PRIMARY KEY     NOT NULL,
         IMO           INT    NOT NULL,
         TIMESTAMP            DATETIME     NOT NULL,
         LATITUDE            TEXT     NOT NULL,
         LONGITUDE            TEXT     NOT NULL);''')
        print ("Tables created successfully")

    def importCsv(self):        
        with open('data/positions.csv', 'r') as csvfile:
            csvreader = csv.reader(csvfile, delimiter=',', quotechar='|')
            for row in csvreader:
                print (row)


# self.conn.execute('''CREATE TABLE COMPANY
#          (ID INT PRIMARY KEY     NOT NULL,
#          NAME           TEXT    NOT NULL,
#          AGE            INT     NOT NULL,
#          ADDRESS        CHAR(50),
#          SALARY         REAL);''')
