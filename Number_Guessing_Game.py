import tkinter as tk
from tkinter import messagebox
import random

# Generate random number
secret_number = random.randint(1, 100)
attempts = 0

# Function to check guess
def check_guess():
    global attempts
    guess = entry.get()

    if not guess.isdigit():
        messagebox.showwarning("Invalid Input", "Please enter a valid number.")
        return

    guess = int(guess)
    attempts += 1

    if guess < secret_number:
        result_label.config(text="Too Low! Try Again.", fg="blue")
    elif guess > secret_number:
        result_label.config(text="Too High! Try Again.", fg="red")
    else:
        messagebox.showinfo(
            "Congratulations!",
            f"You guessed the number in {attempts} attempts!"
        )
        root.destroy()

# Create main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("350x250")
root.config(bg="lightyellow")

# Title
title_label = tk.Label(
    root,
    text="🎮 Number Guessing Game",
    font=("Arial", 16, "bold"),
    bg="lightyellow"
)
title_label.pack(pady=10)

# Instructions
instruction_label = tk.Label(
    root,
    text="Guess a number between 1 and 100",
    font=("Arial", 12),
    bg="lightyellow"
)
instruction_label.pack()

# Entry box
entry = tk.Entry(root, font=("Arial", 14), justify="center")
entry.pack(pady=10)

# Guess button
guess_button = tk.Button(
    root,
    text="Check Guess",
    font=("Arial", 12),
    command=check_guess,
    bg="lightblue"
)
guess_button.pack(pady=5)

# Result label
result_label = tk.Label(
    root,
    text="",
    font=("Arial", 12, "bold"),
    bg="lightyellow"
)
result_label.pack(pady=10)

# Run app
root.mainloop()