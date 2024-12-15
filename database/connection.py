import sqlite3

# Path to the database file
DATABASE_FILE = 'magazine.db'

def get_db_connection():
    """Establish and return a connection to the SQLite database."""
    conn = sqlite3.connect(DATABASE_FILE)
    # Enable foreign key constraints for SQLite
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
