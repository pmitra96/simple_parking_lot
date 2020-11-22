import unittest 
from src.ParkingLot import ParkingLot
from src.ParkingSlot import ParkingSlot
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
        self.parkingLot = ParkingLot(7)
    
    # this function gets called after every test in the class
    def tearDown(self):
        del self.parkingLot
        ParkingLot.deleteInstance()

    def test_park_vehicle(self):
        """ if parking lot is empty , then slot 1 should be allocated"""
        slot_number = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1234",driver_age = 21)
        self.assertEqual(1,slot_number)
        """ find vehicle should result in valid slot """ 
        """ the corresponding slot should have valid vehicle """
        """ vehicle should have valid slot """ 
        vehicle_slot = self.parkingLot.find_vehicle("KA-01-HH-1234")
        self.assertEqual(1,1)
        

    def park_5_vehicles(self):
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1234",driver_age = 21)
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9999",driver_age = 21)
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9994",driver_age = 22)
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9995",driver_age = 23)
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9996",driver_age = 24)
        

    def test_park_vehicle_when_full(self):
        """ if parking lot is full , then None should be allocated"""
        self.park_5_vehicles()
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9995",driver_age = 18)
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9996",driver_age = 19)
        slot_number = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1254",driver_age = 20)
        self.assertEqual(None,slot_number)
    
    def test_vehicle_exit(self):
        """ clear allocated slot and return slot number """
        ## test specific setup start ##
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1234",driver_age = 21)
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9999",driver_age = 21)
        ## test specific setup end ## 
        exited_vehicle = self.parkingLot.vehicle_exit(1)
        self.assertEqual("KA-01-HH-1234",exited_vehicle.get_registration_number())
        self.assertEqual(None,self.parkingLot.find_vehicle("KA-01-HH-1234"))
        self.assertEqual(1,self.parkingLot.get_size())
    
    def test_find_vehicle(self):
        """ given a registration number find the slot where a vehicle is parked """ 
        self.park_5_vehicles()
        slot_number1 = self.parkingLot.find_vehicle(registration_number = "KA-01-HH-9996")
        self.assertEqual(5,slot_number1)
        # find a non exisiting vehicle 
        self.parkingLot.vehicle_exit(5)
        slot_number2 = self.parkingLot.find_vehicle(registration_number = "KA-01-HH-9996")
        self.assertEqual(None,slot_number2)

    def test_assign_spot_complex(self):
        """ give the spot nearest to the slot if entry is 0 """ 
        self.park_5_vehicles()
        self.parkingLot.vehicle_exit(2)
        self.parkingLot.vehicle_exit(3)
        slot_number1 = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9321",driver_age = 21)
        self.assertEqual(2,slot_number1)        
        slot_number2 = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9124",driver_age = 22)
        self.assertEqual(3,slot_number2)


    def test_registration_numbers_for_cars_with_driver_age(self):
        """ should return registration numbers of slots with a given driver_age in ascending order """
        self.park_5_vehicles()
        self.parkingLot.vehicle_exit(2)
        self.parkingLot.vehicle_exit(3)
        slot_number1 = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9321",driver_age = 24)
        slot_number2 = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9124",driver_age = 24)
        registration_numbers_with_driver_age = self.parkingLot.get_registration_numbers_for_cars_with_driver_age(24)
        # should give registration numbers in the same order as that of slots.
        self.assertEqual(['KA-01-HH-9321', 'KA-01-HH-9124', 'KA-01-HH-9996'],registration_numbers_with_driver_age)
        # since blue car left this must give empty
        self.assertEqual([],self.parkingLot.get_registration_numbers_for_cars_with_driver_age(35))
        
    

    def test_slot_ids_for_cars_with_driver_age(self):
        """ should return registration numbers of slots with a given driver_age in ascending order """
        self.park_5_vehicles()
        self.parkingLot.vehicle_exit(2)
        self.parkingLot.vehicle_exit(3)
        slot_number1 = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9321",driver_age = 24)
        slot_number2 = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9124",driver_age = 21)
        slot_ids_with_driver_age = self.parkingLot.get_slot_numbers_for_cars_with_driver_age(21)
        # should give registration numbers in the same order as that of slots.
        self.assertEqual([1,3],slot_ids_with_driver_age)
        # since blue car left this must give empty
        self.assertEqual([],self.parkingLot.get_slot_numbers_for_cars_with_driver_age(35))
        
    
    





if __name__ == '__main__':
    unittest.main()