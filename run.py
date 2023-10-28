import random
import os
from classes.colors import color



def clear_screen():
    """
    Defines function to clear the screen
    """
    os.system('cls' if os.name == 'nt' else 'clear')


DRAGON_LIST = ["knucker", "lung", "wyvern", "amphithere",
               "lindworm", "phoenix", "marsupial", "kirimu",
               "leviathan", "bakunawa", "imoogi", "kihawahine",
               "basilisk", "frost", "cockatrice", "tibetan",
               "taniwha", "uwabami", "orochi", "zahhak"
               ]


def game_intro():
    """
    Prints the name of the game, welcomes user and introduces to the game
    """
    logo = [
        " ____",
        "|  _ \ _ __ __ _  __ _  ___  _ __  ___",
        "| | | | '__/ _` |/ _` |/ _ \| '_ \/ __|",
        "| |_| | | | (_| | (_| | (_) | | | \_ \_",
        "|____/|_|  \__,_|\__, |\___/|_| |_|___/",
        "                 |___/",
    ]

    intro = [
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

    for line in logo:
        print(color["orange"].apply_color(line))

    for line in intro:
        print(color["yellow"].apply_color(line))


def dragon_img():
    """
    ASCII art to print dragon image at the end of the game
    """
    img = [
        r"""
                \||/
                |  @___oo
      /\  /\   / (__,,,,|
     ) /^\) ^\/ _)
     )   /^\/   _)
     )   _ /  / _)
 /\  )/\/ ||  | )_)
<  >      |(,,) )__)
 ||      /    \)___)\
 | \____(      )___) )___
  \______(_______;;; __;;;
    """
    ]
    for line in img:
        print(color["orange"].apply_color(line))


def game_rules(username):
    """
    Shows rules of the game if "yes" is chosen or
    if "no" is entered skips to verifying if player wants to play
    """
    rules = input(
        color["green"].apply_color("Would you like to see the rules (yes/no)?:\n")
        ).lower()

    if rules in ["yes", "y",]:
        clear_screen()
        # Display rules
        print("")
        print(color["green"].apply_color
              ("'Dragons' game rules")
              )
        print("")
        print(color["yellow"].apply_color
              ("1.Enter username to play")
              )
        print("")
        print(color["yellow"].apply_color
              ("2.Your mission is to guess the name of a concealed dragon")
              )
        print("")
        print(color["yellow"].apply_color
              ("3.You will be given a random dragon name to guess")
              )
        print("")
        print(color["yellow"].apply_color
              ("4.Guess one letter at a time")
              )
        print("")
        print(color["yellow"].apply_color
              ("5.You have 8 chances to guess")
              )
        print("")
        print(color["yellow"].apply_color
              ("6.Correct guess will reveal the letter")
              )
        print("")
        print(color["yellow"].apply_color
              ("7.Incorrect guess will add to attempt count")
              )
        print("")
        print(color["yellow"].apply_color
              ("8.When you guess the dragon or run out of attempts,")
              )
        print("")
        print(color["yellow"].apply_color
              ("dragon name and description will be revealed")
              )
        print("")

    elif rules in ["no", "n"]:
        # Skip to verifying if user wants to play
        continue_to_game(username)
        clear_screen()

    else:
        print(color["green"].apply_color("Please enter 'yes' or 'no'!"))


def continue_to_game(username):
    """
    Verifies if user wants to play the game by entering y for yes or n for no.\n
    If user enters yes, game starts, if user enters no - switches back to logo with intro\n
    and username entry
    """
    while True:
        choice = input(color["green"].apply_color
                       ("Would you like to play (yes/no)?:\n")
                       ).strip().lower()

        if choice in ["yes", "y"]:
            clear_screen()
            start_game(username, DRAGON_LIST)
            break
        if choice in ["no", "n"]:
            clear_screen()
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
    game_intro()
    enter_username()


def play_again(username):
    """
    Asks user if they would like to play the game again when previous game is finished.\n
    If user enters yes, game starts again, if no - switches back to logo and intro\n
    with thank you message
    """
    while True:
        choice = input(color["green"].apply_color
                       ("Would you like to play again (yes/no)?:\n")
                       ).strip().lower()

        if choice in ["yes", "y"]:
            clear_screen()
            start_game(username, DRAGON_LIST)
            break
        if choice in ["no", "n"]:
            clear_screen()
            exit_game()
        else:
            print(color["green"].apply_color("Please enter 'yes' or 'no'"))



def enter_username():
    """
    Asks user to create a username consisting of 4 - 15 letters.\n
    hows messages if user has empty space, less than 4 or more than 15 characters,\n
    numbers or special characters
    """
    while True:
        print()
        username = input(color["green"].apply_color
                         ("Please enter username:\n")
                         )

        if " " in username:
            print(color["green"].apply_color
                  ("Username can't contain empty spaces!")
                  )

        elif len(username) < 4:
            print(color["green"].apply_color
                  ("Sorry, username has to contain at least 4 characters!")
                  )

        elif len(username) > 15:
            print(color["green"].apply_color
                  ("Sorry, username can't be longer than 15 characters!")
                  )

        elif not username.isalpha():
            print(color["green"].apply_color
                  ("Sorry, username can't have numbers or special characters!")
                  )

        else:
            return username


def random_name(dragon):
    """
    Function to choose random dragon name from the list.
    """
    dragon = DRAGON_LIST
    return random.choice(dragon)


def display_name(name, guessed_letters):
    """
    Shows the name with guessed letters and underscores in places where letter hasn't been guessed
    """
    display = ""
    for letter in name:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display

def display_with_guessed_letters(name, guessed_letters):
    """
    Returns a string that shows guessed letters in their positions
    """
    display = display_name(name, guessed_letters)
    displayed_name = []
    for i, letter in enumerate(name):
        displayed_name.append(display[i])
    for letter in guessed_letters:
        if letter in name:
            index = name.index(letter)
            displayed_name[index] = letter
    return " ".join(displayed_name)


def is_name_guessed(name, guessed_letters):
    """
    Checks if dragon name is guessed
    """
    return all(letter in guessed_letters for letter in name)


def start_game(username, dragon):
    """
    This function initiates loop for the game. It prints welcoming message first and provides the\n
    info about the number of attempts user has to guess the dragon. The game then proceeds\n
    by user making guesses and tracking their progress until they either guess the name\n
    and win or run out of attempts. At the end it provides the dragon name and\n
    short description and asks if user wants to play again.
    """
    dragon = DRAGON_LIST
    name_to_guess = random_name(dragon)
    guessed_letters = []
    attempts = 8  # Max number of attempts

    print(color["green"].apply_color(f"Welcome, {username}!"))
    print("")
    print(color["green"].apply_color
          (f"You have {attempts} attempts to guess the name.")
          )
    print("")

    # Create a dictionary for dragon descriptions and match them to name
    dragon_descriptions = {
        "knucker": ("A type of water dragon from English folklore.\n"
                    "\n"
                    "Found in damp, wealden locations, near food sources such as rabbit warrens.\n"
                    "\n"
                    "Serpentine in appearance knucker has only vestigial wings and cannot fly."),
        "lung": ("A lung is most often found near rivers, streams and lakes\n"
                 "\n"
                 "that hide it's underwater nest. There are different types of lung dragons.\n"
                 "\n"
                 "Japanese lung has 4 toes, Indonesian 3, Chinese or Imperial lung has 5 toes."),
        "wyvern": ("A largest form of a dragon with 2 legs, 2 wings,\n"
                   "\n"
                   "and often a pointed tail which is said to be a venomous stinger.\n"
                   "\n"
                   "Muddy brown to lime green in color and 50 feet long."),
        "amphithere": ("Generally have light-colored feathers like a sunrise,\n"
                       "\n"
                       "a serpentine body similar to a lindworm, bat-like wings with feathers\n"
                       "\n"
                       "covering most of the forearm and often greenish in coloration,\n"
                       "\n"
                       "and a long tail much like a wyvern's tail."),
        "lindworm": ("A serpent-like dragon living deep in the forest\n"
                     "\n"
                     "with either two or no legs. Grows to 35 feet long, often green\n"
                     "\n"
                     "or sandy yellow in color."),
        "phoenix": ("Described as a composite of birds including the head of a golden pheasant,\n"
                    "\n"
                    "the body of a mandarin duck, the tail of a peacock, the legs of a crane,\n"
                    "\n"
                    "the mouth of a parrot, and the wings of a swallow."),
        "marsupial": ("Green or blue-ish in color with 2 powerful hind legs it grows 25 feet long\n"
                      "\n"
                      "and 15-18 feet high. It breathes blue smoke and rears one young at a time\n"
                      "\n"
                      "in a fiery pouch."),
        "kirimu": ("Described as a large serpent with black hide, teeth like a dog, a huge belly,\n"
                   "\n"
                   "the tail of an eagle and seven horned heads."),
        "leviathan": ("A sea serpent that is often an embodiment of chaos\n"
                      "\n"
                      "and threatening to eat the damned after their life. The body is\n"
                      "\n"
                      "mostly dark green in color, along with purple accents on its webbed\n"
                      "\n"
                      "limbs and head. It has protective plates on the underside of its body\n"
                      "\n"
                      "that start at the neck and run down to where the tentacles begin."),
        "bakunawa": ("A serpent-like dragon in Philippine mythology.\n"
                     "\n"
                     "It is usually depicted with a characteristic looped tail and\n"
                     "\n"
                     "a single horn on the nose. It is believed to be the cause of\n"
                     "\n"
                     "eclipses, earthquakes, rains, and wind."),
        "imoogi": ("A hornless ocean dragon, equated with a sea serpent. It means 'Great Lizard'.\n"
                   "\n"
                   "The legend of the Imoogi says that the sun god gave the Imoogi\n"
                   "\n"
                   "their power through a human girl, which would be transformed into\n"
                   "\n"
                   "the Imoogi on her 17th birthday."),
        "kihawahine": ("A Hawaiian shapeshifting lizard goddess with red or auburn hair.\n"
                       "\n"
                       "She may be missing an eye, lost in a battle with Haumea.\n"
                       "\n"
                       "Kihawahine is the oldest Aumakua or spiritual helper in Polynesia."),
        "basilisk": ("It can take the form of any dragon or psuedo-dragon and\n"
                     "\n"
                     "is armed with the deadliest bite of any creature,\n"
                     "\n"
                     "who causes death to those who look into its eyes."),
        "frost": ("Antarctic migrator, it can fly thousands of miles each year\n"
                  "\n"
                  "to ensure it spends the greater part of the year in winter climate.\n"
                  "\n"
                  "Grows 40 feet long and 12-15 feet high,\n"
                  "\n"
                  "pure white or white tinged with blue or pink in color."),
        "cockatrice": ("A two-legged dragon, part snake and part cock,\n"
                       "\n"
                       "that was said to be able to kill someone by looking at them.\n"
                       "\n"
                       "Hatched by a serpent from an egg laid by a rooster."),
        "tibetan": ("Almost invariable red in color it grows 40 feet long and 10-12 feet high.\n"
                    "\n"
                    "Lover of high altitudes and thinner than Asian lung."),
        "taniwha": ("A huge water lizard in Polynesian mythology.\n"
                    "\n"
                    "At sea, a taniwha often appears as a whale\n"
                    "\n"
                    "or a large shark such as southern right whale or whale shark.\n"
                    "\n"
                    "In inland waters, they may still be of whale-like dimensions,\n"
                    "\n"
                    "but look more like a gecko or tuatara, having a row of spines along back."),
        "uwabami": ("A giant serpent or giant python in the legends of Japan.\n"
                    "\n"
                    "The uwabami could ascend into the sky, or even fly through the air,\n"
                    "\n"
                    "with or without wings. These beasts conceal themselves by\n"
                    "\n"
                    "hiding in the mountains or in the water."),
        "orochi": ("Legendary eight-headed and eight-tailed Japanese dragon/serpent\n"
                   "\n"
                   "with cherry red eyes."),
        "zahhak": ("A serpent with 3 heads, and 1 of the heads is human.\n"
                   "\n"
                   "35 feet long serpent made of the purest, most malevolent darkness,\n"
                   "\n"
                   "and moves with a deadly quiet, slithering grace.")
    }

    while attempts > 0:
        display = display_name(name_to_guess, guessed_letters)
        display_with_spaces = " ".join(display) # Add spaces between letters
        print(color["orange"].apply_color(f"Name to guess: {display_with_spaces}"))
        guess = input(color["yellow"].apply_color("Guess a letter:\n")).lower()

        if len(guess) != 1 or not guess.isalpha():
            print(color["green"].apply_color("Please enter one letter only!"))
            print(color["green"].apply_color("Guess can't be empty, special character or number!"))
            print("")
            continue

        if guess in guessed_letters:
            print(color["green"].apply_color
                  ("Oh, sorry, you have already guessed that letter!")
                  )
            print(color["green"].apply_color
                  ("Please try again!")
                  )
            print("")
            continue

        if guess in name_to_guess:
            guessed_letters.append(guess)
            print(color["orange"].apply_color
                  (f"Name to guess:{display_with_guessed_letters(name_to_guess, guessed_letters)}"))
            print(color["green"].apply_color
                  ("Great guess! You are one step closer to revealing the dragon!")
                  )
            print("")

            if is_name_guessed(name_to_guess, guessed_letters):
                print(color["green"].apply_color
                      ("Congrats! You are a true dragon master!")
                      )
                print("")
                print(color["orange"].apply_color
                      (f"You guessed {name_to_guess} dragon!")
                      )

                # Retrieve and display the dragon's description
                if name_to_guess in dragon_descriptions:
                    print(color["yellow"].apply_color
                        (f"{dragon_descriptions[name_to_guess]}")
                        )
                break

        if guess not in name_to_guess:
            attempts -= 1
            print(color["green"].apply_color
                  (f"Aw, incorrect! You have {attempts} attempts remaining.")
                  )
            print("")

    if attempts == 0 and not is_name_guessed(name_to_guess, guessed_letters):
        print(color["green"].apply_color("Sorry, dragon got you!"))
        print("")
        print(color["orange"].apply_color(f"It was {name_to_guess} dragon!"))

        if name_to_guess in dragon_descriptions:
            print(color["yellow"].apply_color
                  (f"{dragon_descriptions[name_to_guess]}")
                  )


    dragon_img()
    play_again(username)
    game_intro()


def main():
    """
    Runs all functions in program
    """
    game_intro()
    username = enter_username()
    game_rules(username)
    continue_to_game(username)
    start_game(username, DRAGON_LIST)


main()
