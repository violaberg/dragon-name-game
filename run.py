import random


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
        print(line)


def intro():
    """
    Introduces to game
    """
    game_intro = [
        "Welcome to the mystical world of Dragons!",
        "A captivating adventure that will test your knowledge of dragons.",
        "Each dragon has concealed its identity behind a web of letters,",
        "daring you to uncover its name, one letter at a time.",
        "The adventure awaits, and the dragon awaits your daring guesses."
    ]
    for line in game_intro:
        print(line)


def continue_to_game(username, dragon_list):
    """
    Verifies user wants to play the game by entering y for yes or n for no
    """
    while True:
        choice = input("Would you like to play (yes/no)?:\n").strip().lower()

        if choice in ["yes", "y"]:
            start_game(username, dragon_list)
        elif choice in ["no", "n"]:
            exit_game()
        else:
            print("Please enter yes or no")


def exit_game():
    """
    Exits game gracefully and thanks user for visiting.
    """
    print("Thank you for visiting 'Dragons' game. Goodbye!")
    exit()


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
            print("Sorry, username can't contain numbers or special characters!")

        else:
            return username


def random_name(dragon_list):
    """
    Function to choose random dragon name from the list.
    """
    return random.choice(dragon_list)


def display_name(name, guessed_letters):
    """
    Shows the name with guessed letters
    """
    display = ""
    for letter in name:
        if letter in guessed_letters:
            display += letter
        else:
            display = "_"
    return display


def start_game(username, dragon_list):
    """
    Loop for the game
    """
    name_to_guess = random_name(dragon_list)
    guessed_letters = []
    attempts = 8

    print(f"Welcome, {username}!")
    print(f"You have {attempts} attempts to guess the name.")

    while attempts > 0:
        print(f"Name to guess: {display_name(name_to_guess, guessed_letters)}")
        guess = input("Guess a letter:\n").lower()

        if len(guess) != 1 or not guess.isalpha():
            print("Please enter one letter!")
            continue

        if guess in guessed_letters:
            print("Oh, sorry, you have already guessed that letter!")
            continue

        guessed_letters.append(guess)

        if guess in name_to_guess:
            print("Great guess! You are one step closer to revealing dragon!")
        else:
            print("Aw, incorrect! Please try again!")
            attempts -= 1

        if "_" not in display_name(name_to_guess, guessed_letters):
            print("Congrats! You are a true dragon master!")
            print(f"You guessed {name_to_guess} dragon!")
            break

        if "_" in display_name(name_to_guess, guessed_letters):
            print("Aw, sorry, you are out of attempts! Dragon got you!")
            print(f"Name to guess was: {name_to_guess}")


def main():
    """
    Runs all functions in program
    """
    main_logo()
    dragon_list = ["knucker", "asian lung", "wyvern", "amphithere",
                   "lindworm", "phoenix", "marsupial", "kirimu",
                   "leviathan", "bakunawa", "imoogi", "kihawahine",
                   "basilisk", "frost", "cockatrice", "horned serpent",
                   "taniwha", "uwabami", "orochi", "zahhak"
                   ]
    intro()
    username = enter_username()
    continue_to_game(username, dragon_list)
    start_game(username, dragon_list)


main()