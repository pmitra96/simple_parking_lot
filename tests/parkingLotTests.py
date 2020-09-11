import unittest 
import sys 
from src import ParkingLot
class parkingLotTests(unittest.TestCase):

    def get_parking_lot_test_(self):
        self.assertEqual(ParkingLot(5),None)        
    