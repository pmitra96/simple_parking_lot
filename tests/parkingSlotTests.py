import unittest 
from src.ParkingLot import ParkingLot
from src.ParkingSlot import ParkingSlot
from src.vehicles.Car import Car
from src.Exceptions import MultipleSingletonInstantiationException


class parkingSlotTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        print("setting up parking slot tests")
    
    @classmethod 
    def tearDown(cls):
        print("tearing down parking slot tests")

    def setUp(self):
        self.parkingSlot = ParkingSlot(1)
        self.car = Car("KAA-12-BC12",21)

    def tearDown(self):
        self.parkingSlot = None 
        self.car = None 

    def test_get_slot_id(self):
        """ get slot id of the slot """
        self.assertEqual(1,self.parkingSlot.get_slot_id())
    
    def test_assign_vehicle(self):
        """ if vehcile is assigned successfully return the vehicle """
        self.assertEqual(self.car,self.parkingSlot.assign_vehicle(self.car))
    
    def test_get_assigned_vehicle(self):
        """ if parking slot is not empty then assign the vehicle """
        self.parkingSlot.assign_vehicle(self.car)
        car = self.parkingSlot.get_assigned_vehicle()
        self.assertEqual(self.car,car)
    
    def test_get_assigned_vehicle_empty(self):
        """if parking slot is empty return None"""
        self.assertEqual(None,self.parkingSlot.get_assigned_vehicle())

    def test_deassign_vehicle(self):
        """ deassigns the vehicle allocated to slot """
        self.parkingSlot.deassign_vehicle()
        parked_vehicle = self.parkingSlot.get_assigned_vehicle()
        self.assertEqual(None,parked_vehicle)

    
    
    