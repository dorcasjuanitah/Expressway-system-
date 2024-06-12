from helpers import (
    exit_program,
    list_employees,
    find_employee_by_name,
    find_employee_by_id,
    create_employee,
    update_employee,
    delete_employee,
    
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_employees()
        elif choice == "2":
            find_employee_by_name()
        elif choice == "3":
            find_employee_by_id()
        elif choice == "4":
            create_employee()
        elif choice == "5":
            update_employee()
        elif choice == "6":
            delete_employee()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List all employees")
    print("2. Find employee by name")
    print("3. Find employee by id")
    print("4: Create employee")
    print("5: Update employee")
    print("6: Delete employee")
    


if __name__ == "__main__":
    main()
