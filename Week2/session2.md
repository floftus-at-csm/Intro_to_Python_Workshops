# Session 2 
## Structure
* Recap of Visual Studio Code
* Terminal Commands
* Variables
* Python Pillow


## Visual Studio Code
### At Startup
* For a new project create a folder  using your file explorer
* Open Visual Studio Code
* Click ‘open folder’ in the top left
* Open the folder you created in step 1
* Open the terminal (it's in the top nav bar at the right)
<br>
### File Types
All of your programming files will be text files with different file endings.
Python files end with .py 

e.g. process_image.py

Markdown files are used to share information with other coders. They are labelled with .md

e.g. README.md

## VSCode Extensions

* Material Icon Theme

* Python Core Extension

* Python Indent

* Pylance

* Jupyter

* Auto-save on Window Change

<br>
<hr>

## Command Line Notes

[Core commands list](https://docs.google.com/document/d/1Rq6jStITNX6Acy1ZECaBhcPyQJsI3XpBUpmiyJYIUGI/edit#heading=h.fbk47x1mij41)

[Windows List](http://www.cs.columbia.edu/~sedwards/classes/2015/1102-fall/Command%20Prompt%20Cheatsheet.pdf)

 <br> 

### General structure
For most commands we first say what program we want to use, then we put a space, then we say what process we want to use, then we put a space, then we add our inputs to the process, with a space between each one. These inputs are sometimes referred to as arguments.
```
$ <program> <process> <process-settings/inputs>
```
Specific example: 
```
$ pip install Pillow
```
General example
```
$ pip install <package_name>
```

Alternative general:
```
$ pip install <package_name>
```
#### Longer example:
Here pip is an argument of the python program. -U is an argument that stands for upgrade. Pillow==9.0.1 refers to a specific version of Pillow. This will become useful when we start using Virtual Environments, later on in our python learning. [Some info about virtual environments for anyone who wants to read ahead](https://www.pythoncheatsheet.org/cheatsheet/virtual-environments) 
``` 
$ python3 -m pip install -U Pillow==9.0.1
``` 
### Longer Example 2
In this example pip will read a text file which has a note of all the packages necessary for a library. Pip will then download all of these packages.
```
$ python -m pip install -r requirements.txt
```
Notes
* The dollar sign ($) just indicates that this is a command that *runs in the terminal* rather than in a script.
* Every new command is designated with a space. So don't put spaces in your folder or file names!


### Single Function Programs
Some programs only do one function and so you miss out the process step
e.g.
```
cd this_directory
```
These are generally in built commands like 
``` 
pwd
ls
cd <folder_name>
touch <file_name>
nano <file_name>
```




## Git 
Here are some command line phrases for using git. If you want to use a graphical interface you can use the [Github Desktop Client](https://desktop.github.com/)


<b>Git clone</b> will download the files from a git directory. 

Specific example:
```
$ git clone https://github.com/floftus-at-csm/Intro_to_Python_Workshops.git
```
General Example
```
$ git clone <repository_name>
```
<b>Git Pull</b> will pull any updates from a git directory you've cloned. You need to make sure your terminal is within the git directory you're trying to update for this to work
```
$ git pull
```
<b>Git add</b> tells git which files to track in your repository. Try to <i>avoid adding files with sensitive information</i> or <i>files that take up lots of memory</i>. Github is primarily for your coding files, and should be used a storage system for media. 

Specific:
```
$ git add tester.py
```
General:
```
$ git add <filename>
```

<b>Git commit</b> will save any changes you've made in your directory. Using the -am method says you will commit all of your changes in the tracked files, and will add a message. This is the standard way to commit
```
$ git commit -am 'commit reference'
```
<b>Git push</b> uploads your changes to github. 
Pushing to the origin is for when you are pushing changes to your own repository. 
```
$ git push origin main
```

<b>Git checkout</b> allows you to create your own version of a repository.
```
$ git checkout -b <branch_name>
```
Use this in conjunction with pushing to your branch
```
$ git push -u origin <branch_name>
```

An example of a full workflow for commiting your changes to a new branch. Lets say you've created two new files: image_process.py and mynotes.md

```
$ git add image_process.py mynotes.md
$ git commit -am 'added image_process file and my notes'
$ git checkout -b felixs_branch
$ git push -u origin felixs_branch
```



<hr>

## Python Scripts

### General structure
```
Importing packages
====
Defining Functions
====
Main loop that calls functions
```

### Main Loop
This allows us to continue to run our script over time. We'll go through loops in more detail next time. There is some [info here though](https://www.pythoncheatsheet.org/cheatsheet/control-flow#while-loop-statements) 
```
while True:
    your script
```

### If Main
This just says run this code if this script is directly called on the command line. Sometimes we just want to use a scripts functions and not the content of the main loop
```
if __name__ == "__main__":
   Do something here
```

### Printing
Printing allows you to check values in your script. You can also use printing to make command line applications. The general structure of how to print is to say what you're printing, then print it. 

e.g.
```
print("The lamp variable is: ", lamp_variable)
```
Note the comma separation between comment and value. Adding a comment makes it easier for you to find your print in the console.


### Variables
You can think of variabes as containers for information (a labelled box that we keep track of a value with). Physically, they are a storage location paired with a virtual name. 
Python is dynamically typed, so we don't have to declare what type of information we're saving. But its worth knowing what types are available to avoid errors further down the line!
* String
    * groups of letter 
    * Use quotation marks to designate a string (can be single or double). Generally double quotes are used for natural language or wherever there might be single quotes in a string.
    * example strings: 'plant', "Over the moon", '/Week2/input_images/image1.png'
* Char 
    * individual characters 
    * single quotes designates a char
    * example chars: 'c', 'q', 'p'
* Int  
    * integer values 
    * example ints: 1, 8, 2045 
* Float 
    * Numbers with decimal points 
    * example floats: 1.000, 8.450, 2045.888)
* Bool 
    * True or False
    * Capitalise your Trues and Falses in python!
* Class 
    * an object 
    * example classes: a Pillow Image, a google maps api object

<b>Declaring variables:</b> In python we just need to give a variable a name and assign a value to the variable name 
```
<variablename> = <information>
```
e.g. 
```
my_variable = 5
print("the value of my variable is: ", my_variable)
```


Some functions require their inputs to be a specific type. e.g. the input of Image.open() needs to be a string. If you put the wrong type of variable in you will most likely get an error. 

### Error Messages
Error messages generally contain the information you need to fix the error. Do try to take the time to read them. They will also have details about where the error is in your script. Common errors will be documented on Stack Overflow with solutions. 

### Comments
Comments are designated with a hashtag. This is text that the interpreter will ignore!
e.g.
```
# this text will be ignored
this text will run and create an error
```

### Conditionals and Comparisons
In python we can write conditional statements with <b>if, else,</b> and <b>elif</b>
They take this structure in pseudo code.
```
if condition:
    do something
elif another_condition:
    something else
else:
    a whole other thing
```
To create conditions we need comparisons: <b> less than (<>), more than (>), equal to (==) [note the double equal sign!], less than or equal to (<=), more than (>=) or equal to, not equal to (!=)</b>
e.g.
```
# if a is not equal to be do c

if a != b:
    do c
```
Sometimes we need to combine comparisons. We can use <b>and, not</b> and <b>or.</b> The english words are enough in python

e.g.
```
# if a is not equal to b and c is true then do d
if (a != b) and c == True:
    do d
```
 
### Paths
There are two main libraries to handle paths: os, and pathlib.
Pathlib is newer and better, so I recommend using this when writing, but you might find os used when adapting other peoples' code or working with libraries.

The tricky thing about paths is that Windows uses a backwards slash (\) to designate a folder, while everything else uses a forward slash (/) [sigh] 

This can be a problem for ensuring your code works cross platform.

<b>Pathlib</b> handles this like this:
```
from pathlib import Path

input_folder = Path("Week2/input_images/")

file_to_open = input_folder / "image.png"
```
or
```
from pathlib import Path

input_folder = Path("Week2/input_images/images.png")
```

You will need to input your filepath with forward slashes for this to work

<b>os</b> handles paths like this
```
import os.path
input_folder = os.path.join("Week2", "input_images")
file_to_open = os.path.join(input_folder, "image.png")
```

### Modules and Libraries
We can import libraries and modules using the import method. A module is one script. A library is a collection of connected scripts.
```
import <module_name>
import <library_name>
```
e.g.
```
import os
import week1
```
We can also import specific functions and classes from libraries or modules using 'from'
```
from PIL import Image, ImageOps
```