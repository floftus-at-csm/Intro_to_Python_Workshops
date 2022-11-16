
## Ensuring Python is Installed on your Computer
### Windows
If you are on windows and would like to do more coding, I suggest you install WSL (windows subsystem for linux) - please do this after this session as it takes a little while - there are instructions [here](https://github.com/lewagon/data-setup/blob/master/WINDOWS.md). I can help you with this

1. open powershell / command prompt / windows terminal
2. Type:
``` python3 --version ```  
3. press enter
4. If you get a response saying python is not installed then we’ll have to install python
5. Go to start → system information
6. Look for “system type”
7. Check if it says x64 or x32 (64 bit or 32 bit)
8. Go to [this link](https://www.python.org/downloads/windows/) and install the relevant executable
9. Run the executable and install
10. Go back to the terminal and type the command again



### Mac

1. Open Terminal
2. Type:
``` python3 --version ```  
3. press enter
4. Either it will say what version of python is on your computer or it will ask you to install developer tools. If it says which version you have installed you're good to go
5. if it asked you to install developer tool click 'yes'
6. Wait until they are installed
7. Run the command ```python3 --version``` and hopefully it should now say that you have a version of python installed



## Installing a package
In python we use a package manager to install a package. pip is the standard method, yarn is an alternative, and conda (anaconda) is another alternative
We'll be using pip

### simple method
this method installs a package into your home directory
1. Open a terminal
2. type ```pip3 --version``` to ensure pip is installed
3. use the command ```pip3 install <package_name>``` (e.g. ```pip3 install Pillow```)


## Running a Script

1. create a python script (e.g. tester.py)
2. add some content to the script ```print("is this on")```
3. open up a terminal
4. run ```python3 <scriptname.py>```


## Importing a Module
To import a whole module use

``` 
import <module name>
``` 
e.g. 
```
import numpy
```

To then use that module use
```
modulename.functionname()
```

e.g. 
``` import Pillow
image1 = Pillow.Image("path_to_image.png")
```


To import a particular function use

```
from <module name> import <function name>
```

