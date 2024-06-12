# lib/helpers.py
from models.payment import Payment
from models.station import Station

def exit_program():
    print("Goodbye!")
    exit()

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


