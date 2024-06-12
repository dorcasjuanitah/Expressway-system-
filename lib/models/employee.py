# lib/models/employee.py
from models.__init__ import CURSOR, CONN
from models.station import Station


class Employee:

    # Dictionary of objects saved to the database.
    all = {}

    def __init__(self, emp_name, designation, shift, station_id, id=None):
        self.id = id
        self.emp_name = emp_name
        self.designation = designation
        self.shift = shift
        self.station_id = station_id

    def __repr__(self):
        return (
            f"<Employee {self.id}: {self.emp_name}, {self.designation}, " +
            f"Shift: {self.shift}, Station ID: {self.station_id}>"
        )

    @property
    def emp_name(self):
        return self._emp_name

    @emp_name.setter
    def emp_name(self, emp_name):
        if isinstance(emp_name, str) and len(emp_name):
            self._emp_name = emp_name
        else:
            raise ValueError("emp_name must be a non-empty string")

    @property
    def designation(self):
        return self._designation

    @designation.setter
    def designation(self, designation):
        if isinstance(designation, str) and len(designation):
            self._designation = designation
        else:
            raise ValueError("designation must be a non-empty string")

    @property
    def shift(self):
        return self._shift

    @shift.setter
    def shift(self, shift):
        allowed_shifts = {"morning", "afternoon", "night"}
        if shift in allowed_shifts:
            self._shift = shift
        else:
            raise ValueError("shift must be one of the following: 'morning', 'afternoon', or 'night'")

    @property
    def station_id(self):
        return self._station_id

    @station_id.setter
    def station_id(self, station_id):
        if type(station_id) is int and Station.find_by_id(station_id):
            self._station_id = station_id
        else:
            raise ValueError("station_id must reference a station in the database")

    @classmethod
    def create_table(cls):
        """ Create a new table to persist the attributes of Employee instances """
        sql = """
            CREATE TABLE IF NOT EXISTS employees (
            id INTEGER PRIMARY KEY,
            emp_name TEXT DEFAULT NULL,
            designation TEXT DEFAULT NULL,
            shift TEXT DEFAULT NULL,
            station_id INTEGER DEFAULT NULL,
            FOREIGN KEY (station_id) REFERENCES stations(id))
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """ Drop the table that persists Employee instances """
        sql = """
            DROP TABLE IF EXISTS employees;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """ Insert a new row with the emp_name, designation, shift, and station_id values of the current Employee object.
        Update object id attribute using the primary key value of new row.
        Save the object in local dictionary using table row's PK as dictionary key"""
        sql = """
                INSERT INTO employees (emp_name, designation, shift, station_id)
                VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.emp_name, self.designation, self.shift, self.station_id))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    def update(self):
        """Update the table row corresponding to the current Employee instance."""
        sql = """
            UPDATE employees
            SET emp_name = ?, designation = ?, shift = ?, station_id = ?
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.emp_name, self.designation, self.shift, self.station_id, self.id))
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current Employee instance,
        delete the dictionary entry, and reassign id attribute"""

        sql = """
            DELETE FROM employees
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]

        # Set the id to None
        self.id = None

    @classmethod
    def create(cls, emp_name, designation, shift, station_id):
        """ Initialize a new Employee instance and save the object to the database """
        employee = cls(emp_name, designation, shift, station_id)
        employee.save()
        return employee

    @classmethod
    def instance_from_db(cls, row):
        """Return an Employee object having the attribute values from the table row."""

        # Check the dictionary for existing instance using the row's primary key
        employee = cls.all.get(row[0])
        if employee:
            # ensure attributes match row values in case local instance was modified
            employee.emp_name = row[1]
            employee.designation = row[2]
            employee.shift = row[3]
            employee.station_id = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            employee = cls(row[1], row[2], row[3], row[4])
            employee.id = row[0]
            cls.all[employee.id] = employee
        return employee

    @classmethod
    def get_all(cls):
        """Return a list containing one Employee object per table row"""
        sql = """
            SELECT *
            FROM employees
        """

        rows = CURSOR.execute(sql).fetchall()

        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return Employee object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM employees
            WHERE id = ?
        """

        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, emp_name):
        """Return Employee object corresponding to first table row matching specified name"""
        sql = """
            SELECT *
            FROM employees
            WHERE emp_name = ?
        """

        row = CURSOR.execute(sql, (emp_name,)).fetchone()
        return cls.instance_from_db(row) if row else None
cd