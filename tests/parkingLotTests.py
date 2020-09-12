import unittest 
import sys 
from src.ParkingLot import ParkingLot
from src import ParkingSpot
from src.vehicles import *
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
        

class ParkingLotBasicCRUDTests(unittest.TestCase):

    @classmethod
    def setUp(cls):
        print("setting up ParkingLotFunctionalTests")
    
    @classmethod
    def tearDown(cls):
        print("tearingDown ParkingLotFunctionalTests")
    
    # this function gets called for before every test in the class 
    def setUp(self):
        self.parkingLot = ParkingLot(5)
    
    # this function gets called after every test in the class
    def tearDown(self):
        del self.parkingLot
        ParkingLot.deleteInstance()

    def test_park_vehicle(self):
        """ if parking lot is empty , then slot 1 should be allocated"""
        slot_number = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1234",color = "White")
        self.assertEqual(1,slot_number)
    
    def test_park_vehicle_when_full(self):
        """ if parking lot is full , then None should be allocated"""
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1234",color = "White")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9999",color = "White")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9994",color = "Blue")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9995",color = "Pink")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9996",color = "Red")
        slot_number = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1254",color = "White")
        self.assertEqual(None,slot_number)
    
    def test_vehicle_exit(self):
        """ clear allocated slot and return slot number """
        ## test specific setup start ##
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1234",color = "White")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9999",color = "White")
        ## test specific setup end ## 
        slot_number = self.parkingLot.vehicle_exit(1)
        self.assertEqual(1,slot_number)
    
    def test_find_vehicle(self):
        """ given a registration number find the slot where a vehicle is parked """ 
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1234",color = "White")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9999",color = "White")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9994",color = "Blue")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9995",color = "Pink")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9996",color = "Red")
        slot_number = self.parkingLot.find_vehicle(registration_number = "KA-01-HH-9996")
        self.assertEqual(5,slot_number)

    def test_assign_spot_complex(self):
        """ give the spot nearest to the slot if entry is 0 """ 
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1234",color = "White")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9999",color = "White")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9994",color = "Blue")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9995",color = "Pink")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9996",color = "Red")
        self.parkingLot.vehicle_exit(2)
        self.parkingLot.vehicle_exit(3)
        slot_number1 = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9321",color = "fieryRed")
        self.assertEqual(2,slot_number1)        
        slot_number2 = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9124",color = "fieryRed")
        self.assertEqual(3,slot_number2)






if __name__ == '__main__':
    unittest.main()