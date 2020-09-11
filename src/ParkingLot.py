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


    def __init__(self,size):
        """ Virtually private constructor. """
        if ParkingLot.__instance != None:
            raise MultipleSingletonInstantiationException("class instance already created")
        else:
            ParkingLot.__instance = self
            self.__size = size


