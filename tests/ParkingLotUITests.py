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
        response = self.parkingLotUI.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1234",color = "White")
        self.assertEqual("Allocated slot number: 1",response)
        

    def park_5_vehicles(self):
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1234",color = "White")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9999",color = "White")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9994",color = "Blue")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9995",color = "Pink")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9996",color = "Red")
        

    def test_park_vehicle_when_full(self):
        """ if parking lot is full , then None should be allocated"""
        self.park_5_vehicles()
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9995",color = "Pink")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9996",color = "Red")
        response = self.parkingLotUI.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1254",color = "White")
        self.assertEqual("Sorry, parking lot is full",response)
    
    def test_vehicle_exit(self):
        """ clear allocated slot and return slot number """
        ## test specific setup start ##
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1234",color = "White")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9999",color = "White")
        ## test specific setup end ## 
        response = self.parkingLotUI.vehicle_exit(1)
        self.assertEqual("Slot number 1 is free",response)
        
    
    def test_find_vehicle(self):
        """ given a registration number find the slot where a vehicle is parked """ 
        self.park_5_vehicles()
        slot_number1 = self.parkingLotUI.find_vehicle(registration_number = "KA-01-HH-9996")
        self.assertEqual("5",slot_number1)
        # find a non exisiting vehicle 
        self.parkingLot.vehicle_exit(5)
        slot_number2 = self.parkingLot.find_vehicle(registration_number = "KA-01-HH-9996")
        self.assertEqual("Not found",slot_number2)

    def test_registration_numbers_for_cars_with_color(self):
        """ should return registration numbers of slots with a given color in ascending order """
        self.park_5_vehicles()
        self.parkingLot.vehicle_exit(2)
        self.parkingLot.vehicle_exit(3)
        slot_number1 = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9321",color = "White")
        slot_number2 = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9124",color = "fieryRed")
        registration_numbers_with_color = self.parkingLotUI.get_registration_numbers_for_cars_with_color("White")
        # should give registration numbers in the same order as that of slots.
        self.assertEqual("KA-01-HH-1234, KA-01-HH-9321",registration_numbers_with_color)
        ## TODO : verify this 
        # since blue car left this must give empty
        self.assertEqual("No cars with given color",self.parkingLotUI.get_registration_numbers_for_cars_with_color("Blue"))
        
    

    def test_slot_ids_for_cars_with_color(self):
        """ should return registration numbers of slots with a given color in ascending order """
        self.park_5_vehicles()
        self.parkingLot.vehicle_exit(2)
        self.parkingLot.vehicle_exit(3)
        slot_number1 = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9321",color = "White")
        slot_number2 = self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9124",color = "fieryRed")
        slot_ids_with_color = self.parkingLot.get_slot_numbers_for_cars_with_color("White")
        # should give registration numbers in the same order as that of slots.
        self.assertEqual("1, 2, 4",slot_ids_with_color)
        # since blue car left this must give empty
        ## TODO : verify this 
        self.assertEqual("No cars with given color",self.parkingLot.get_slot_numbers_for_cars_with_color("Blue"))
        
    def test_get_status_list(self):
        # self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-1234",color = "White")
        # self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9999",color = "White")
        # self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9994",color = "Blue")
        # self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9995",color = "Pink")
        # self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9996",color = "Red")
        self.park_5_vehicles()
        self.parkingLot.vehicle_exit(2)
        self.parkingLot.vehicle_exit(3)  
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9321",color = "White")
        self.parkingLot.park_vehicle(vehicle_type = "car",registration_number = "KA-01-HH-9124",color = "FieryRed")
        response = self.parkingLotUI.get_status_list()
        expectedResponse = [
            "Slot No.   Registration No     Colour      ",
            "1          KA-01-HH-1234       White       ",
            "2          KA-01-HH-9321       White       ",                        
            "3          KA-01-HH-9124       FieryRed    ",
            "4          KA-01-HH-9995       Pink        ",
            "5          KA-01-HH-9996       Red         "
        ]
        self.assertEqual(expectedResponse,response)        
