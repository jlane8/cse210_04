"""
file: director.py
author: Jerry Lane and the authors of RobotFindsKitten
purpose: This class directs the Greed game action by controlling the cast
of banner, actor, and artifacts through their respective classes, reading
the keyboard_service inputs, and displaying the game onscreen through the
video_service outputs.
"""
# import the random and Point modules
import random
from game.shared.point import Point

# set defaults, in case needed
FRAME_RATE = 12 
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Greed"
DEFAULT_ARTIFACTS = 40

# class declaration
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
        """
        # create private variables for the keyboard and video services
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        
        # keep track of score and velocity
        self._score = 0
        self._velocity = Point(0, 1)
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot
            and artifact velocity.
        
        Args:
            cast (Cast): The cast of actors.
        """
        # get robot and artifacts from cast
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")

        # get input from keyboard service, separate into x and y
        velocity = self._keyboard_service.get_direction()
        x = velocity.get_x()
        y = velocity.get_y()
        
        # y changes the game velocity, x changes the robot velocity
        # if y equals zero, skip
        if y != 0:

            # limit amount of change up or down to 1
            if y > 0:
                y = 1
            else:
                y = -1

            # get current self._velocity
            self._y = self._velocity.get_y()

            # if the new input doesn't take the velocity less than one
            # or more than 14, apply new game velocity to all artifacts
            if (self._y >= 0 and y > 0 and self._y <= 13) or \
               (self._y <= 14 and y < 0 and self._y > 1):
                self._y += y
                self._velocity = Point(0, self._y)
                for artifact in artifacts:
                    artifact.set_velocity(Point(0, self._y))
        
        # take keyboard input from above, adjust robot velocity left or right
        velocity = Point(x, 0)
        robot.set_velocity(velocity)

    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        Updates the artifact positions and resets any which reach the bottom of 
        screen to a new column at the top of screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        # get banner, robot, and artifacts from cast
        banner = cast.get_first_actor("banners")
        robot = cast.get_first_actor("robots")
        artifacts = cast.get_actors("artifacts")
        
        # if score is zero, alert player how to change game velocity
        self._y = self._velocity.get_y()
        if self._y == 1:
            banner.set_text(f"Press up and down arrows to change velocity. Velocity: {self._y} Score: {self._score}")
        
        # show artifact velocity and score
        else:    
            banner.set_text(f"Velocity: {self._y} Score: {self._score}")
        
        # move the robot
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        # update artifacts, adjust score if collision
        for artifact in artifacts:
            artifact.move_next(max_x, max_y)
            artifact_position = artifact.get_position()
            
            # if robot and artifact collide, adjust score, change artifact to new location
            if robot.get_position().get_x() == artifact_position.get_x() and \
            robot.get_position().get_y() <= artifact_position.get_y() and \
            (artifact_position.get_y() - robot.get_position().get_y()) <= artifact.get_velocity().get_y():
                
                # get value from artifact and adjust score
                artifact_value = int(artifact.get_message())
                self._score += artifact_value
                
                # set new column for the artifact at top of screen
                x = random.randint(1, COLS - 1)
                position = Point(x, 0)
                position = position.scale(CELL_SIZE)
                artifact.set_position(position)   
            
            # if no collision, if artifact reaches bottom of screen, reset to new position
            elif artifact_position.get_y() >= (max_y - 15):
                
                # get new column, assign new position to artifact
                x = random.randint(1, COLS - 1)
                position = Point(x, 0)
                position = position.scale(CELL_SIZE)
                artifact.set_position(position)

    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        # send updated cast locations to video_service for drawing 
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()