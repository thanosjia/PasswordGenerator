import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_pwd():
    if passwordLabel.cget("text"):  # Check if a password has already been generated
        answer = messagebox.askyesno("Confirm", "Are you sure you want to generate a new password? The generated password will be lost.")
        if not answer:
            return

    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = "!#$%&"

    # Ensure at least one character from each set
    pwd = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]

    # Fill the rest of the password length with random characters from all sets
    all_characters = lowercase + uppercase + digits + special
    length = random.randint(12, 20) - len(pwd)  # Remaining length after adding one of each required type
    pwd += random.choices(all_characters, k=length)

    # Shuffle the resulting password list to ensure randomness
    random.shuffle(pwd)

    # Join the list into a string
    password = ''.join(pwd)

    passwordLabel.config(text=password)  # Update the password label with the generated password
    copyButton.config(state=tk.NORMAL)  # Enable the copy button when a password is generated



def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(passwordLabel.cget("text"))
    copyLabel.pack()
    root.after(3000, copyLabel.pack_forget)

root = tk.Tk()

# Adjust size
root.geometry("400x400")
 
# set minimum window size value
root.minsize(400, 400)
 
# set maximum window size value
root.maxsize(400, 400)

root.title('Password Generator v1.0')
welcomeLabel = tk.Label(root, text='Welcome to Password Generator v1.0!')
welcomeLabel.pack(pady=20)

passwordLabel = tk.Label(root, text='', font=('Helvetica', 12), fg='green')
passwordLabel.pack(pady=20)

copyLabel = tk.Label(root, text='Copied to clipboard!')

generateButton = tk.Button(root, text='Generate Password', width=25, command=generate_pwd)
generateButton.pack(pady=20)

copyButton = tk.Button(root, text='Copy to Clipboard', width=25, state=tk.DISABLED, command=copy_to_clipboard)
copyButton.pack(pady=10)

root.mainloop()
