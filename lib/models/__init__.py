# lib/models/__init__.py

import sqlite3

CONN = sqlite3.connect('expressway.db')
CURSOR = CONN.cursor()
