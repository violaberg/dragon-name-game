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


def main():
    """
    Runs all functions in program
    """
    main_logo()
    intro()


main()