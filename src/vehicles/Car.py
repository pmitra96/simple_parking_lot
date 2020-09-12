from Vehicle import Vehicle 


class Car(Vehicle):
    def __init__(self,registration_number,color):
        Vehicle.__init__(self,registration_number,color)
        
    def get_slot(self):
        return self.__slot

    def assign_slot(self,slot):
        self.__slot = slot
    
    