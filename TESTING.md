# Testing Page

## **Table of Contents**

## **Manual testing**
I manually tested this project several ways:
### **PEP8 Linter**
It showed a lot of errors, most being too many characters in line that was easily fixed by creating additional lines for text. Couple were accidental extra blank lines or whitespaces. Here is the screenshot of first check with CI provided Linter:<br>
![PEP8 Linter errors](../dragon-guessing-game/docs/screenshots/linter-errors.png)

### **Playing game**
I played the game countless times both in VSCode terminal and deployed version to fix all bugs and make sure there are no errors found. Additionally it helped with choosing colors and adding ASCII images to make game more appealing.

## **Bugs and fixes**
* ***Intended Outcome***

    Added background image to make game more appealing to user

    **Problem**

    After adding background image and creating CSS properties for it, I noticed it wasn't showing up in deployed app, only in live server in VSCode. 
    ![Background error](../dragon-guessing-game/docs/screenshots/background-error.png)

    **Reason**

    After a quick Google, Slack search, remembering my first hackathon with the same issue and a chat with my mentor, I knew Heroku doesn't host static files.

    **Solution**

    My mentor suggested couple of ways and introduced me to [Cloudinary](https://cloudinary.com/) as a way to add web hosted background which was the way I solved the issue.

* ***Intended Outcome***

    After a letter is guessed correctly in game, replace placement with guessed letter in correct possition.

    **Problem**

    Guessed letter printed under Guess a letter line not beside Name to guess, replacing placement in correct position.
    ![Letter not on line](../dragon-guessing-game/docs/screenshots/guessed-letter-not-on-line.png)

    **Reason**

    No function created to replace placement with letter.

    **Solution**

    I created function display_with_guessed_letters that iterates through dragon name to be guessed and replaces placement with guessed letter.

* ***Intended Outcome***

    **Problem**

    **Reason**

    **Solution**

* ***Intended Outcome***

    **Problem**

    **Reason**

    **Solution**