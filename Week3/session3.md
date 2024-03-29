```
                          :                      :M
                         XMX                   .HMM>
                         MMMM.                dMMMM>
                        'MMMMMX     .....   dMMMMMMX
                        XMMMMMMMnMMMMMMMMMMMMMMMMMMM
                       :MMMMMMMMMMMMMMMMMMMMMMMMMMMM>
                       XMMMMM!"    "MMMMMM"`  `"MMMMM
                       MMMM#         4MMf        `MMMX
                      XMMM            MX          'MMM:
                     'MMM~            '>            MMM
                     MMMf       .     '>            `MMX
                    MMMM>     :MMM    '>   :MMM      MMMX
                   XMMMM      MMMM>   '>   XMMMX     MMMMk
                  MMMMMM>     MMMM~   'k   MMMMX     MMMMMh
                 MMMMMMMX     XMMM    XX   ?MMM     XMMMMMMM
                 MMMMMMMMk     ^`    X 'h    `     :MM##MMM~
                  ?MM>  ^?M.       .!    %.      .HM"   MM
                 .?M      '"%+++!".nMMMMn "%++!*" %.. 'M..
                  `?M>+%L         <MMMMMMMM>       :   XM"
                    'X   %        XMMMMMMMM>      X   'f
                      X   `M.      ?MMMMMM~    .HM   :`
                       %.  `MMMx.          .xHMMM   X
                        `X  `MMMMMMMMMMMMMMMMMMM  :f
                           .M. 4MM     "     MM" xM
                                `%x.......x"`.H
                                 hx.......x
``` 
# Session 3
## recap

## Data Structures
### Arrays
Lists and arrays are one of the core data structures in python. For now, lets see them as interchangeable terms.
Lists allow you to group data together. 
We declare an empty list like
```
my_list = []
```
or a list with content like
```
my_list = ["youtube_url", "youtube_url2"]
```
or an empty list of a specific size
```
my_empty_list = [None] * 10
```
to access values use the values position 
``` 
print(my_list[3])
```
to add values we generally use append. This adds the value to the end of the array
```
my_list = my_list.append(2012)
```
to delete a value we can either use ```del``` or ```remove```. Note the different brackets.
```
del my_list[2]
my_list.remove(2012)
```
We often need to check how big our array is. In python we can do this with the ```len``` method
```
print("the length of the array is: ", len(array))
```
### Example Case: Getting All File Paths in a Directory into an Array
There are multiple methods for this. I'll show you two

1. using os.listdir
```
import os

path = "path/to/directory"
arr = os.listdir(path)
print("the first position in the array is: ", arr[0])
print("the length of the array is: ", arr)
```
2. Using Path Lib
```
from pathlib import Path

path = Path("path/to/directory")
arr = list(path.iterdir()) # iterate through directory and then put the results in a list
print("the first position in the array is: ", arr[0])
print("the length of the array is: ", arr)
```
Note, currently we will get any files in this directory (python files, images, videos etc. etc.). Often we will only want to look for one type of files (e.g. just images). There is a quick tutorial about getting only files of one type [HERE](https://www.geeksforgeeks.org/how-to-iterate-through-images-in-a-folder-python/) 


```
	
             __,aaPPPPPPPPaa,__
         ,adP"""'          `""Yb,_
      ,adP'                     `"Yb,
    ,dP'     ,aadPP"""""YYba,_     `"Y,
   ,P'    ,aP"'            `""Ya,     "Y,
  ,P'    aP'     _________     `"Ya    `Yb,
 ,P'    d"    ,adP""""""""Yba,    `Y,    "Y,
,d'   ,d'   ,dP"            `Yb,   `Y,    `Y,
d'   ,d'   ,d'    ,dP""Yb,    `Y,   `Y,    `b
8    d'    d'   ,d"      "b,   `Y,   `8,    Y,
8    8     8    d'    _   `Y,   `8    `8    `b
8    8     8    8     8    `8    8     8     8
8    Y,    Y,   `b, ,aP     P    8    ,P     8
I,   `Y,   `Ya    """"     d'   ,P    d"    ,P
`Y,   `8,    `Ya         ,8"   ,P'   ,P'    d'
 `Y,   `Ya,    `Ya,,__,,d"'   ,P'   ,P"    ,P
  `Y,    `Ya,     `""""'     ,P'   ,d"    ,P'
   `Yb,    `"Ya,_          ,d"    ,P'    ,P'
     `Yb,      ""YbaaaaaadP"     ,P'    ,P'
       `Yba,                   ,d'    ,dP'
          `"Yba,__       __,adP"     dP"
              `"""""""""""""'
```

## Loops
<b>Loops are used to repeat actions</b>. This can be useful to do an action lots of times, to acces all the values in an array, or have a script run in real time responding to some input data (e.g. a video stream or a stream of data from a sensor)


There are two main ways to create loops: <b>for loops</b> and <b>while loops</b>. Generally we'll use a <b>for loop to do a process a specific number of times</b> and a <b>while loop to leave a process running for an indefinite amount of time</b> (though we need to be careful to always have an off 'button' for a while loop)
### For Loops
A simple for loop in Python looks like this:
```
for i in range(0, 10):
    print("the value of i is: ", i)
```
This will print: ``` 0, 1, 2, ...```

This says to 
1. create a variable i and set i to be equal to 0 
2. do whatever is inside the loop (here it is just a print command)
3. increase i by 1 
4. do whatever is inside the loop
5. continue this loop until i is 10 
6. when i is 10 we do not go into the loop

Note that <i>what is inside a loop must be indented</i>. This should happen automatically after you write a colon after writing 'for. If it does not, <i>you can indent using the tab key </i>.

To indent a whole group of text, highlight over it and then press tab.

This loop uses the <b>range</b> method. But there are a few others ways we can do for loops in python. 


#### <b>Looping over a List</b>
In python we can loop over a list to access the values within that list very easily
```
my_list = ["rock", "classical", "hip hop", "heavy metal"]

for item in list:
    print("the item is: ", item)
```
Here <b>item could be replaced with any other word </b> 

We could do the exact same thing with a range method:
```
my_list = ["rock", "classical", "hip hop", "heavy metal"]

for i in range(0, len(my_list)):
    print(my_list[i])
```
#### <b>Looping over some values in a list</b>
Sometimes you want iterate over a list but your list is huge. So you just want to try your code on a few loops

This is fairly easy in python
```
# This would print the first two items
for item in list[0:2]:
    print(item)
```


```
# This would print the 3rd and 4th item
for item in list[2:4]:
    print(item)
```

#### Enumerate
Sometimes, we want the value of the item in the list, and the number of times we've gone through our loop. For this, we use pythons ```enumerate``` method
```
my_list = ["rock", "classical", "hip hop", "heavy metal"]

for count, value in enumerate(my_list):
    print("the count is: ", count)
    print("the value is: ", value)
```

#### <b>Stopping a loop</b>
We can stop a loop midway through using the ```break``` method
```
my_list = ["rock", "classical", "hip hop", "heavy metal"]

for count, value in enumerate(my_list):
    print("the value is: ", value)
    if value == "classical":
        break
print("we exited the loop")
```

### While Loops
While loops run until a condition is met.
We could use while loops to do what for loops do but generally <i> they are used when we don't know how many times we need to do the loop for. </i>
For example
* if we're waiting for a correct input from a user - like a password
* if we want to run a chunk of code for the duration of a performance 

The general structure of a while loop is:
```
while <condition>:
    code that you want repeated
```
e.g. 
```
i = 0
while i < 10:
    print(i)
    i = i + 1
print("we've exited the loop")
```
This is a recreation of a for loop using a while. Generally we won't do this. Instead we often put the most generic condition ``` while True:``` and then use ```break``` to stop the while loop.
e.g.
```
while True:
    mask_image(im1, im2, sensor_data)
    if(sensor_data < 100.0):
        break
```
Its always good practice to have a way of breaking your loop because otherwise your program can get stuck in a loop. The code below will break the loop if someone presses the q on their keyboard
```
while True:
    mask_image(im1, im2, sensor_data)
    //get the input from the keyboard
    int keyboard = waitKey(30);
    if (keyboard == 'q' || keyboard == 27)
        break;
```
<hr>

```	
             ..                                       ..
             []                                       []
           .:[]:_          ^^                       ,:[]:.
         .: :[]: :-.                             ,-: :[]: :.
       .: : :[]: : :`._                       ,.': : :[]: : :.
     .: : : :[]: : : : :-._               _,-: : : : :[]: : : :.
 _..: : : : :[]: : : : : : :-._________.-: : : : : : :[]: : : : :-._
 _:_:_:_:_:_:[]:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:_:[]:_:_:_:_:_:_
 !!!!!!!!!!!![]!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!![]!!!!!!!!!!!!!
 ^^^^^^^^^^^^[]^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^[]^^^^^^^^^^^^^
             []                                       []
             []                                       []
             []                                       []
  ~~^-~^_~^~/  \~^-~^~_~^-~_^~-^~_^~~-^~_~^~-~_~-^~_^/  \~^-~_~^-~~-
 ~ _~~- ~^-^~-^~~- ^~_^-^~~_ -~^_ -~_-~~^- _~~_~-^_ ~^-^~~-_^-~ ~^
    ~ ^- _~~_-  ~~ _ ~  ^~  - ~~^ _ -  ^~-  ~ _  ~~^  - ~_   - ~^_~
      ~-  ^_  ~^ -  ^~ _ - ~^~ _   _~^~-  _ ~~^ - _ ~ - _ ~~^ -
         ~^ -_ ~^^ -_ ~ _ - _ ~^~-  _~ -_   ~- _ ~^ _ -  ~ ^-
             ~^~ - _ ^ - ~~~ _ - _ ~-^ ~ __- ~_ - ~  ~^_-
                 ~ ~- ^~ -  ~^ -  ~ ^~ - ~~  ^~ - ~
```
## Functions
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


# calling the function
combo_word = combine_words("hello", "world")
print(combo_word)
```


```
                 ¶¶¶¶¶¶¶¶¶¶¶¶ 
                 ¶¶            ¶¶ 
   ¶¶¶¶¶        ¶¶                ¶¶ 
   ¶     ¶     ¶¶      ¶¶    ¶¶     ¶¶ 
    ¶     ¶    ¶¶       ¶¶    ¶¶      ¶¶ 
     ¶    ¶   ¶¶        ¶¶    ¶¶      ¶¶ 
      ¶   ¶   ¶                         ¶¶ 
    ¶¶¶¶¶¶¶¶¶¶¶¶                         ¶¶ 
   ¶            ¶    ¶¶            ¶¶    ¶¶ 
  ¶¶            ¶    ¶¶            ¶¶    ¶¶ 
 ¶¶   ¶¶¶¶¶¶¶¶¶¶¶      ¶¶        ¶¶     ¶¶ 
 ¶               ¶       ¶¶¶¶¶¶¶       ¶¶ 
 ¶¶              ¶                    ¶¶ 
  ¶   ¶¶¶¶¶¶¶¶¶¶¶¶                   ¶¶ 
  ¶¶           ¶  ¶¶                ¶¶ 
  ¶¶¶¶¶¶¶¶¶¶¶¶    ¶¶            ¶¶
                  ¶¶¶¶¶¶¶¶¶¶¶
```