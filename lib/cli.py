# lib/cli.py

from helpers import (
    exit_program,
    list_all_payments,
    find_payment_by_id,
    find_payment_by_date,
    create_payment, 
    test_our_cli,
    list_all_stations,
    find_station_by_id,
    find_station_by_name
    )


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_all_payments()
        elif choice == "2":
            find_payment_by_id()
        elif choice == "3":
            find_payment_by_date()
        elif choice == "4":
            create_payment()
        elif choice == "5":
            test_our_cli()
        elif choice == "6":
            list_all_stations()
        elif choice == "7":
            find_station_by_id()
        elif choice == "8":
            find_station_by_name()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all payments")
    print("2. Find a payment by id")
    print("3. Find a payment by date")
    print("4. Create a new payment")
    print("5. Test our CLI")
    print("6. List all stations")
    print("7. Find a station by id")
    print("8. Find a station by name")
    


if __name__ == "__main__":
    main()
