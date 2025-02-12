import tkinter as tk
import random

WORDS = ["python", "tkinter", "developer", "hangman", "programming", "code", "computer", "software", "django", "javascript"],
word = random.choice(WORDS).lower()
guessed_letters = set()
attempts = 6

def update_word_display():
    displayed = " ".join([letter if letter in guessed_letters else "_" for letter in word])
    word_display.set(displayed)

def check_letter(event):
    global attempts
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if len(letter) != 1 or not letter.isalpha():
        message_label.config(text="Enter a single letter!")
        return

    if letter in guessed_letters:
        message_label.config(text="You already guessed that letter!")
        return

    guessed_letters.add(letter)

    if letter in word:
        message_label.config(text="Correct!")
    else:
        attempts -= 1
        message_label.config(text="Wrong!")

    update_word_display()
    attempts_label.config(text=f"Attempts left: {attempts}")

    if "_" not in word_display.get():
        message_label.config(text="You won!")
    elif attempts == 0:
        message_label.config(text=f"Game Over! Word was: {word}")

def restart_game():
    global word, guessed_letters, attempts
    word = random.choice(WORDS).lower()
    guessed_letters.clear()
    attempts = 6
    update_word_display()
    attempts_label.config(text=f"Attempts left: {attempts}")
    message_label.config(text="")

# GUI setup
root = tk.Tk()
root.title("Hangman Game")

word_display = tk.StringVar()
update_word_display()

label = tk.Label(root, textvariable=word_display, font=("Arial", 20))
label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()
entry.bind("<Return>", check_letter)

message_label = tk.Label(root, text="", font=("Arial", 14))
message_label.pack(pady=10)

attempts_label = tk.Label(root, text=f"Attempts left: {attempts}", font=("Arial", 14))
attempts_label.pack()

restart_button = tk.Button(root, text="Restart", command=restart_game, font=("Arial", 14))
restart_button.pack(pady=10)

root.mainloop()
