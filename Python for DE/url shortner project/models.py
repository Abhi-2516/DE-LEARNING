import sqlite3

DB_NAME = "databse.db"


def get_connection():
    """
    Create and return a database connection.
    """
    conn = sqlite3.connect(DB_NAME)

    # Allows us to access columns by name
    conn.row_factory = sqlite3.Row

    return conn


def init_db():
    """
    Create the URLs table if it doesn't already exist.
    """

    with get_connection() as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS urls (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                original_url TEXT NOT NULL,
                short_code TEXT UNIQUE NOT NULL,
                visit_count INTEGER DEFAULT 0
            )
        """)


def insert_url(original_url, short_code):
    """
    Insert a new shortened URL into the database.
    """

    with get_connection() as conn:
        conn.execute("""
            INSERT INTO urls (original_url, short_code)
            VALUES (?, ?)
        """, (original_url, short_code))


def get_url(short_code):
    """
    Find one URL using its short code.
    """

    with get_connection() as conn:
        cursor = conn.execute("""
            SELECT *
            FROM urls
            WHERE short_code = ?
        """, (short_code,))

        return cursor.fetchone()


def get_all_url():
    """
    Return all shortened URLs.
    """

    with get_connection() as conn:
        cursor = conn.execute("""
            SELECT original_url, short_code, visit_count
            FROM urls
            ORDER BY id DESC
        """)

        return cursor.fetchall()


def increment_visit_count(short_code):
    """
    Increase the visit count whenever someone
    opens a shortened URL.
    """

    with get_connection() as conn:
        conn.execute("""
            UPDATE urls
            SET visit_count = visit_count + 1
            WHERE short_code = ?
        """, (short_code,))


def delete_url_by_code(short_code):
    """
    Delete a shortened URL using its short code.
    """

    with get_connection() as conn:
        conn.execute("""
            DELETE FROM urls
            WHERE short_code = ?
        """, (short_code,))