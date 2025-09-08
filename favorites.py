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
    new_book = Book(title, author, length, genre)
    c.execute("INSERT INTO books VALUES (?, ?, ?, ?)", (new_book.title, new_book.author, new_book.length, new_book.genre))
    conn.commit()
    print("book added")
    
    

def delete_one(title):
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute("DELETE FROM books WHERE title = (?)", (title,))
    conn.commit()
    print("book deleted")
    
    


# c.execute("SELECT * FROM books")  
# rows = c.fetchall()
# print(rows) 

# Execute the query to fetch all rows from the 'books' table


# Fetch all results

def show():
    conn = sqlite3.connect('books.db')
    c = conn.cursor()
    c.execute("SELECT * FROM books")
    rows = c.fetchall()
    last = []
    for row in rows:
        last += row 
        last += "\n"
    return last

print(show())

# add_one("so", "jo", 15, "no")


# conn.commit()


# conn.close()

    
