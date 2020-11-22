# simple_parking_lot
very simple parking lot repo with prime focus on OOD and design patterns 
# Parking Lot OOD (Python)

## 1. Problem Statment
Design a Parking lot The parking lot can hold upto maximum of n car. Every car that enters is assinged the nearest free slot to entry. basic functional_cass:
- create a parking lot 
- vehicles can enter
- vehicles can exit 
- Registration numbers of all cars of a particular driver_age.
- Slot number in which a car with a given registration number is parked.
- Slot numbers of all slots where a car of a particular driver_age is parked.

## 2. Solution Approach
classes : Cars,Slots,ParkingLot , ParkingLotUI , HomeUI , slotManager
relationships : slot has vehicle and vehicle has slot . Slots are managed by slot manager.
each parking Lot has a parkingLot UI and each HomeUI has a parkingLotUI. 
Notes : slotManager manages all the slot updation and retrieval , We use the HomeUI class to interact with user.
ExecutionFlow :- HomeUI -> ParkingLOtUI -> ParkingLot -> SlotManager 

## 3. Supported Commands

- `Create_parking_lot` <`capacity`>   
To create a Parking lot. Where `capacity` is the size of the parking lot

- `Park` <`car_registration_number`> driver_age <`car_driver_age`>   
To park the car in the parking lot and prints the allocated slot in the parking lot. Where `car_registration_number` is given registration number for the car and `car_driver_age` is given driver_age for the car

- `Leave` <`slot_id`>   
To leave the parking lot from desired slot and prints the leaving slot. given slot number. Where `slot_id` is given sloat number

- `Slot_numbers_for_driver_of_age` <`driver_age`>   
To prints the registration number of the cars for the given driver_age. Where `driver_age` is given driver_age

- `Slot_number_for_car_with_number` <`registration_number`>   
prints the slot number of the cars for the given number. Where `registration_number` is given registration number.

- `Vehicle_registration_number_for_driver_of_age` <`driver_age`>   
To prints the slot number of the cars for the given driver_age.  Where `driver_age` is given driver_age.

- `exit` 
To exit the application.

## 4. Running Application
#### 4.1 Running the application in File mode:

```python

cd {parking_lot_dir} && python -m src.HomeUI bin/input.txt
```

## 5. Test Cases
- Total number of test cases - 30

#### 5.1 For running the tests
```python
cd {parking_lot_dir} && python -m unittest discover tests/ "*py"
```

## 5.3 Note 
since the output for exceptional cases hasn't been specified , i'm returing `null` for all the exceptional cases.