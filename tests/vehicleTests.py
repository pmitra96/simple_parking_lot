import unittest 
from src.ParkingLot import ParkingLot
from src import ParkingSlot
from src.vehicles import *
from src.Exceptions import MultipleSingletonInstantiationException

#---------------------------------------------------------------------------------------------------#

class CarTests(unittest.TestCase):

# ------------------------------------------------------------------------------------------------- # 

    @classmethod
    def setUp(cls):
        print("setting up vehicles test class")
    
    @classmethod 
    def tearDown(cls):
        print("tearing down vehicle class")

    def setUp(self):
        self.car = Car("KAA-12-BC12","White")
        self.parkingSlot = ParkingSlot(1)
    
    def tearDown(self):
        del self.car
        self.car = None
    
    def test_get_registration_number(self):
        reg_num = self.car.get_registration_number()
        self.assertEqual("KAA-12-BC12",reg_num)

    def test_assign_slot(self):
        assigned_slot = self.car.assign_slot(self.parkingSlot)
        self.assertEqual(1,assigned_slot)

    def test_get_assigned_slot(self):
        assigned_slot = self.car.assign_slot(self.parkingSlot)
        self.assertEqual(assigned_slot,self.car.get_assigned_slot())

