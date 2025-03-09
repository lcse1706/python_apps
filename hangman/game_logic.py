import random

WORDS = ["python", "tkinter", "developer", "hangman", "programming", "code", "computer", "software", "django", "javascript"]

HANGMAN_PICS = [
    r"""
       +---+
       |   |
           |
           |
           |
           |
    =========
    """,
    r"""
       +---+
       |   |
       O   |
           |
           |
           |
    =========
    """,
    r"""
       +---+
       |   |
       O   |
       |   |
           |
           |
    =========
    """,
    r"""
       +---+
       |   |
       O   |
      /|   |
           |
           |
    =========
    """,
    r"""
       +---+
       |   |
       O   |
      /|\  |
           |
           |
    =========
    """,
    r"""
       +---+
       |   |
       O   |
      /|\  |
      /    |
           |
    =========
    """,
    r"""
       +---+
       |   |
       O   |
      /|\  |
      / \  |
           |
    =========
    """
]

game_state = {
    "word": "",
    "guessed_letters": set(),
    "attempts": 6
}

def initialize_game():
    game_state["word"] = random.choice(WORDS).lower()
    game_state["guessed_letters"].clear()
    game_state["attempts"] = 6
    return game_state

def update_display_word():
    return " ".join([letter if letter in game_state["guessed_letters"] else "_" for letter in game_state["word"]])

def check_letter(letter):
    if len(letter) != 1 or not letter.isalpha():
        return "Enter a single letter!"
    
    if letter in game_state["guessed_letters"]:
        return "You already guessed that letter!"

    game_state["guessed_letters"].add(letter)

    if letter in game_state["word"]:
        return "Correct!"
    else:
        game_state["attempts"] -= 1
        return "Wrong!"

def get_hangman_stage():
    return HANGMAN_PICS[6 - game_state["attempts"]]

def is_won():
    return "_" not in update_display_word()

def is_lost():
    return game_state["attempts"] == 0
