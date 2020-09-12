from src.Exceptions import MultipleSingletonInstantiationException
from src.ParkingSlot import ParkingSlot
from src.SlotManager import SlotManager
from src.vehicles.Car import Car

class ParkingLot:
    __instance = None
    @staticmethod
    def getorCreateParkingLot(size):
      """ Static access method. """
      if ParkingLot.__instance == None:
         ParkingLot(size)
      return ParkingLot.__instance
    
    @staticmethod
    def deleteInstance():
        ParkingLot.__instance = None 

    def __init__(self,capacity):
        """ ----- Virtually private constructor. ----- """
        if ParkingLot.__instance != None:
            raise MultipleSingletonInstantiationException("class instance already created")
        else:
            ParkingLot.__instance = self
            self.__capacity = capacity
            self.__slotManager = SlotManager(self,self.__capacity)

    def park_vehicle(self,vehicle_type,registration_number,color):
        return self.__slotManager.park_vehicle(vehicle_type,registration_number,color)

    def vehicle_exit(self,slot_id):
        return self.__slotManager.vehicle_exit(slot_id)

    def find_vehicle(self,registration_number):
        return self.__slotManager.find_vehicle(registration_number)
    
    def get_registration_numbers_for_cars_with_color(self,color):
        return self.__slotManager.registration_numbers_for_cars_with_color(color)
    
    def get_slot_numbers_for_cars_with_color(self,color):
        return self.__slotManager.slot_numbers_for_cars_with_color(color)

    def get_size(self):
        return self.__slotManager.get_size()
    
    def get_capacity(self):
        return self.__capacity
    

    def get_status(self):
        return self.__slotManager.get_status()