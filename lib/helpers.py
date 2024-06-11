# lib/helpers.py

def display_main_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all rates")
    print("2. Add a new rate")
    print("3. Update a rate")
    print("4. Delete a rate")

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
# lib/helpers.py

def display_main_menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all rates")
    print("2. Add a new rate")
    print("3. Update a rate")
    print("4. Delete a rate")

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
