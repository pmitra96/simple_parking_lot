from Vehicle import Vehicle 


class Car(Vehicle):
    def __init__(self,registration_number,age):
        Vehicle.__init__(self,registration_number)
        self.__age = age 
   
    def get_slot(self):
        return self.__slot

    def assign_slot(self,slot):
        self.__slot = slot
        return self.__slot
    
    def set_driver_age(self,age):
        self.__age = age 
    
    def get_driver_age(self):
        return self.__age
