# lib/cli.py
import click
import sqlite3
from helpers import (
    exit_program,
    add_vehicle_to_database,
    get_all_vehicles,
    find_vehicle_by_id,
    find_plate_number
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
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_vehicle_to_database()
        elif choice == "2":
            get_all_vehicles()
        elif choice == "3":
            find_vehicle_by_id()
        elif choice == "4":
            find_plate_number()
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
    print("9. Test our CLI")
    print("10. List all stations")
    print("11. Find a station by id")
    print("12. Find a station by name")
   


if __name__ == "__main__":
    main()