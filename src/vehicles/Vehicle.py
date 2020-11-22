class Vehicle:
    def __init__(self,registration_number):
        self.__registration_number = registration_number

    def get_registration_number(self):
        return self.__registration_number
