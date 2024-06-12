# lib/models/rate.py

import sqlite3

class Rate:
    def __init__(self, entry_point, exit_point, rate, rate_id=None):
        self.id = rate_id
        self.entry_point = entry_point
        self.exit_point = exit_point
        self.rate = rate

    def create():
        connection = sqlite3.connect('expressway.db')
        cursor = connection.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS rates (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                entry_point TEXT NOT NULL,
                exit_point TEXT NOT NULL,
                rate REAL NOT NULL
            )
        ''')
        connection.commit()
        connection.close()


    def save(self):
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        if self.id is None:
            cursor.execute('''
                INSERT INTO rates (entry_point, exit_point, rate)
                VALUES (?, ?, ?)
            ''', (self.entry_point, self.exit_point, self.rate))
            self.id = cursor.lastrowid
        else:
            cursor.execute('''
                UPDATE rates
                SET entry_point = ?, exit_point = ?, rate = ?
                WHERE id = ?
            ''', (self.entry_point, self.exit_point, self.rate, self.id))
        connection.commit()
        connection.close()

    def delete(self):
        if self.id is not None:
            connection = sqlite3.connect('expressway.db')
            cursor = connection.cursor()
            cursor.execute('DELETE FROM rates WHERE id = ?', (self.id,))
            connection.commit()
            connection.close()

    @classmethod
    def find_by_id(cls, rate_id):
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM rates WHERE id = ?', (rate_id,))
        row = cursor.fetchone()
        connection.close()
        if row:
            return cls(row[1], row[2], row[3], row[0])
        return None

    @classmethod
    def find_by_points(cls, entry_point, exit_point):
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        cursor.execute('''
            SELECT * FROM rates WHERE entry_point = ? AND exit_point = ?
        ''', (entry_point, exit_point))
        row = cursor.fetchone()
        connection.close()
        if row:
            return cls(row[1], row[2], row[3], row[0])
        return None

    @classmethod
    def all(cls):
        connection = sqlite3.connect(DATABASE_FILE)
        cursor = connection.cursor()
        cursor.execute('SELECT * FROM rates')
        rows = cursor.fetchall()
        connection.close()
        return [cls(row[1], row[2], row[3], row[0]) for row in rows]

    def __repr__(self):
        return f"<Rate(entry_point={self.entry_point}, exit_point={self.exit_point}, rate={self.rate})>"
