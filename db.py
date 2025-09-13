import sqlite3

DB_NAME = "library.db"

def connect():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            author TEXT NOT NULL,
            year INTEGER,
            isbn TEXT UNIQUE
        )
    """)
    conn.commit()
    conn.close()

def add_book(title, author, year, isbn):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("INSERT INTO books (title, author, year, isbn) VALUES (?, ?, ?, ?)", 
                (title, author, year, isbn))
    conn.commit()
    conn.close()

def view_books():
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    rows = cur.fetchall()
    conn.close()
    return rows

def search_books(title="", author="", year="", isbn=""):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("SELECT * FROM books WHERE title LIKE ? OR author LIKE ? OR year LIKE ? OR isbn LIKE ?", 
                (f"%{title}%", f"%{author}%", f"%{year}%", f"%{isbn}%"))
    rows = cur.fetchall()
    conn.close()
    return rows

def update_book(book_id, title, author, year, isbn):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("UPDATE books SET title=?, author=?, year=?, isbn=? WHERE id=?", 
                (title, author, year, isbn, book_id))
    conn.commit()
    conn.close()

def delete_book(book_id):
    conn = sqlite3.connect(DB_NAME)
    cur = conn.cursor()
    cur.execute("DELETE FROM books WHERE id=?", (book_id,))
    conn.commit()
    conn.close()
