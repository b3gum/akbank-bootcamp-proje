Python 3.12.2 (tags/v3.12.2:6abddd9, Feb  6 2024, 21:26:36) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import tkinter as tk
from tkinter import messagebox

class Library:
    def _init_(self, filename="books.txt"):
        self.filename = filename
        self.file = open(self.filename, "a+")

    def _del_(self):
        self.file.close()

    def list_books(self):
        self.file.seek(0)
        books = self.file.read().splitlines()
        book_list = "\n".join([book.strip().split(',')[0] for book in books])
        if book_list == "":
            messagebox.showerror("List of Books", "Empty")
        else:
            messagebox.showinfo("List of Books", book_list)

    def add_book(self):
        title = entry_title.get()
        author = entry_author.get()
        release_year = entry_release_year.get()
        num_pages = entry_num_pages.get()
        book_info = f"{title},{author},{release_year},{num_pages}\n"
        self.file.write(book_info)
        messagebox.showinfo("Success", "Book added successfully.")

    def remove_book(self):
        title = entry_remove_title.get()
        if title == "":
            messagebox.showerror("Remove Book", "Please enter a title.")
            return

        self.file.seek(0)
        books = self.file.readlines()
        updated_books = [book for book in books if title not in book]

        if len(updated_books) == len(books):
            messagebox.showerror("Remove Book", "Invalid title.")
        else:
            self.file.seek(0)
            self.file.truncate(0)
            self.file.writelines(updated_books)
            self.file.truncate()
            self.file.flush()
            messagebox.showinfo("Remove Book", "Book removed successfully.")


def list_books():
    lib.list_books()

def add_book():
    lib.add_book()

def remove_book():
    lib.remove_book()

... root = tk.Tk()
... root.title("Library Management System")
... 
... lib = Library()
... 
... label_title = tk.Label(root, text="Title:")
... label_title.grid(row=0, column=0)
... entry_title = tk.Entry(root)
... entry_title.grid(row=0, column=1)
... 
... label_author = tk.Label(root, text="Author:")
... label_author.grid(row=1, column=0)
... entry_author = tk.Entry(root)
... entry_author.grid(row=1, column=1)
... 
... label_release_year = tk.Label(root, text="Release Year:")
... label_release_year.grid(row=2, column=0)
... entry_release_year = tk.Entry(root)
... entry_release_year.grid(row=2, column=1)
... 
... label_num_pages = tk.Label(root, text="Number of Pages:")
... label_num_pages.grid(row=3, column=0)
... entry_num_pages = tk.Entry(root)
... entry_num_pages.grid(row=3, column=1)
... 
... button_list_books = tk.Button(root, text="List Books", command=list_books)
... button_list_books.grid(row=4, column=0)
... 
... button_add_book = tk.Button(root, text="Add Book", command=add_book)
... button_add_book.grid(row=4, column=1)
... 
... label_remove_title = tk.Label(root, text="Title to Remove:")
... label_remove_title.grid(row=5, column=0)
... entry_remove_title = tk.Entry(root)
... entry_remove_title.grid(row=5, column=1)
... 
... button_remove_book = tk.Button(root, text="Remove Book", command=remove_book)
... button_remove_book.grid(row=6, column=0, columnspan=2)
... 
