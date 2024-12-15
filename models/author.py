import sqlite3

class Author:
    def __init__(self, id=None, name=None):
        self.id = id
        self.name = name

    @staticmethod
    def create_table():
        """Create the authors table in the database."""
        with sqlite3.connect("magazine.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS authors (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL
                )
            ''')
            conn.commit()

    @staticmethod
    def create(name):
        """Create a new author record in the database."""
        Author.validate_string(name, "Author name")
        with sqlite3.connect("magazine.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                INSERT INTO authors (name) VALUES (?)
            ''', (name,))
            conn.commit()
        print(f"Author '{name}' created successfully.")

    @staticmethod
    def list_all():
        """List all authors from the database."""
        with sqlite3.connect("magazine.db") as conn:
            cursor = conn.cursor()
            cursor.execute('SELECT * FROM authors')
            authors = [Author(id=row[0], name=row[1]) for row in cursor.fetchall()]
            return authors

    @staticmethod
    def update(author_id, new_name):
        """Update an author's name."""
        Author.validate_string(new_name, "Author name")
        with sqlite3.connect("magazine.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                UPDATE authors SET name = ? WHERE id = ?
            ''', (new_name, author_id))
            conn.commit()
        print(f"Author ID {author_id} updated successfully to '{new_name}'.")

    @staticmethod
    def delete(author_id):
        """Delete an author by ID."""
        with sqlite3.connect("magazine.db") as conn:
            cursor = conn.cursor()
            cursor.execute('''
                DELETE FROM authors WHERE id = ?
            ''', (author_id,))
            conn.commit()
        print(f"Author ID {author_id} deleted successfully.")

    @staticmethod
    def validate_string(value, field_name):
        """Helper function to validate that the string is not empty."""
        if not value or not isinstance(value, str):
            raise ValueError(f"{field_name} must be a valid string.")

# Example Usage
# Author.create("John Doe")
# authors = Author.list_all()
# for author in authors:
#     print(author.name)
# Author.update(1, "Jane Doe")
# Author.delete(1)
