import unittest 
import sys 
from src.ParkingLot import ParkingLot
from src.ParkingSlot import ParkingSlot
from src.ParkingLotUI import ParkingLotUI
from src.vehicles import *
from src.Exceptions import MultipleSingletonInstantiationException

class ParkingLotUITests(unittest.TestCase):
    
    def setUp(self):
        self.parkingLot = ParkingLot(7)
        self.parkingLotUI = ParkingLotUI(self.parkingLot)

    def tearDown(self):
        del self.parkingLot
        del self.parkingLotUI
        ParkingLot.deleteInstance()

    def test_park_vehicle(self):
        """ if parking lot is empty , then slot 1 should be allocated"""
        response = self.parkingLotUI.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1234",driver_age = 21)
        self.assertEqual("Car with vehicle registration number KA-01-HH-1234 has been parked at slot number 1",response)
        

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
        response = self.parkingLotUI.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1254",driver_age = 20)
        self.assertEqual("Sorry, parking lot is full",response)
    
    def test_vehicle_exit(self):
        """ clear allocated slot and return slot number """
        ## test specific setup start ##
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1234",driver_age = 18)
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9999",driver_age = 19)
        ## test specific setup end ## 
        response = self.parkingLotUI.vehicle_exit(1)
        self.assertEqual("Slot number 1 vacated ,the car with vehicle registration number KA-01-HH-1234 left the space, the driver of the car was of age 18",response)
        
    
    def test_find_vehicle(self):
        """ given a registration number find the slot where a vehicle is parked """ 
        self.park_5_vehicles()
        slot_number1 = self.parkingLotUI.find_vehicle(registration_number = "KA-01-HH-9996")
        self.assertEqual("5",slot_number1)
        # find a non exisiting vehicle 
        self.parkingLot.vehicle_exit(5)
        slot_number2 = self.parkingLotUI.find_vehicle(registration_number = "KA-01-HH-9996")
        self.assertEqual("null",slot_number2)

    def test_registration_numbers_for_cars_with_driver_age(self):
        """ should return registration numbers of slots with a given color in ascending order """
        self.park_5_vehicles()
        self.parkingLot.vehicle_exit(2)
        self.parkingLot.vehicle_exit(3)
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9321",driver_age = 21)
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9124",driver_age = 10)
        registration_numbers_with_driver_age = self.parkingLotUI.get_registration_numbers_for_cars_with_driver_age(21)
        # should give registration numbers in the same order as that of slots.
        self.assertEqual("KA-01-HH-1234, KA-01-HH-9321",registration_numbers_with_driver_age)
        ## TODO : verify this 
        # since blue car left this must give empty
        self.assertEqual("null",self.parkingLotUI.get_registration_numbers_for_cars_with_driver_age(5))
        
    

    def test_slot_ids_for_cars_with_driver_age(self):
        """ should return registration numbers of slots with a given color in ascending order """
        self.park_5_vehicles()
        self.parkingLot.vehicle_exit(2)
        self.parkingLot.vehicle_exit(3)
        slot_number1 = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9321",driver_age = 21)
        slot_number2 = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9124",driver_age = 29)
        slot_ids_with_driver_age = self.parkingLotUI.get_slot_numbers_for_cars_with_driver_age(21)
        # should give registration numbers in the same order as that of slots.
        self.assertEqual("1,2",slot_ids_with_driver_age)
        # since blue car left this must give empty
        ## TODO : verify this 
        self.assertEqual("null",self.parkingLotUI.get_slot_numbers_for_cars_with_driver_age(30))
        
    