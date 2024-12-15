from database.connection import get_db_connection

class Magazine:
    def __init__(self, id=None, name=None, category=None):
        self.id = id
        self.name = name
        self.category = category

    @staticmethod
    def create_table():
        """Create the magazines table in the database."""
        conn = get_db_connection()
        try:
            conn.execute("""
            CREATE TABLE IF NOT EXISTS magazines (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT NOT NULL
            );
            """)
            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def create(name, category):
        """Create a new magazine record in the database."""
        Magazine.validate_string(name, "Magazine name")
        Magazine.validate_string(category, "Category")
        
        conn = get_db_connection()
        try:
            conn.execute("INSERT INTO magazines (name, category) VALUES (?, ?)", 
                         (name, category))
            conn.commit()
            print(f"Magazine '{name}' created successfully.")
        finally:
            conn.close()

    @staticmethod
    def list_all():
        """List all magazines from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute("SELECT * FROM magazines")
            magazines = [Magazine(id=row[0], name=row[1], category=row[2]) for row in cursor.fetchall()]
            return magazines
        finally:
            conn.close()

    @staticmethod
    def update(magazine_id, new_name, new_category):
        """Update an existing magazine's name and category."""
        Magazine.validate_string(new_name, "Magazine name")
        Magazine.validate_string(new_category, "Category")
        
        conn = get_db_connection()
        try:
            conn.execute("UPDATE magazines SET name = ?, category = ? WHERE id = ?", 
                         (new_name, new_category, magazine_id))
            conn.commit()
            print(f"Magazine ID {magazine_id} updated successfully to '{new_name}' with category '{new_category}'.")
        finally:
            conn.close()

    @staticmethod
    def delete(magazine_id):
        """Delete a magazine by ID."""
        conn = get_db_connection()
        try:
            conn.execute("DELETE FROM magazines WHERE id = ?", (magazine_id,))
            conn.commit()
            print(f"Magazine ID {magazine_id} deleted successfully.")
        finally:
            conn.close()

    @staticmethod
    def validate_string(value, field_name):
        """Helper function to validate that the string is not empty."""
        if not value or not isinstance(value, str):
            raise ValueError(f"{field_name} must be a valid string.")

# Example Usage
# Magazine.create("Tech Today", "Technology")
# magazines = Magazine.list_all()
# for magazine in magazines:
#     print(magazine.name, magazine.category)
# Magazine.update(1, "Tech Weekly", "Tech")
# Magazine.delete(1)
