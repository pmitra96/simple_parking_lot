import unittest 
import sys 
from src.ParkingLot import ParkingLot
from src.Exceptions import MultipleSingletonInstantiationException

def setUpModule():
        print("setup module")
def tearDownModule():
        print("teardown module")
class parkingLotSingletonTests(unittest.TestCase):

    @classmethod
    def setUp(cls):
        print("setup parkingLotTests")
    
    @classmethod
    def tearDown(cls):
        print("teardown parkingLotTests")
    
    # this function gets called for before every test in the class 
    def setUp(self):
        self.parkingLot = ParkingLot(5)
    
    # this function gets called after every test in the class
    def tearDown(self):
        del self.parkingLot
        ParkingLot.deleteInstance()

    ## BASIC UTILITIES START ##

    def create_parking_lot(self):
        ParkingLot(5)

    ## BASIC UTILITIES END ##

    def test_multiple_class_instantiation(self):
        """ creation of multiple instances should raise Exception """
        self.assertRaises(MultipleSingletonInstantiationException,self.create_parking_lot)
        
    def test_get_or_create_parking_lot(self):
        """ creates an instance if not present , if an instance is already created ,then return it  """
        self.assertIsInstance(self.parkingLot,ParkingLot) 
        
    def test_get_or_create_multiple_instances(self):
        """ if test_get_or_create_multiple_instances is called multiple times , same object must be returned """
        newInstance = ParkingLot.getorCreateParkingLot(5)
        self.assertEqual(self.parkingLot,newInstance)
        
if __name__ == '__main__':
    unittest.main()