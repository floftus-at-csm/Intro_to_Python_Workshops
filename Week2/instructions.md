# Week 2 Task List
## Shell Commands Interactive

### Task 1: Running Scripts
1. start by opening a new folder in VSCode
2. create a new python script in your VSCode folder
3. Set up your script to print out something when it runs (tip, if you want to print text, it needs to be in quotation marks - [there is help here](https://www.pythoncheatsheet.org/builtin/print))
4. Run your script in using the terminal
5. (If you have more time) create an input in your script and then print out the users input ([help is here](https://www.pythoncheatsheet.org/builtin/input)) 


## Task 2: Variables and Conditionals
1. write and run a script that says the value of a variable
2. write and run a script that changes the value of a variable during the script
3. write and run a script that only prints the value of a variable if the value is above a certain value
4. write and run a script that takes an input from a user ([help is here](https://www.pythoncheatsheet.org/builtin/input))
5. write and run a script that takes an numbered input from a user and only prints it if its above a certain value and otherwise prints that the value is too low 


## Task 3: Introductory Image Processing
NOTE: If you want this to work with pngs as well as JPGs you'll need my function from my ```solarize.py``` file
1. Create a folder within your project for content
2. add an 'input_images' and an 'output_images' folder
3. add an image to the input folder
4. Create a new script 
5. In your script, import the Image module from the PIL package. Use the image module to load an image into a variable using PILs Image.open method. Then show the image to check its been loaded ok. (Tip - use the relative filepath of the image). For help, either use the official [PIL documentation](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html) or use [this tutorial](https://www.geeksforgeeks.org/python-pil-image-open-method/) 
5. Ensure your script runs without errors!
6. Import the ImageOps module into your script
7. Use the solarize method to process your image. Then use the .show() method to check if your changes have worked. The documentation is [here](https://pillow.readthedocs.io/en/stable/reference/ImageOps.html#PIL.ImageOps.solarize_) and [help is here if you need](https://www.geeksforgeeks.org/python-pil-imageops-solarize-method/) 
8. Now use the .save() method to save your image. try to save the image in your output folder. Tip, you might want to create a variable to store your new image paths

## Task 4: Extensions
1. Can you change the threshold level with a variable?
2. Can you ask for an input from a user to set the threshold level?
3. Can you process all the files in a folder in one script? (this goes onto what we'll learn next time)