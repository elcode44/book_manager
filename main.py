import tkinter as tk
from favorites import add_one
from favorites import delete_one
from favorites import show




root = tk.Tk()

root.title("Favorite books")

root.geometry("1000x600")

root.title("Read Books")

label = tk.Label(root, text = "book list", font = ('Arial', 18))
label.pack(padx = 20, pady = 20)

# book name
book_frame = tk.Frame(root)
book_frame.pack(anchor = "w", padx = 20)

book_label = tk.Label(root, text = "Book name")
book_label.pack(anchor = "w", padx = 10)

book_name = tk.Entry(root)
book_name.pack(anchor = "w", padx=10, pady =10)

# author name
author_frame = tk.Frame(root)
author_frame.pack(anchor = "w", padx = 20, pady=10)

author_label = tk.Label(root, text = "Author name")
author_label.pack(anchor = "w", padx = 10)

author_entry = tk.Entry(root)
author_entry.pack(anchor = "w", padx=10, pady =10)

# book length
length_frame = tk.Frame(root)
length_frame.pack(anchor = "w", padx = 20, pady=10)

length_label = tk.Label(root, text = "Book length")
length_label.pack(anchor = "w", padx = 10)

length_entry = tk.Entry(root)
length_entry.pack(anchor = "w", padx=10, pady =10)

# book genre
genre_frame = tk.Frame(root)
genre_frame.pack(anchor = "w", padx = 20, pady=10)

genre_label = tk.Label(root, text = "Book genre")
genre_label.pack(anchor = "w", padx = 10)

genre_entry = tk.Entry(root)
genre_entry.pack(anchor = "w", padx=10, pady =10)

#add button
add_frame = tk.Frame(root)
add_frame.pack(anchor = "w", padx = 20, pady=10)

add_a_book = tk.Button(root, text = "Add book", command = lambda: add_one(book_name.get(), author_entry.get(), length_entry.get(), genre_entry.get()))
add_a_book.pack(anchor = "w", padx = 10)

# delete book button
delete_frame = tk.Frame(root)
delete_frame.pack(anchor = "w", padx = 10, pady=10)

delete_label = tk.Label(root, text = "name of book to delete")
delete_label.pack(anchor = "w", padx = 10)

delete_entry = tk.Entry(root)
delete_entry.pack(anchor = "w", padx=10, pady =10)

#add button
delete_frame = tk.Frame(root)
delete_frame.pack(anchor = "w", padx = 20, pady=10)

delete_a_book = tk.Button(root, text = "Delete a book", command = lambda: delete_one(delete_entry.get()))
delete_a_book.pack(anchor = "w", padx = 10)




# update button
update_frame = tk.Frame(root)
update_frame.pack(anchor = "e", padx = 20)

update_a_book = tk.Button(root, text = "update collection", command = lambda: update())
update_a_book.pack(anchor = "w", padx = 10)

# output
output = tk.Text(root, height='20', borderwidth='3')
output.place(anchor = "e", x=900, y=300)


def update():
    output.delete(1.0,tk.END)
    output.insert(tk.END, show())
    

# so basically have at the end of the add book and delete book a thing that will change a textbox that will have the current books.

root.mainloop()