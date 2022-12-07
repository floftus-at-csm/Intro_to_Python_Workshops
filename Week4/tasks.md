
# Session 4
The aim of today is to create a console based game.
I've though of two versions of the game, you can choose either. The first is a bit easier, the second a bit harder:

1. a text based cooking game. The player sets the type of ingredients they want to use, and some other parameters (e.g. how spicy) and then is taken through the steps of making a meal with these ingredients 
2. a youtube guesser game
    * We download a video into a folder on the players computer and ask them to watch the video <b>or</b>
     We'll serve up some audio to the player from a youtube video and will ask the player to guess the name of the youtube video. 

## Task 1: Recap Task
can you create and run a program shows three (or more) youtube video titles and then asks a user to choose one?
* store the youtube video titles in an array like ```youtube_titles = [title1, title2, title3]```
* show the titles with the ```print``` command like
    * ```print(title 1: youtube_titles[0])```
    * could you use a for loop to print the titles?
* use an input like ``` user_input = input("press 1, 2 or 3 then enter to make your decision")```
* Use a conditional statement to say they were correct if they click 2

## Task 2: Functions 1
I have two functions for creating a typewriter effect:
```
def texttime(words):
	for c in words:
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(0.1)

def texttimeRandom(words):
    for c in words:
        sys.stdout.write(c)
        sys.stdout.flush()
        if randrange(1, 5) == 3:
            time.sleep(0.1)
```
They take an input of some words (a string) and write them to the console.
* Can you now use these functions with code you've written in Task 1? Try replacing where you've used  ```print()``` with these functions


```
⠀⢀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠉⠛⠛⠛⠶⠶⠦⠤⢤⣄⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⣠⣤⣤⣤⣄⣀⣀⣀⣀⡀⠀⠈⠉⠉⠙⠛⠛⠶⠶⠶⣤⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠉⠉⠉⠉⠙⠛⠛⠛⠛⠳⠶⠶⠶⠶⣤⣤⡄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣰⡟⢀⣴⠂⣠⠆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢰⡟⢀⡾⠃⣴⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣄⠘⣧⡀⢿⡄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⣦⠈⢷⡄⠹⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠟⠀⠼⠃⠰⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⢰⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡆⠀⠀
⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⠀⠀
⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠁⠀⠀⠀
⠀⠀⠀⠀⠀⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢉⣉⣉⣉⣉⣉⣉⡉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
```
## Task 4: Algorithm Planning
Now we have some of the framework of the game settled, lets plan out the algorithm.

For either the text-based cooking game, or a youtube guesser game:
* plan out the algorithm for the game using pen and paper (notes on your computer or a design tool like miro is fine)
* create a new folder and write out the framework of your algorithm in terms of the states needed
* now write out what functions will be needed (start without defining the function)
* now define the functions, and write out what the inputs and outputs will be. Remember, the inputs go inside the opening brackets like ```def myFunction(input1, input2):``` and the outputs are put after a return tag like: ```return output1, output2```. We then use our function like: ``` currentOutput1, currentOutput2 = myFunction(input, another_input)```
* now consider what input variables and libraries you'll need
* now try to flesh out each individual function

