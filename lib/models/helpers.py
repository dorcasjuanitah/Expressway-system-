# helpers.py
from models.employee import Employee
from models.station import Station

def exit_program():
    print("Goodbye!")
    exit()

# Employee functions

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

def main():
    while True:
        print("""
            Please select an option:
            0. Exit the program
            1. List all employees
            2. Find employee by name
            3. Find employee by id
            4. Create employee
            5. Update employee
            6. Delete employee
            
        """)
        choice = input("Enter your choice: ")
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
            print("Invalid choice.")

if __name__ == "__main__":
    main()
