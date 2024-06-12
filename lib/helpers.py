# lib/helpers.py
from models.vehicle import Vehicle

def exit_program():
    print("Goodbye!")
    exit()

def add_vehicle_to_database():
    """Add a new vehicle."""
    plate_number = input("Enter plate number: ")
    owner_name = input("Enter owner name: ")
    phone_number = input("Enter phone number: ")
    try:
        add_vehicle_to_database(plate_number, owner_name, phone_number)
        print("Vehicle added successfully.")
    except Exception as e:
        print(f"Error: {str(e)}")

def get_all_vehicles():
    """View all vehicles."""
    vehicles = get_all_vehicles()
    if vehicles:
        print("List of vehicles:")
        for vehicle in vehicles:
            print(f"Plate Number: {vehicle[1]}, Owner Name: {vehicle[2]}, Phone Number: {vehicle[3]}")
    else:
        print("No vehicles found.")

def find_vehicle_by_id():
    id_ = input("Enter the vehicle's id: ")
    vehicle  = Vehicle.find_by_id(id_)
    print(vehicle) if vehicle else print(f"vehicle {id_} not found")

def find_plate_number():
    plate_number = input("Enter the plate number: ")
    vehicle  = Vehicle.find_by_plate_number(plate_number)
    print(plate_number) if plate_number else print(f"plate number {plate_number} not found")

