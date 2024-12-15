from database.connection import get_db_connection

class Article:
    def __init__(self, id=None, author_id=None, magazine_id=None, title=None):
        self.id = id
        self.author_id = author_id
        self.magazine_id = magazine_id
        self.title = title

    @staticmethod
    def create_table():
        """Create the articles table in the database."""
        conn = get_db_connection()
        try:
            conn.execute('''
                CREATE TABLE IF NOT EXISTS articles (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    author_id INTEGER,
                    magazine_id INTEGER,
                    title TEXT NOT NULL,
                    FOREIGN KEY (author_id) REFERENCES authors(id),
                    FOREIGN KEY (magazine_id) REFERENCES magazines(id)
                )
            ''')
            conn.commit()
        finally:
            conn.close()

    @staticmethod
    def create(author_id, magazine_id, title):
        """Create a new article record in the database and return the new article ID."""
        Article.validate_string(title, "Article title")
        
        conn = get_db_connection()
        try:
            cursor = conn.execute('''
                INSERT INTO articles (author_id, magazine_id, title) VALUES (?, ?, ?)
            ''', (author_id, magazine_id, title))
            conn.commit()
            article_id = cursor.lastrowid  # Get the ID of the newly inserted article
            print(f"Article '{title}' created successfully with ID {article_id}.")
            return article_id
        finally:
            conn.close()

    @staticmethod
    def list_all():
        """List all articles from the database."""
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute('SELECT * FROM articles')
            articles = [Article(id=row[0], author_id=row[1], magazine_id=row[2], title=row[3]) for row in cursor.fetchall()]
            return articles
        finally:
            conn.close()

    @staticmethod
    def update(article_id, new_title):
        """Update an article's title."""
        Article.validate_string(new_title, "Article title")
        
        conn = get_db_connection()
        try:
            conn.execute('UPDATE articles SET title = ? WHERE id = ?', (new_title, article_id))
            conn.commit()
            print(f"Article ID {article_id} updated successfully to '{new_title}'.")
        finally:
            conn.close()

    @staticmethod
    def delete(article_id):
        """Delete an article by ID."""
        conn = get_db_connection()
        try:
            conn.execute('DELETE FROM articles WHERE id = ?', (article_id,))
            conn.commit()
            print(f"Article ID {article_id} deleted successfully.")
        finally:
            conn.close()

    @staticmethod
    def validate_string(value, field_name):
        """Helper function to validate that the string is not empty."""
        if not value or not isinstance(value, str):
            raise ValueError(f"{field_name} must be a valid string.")
