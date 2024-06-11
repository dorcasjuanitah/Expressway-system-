# lib/cli.py

from models.rate import Rate
from models.database import initialize_database
from helpers import (
    display_main_menu,
    get_input,
    get_float_input,
    get_int_input,
    exit_program,
)

def main():
    initialize_database()
    while True:
        display_main_menu()
        choice = get_input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_rates()
        elif choice == "2":
            add_rate()
        elif choice == "3":
            update_rate()
        elif choice == "4":
            delete_rate()
        else:
            print("Invalid choice")

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
