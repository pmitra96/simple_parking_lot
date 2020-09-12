
class ParkingSlot:
    def __init__(self,slot_id):
        self.__slot_id = slot_id 
        self.__vehicle = None 

    def is_slot_free(self):
        return self.__is_free
    
    def assign_vehicle(self,vehicle):
        self.__vehicle = vehicle
        return self.__vehicle
    
    def deassign_vehicle(self):
        self.__vehicle = None 
        
    def get_slot_id(self):
        return self.__slot_id

    def get_assigned_vehicle(self):
        return self.__vehicle

    def __repr__(self):
        if self.__vehicle:
            return "slot_id : " + str(self.__slot_id) + " vehicle_parked : " + str(self.__vehicle)
        else:
             return "slot_id : " + str(self.__slot_id) + " vehicle_parked : None" 
        

