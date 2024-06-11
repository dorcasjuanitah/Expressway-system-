# lib/models/__init__.py

import sqlite3

# Database connection
DATABASE_NAME = 'expressway_system.db'

connection = sqlite3.connect(DATABASE_NAME)
cursor = connection.cursor()

# Create tables
cursor.execute('''
    CREATE TABLE IF NOT EXISTS rates (
        id INTEGER PRIMARY KEY,
        entry_point TEXT NOT NULL,
        exit_point TEXT NOT NULL,
        rate REAL NOT NULL
    )
''')

# Commit the changes and close the connection setup
connection.commit()
connection.close()
