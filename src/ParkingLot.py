from Exceptions import MultipleSingletonInstantiationException
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
        """ Virtually private constructor. """
        if ParkingLot.__instance != None:
            raise MultipleSingletonInstantiationException("class instance already created")
        else:
            ParkingLot.__instance = self
            self.__capacity = capacity
            self.__size = 0 

    def park_vehicle(self,type,registration_number,color):
        if self.__size == 0:
            self.__size+=1 
            return 1 
        elif self.__size == self.__capacity:
            return None 
        else:
            self.__size+=1 
            return self.__size

    def vehicle_exit(self,slot_number):
        self.__size-=1 
        return slot_number
    
