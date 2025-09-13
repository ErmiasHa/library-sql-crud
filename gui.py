import tkinter as tk
from tkinter import messagebox
import db

def view_books():
    listbox.delete(0, tk.END)
    for book in db.view_books():
        listbox.insert(tk.END, book)

def add_book():
    title = title_entry.get()
    author = author_entry.get()
    year = year_entry.get()
    isbn = isbn_entry.get()
    if title and author:
        db.add_book(title, author, year, isbn)
        messagebox.showinfo("Info", "✅ Bok tillagd!")
        view_books()
    else:
        messagebox.showwarning("Varning", "Titel och författare krävs")

def search_books():
    listbox.delete(0, tk.END)
    results = db.search_books(title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get())
    for book in results:
        listbox.insert(tk.END, book)

def delete_book():
    selected = listbox.curselection()
    if selected:
        book_id = listbox.get(selected[0])[0]
        db.delete_book(book_id)
        messagebox.showinfo("Info", "🗑️ Bok borttagen!")
        view_books()
    else:
        messagebox.showwarning("Varning", "Välj en bok att ta bort")

def update_book():
    selected = listbox.curselection()
    if selected:
        book_id = listbox.get(selected[0])[0]
        db.update_book(book_id, title_entry.get(), author_entry.get(), year_entry.get(), isbn_entry.get())
        messagebox.showinfo("Info", "✅ Bok uppdaterad!")
        view_books()
    else:
        messagebox.showwarning("Varning", "Välj en bok att uppdatera")

# Initiera DB
db.connect()

# Tkinter fönster
root = tk.Tk()
root.title("📚 Mini Bibliotekssystem (GUI)")

# Labels
tk.Label(root, text="Titel").grid(row=0, column=0)
tk.Label(root, text="Författare").grid(row=0, column=2)
tk.Label(root, text="År").grid(row=1, column=0)
tk.Label(root, text="ISBN").grid(row=1, column=2)

# Entry widgets
title_entry = tk.Entry(root)
title_entry.grid(row=0, column=1)
author_entry = tk.Entry(root)
author_entry.grid(row=0, column=3)
year_entry = tk.Entry(root)
year_entry.grid(row=1, column=1)
isbn_entry = tk.Entry(root)
isbn_entry.grid(row=1, column=3)

# Listbox + scrollbar
listbox = tk.Listbox(root, height=10, width=60)
listbox.grid(row=2, column=0, columnspan=4, pady=10)

scrollbar = tk.Scrollbar(root)
scrollbar.grid(row=2, column=4, sticky="ns")

listbox.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=listbox.yview)

# Buttons
tk.Button(root, text="Visa alla", width=12, command=view_books).grid(row=3, column=0)
tk.Button(root, text="Sök", width=12, command=search_books).grid(row=3, column=1)
tk.Button(root, text="Lägg till", width=12, command=add_book).grid(row=3, column=2)
tk.Button(root, text="Uppdatera", width=12, command=update_book).grid(row=3, column=3)
tk.Button(root, text="Ta bort", width=12, command=delete_book).grid(row=4, column=1)
tk.Button(root, text="Avsluta", width=12, command=root.quit).grid(row=4, column=2)

view_books()
root.mainloop()
