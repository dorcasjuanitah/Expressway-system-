# lib/models/database.py

import sqlite3

DATABASE_NAME= 'expressway_system.db'

def initialize_database():
    connection = sqlite3.connect(DATABASE_NAME)
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
