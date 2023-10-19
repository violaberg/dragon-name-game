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


def random_name(dragon_list):
    """
    Function to choose random dragon name from the list
    """
    dragon_list = ["knucker", "asian lung", "wyvern", "amphithere",
                   "lindworm", "phoenix", "marsupial", "kirimu",
                   "leviathan", "bakunawa", "imoogi", "kihawahine",
                   "basilisk", "frost", "cockatrice", "horned serpent",
                   "taniwha", "uwabami", "orochi", "zahhak"
                   ]
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


def start_game():
    """
    Loop for the game
    """
    name_to_guess = random_name(dragon_list)
    guessed_letters = []
    attempts = 8
    
    print("Welcome to Dragon Guessing Game!")
    print("You have {} attempts to guess the name."format(attempts))
    
    while attempts > 0:
        print("\nName to guess {}".format(display_name(name_to_guess, guessed_letters)))
        guess = input("Guess a letter {}").lower()
        
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
            print("\nCongratulations! You are a true dragon master! You guessed {} dragon!".format(name_to_guess))
            break
        
        if "_" in display_name(name_to_guess, guessed_letters):
            print("Aw, sorry, you are out of attempts! Dragon got you! Name was: {}".format(name_to_guess))

def main():
    """
    Runs all functions in program
    """
    main_logo()
    intro()


main()
start_game()