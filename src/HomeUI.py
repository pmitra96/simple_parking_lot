from src.ParkingLot import ParkingLot
from src.ParkingLotUI import ParkingLotUI
from config.instructionSetConstants import *
import sys

class HomeUI:
    def __init__(self):
        self.parkingLotUI = None
        self.__validCommands = set([ 
                                    CREATE_PARKING_LOT,
                                    PARK_CAR,CAR_EXIT,
                                    GET_SLOTS_HAVING_CAR_OF_DRIVER_AGE,
                                    GET_REGISTRATION_NUMBERS_HAVING_DRIVER_AGE,
                                    SEARCH_SLOT_BY_REGISTRATION_NUMBER,
                                    EXIT_UI])
        self.__commandsExecuted = []

    def create_parking_lot_ui(self, capacity):
        parking_lot = ParkingLot(capacity)
        parking_lot_ui = ParkingLotUI(parking_lot)
        self.parkingLotUI = parking_lot_ui
        print("Created parking of " +str(capacity) + " slots" )
    
    def run_command(self, command):
        if command[0] == CREATE_PARKING_LOT:
            if self.parkingLotUI:
               print("parking lot is already created")
            else:
                self.create_parking_lot_ui(int(command[1])) 
        elif command[0] != CREATE_PARKING_LOT:
            if self.parkingLotUI:
                if command[0] == PARK_CAR:
                    print(self.parkingLotUI.park_vehicle(vehicle_type="car",registration_number = command[1],driver_age = command[3]))
                elif command[0] == CAR_EXIT:
                    print(self.parkingLotUI.vehicle_exit(slot_id = int(command[1])))
                elif command[0] == SEARCH_SLOT_BY_REGISTRATION_NUMBER:
                    print(self.parkingLotUI.find_vehicle(command[1]))
                elif command[0] == GET_SLOTS_HAVING_CAR_OF_DRIVER_AGE:
                    print(self.parkingLotUI.get_slot_numbers_for_cars_with_driver_age(command[1]))
                elif command[0] == GET_REGISTRATION_NUMBERS_HAVING_DRIVER_AGE:
                    print(self.parkingLotUI.get_registration_numbers_for_cars_with_driver_age(command[1]))
            else:
                print("parking lot is not created yet,create a parking lot using " +CREATE_PARKING_LOT +" command")
        self.__commandsExecuted.append(command)

class FileInputModeUI(HomeUI):
    def __init__(self):
        HomeUI.__init__(self)
    
    def validate_command(self,command):
        return command[0] in self.__validCommands
    
    def run(self,input_file):
        try:
            with open(input_file) as file:
                commands = file.readlines()
                for command in commands:
                    self.run_command(command.strip().split())
        except Exception as e:
            print(e)

if __name__ == "__main__":
    if len(sys.argv) == 2:
        file_name = sys.argv[1]
        file_input_ui = FileInputModeUI()
        file_input_ui.run(file_name.strip())
    else:
        print("script is executed for wrong number of arguments")