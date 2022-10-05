"""
file: __main__.py
authors: Jerry Lane and the authors of RobotFindsKitten
This is the launcher of the Greed game. It will create the
cast of characters, then transfer game control to a
Director instance.
"""
# import the numerous modules needed to make the Greed game work
import os 
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point


# set defaults
FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 40


def main():
    """
    parameters: none
    return: nothing
    The main function sets up the game parameters and then transfers
    control of the game to a Director instance.
    """
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = Actor()
    banner.set_text("")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", banner)
    
    # create the robot at bottom of screen
    x = int(MAX_X / 2)
    y = int(MAX_Y - 15)
    position = Point(x, y)

    # instantiate robot as an Actor
    robot = Actor()
    robot.set_text(chr(164))
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the artifacts randomly, either rock or gem
    # loop through the default number of artifacts
    for n in range(DEFAULT_ARTIFACTS):
        
        # if random number is 0, create a gem with a value of 1
        if random.randint(0, 1) == 0:
            text = chr(111)
            message = "1"
        
        # otherwise, create a rock with a value of -1
        else:
            text = chr(42)
            message = "-1"

        # position artifact randomly on the screen
        x = random.randint(1, COLS - 1)
        y = random.randint(1, ROWS - 1)
        position = Point(x, y)
        position = position.scale(CELL_SIZE)

        # assign a random color to the artifact
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)
        
        # create the artifact as an Artifact instance, child class of Actor
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        artifact.set_message(message)
        cast.add_actor("artifacts", artifact)
    
    # once all the cast has been created, start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)

# check to see if run directly or called, if direct then run main
if __name__ == "__main__":
    main()