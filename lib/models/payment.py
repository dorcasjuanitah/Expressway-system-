# lib/models/payment.py

# import datetime
from models.__init__ import CURSOR, CONN
from models.vehicle import Vehicle
from models.station import Station
from models.employee import Employee
from models.charge import Charge

class Payment:
    all = {}
    def __init__(self, mode_of_payment,vehicle_plate, entry_station, exit_station, amount_paid, check_in_employee, check_out_employee, date, id=None):
        self.id=id
        self.date = date
        self.mode_of_payment = mode_of_payment
        
        self.vehicle_plate = vehicle_plate
        self.entry_station = entry_station
        self.exit_station = exit_station
        self.amount_paid = amount_paid
        self.check_in_employee = check_in_employee
        self.check_out_employee = check_out_employee

    def __repr__(self):
        return (
            f"<Payment {self.id}: {self.date}, {self.mode_of_payment}, " +
            f"Vehicleplate {self.vehicle_plate}, " +
            f"entry station {self.entry_station}, exit station {self.exit_station}, amountpaid {self.amount_paid}, " +
            f"check in employee {self.check_in_employee}, check out employee {self.check_out_employee} >"
        )

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, date):
        if isinstance(date, str) and len(date) > 0:
            self._date = date
        else:
            raise ValueError(
                "Date must be a non-empty string"
            )

    @property
    def mode_of_payment(self):
        return self._mode_of_payment

    @mode_of_payment.setter
    def mode_of_payment(self, mode_of_payment):
        if isinstance(mode_of_payment, str) and len(mode_of_payment)>0:
            self._mode_of_payment = mode_of_payment
        else:
            raise ValueError(
                "mode_of_payment must be a non-empty string"
            )

    @property
    def vehicle_plate(self):
        return self._vehicle_plate

    @vehicle_plate.setter
    def vehicle_plate(self, vehicle_plate):
        if type(vehicle_plate) is str and Vehicle.find_by_plate_number(vehicle_plate) and len(vehicle_plate)==7:
            self._vehicle_plate = vehicle_plate
        else:
            raise ValueError(
                "Enter the correct plate")
        
    @property
    def entry_station(self):
        return self._entry_station

    @entry_station.setter
    def entry_station(self, entry_station):
        if type(entry_station) is int and Station.find_by_id(entry_station):
            self._entry_station = entry_station
        else:
            raise ValueError(
                "Enter the correct ENTRY station")
    @property
    def exit_station(self):
        return self._exit_station

    @exit_station.setter
    def exit_station(self, exit_station):
        if type(exit_station) is int and Station.find_by_id(exit_station):
            self._exit_station = exit_station
        else:
            raise ValueError(
                "Enter the correct EXIT station")

    @property
    def check_in_employee(self):
        return self._check_in_employee

    @check_in_employee.setter
    def check_in_employee(self, check_in_employee):
        if type(check_in_employee) is int and Employee.find_by_id(check_in_employee):
            self._check_in_employee = check_in_employee
        else:
            raise ValueError(
                "Enter the correct EMPLOYEE at entry station")
        
    @property
    def check_out_employee(self):
        return self._check_out_employee

    @check_out_employee.setter
    def check_out_employee(self, check_out_employee):
        if type(check_out_employee) is int and Employee.find_by_id(check_out_employee):
            self._check_out_employee = check_out_employee
        else:
            raise ValueError(
                "Enter the correct EMPLOYEE at the exit station")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Payment instances """
        sql = """
            CREATE TABLE IF NOT EXISTS payments (
            id INTEGER PRIMARY KEY,
            date TEXT, 
            mode_of_payment TEXT,
            vehicle_plate TEXT, 
            entry_station INTEGER, 
            exit_station INTEGER, 
            amount_paid INTEGER, 
            check_in_employee INTEGER, 
            check_out_employee INTEGER,
            FOREIGN KEY (vehicle_plate) REFERENCES vehicle(plate_number),
            FOREIGN KEY (entry_station) REFERENCES station(id),
            FOREIGN KEY (exit_station) REFERENCES station(id),
            FOREIGN KEY (amount_paid) REFERENCES charge(id),
            FOREIGN KEY (check_in_employee) REFERENCES employee(id),
            FOREIGN KEY (check_out_employee) REFERENCES employee(id)
            )
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Payment instances """
        sql = """
            DROP TABLE IF EXISTS payments;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with date, mode_of_payment,vehicle_plate, entry_station, exit_station, amount_paid, check_in_employee, check_out_employee values of the current Payment object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's Primary Key as dictionary key"""
        sql = """
                INSERT INTO payments (date, mode_of_payment,vehicle_plate, entry_station, exit_station, amount_paid, check_in_employee, check_out_employee)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.date, self.mode_of_payment, self.vehicle_plate,
                             self.entry_station, self.exit_station, self.amount_paid, 
                             self.check_in_employee, self.check_out_employee))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    # def update(self):
    #     """Update the table row corresponding to the current Employee instance."""
    #     sql = """
    #         UPDATE employees
    #         SET name = ?, job_title = ?, department_id = ?
    #         WHERE id = ?
    #     """
    #     CURSOR.execute(sql, (self.name, self.job_title,
    #                          self.department_id, self.id))
    #     CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Payment instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM payments
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, date, mode_of_payment,vehicle_plate, entry_station, exit_station, amount_paid, check_in_employee, check_out_employee):
        """ Initialize a new Payment instance and save the object to the database """
        payment = cls(date, mode_of_payment,vehicle_plate, entry_station, exit_station, amount_paid, check_in_employee, check_out_employee)
        payment.save()
        return payment

    @classmethod
    def instance_from_db(cls, row):
        """Return an Payment object having the attribute values from the table row."""

        # Check the dictionary for  existing instance using the row's primary key
        payment = cls.all.get(row[0])
        if payment:
            # ensure attributes match row values in case local instance was modified
            payment.date = row[1]
            payment.mode_of_payment = row[2]
            payment.vehicle_plate = row[3]
            payment.entry_station = row[4]
            payment.exit_station = row[5]
            payment.amount_paid = row[6]
            payment.check_in_employee = row[7]
            payment.check_out_employee = row[8]
            
        else:
            # not in dictionary, create new instance and add to dictionary
            payment = cls(row[1], row[2], row[3], row[4], row[5], row[6], row[7], row[8])
            payment.id = row[0]
            cls.all[payment.id] = payment
        return payment

    @classmethod
    def get_all(cls):
        """Return a list containing one Payment object per table row"""
        sql = """
            SELECT *
            FROM payments
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Payment object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM payments
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_date(cls, date):
        """Return Payment object corresponding to first table row matching specified date"""
        sql = """
            SELECT *
            FROM payments
            WHERE name is ?
        """

        row = CURSOR.execute(sql, (date,)).fetchone()
        return cls.instance_from_db(row) if row else None
