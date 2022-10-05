# Greed
About the only "good" thing that can happen when a volcano erupts is that gems fall from the sky. If you're lucky enough to avoid the mud flows and lava, can
see through the ash cloud, and have special equipment that can let you catch these things without ripping your arms off, then you migh love this game. Both
rocks and gems are falling. Avoid the rocks while catching the gems, and you might get rich. Either way, enjoy yourself!

## Getting Started
---
Make sure you have Python 3.8.0 or newer and Raylib Python CFFI 3.7 installed and running on your machine. You can install Raylib Python CFFI by opening a terminal and running the following command.
```
python3 -m pip install raylib
```
After you've installed the required libraries, open a terminal and browse to the project's root folder. Start the program by running the following command.```

python3 greed 
```
You can also run the program from an IDE like Visual Studio Code. Start your IDE and open the 
project folder. Select the main module inside the hunter folder and click the "run" icon.

## Project Structure
---
The project files and folders are organized as follows:
```
root                            (project root folder)
+-- greed                       (source code for game)
  +-- game                      (specific game classes)
    +-- casting                 (folder containing the classes representing game objects)  
       +-- actor.py             (actor class of the game such as the player catching the falling objects)
       +-- artifact.py          (artifact class of the game, child class of actor, represents falling objects)
       +-- cast.py              (class representing all the objects on the screen)
    +-- directing               (folder containing the director class)
       +-- director.py          (director class controls all the objects in the game)
    +-- services                (folder containing service classes)
       +-- keyboard_service.py  (class dealing with game keyboard inputs)
       +-- video_service.py     (class dealing with game video output)
    +-- shared                  (folder containing classes which are shared among other classes)
       +-- color.py             (class representing the color of a given game object)
       +-- point.py             (class representing the position of a given game object)
  +-- __main__.py               (entry point for program)
  +-- README.md                 (general game info)
```

## Required Technologies
---
* Python 3.8.0
* Raylib Python CFFI 3.7

## Authors
---
* Jerry Lane and the authors of RFK
