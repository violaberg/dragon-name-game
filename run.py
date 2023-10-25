import random
import os
from colors import color


def clear_screen():
    """
    Defines function to clear the screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')


dragon_list = ["knucker", "lung", "wyvern", "amphithere",
               "lindworm", "phoenix", "marsupial", "kirimu",
               "leviathan", "bakunawa", "imoogi", "kihawahine",
               "basilisk", "frost", "cockatrice", "serpent",
               "taniwha", "uwabami", "orochi", "zahhak"
               ]


def main_logo():
    """
    Print the name of the game
    """
    logo = [
        " ____",
        "|  _ \ _ __ __ _  __ _  ___  _ __  ___",
        "| | | | '__/ _` |/ _` |/ _ \| '_ \/ __|",
        "| |_| | | | (_| | (_| | (_) | | | \_ \_",
        "|____/|_|  \__,_|\__, |\___/|_| |_|___/",
        "                 |___/",
    ]
    for line in logo:
        print(color["orange"].apply_color(line))


def intro():
    """
    Introduces to game
    """
    game_intro = [
        "",
        "Welcome to the mystical world of Dragons!",
        "",
        "A captivating adventure that will test your knowledge of dragons.",
        "",
        "Each dragon has concealed its identity behind a web of letters,",
        "",
        "daring you to uncover its name, one letter at a time.",
        "",
        "The adventure awaits, and the dragon awaits your daring guesses.",
        ""
    ]
    for line in game_intro:
        print(color["yellow"].apply_color(line))


def game_rules(username):
    """
    Shows rules of the game if "yes" is chosen or
    if "no" is entered skips to verifying if player wants to play
    """
    rules = input("Would you like to see the rules (yes/no)?:\n").lower()

    if rules in ["yes", "y",]:
        clear_screen()
        # Display rules
        print("")
        print("'Dragons' game rules")
        print("")
        print("1.Enter username to play")
        print("")
        print("2.Your mission is to guess the name of a concealed dragon")
        print("")
        print("3.You will be given a random dragon name to guess")
        print("")
        print("4.Guess one letter at a time")
        print("")
        print("5.You have 8 chances to guess")
        print("")
        print("6.Correct guess will reveal the letter,")
        print("")
        print("7.Incorrect guess will add to attempt count")
        print("")
        print("8.When you guess the dragon or run out of attempts,")
        print("")
        print("dragon name and description will be revealed")
        print("")

    elif rules in ["no", "n"]:
        # Skip to verifying if user wants to play
        continue_to_game(username, dragon_list)

    else:
        print(color["green"].apply_color("Please enter 'yes' or 'no'!"))


def continue_to_game(username, dragons):
    """
    Verifies user wants to play the game by entering y for yes or n for no
    """
    dragons = dragon_list
    while True:
        choice = input("Would you like to play (yes/no)?:\n").strip().lower()

        if choice in ["yes", "y"]:
            clear_screen()
            start_game(username, dragons)
            break
        if choice in ["no", "n"]:
            exit_game()
        else:
            print(color["green"].apply_color("Please enter 'yes' or 'no'"))


def exit_game():
    """
    Thanks user for visiting and exits game gracefully by returning to logo.
    """
    print(color["green"].apply_color("Thank you for visiting 'Dragons' game."))
    print("")
    print(color["green"].apply_color("Goodbye!"))
    main_logo()
    intro()


def enter_username():
    """
    Asks user to create a username consisting of 4 - 15 letters.
    """
    while True:
        print()
        username = input("Please enter username:\n")

        if " " in username:
            print("Username can't contain empty spaces!")

        elif len(username) < 4:
            print("Sorry, username has to contain at least 4 characters!")

        elif len(username) > 15:
            print("Sorry, username can't be longer than 15 characters!")

        elif not username.isalpha():
            print("Sorry, username can't have numbers or special characters!")

        else:
            return username


def random_name(dragons):
    """
    Function to choose random dragon name from the list.
    """
    return random.choice(dragons)


def display_name(name, guessed_letters):
    """
    Shows the name with guessed letters
    """
    display = ""
    for letter in name:
        if letter in guessed_letters:
            display += letter
        else:
            display = ""
    return display


def start_game(username, dragons_list):
    """
    Loop for the game
    """
    name_to_guess = random_name(dragons_list)
    guessed_letters = []
    attempts = 8  # Max number of attempts

    print(color["green"].apply_color(f"Welcome, {username}!"))
    print("")
    print(f"You have {attempts} attempts to guess the name.")
    print("")

    # Create a dictionary for dragon descriptions and match them to name
    dragon_descriptions = {
        "knucker": "A type of water dragon from English folklore.",
        "lung": "A type of water dragon from English folklore.",
        "wyvern": "A type of water dragon from English folklore.",
        "amphithere": "A type of water dragon from English folklore.",
        "lindworm": "A type of water dragon from English folklore.",
        "phoenix": "A type of water dragon from English folklore.",
        "marsupial": "A type of water dragon from English folklore.",
        "kirimu": "A type of water dragon from English folklore.",
        "leviathan": "A type of water dragon from English folklore.",
        "bakunawa": "A type of water dragon from English folklore.",
        "imoogi": "A type of water dragon from English folklore.",
        "kihawahine": "A type of water dragon from English folklore.",
        "basilisk": "A type of water dragon from English folklore.",
        "frost": "A type of water dragon from English folklore.",
        "cockatrice": "A type of water dragon from English folklore.",
        "serpent": "A type of water dragon from English folklore.",
        "taniwha": "A type of water dragon from English folklore.",
        "uwabami": "A type of water dragon from English folklore.",
        "orochi": "A type of water dragon from English folklore.",
        "zahhak": "A type of water dragon from English folklore."
    }

    while attempts > 0:
        display = display_name(name_to_guess, guessed_letters)
        print(color["orange"].apply_color(f"Name to guess: {display}"))
        guess = input(color["yellow"].apply_color("Guess a letter:\n")).lower()

        if len(guess) != 1 or not guess.isalpha():
            print(color["green"].apply_color("Please enter one letter!"))
            continue

        if guess in guessed_letters:
            print("Oh, sorry, you have already guessed that letter!")
            print("Try again!")
            continue

        guessed_letters.append(guess)

        if display == name_to_guess:
            print("Great guess! You are one step closer to revealing dragon!")
            print("Congrats! You are a true dragon master!")
            print(f"You guessed {name_to_guess} dragon!")

            # Retrieve and display the dragon's description
            if name_to_guess in dragon_descriptions:
                print(f"Description: {dragon_descriptions[name_to_guess]}")

            break

        if guess not in name_to_guess:
            print(f"Aw, incorrect! You have {attempts} attempts remaining.")
            attempts -= 1

    if attempts == 0:
        print("Aw, sorry, you are out of attempts! Dragon got you!")
        print(color["orange"].apply_color(f"It was {name_to_guess} dragon!"))

        if name_to_guess in dragon_descriptions:
            print(f"Description: {dragon_descriptions[name_to_guess]}")

    clear_screen()
    main_logo()


def main():
    """
    Runs all functions in program
    """
    main_logo()
    intro()
    username = enter_username()
    game_rules(username)
    continue_to_game(username, dragon_list)
    start_game(username, dragon_list)


main()
