import tkinter as tk
from game_logic import initialize_game, update_display_word, check_letter, get_hangman_stage, is_won, is_lost, game_state

initialize_game()

def update_ui():
    word_display.set(update_display_word())
    hangman_label.config(text=get_hangman_stage())
    attempts_label.config(text=f"Attempts left: {game_state['attempts']}")

def check_letter_event(event):
    letter = entry.get().lower()
    entry.delete(0, tk.END)

    message = check_letter(letter)
    message_label.config(text=message)

    update_ui()

    if is_won():
        message_label.config(text="You won!")
    elif is_lost():
        message_label.config(text=f"Game Over! Word was: {game_state['word']}")

def restart_game():
    initialize_game()
    message_label.config(text="")
    update_ui()

# GUI setup
root = tk.Tk()
root.title("Hangman Game")
root.geometry("400x450")

word_display = tk.StringVar()
hangman_label = tk.Label(root, text=get_hangman_stage(), font=("Courier", 12))
hangman_label.pack(pady=10)

label = tk.Label(root, textvariable=word_display, font=("Arial", 20))
label.pack(pady=20)

entry = tk.Entry(root, font=("Arial", 14))
entry.pack()
entry.bind("<Return>", check_letter_event)

message_label = tk.Label(root, text="", font=("Arial", 14))
message_label.pack(pady=10)

attempts_label = tk.Label(root, text=f"Attempts left: {game_state['attempts']}", font=("Arial", 14))
attempts_label.pack()

restart_button = tk.Button(root, text="Restart", command=restart_game, font=("Arial", 14))
restart_button.pack(pady=10)

update_ui()
root.mainloop()
