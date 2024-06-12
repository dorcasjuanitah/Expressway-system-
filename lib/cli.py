# lib/cli.py

from models.rate import Rate
from models.employee import Employee
from models.station import Station
from models.vehicle import Vehicle

import click
import sqlite3
from helpers import(
    get_input,
    get_float_input,
    get_int_input,
    exit_program,
    add_vehicle_to_database,
    get_all_vehicles,
    find_vehicle_by_id,
    find_plate_number,
    list_employees,
    find_employee_by_name,
    find_employee_by_id,
    create_employee,
    update_employee,
    delete_employee,
    list_all_payments,
    find_payment_by_id,
    find_payment_by_date,
    create_payment, 
    test_our_cli,
    list_all_stations,
    find_station_by_id,
    find_station_by_name
    
    )

DATABASE = 'expressway.db'

def main():
    while True:
        menu()
        choice = get_input("> ")
        if choice == "0":
            exit_program()
        if choice == "1":
            add_vehicle_to_database()
        elif choice == "2":
            get_all_vehicles()
        elif choice == "3":
            find_vehicle_by_id()
        elif choice == "4":
            find_plate_number()
        elif choice == "22":
            list_all_payments()
        elif choice == "5":
            find_payment_by_id()
        elif choice == "6":
            find_payment_by_date()
        elif choice == "7":
            create_payment()
        elif choice == "8":
            test_our_cli()
        elif choice == "9":
            list_all_stations()
        elif choice == "10":
            find_station_by_id()
        elif choice == "11":
            find_station_by_name()
        elif choice == "12":
            list_rates()
        elif choice == "13":
            add_rate()
        elif choice == "14":
            update_rate()
        elif choice == "15":
            delete_rate()
        elif choice == "16":
            list_employees()
        elif choice == "17":
            find_employee_by_name()
        elif choice == "18":
            find_employee_by_id()
        elif choice == "19":
            create_employee()
        elif choice == "20":
            update_employee()
        elif choice == "21":
            delete_employee()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a new vehicle")
    print("2. View all vehicles")
    print("3. Find Vehicle by id")
    print("4. Find vehicle by plate number")
    # Add other options for Trip, Charge, and Employee...
    print("5. List all payments")
    print("6. Find a payment by id")
    print("7. Find a payment by date")
    print("8. Create a new payment")
    print("9. List all stations")
    print("10. List all stations")
    print("11. Find a station by id")
    print("12. Find a station by name")
    print("13. List all rates")
    print("14. Add a new rate")
    print("15. Update a rate")
    print("16. Delete a rate")
    print("17. List all employees")
    print("18. Find Employees by Id")
    print("19. Create Employee")
    print("20. Update Employee")
    print("21. Delete Employee") 
    

def list_rates():
    rates = Rate.all()
    for rate in rates:
        print(rate)

def add_rate():
    entry_point = get_input("Enter entry point: ")
    exit_point = get_input("Enter exit point: ")
    rate_value = get_float_input("Enter rate: ")
    new_rate = Rate(entry_point, exit_point, rate_value)
    new_rate.save()
    print("Rate added successfully.")

def update_rate():
    rate_id = get_int_input("Enter rate ID to update: ")
    rate = Rate.find_by_id(rate_id)
    if rate:
        entry_point = get_input("Enter new entry point: ")
        exit_point = get_input("Enter new exit point: ")
        rate_value = get_float_input("Enter new rate: ")
        rate.entry_point = entry_point
        rate.exit_point = exit_point
        rate.rate = rate_value
        rate.save()
        print("Rate updated successfully.")
    else:
        print("Rate not found.")
def delete_rate():
    rate_id = get_int_input("Enter rate ID to delete: ")
    rate = Rate.find_by_id(rate_id)
    if rate:
        rate.delete()
        print("Rate deleted successfully.")
    else:
        print("Rate not found.")

if __name__ == "__main__":
    main()