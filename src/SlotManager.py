from src.ParkingSlot import ParkingSlot
from src.vehicles.Car import Car
class SlotManager:
    def __init__(self,parking_lot,capacity):
        self.parking_lot = parking_lot
        self.__SlotsMap = {}
        self.__parkedCarsMap = {}
        self.__size = 0 
        self.__capacity =  capacity
        self.initialize_slots()
        
    def initialize_slots(self):
        for i in range(1,self.__capacity+1):
            self.__SlotsMap[i] = (ParkingSlot(i))
        
    def park_vehicle(self,vehicle_type,registration_number,color):
        if self.__size == self.__capacity:
            return None 
        else:
            if vehicle_type == "car":
               return self.park_vehicle_internal(registration_number,color)
            else:
                raise NotImplementedError

    def park_vehicle_internal(self,registration_number,color):
        # create car
        car = Car(registration_number,color)
        # get free slot 
        free_slot_id = self.get_free_slot_id()   
        free_slot = self.__SlotsMap[free_slot_id]
        free_slot.assign_vehicle(car)
        car.assign_slot(free_slot)
        # add car to parked cars 
        self.__parkedCarsMap[registration_number] = car
        self.__size+=1
        return free_slot_id

    def get_free_slot_id(self):
        ## TODO : optimize this 
        minSlot = self.__capacity+1
        for slot_id,slot in self.__SlotsMap.items():
            if slot.get_assigned_vehicle() is None:
                minSlot = min(minSlot,slot_id)
        return minSlot
        
    def vehicle_exit(self,slot_id):
        slot = self.__SlotsMap[slot_id]
        current_vehicle = slot.get_assigned_vehicle()
        if current_vehicle is None:
            return slot_id
        else:
            registration_number = current_vehicle.get_registration_number()
            del self.__parkedCarsMap[registration_number]
            slot.deassign_vehicle()
            self.__size -= 1
            return slot_id

    def find_vehicle_slot(self,registration_number):
        if registration_number in self.__parkedCarsMap:
            return self.__parkedCarsMap[registration_number].get_slot()
        else:
            return None

    def find_vehicle(self,registration_number):
        vehicle_slot = self.find_vehicle_slot(registration_number)
        if vehicle_slot is not None:
            return vehicle_slot.get_slot_id()
        else:
            return None

    def get_slots_having_cars_with_color(self,color):
        result_list = []
        for i in range(1,self.__capacity+1):
            if self.__SlotsMap[i].get_assigned_vehicle() is not None:
                slot = self.__SlotsMap[i]
                assigned_vehicle = slot.get_assigned_vehicle()
                vehicle_color = assigned_vehicle.get_color()
                if vehicle_color == color:
                    result_list.append(slot)
        return result_list

    def registration_numbers_for_cars_with_color(self,color):
        slots_with_color = self.get_slots_having_cars_with_color(color)
        return [slot.get_assigned_vehicle().get_registration_number() for slot in slots_with_color]

    def slot_numbers_for_cars_with_color(self,color):
        slots_with_color = self.get_slots_having_cars_with_color(color)
        return [slot.get_slot_id() for slot in slots_with_color]

    def get_status(self):
        result_list = []
        for i in range(1,self.__capacity+1):
            if self.__SlotsMap[i].get_assigned_vehicle() is not None:
                slot = self.__SlotsMap[i]
                assigned_vehicle = slot.get_assigned_vehicle()
                vehicle_color = assigned_vehicle.get_color()
                vehicle_registration_number = assigned_vehicle.get_registration_number()
                result_list.append((i,vehicle_registration_number,vehicle_color))
        return result_list

    def get_slots_map(self):
        return self.__SlotsMap

    def get_parked_cars_map(self):
        return self.__parkedCarsMap
    
    def get_size(self):
        return self.__size