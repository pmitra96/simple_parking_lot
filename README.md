# simple_parking_lot
very simple parking lot repo with prime focus on OOD and design patterns 
# Parking Lot OOD (Python)

## 1. Problem Statment
Design a Parking lot The parking lot can hold upto maximum of n car. Every car that enters is assinged the nearest free slot to entry. basic functional_cass:
- create a parking lot 
- vehicles can enter
- vehicles can exit 
- Registration numbers of all cars of a particular colour.
- Slot number in which a car with a given registration number is parked.
- Slot numbers of all slots where a car of a particular colour is parked.

## 2. Solution Approach
classes : Cars,Slots,ParkingLot , ParkingLotUI , HomeUI , slotManager
relationships : slot has vehicle and vehicle has slot . Slots are managed by slot manager.
each parking Lot has a parkingLot UI and each HomeUI has a parkingLotUI. 
Notes : slotManager manages all the slot updation and retrieval , We use the HomeUI class to interact with user.
ExecutionFlow :- HomeUI -> ParkingLOtUI -> ParkingLot -> SlotManager 

## 3. Supported Commands

- `create_parking_lot` <`capacity`>   
To create a Parking lot. Where `capacity` is the size of the parking lot

- `park` <`car_registration_number`> <`car_color`>   
To park the car in the parking lot and prints the allocated slot in the parking lot. Where `car_registration_number` is given registration number for the car and `car_color` is given color for the car

- `leave` <`slot_id`>   
To leave the parking lot from desired slot and prints the leaving slot. given slot number. Where `slot_id` is given sloat number

- `status`   
To check the status of Parking Lot

- `slot_numbers_for_cars_with_colour` <`colour`>   
To prints the registration number of the cars for the given colour. Where `color` is given colour

- `slot_number_for_registration_number` <`registration_number`>   
prints the slot number of the cars for the given number. Where `registration_number` is given registration number.

- `registration_numbers_for_cars_with_colour` <`colour`>   
To prints the slot number of the cars for the given colour.  Where `colour` is given colour.

- `exit` 
To exit the application.

## 4. Running Application
#### 4.1 Running the application in File mode:

```python
./{parking_lot_dir}/bin/ParkingLot.py path_to_input_file
```

#### 4.2 Running the application in Interactive mode:

```python
./{parking_lot_dir}/bin/parking_lot
```

## 5. Test Cases
- Total number of test cases - 30

#### 5.1 For running the tests

```python
./{parking_lot_dir}/bin/setup
```

#### examples 
- for interactive mode :- examples/command_mode.png 
- for file mode :- examples/file_mode.png
