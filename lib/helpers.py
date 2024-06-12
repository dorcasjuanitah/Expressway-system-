# lib/helpers.py
from models.vehicle import Vehicle
#from models.payment import Payment
from models.station import Station

def display_rate_menu(rate):
    print(f"Rate ID: {rate.id}")
    print(f"Entry Point: {rate.entry_point}")
    print(f"Exit Point: {rate.exit_point}")
    print(f"Rate: {rate.rate}")

def get_input(prompt):
    return input(prompt)

def get_float_input(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")

def get_int_input(prompt):
    while True:
        try:
            return int(input(prompt))
        except ValueError:
            print("Invalid input. Please enter an integer.")


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

def list_all_stations():
    stations = Station.get_all()
    for station in stations:
        print(station)

def find_station_by_id():
    id_ = input("Enter the station's id: ")
    station  = Station.find_by_id(id_)
    print(station) if station else print(f"Station {id_} not found")


def find_station_by_name():
    name = input("Enter the name of the station: ")
    station = Station.find_by_name(name)
    print(station) if station else print(f"Station name {name} not found")

def list_all_payments():
    payments = Payment.get_all()
    for payment in payments:
        print(payment)

def find_payment_by_id():
    id_ = input("Enter the payment's id: ")
    payment  = Payment.find_by_id(id_)
    print(payment) if payment else print(f"Payment {id_} not found")


def find_payment_by_date():
    date = input("Enter the date in dd-mm-yyyy: ")
    payment = Payment.find_by_date(date)
    print(payment) if payment else print(f"Payment on {date} not found")

def create_payment():
    date = input("Today's date: ")
    mode_of_payment = input("Enter the mode of payment: ")
    vehicle_plate = input("Enter the number plate: ")
    entry_station = input("Enter the station of entry: ")
    exit_station = input("Enter the station of exit: ")
    check_in_employee = input("Enter the employee at entry booth: ")
    check_out_employee = input("Enter the employee at exit booth: ")
    try:
        payment = Payment.create(date, mode_of_payment,vehicle_plate, entry_station, exit_station, check_in_employee, check_out_employee)
        print(f"Success {payment}")
    except Exception as exc:
        print("Error creating payment:", exc)

def test_our_cli():
    print("CLI works alright!!")

def list_employees():
    employees = Employee.get_all()
    if employees:
        for employee in employees:
            print(employee)
    else:
        print("No employees found.")

def find_employee_by_name():
    name = input("Enter the employee name: ")
    employee = Employee.find_by_name(name)
    if employee:
        print(employee)
    else:
        print("Employee not found.")

def find_employee_by_id():
    id = int(input("Enter the employee ID: "))
    employee = Employee.find_by_id(id)
    if employee:
        print(employee)
    else:
        print("Employee not found.")

def create_employee():
    name = input("Enter the employee name: ")
    job_title = input("Enter the job title: ")
    shift = input("Enter the shift (morning, afternoon, night): ")
    station_id = int(input("Enter the station ID: "))

    # Ensure the station_id references a valid station
    if not Station.find_by_id(station_id):
        print("Error: The provided station ID does not exist.")
        return

    try:
        employee = Employee.create(name, job_title, shift, station_id)
        print(f"Employee created: {employee}")
    except ValueError as e:
        print(f"Error: {e}")

def update_employee():
    id = int(input("Enter the employee ID: "))
    employee = Employee.find_by_id(id)
    if employee:
        new_name = input("Enter the new employee name: ")
        new_job_title = input("Enter the new job title: ")
        new_shift = input("Enter the new shift (morning, afternoon, night): ")
        new_station_id = int(input("Enter the new station ID: "))

        # Ensure the station_id references a valid station
        if not Station.find_by_id(new_station_id):
            print("Error: The provided station ID does not exist.")
            return

        try:
            employee.emp_name = new_name
            employee.designation = new_job_title
            employee.shift = new_shift
            employee.station_id = new_station_id
            employee.update()
            print("Employee updated.")
        except ValueError as e:
            print(f"Error: {e}")
    else:
        print("Employee not found.")

def delete_employee():
    id = int(input("Enter the employee ID: "))
    employee = Employee.find_by_id(id)
    if employee:
        employee.delete()
        print("Employee deleted.")
    else:
        print("Employee not found.")

