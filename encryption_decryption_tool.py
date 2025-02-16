import tkinter as tk
from tkinter import ttk

def encryption():
    t = text.get()
    k = int(key.get())  # Convert the key to an integer
    en = ""

    for letter in t:
        if letter.isalpha():  # Check if the character is a letter
            new_position = (alphabets.find(letter) + k) % len(alphabets)
            en += alphabets[new_position]
        else:
            en += letter  # Keep non-alphabet characters unchanged

    result_text.config(state="normal")
    result_text.delete(1.0, "end")
    result_text.insert("end", en)
    result_text.config(state="disabled")

def decryption():
    t = text.get()
    k = int(key.get())  # Convert the key to an integer
    de = ""

    for letter in t:
        if letter.isalpha():  # Check if the character is a letter
            new_position = (alphabets.find(letter) - k) % len(alphabets)
            de += alphabets[new_position]
        else:
            de += letter  # Keep non-alphabet characters unchanged

    result_text.config(state="normal")
    result_text.delete(1.0, "end")
    result_text.insert("end", de)
    result_text.config(state="disabled")

# Create the main window
window = tk.Tk()
window.title("Message Encryption Decryption")
window.geometry("400x400")  # Set the window size

# Create a style for a more modern look
style = ttk.Style()
style.configure("TButton", padding=10, font=('Helvetica', 12))
style.configure("TLabel", font=('Helvetica', 14), foreground="black")
style.configure("TFrame", background="white")

# Create a frame for better organization
frame = ttk.Frame(window)
frame.pack(fill=tk.BOTH, expand=True, padx=20, pady=20)

# Labels
ttk.Label(frame, text="Enter the text to be encrypted and decrypted:", font=('Helvetica', 14)).pack()
text = tk.StringVar()
entry_text = ttk.Entry(frame, textvariable=text, font=('Helvetica', 12))
entry_text.pack()

ttk.Label(frame, text="Enter the key:", font=('Helvetica', 14)).pack()
key = tk.StringVar()
entry_key = ttk.Entry(frame, textvariable=key, font=('Helvetica', 12), show="*")  # Show key as asterisks
entry_key.pack()

# Buttons
encrypt_button = ttk.Button(frame, text="ENCRYPT", style="TButton", command=encryption)
encrypt_button.pack(pady=10)
decrypt_button = ttk.Button(frame, text="DECRYPT", style="TButton", command=decryption)
decrypt_button.pack(pady=10)

# Text widget for displaying Results
result_text = tk.Text(frame, wrap=tk.WORD, height=5, font=('Helvetica', 12), state="disabled")
result_text.pack(fill=tk.BOTH, expand=True)

alphabets = "abcdefghijklmnopqrstuvwxyz"

window.mainloop()