# lib/cli.py
import click
import sqlite3
from helpers import (
    exit_program,
    add_vehicle_to_database,
    get_all_vehicles,
    find_vehicle_by_id,
    find_plate_number

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


if __name__ == "__main__":
    main()