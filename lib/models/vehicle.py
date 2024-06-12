import sqlite3

class Vehicle:
    def __init__(self, vehicle_id, plate_number, owner_name, phone_number):
        self.vehicle_id = vehicle_id
        self.plate_number = plate_number
        self.owner_name = owner_name
        self.phone_number = phone_number

    @property
    def plate_number(self):
        return self._plate_number
    
    @plate_number.setter
    def plate_number(self, value):
        if len(value) > 6:
            raise ValueError("Plate number should be a maximum of 6 characters.")
        self._plate_number = value
    
    @property
    def phone_number(self):
        return self._phone_number
    
    @phone_number.setter
    def phone_number(self, value):
        if not value.isdigit():
            raise ValueError("Phone number should contain only digits.")
        if len(value) > 10:
            raise ValueError("Phone number should be a maximum of 10 digits.")
        self._phone_number = value

    @classmethod
    def create_table(cls):
        conn = sqlite3.connect('expressway.db')
        cursor = conn.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS vehicles (
                            vehicle_id INTEGER PRIMARY KEY AUTOINCREMENT,
                            plate_number TEXT NOT NULL,
                            owner_name TEXT NOT NULL,
                            phone_number TEXT NOT NULL)''')
        conn.commit()
        conn.close()

    def save(self):
        conn = sqlite3.connect('expressway.db')
        cursor = conn.cursor()
        if self.vehicle_id is None:
            sql = """
                INSERT INTO vehicles (plate_number, owner_name, phone_number)
                VALUES (?, ?, ?)
            """
            cursor.execute(sql, (self.plate_number, self.owner_name, self.phone_number))
            self.vehicle_id = cursor.lastrowid
        else:
            sql = """
                UPDATE vehicles
                SET plate_number = ?, owner_name = ?, phone_number = ?
                WHERE vehicle_id = ?
            """
            cursor.execute(sql, (self.plate_number, self.owner_name, self.phone_number, self.vehicle_id))
        conn.commit()
        conn.close()

    @classmethod
    def create(cls, plate_number, owner_name, phone_number):
        vehicle = cls(None, plate_number, owner_name, phone_number)
        vehicle.save()
        return vehicle
    
    @classmethod
    def delete_table(cls):
        conn = sqlite3.connect('expressway.db')
        cursor = conn.cursor()
        cursor.execute('DROP TABLE IF EXISTS vehicles')
        conn.commit()
        conn.close()

    @classmethod
    def find_by_id(cls, vehicle_id):
        conn = sqlite3.connect('expressway.db')
        cursor = conn.cursor()
        sql = """
            SELECT * FROM vehicles WHERE vehicle_id = ?
        """
        row = cursor.execute(sql, (vehicle_id,)).fetchone()
        conn.close()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_plate_number(cls, plate_number):
        conn = sqlite3.connect('expressway.db')
        cursor = conn.cursor()
        sql = """
            SELECT * FROM vehicles WHERE plate_number = ?
        """
        row = cursor.execute(sql, (plate_number,)).fetchone()
        conn.close()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def instance_from_db(cls, row):
        if row:
            return cls(vehicle_id=row[0], plate_number=row[1], owner_name=row[2], phone_number=row[3])
        return None

    def __repr__(self):
        return f"Vehicle({self.vehicle_id}, {self.plate_number}, {self.owner_name}, {self.phone_number})"