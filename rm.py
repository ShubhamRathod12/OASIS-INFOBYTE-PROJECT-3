
import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip 

def generate_password(length, use_letters=True, use_numbers=True, use_symbols=True):
    """Generate a random password based on the specified criteria."""
    character_pool = ""
    
    if use_letters:
        character_pool += string.ascii_letters
    if use_numbers:
        character_pool += string.digits
    if use_symbols:
        character_pool += string.punctuation
    
    if not character_pool:
        raise ValueError("At least one character type must be selected.")
    
    password = ''.join(random.choice(character_pool) for _ in range(length))
    return password

def generate_and_display_password():
    try:
        length = int(length_entry.get())
        use_letters = letters_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()
        
        if length <= 0:
            raise ValueError("Length must be a positive integer.")
        
        password = generate_password(length, use_letters, use_numbers, use_symbols)
        password_entry.delete(0, tk.END)
        password_entry.insert(0, password)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def copy_to_clipboard():
    password = password_entry.get()
    if password:
        pyperclip.copy(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showerror("Copy Error", "No password to copy.")

# Create the main application window
app = tk.Tk()
app.title("Advanced Password Generator")
app.geometry("400x300")

# Create and place widgets
length_label = tk.Label(app, text="Password Length:")
length_label.pack(pady=5)
length_entry = tk.Entry(app)
length_entry.pack(pady=5)

letters_var = tk.BooleanVar(value=True)
letters_check = tk.Checkbutton(app, text="Include Letters", variable=letters_var)
letters_check.pack(pady=5)

numbers_var = tk.BooleanVar(value=True)
numbers_check = tk.Checkbutton(app, text="Include Numbers", variable=numbers_var)
numbers_check.pack(pady=5)

symbols_var = tk.BooleanVar(value=True)
symbols_check = tk.Checkbutton(app, text="Include Symbols", variable=symbols_var)
symbols_check.pack(pady=5)

generate_button = tk.Button(app, text="Generate Password", command=generate_and_display_password)
generate_button.pack(pady=10)

password_label = tk.Label(app, text="Generated Password:")
password_label.pack(pady=5)
password_entry = tk.Entry(app, width=50)
password_entry.pack(pady=5)

copy_button = tk.Button(app, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack(pady=10)

# Run the main application loop
app.mainloop()
