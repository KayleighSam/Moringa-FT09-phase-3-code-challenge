from connection import get_db_connection

# Initialize tables
def initialize_tables():
    conn = get_db_connection()
    conn.execute("""
    CREATE TABLE IF NOT EXISTS authors (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL
    );
    """)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS magazines (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        category TEXT NOT NULL
    );
    """)
    conn.execute("""
    CREATE TABLE IF NOT EXISTS articles (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        author_id INTEGER NOT NULL,
        magazine_id INTEGER NOT NULL,
        title TEXT NOT NULL,
        FOREIGN KEY (author_id) REFERENCES authors(id),
        FOREIGN KEY (magazine_id) REFERENCES magazines(id)
    );
    """)
    conn.commit()
    conn.close()

# Example usage
initialize_tables()
