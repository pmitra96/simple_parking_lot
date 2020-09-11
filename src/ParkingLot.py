
class ParkingLot:
    parkingLotInstance = None 
    class __ParkingLotSingleton:
        def __init__(self,size):
            pass
    
    def __init__(self,size):
        return ParkingLot.parkingLotInstance