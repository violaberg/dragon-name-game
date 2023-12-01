# **Dragons**

## **Overview**

Guess the name of the mysterious dragon in this exciting terminal-based word guessing game! You'll be presented with a hidden dragon name, and your task is to reveal the name one letter at a time. With a limited number of incorrect guesses, can you unveil the dragon's identity and discover the secrets it holds? A fun and challenging adventure awaits as you uncover the name of the enigmatic dragon while enjoying the thrill of the hunt. Prepare to test your word-solving skills!

I chose to create a dragon guessing game for this project inspired by my 5 year old son and his ever-lasting interest in dragons. During planning phase I decided to add a background, some color and ASCII art to create more visually appealing and easy to understand game to attract grown-ups and children alike. Get started, enjoy and don't get burned!<br>
Link to game: [Dragons](https://dragon-name-game-933534f361b7.herokuapp.com/)

![Deployed game](docs/screenshots/dragons-shot.png)

## **Table of Contents** :
- [**Dragons**](#dragons)
  - [**Overview**](#overview)
  - [Table of Contents:](#table-of-contents)
  - [**Planning**](#planning)
    - [**Intended Users**](#intended-users)
    - [**User Stories**](#user-stories)
    - [**Goals**](#goals)
    - [**Lucidchart**](#lucidchart)
  - [**Features and Future Development**](#features-and-future-development)
    - [**Favicon**](#favicon)
    - [**Game intro**](#game-intro)
    - [**Username entry / rules question**](#username-entry--rules-question)
    - [**Username error messages**](#username-error-messages)
    - [**Rules**](#rules)
    - [**Guess messages**](#guess-messages)
    - [**Game won / lost**](#game-won--lost)
    - [**Thank You message**](#thank-you-message)
    - [**Dragon ASCII art**](#dragon-ascii-art)
    - [**Future Development**](#future-development)
  - [**Testing**](#testing)
  - [**Deployment**](#deployment)
    - [**Deploying to Heroku**](#deploying-to-heroku)
  - [**Acknowledgments and Credits**](#acknowledgments-and-credits)

## **Planning**

### **Intended Users**

* Anyone who loves a guessing game.
* Anyone with interest in dragons.
* People who are looking for fun with added challenge.

### **User Stories**

* As a user, I want to know the main intention of the site.
* As a user I want to see the game rules clearly written.
* As a user I want to play puzzle without compromising space.
* As a user I want to be able to navigate through the site easily.

### **Goals**

* Make game easy to navigate through.
* Provide a free guessing game.
* Provide simple and short rules of the game.
* Educate user about different dragons and provide a short description of each.

### **Lucidchart**

I created a flowchart using [Lucidchart](https://lucid.co/?_gl=1*x824jw*_ga*MTQ0OTcxNjc5Ni4xNjk3NTYwMDUx*_ga_MPV5H3XMB5*MTY5NzYyMzg3Ny4zLjAuMTY5NzYyMzg3Ny42MC4wLjA.) website to help with a flow of the game, with some deviation during development to improve the game.<br>

![Lucidchart](docs/dragon_guessing_game.jpeg)

## **Features and Future Development**

### **Favicon**

I originally created favicon using a vector from [Vecteezy](https://www.vecteezy.com/) website with an idea to recreate the look of a dragon eye and used [Faviconer](http://www.faviconer.com/) website to change it into favicon but soon after realized [Heroku](https://www.heroku.com/) doesn't host static files. During session with my mentor he explained how to use web hosted image so I used [Google](https://www.google.com/) to search for dragon's eye and I chose one from [Deviant Art](https://www.deviantart.com/christoskarapanos/art/Dragon-s-Eye-585971591) and added it succesfully to my project.

### **Game intro**

Welcomes user to 'Dragons' game with a short introduction to intrigue them and asks to enter username.

![Game intro](docs/screenshots/game-intro.png)

### **Username entry / rules question**

Once username has been entered correctly, asks if user would like to see the rules of the game. By entering 'yes', starts the game. If user enters 'no', returns to game intro screen.

![Username and rules](docs/screenshots/username-rules.png)

### **Username error messages**

If user doesn't enter username accordingly to rules, shows appropriate error message.

![Username errors](docs/screenshots/username-errors.png)

### **Rules**

Shows clearly written short rules of the game and asks if user would like to play.

![Rules](docs/screenshots/rules.png)

### **Guess messages**

Shows appropriate message after a guess is entered to let user know if he has guessed correct/ incorrect or input is invalid. If guess is incorrect, shows how many attempts to guess user has. If guess is correct, guessed letter appears in correct dragon name placement.

![Guess messages](docs/screenshots/guess-message1.png)

![Invalid guess](docs/screenshots/invalid-guess.png)

### **Game won / lost**

At the end, the game either congrats user or expresses sympathy for loss and shows dragon name revealed/ not guessed and it's description with a ASCII dragon art. Initially I wanted to clear the screen one game has finished before dragon name and description appears but decided to leave it as an option for user to be able to check guessing history.<br>

I chose this cute and happy looking dragon ASCII art to show up when user wins the game, reminding me of a dragon from my childhood cartoon.

![Game won](docs/screenshots/game-won-ascii-art.png)

This fire blowing dragon appears if user has lost the game. Be careful not to get burned to crisp!

![Game lost](docs/screenshots/game-lost-ascii-art.png)

### **Thank You message**

Thanks user for visiting 'Dragons' game and asks if user wants to play again.

![Thank you message](docs/screenshots/thank-you-message1.png)

### **Dragon ASCII art**

Overall I got intrigued by ASCII art, amazingly never seen before. I think together with colourful text it helped to create a visually appealing game that was my intention from planning stage.

![Dragon art game intro](docs/screenshots/game-intro-art.png)
![Dragon art game won](docs/screenshots/game-end-art.png)
![Dragon art game lost](docs/screenshots/game-lost-ascii-img.png)

### **Future development**

* I really enjoyed creating this game and would love to have more time to develop it further but as everything in life, this project had its deadline and I'm happy with result of this as MVP. In future I would like to enhance the game by following:
  * Add sound effects, such as dragon roars, flying byor snoring dragon to further improve experience for user, especially children
  * Create ASCII art matching each dragon description
  * Create one dictionary instead of separate dragon list and dragon descriptions and use keys and values accordingly

## **Testing**

I have included details of testing in a separate file [TESTING.md](TESTING.md).

## **Deployment**

### **Deploying to Heroku**

Code Institute Python Essentials Template was used for this project so the python code can be viewed in a terminal in a browser:
1. Google Heroku and open website, log in to Heroku or create a new account
2. On the dashboard click "New" and select "Create new app"
3. Enter unique app name and select region
4. Click "Create app"
5. On the next page find "Settings" tab and locate "Config Vars"
6. Click "Reveal Config Vars" and add "PORT" as a key and with value "8000", click "Add"
7. Scroll down to "Buildpack" and click "Add", select "Python" first
8. Repeat step 7. to add "Node.js", making sure "Python" is first on the list
9. Scroll to the top and select "Deploy" tab
10. Select GitHub as deployment method and search for your repository, once found click "Connect"
11. Scroll down and choose between "Enable Automatic Deploys" so the code is updated every time it is pushed to Github or "Manual Deploy"
12. Deployed site accesible through this link [Dragons](https://dragon-guessing-game-d41047f8049b.herokuapp.com/)

## **Acknowledgments and Credits**

* Image for background taken from [Freepik](https://www.freepik.com/), owner [stockgiu](https://www.freepik.com/free-ai-image/majestic-dragon-perched-mountain-peak-overlooking-breathtaking-landscape-generated-by-ai_47589515.htm)
* Ascii art for game intro made with [Ascii](https://www.ascii-art-generator.org/)
* Ascii art for dragon image if game is won taken from [Ascii Art](https://www.asciiart.eu/mythology/dragons) created by Gunnar Z
* Ascii art for dragon image if game is lost taken from [Ascii Art](https://www.asciiart.eu/mythology/dragons) created by Laura Brown
* Image for Favicon taken from Deviant Art [Christos Karapanos](https://www.deviantart.com/christoskarapanos/art/Dragon-s-Eye-585971591)
* For code ideas and issues I used [W3 Schools](https://www.w3schools.com/python/default.asp), [Stack Overflow](https://stackoverflow.com/questions/tagged/python) and [Github](https://github.com/search?q=name%20guessing%20game&type=repositories) to search for other project to see how terminal can be moved from original position
* Dragon names and descriptions taken from several sources:
  * [Pathfinder Wiki](https://pathfinderwiki.com/wiki/Pathfinder_Wiki)
  * [Wikipedia](https://en.wikipedia.org/wiki/Dragon)
  * Dr. Ernest Drake "Dragonology" The complete book of dragons

* The biggest thank you as always to my family during this busy time of juggling project, hackathon and life in general.
* Thank you as well to my mentor [David Bowers](https://github.com/dnlbowers) who supported me from the very beginning always giving the best advice and ideas for solutions.
* And thank you to [Kim](https://github.com/kimatron) for continuous support and in general for convincing me to take on this course.