class ParkingLotUI:
    def __init__(self,parking_lot):
        self.parkingLot = parking_lot

    def park_vehicle(self,vehicle_type,registration_number,color):
        assigned_slot= self.parkingLot.park_vehicle(vehicle_type,registration_number,color)
        if assigned_slot is None:
            return "Sorry, parking lot is full"
        else:
            return "Allocated slot number: " + str(assigned_slot)

    def vehicle_exit(self,slot_id):
        freed_slot = self.parkingLot.vehicle_exit(slot_id)
        return "Slot number " + str(freed_slot) + " is free"

    def find_vehicle(self,registration_number):
        vehicle_slot_id = self.parkingLot.find_vehicle(registration_number)
        if vehicle_slot_id is None:
            return "Not found"
        else:
            return str(vehicle_slot_id)

    def get_registration_numbers_for_cars_with_color(self,color):
        result = self.parkingLot.get_registration_numbers_for_cars_with_color(color)
        if result == []:
            return "No cars with given color"
        else:
           return ", ".join(result)
            
    def get_slot_numbers_for_cars_with_color(self,color):
        result= self.parkingLot.get_slot_numbers_for_cars_with_color(color)
        if result == []:
            return "No cars with given color"
        else:
            return ", ".join([str(x) for x in result])

    def get_status_list(self):
        status_list = self.parkingLot.get_status()
        if status_list != []:
            final_status_list = []
            header = "Slot No.".ljust(10) + "Registration No".ljust(20) + "Colour".ljust(10) 
            final_status_list.append(header)
            for slot_info in status_list:
                formatted_string = self.format_slot_information(slot_info)
                final_status_list.append(formatted_string)
            return final_status_list
        else:
            return []
        
    def format_slot_information(self,slot_info):
        s = ""
        s+=slot_info[0].ljust(10)
        s+=slot_info[1].ljust(20)
        s+=slot_info[2].ljust(10)
        return s 


