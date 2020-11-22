class ParkingLotUI:
    def __init__(self,parking_lot):
        self.parkingLot = parking_lot

    def park_vehicle(self,vehicle_type,registration_number,driver_age):
        assigned_slot= self.parkingLot.park_vehicle(vehicle_type,registration_number,driver_age)
        if assigned_slot is None:
            return "Sorry, parking lot is full"
        else:
            
            return "Car with vehicle registration number {} has been parked at slot number {}".format(registration_number,assigned_slot)

    def vehicle_exit(self,slot_id):
        exited_vehicle = self.parkingLot.vehicle_exit(slot_id)
        if exited_vehicle != None:
            return "Slot number {} vacated ,the car with vehicle registration number {} left the space, the driver of the car was of age {}".format(slot_id,exited_vehicle.get_registration_number(),exited_vehicle.get_driver_age()) 
        else:
            return "null"
    def find_vehicle(self,registration_number):
        vehicle_slot_id = self.parkingLot.find_vehicle(registration_number)
        if vehicle_slot_id is None:
            return "null"
        else:
            return str(vehicle_slot_id)

    def get_registration_numbers_for_cars_with_driver_age(self,driver_age):
        result = self.parkingLot.get_registration_numbers_for_cars_with_driver_age(driver_age)
        if result == []:
            return "null"
        else:
           return ", ".join(result)
            
    def get_slot_numbers_for_cars_with_driver_age(self,driver_age):
        result= self.parkingLot.get_slot_numbers_for_cars_with_driver_age(driver_age)
        if result == []:
            return "null"
        else:
            return ",".join([str(x) for x in result])

    def get_status_list(self):
        status_list = self.parkingLot.get_status()
        if status_list != []:
            final_status_list = []
            header = "Slot No.".ljust(10) + "Registration No".ljust(20) + "Age".ljust(10) 
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


