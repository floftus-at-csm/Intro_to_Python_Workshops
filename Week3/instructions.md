# Week 3 Tasks
### 1. Recap Part A
* can you create a script that 
    * asks the user for their favourite year for music (remember you'll have to put their input into a variable)
    * converts this date from a string to an int 
    * checks if this year is in the 90s, 00s, 10s, 20s,
    * tells the user they are a "90s kid" or a "00s kid" (or whatever you would like to say here) if their date is in the 90s
    * tells them that you don't consider dates further back than the 90s if the year is in the 80s

### 2. Recap Part B
* install yt-dlp with the command ``` pip install yt-dlp``` or ```pip3 install yt-dlp```
* check that the install is succesful by creating a new script called  ```youtube_downloader.py``` and adding the content ```from yt_dlp import YoutubeDL```
* run this script and check for errors

### 3. Getting all files from a directory
* create an ```input``` folder within week 3 and within that folder create an ```images``` folder
* add a set of images to this folder
* use one of the methods from 'session3.md' to get all the image paths from this folder into an array. You'll need to set your path from where you are running the code from. E.g. if I run the code from ```Intro_To_Python_Workshops``` I'll need to include ```/Week3``` in my path.
* see if you can access one of the file paths in the array and can print it to the console
* see if you can use the file path to show the image

### 4a. Loops 
* take your array with your filepaths in it
* can you print out all of the filepaths using a for loop?
* can you check just one filepath using its position in the array?
* Now return to solarizing your code from Week 2. Can you use a for loop to solarize all of the images in your input folder? 
* notes
    * If you don't have working code from last week, check the ```solarize.py``` file in the ```/Week2/``` folder
    * You will need to set a different output name for every file. This could be a good candidate for ```enumerate```


### 4b. (extension) Live Webcam
The aim here is to get a feed from your webcam using opencv
* install opencv with ```pip install opencv-python```
* create a new file and add this code to it 
```
# import the opencv library
import cv2


# define a video capture object
vid = cv2.VideoCapture(0)
``` 
* this is the code to get one frame from your webcam:
```
ret, frame = vid.read()
cv2.imshow('frame', frame)
if cv2.waitKey(1) & 0xFF == ord('q'):
    break
```
* can you use a <b>while loop</b> to get a consistent stream from your webcam?



## 5. Functions
The aim here is to neaten up your code by creating some resuable functions.
* create a function for iterating through a directory to get all of the file paths in the directory. Try to follow these steps:
    1. define the function and give the function a name
    2. consider whether the function has any inputs (e.g. a directory path)
    3. add those inputs after the function name like ``` def my_function(input)```
    4. consider whether the function should have an output
    5. write the output like ```return your_output```
    6. now you just need to fill in the middle of the function to work out how you get from input to output!
    7. now call the function in your script and put the output into a variable like ```my_array = my_function(filepath)```
    8. print out the output of the function to check it worked
* create a function for solarising an image


