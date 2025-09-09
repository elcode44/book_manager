import sqlite3 
from Books import Book

conn = sqlite3.connect('books.db')

c = conn.cursor()

c.execute(""" CREATE TABLE IF NOT EXISTS books (
          title TEXT,
          author TEXT,
          length INTEGER,
          genre TEXT
          )""")


def add_one(title, author, length, genre):
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    if int(length)>0:
        new_book = Book(title, author, length, genre)
        c.execute("INSERT INTO books VALUES (?, ?, ?, ?)", (new_book.title, new_book.author, new_book.length, new_book.genre))
        conn.commit()
        print("book added")
    else:
        print("Book must be bigger than 0")
    

def delete_one(title):
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE title = (?)", (title,))
    conn.commit()
    print("book deleted")
    

def search(title):
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute("SELECT * FROM books WHERE title = ?", (title,))
    rows = c.fetchall()
    conn.close()
    return rows



def show():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    rows = c.fetchall()
    conn.close()

    result = ""
    for row in rows:
        line= "|".join(str(item)for item in row)
        result += line + "\n"
        
    return result


conn.commit()


conn.close()

    
