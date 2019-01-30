import test
from lib import datamodel
dbmodel = datamodel.DbCon()
# content of test_class.py
class TestClass(object):
    def test_one(self):
        t = test.Test()        
        ships = dbmodel.getShips()
        assert len(ships), 3

    def test_two(self):
        no_of_positions = dbmodel.getAllPositions()
        assert no_of_positions, 2000