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

## What we'll cover

* Recap task
* writing functions in python
* planning algorithms

## Functions
# 📪📩📫🛩👀
Functions are is a set of code that perform a specific function. They allow you to re-use code easily. Good functions are <i>generalised</i>
### Writing functions
To create a function you need to first <i>define</i> the function.
Note that in python, what goes inside the function must be <i>indented</i>
e.g.
```
def my_first_function():
    print("lets start functional programming")
```
To then use the function we <i>call</i> the function.
We could call the above function like
```
my_first_function()
```

### Inputs and Outputs
Often we want a function to have a set of inputs and then to return us an output. The inputs are often called <i>arguments</i>, the output are what we <i>return</i>.

<i>If the function returns an output then we need to store that output somewhere</i>. We store the output in a variable.


e.g.
```
# defining the function
def combine_words(word1, word2):
    if type(word1) not str:
        word1 = str(word1)
    if type(word2) not str:
        word2 = str(word2)
    return word1 + " " + word2
```

### calling the function
```
combo_word = combine_words("hello", "world")
print(combo_word)
```

## Algorithm Planning
# 🔪🌶🍤🔥🍜
Algorithms are a set of rules and instructions. They're similar to a recipes, just sets of instructions that are then implemented. In the case of recipes, a human probably implements the algorithm, but with code, we send the recipe off to the central processing unit of the computer.
One really useful concept to have in mind when designing algorithms are states.

### states
If we think of algorithms as recipes, then states are the different paragraphs in the recipe. For cooking a meal we might have one paragraph about preparing the good, one for the first stage of cooking, another for the next stage, and then a final paragraph about serving the food.


States can be useful to control the flow of your program. Consider a Digital Camera that has a 'timelapse', 'low light', and 'manual exposure' setting. Each of these could be considered a <b>state</b> of the wider camera program.
The simplest way to use states is with conditional statements

```# Define the different states
START_STATE = 0
PROCESSING_STATE = 1
END_STATE = 2

# Set the initial state
current_state = START_STATE

while True:
    # Check the current state
    if current_state == START_STATE:
        # Do some initial setup
        mySetupFunction()
        # Update the state
        current_state = PROCESSING_STATE
    elif current_state == PROCESSING_STATE:
        # Do the main processing
        myProcessingState()
        # Update the state
        current_state = END_STATE
    elif current_state == END_STATE:
        # Do any final cleanup
        myEndState()
        # Break out of the loop
        break
```

Lots of your program can be designed without writing any code. 
I like to start with pen and paper. 
* I first create a loose diagram of what will happen in the script
    * this gives me the structure of a program (where we start and where we go to)
    * this structure generally makes up the <b>states</b> of our program
* I then notate my diagram with the logic needed. For each of the states ask yourself questions like
    * What are the inputs to this state?
    * Do we need any conditional statements in this state?
    * do we need any functions for this state?
    * what are the outputs of this state?
* I then move to my IDE (visual studio code) and write up this diagram in pseudo code. Once this is written up, the whole structure of my program is planned out 
* 

