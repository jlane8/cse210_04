"""
file: keyboard_service.py
authors: authors of RobotFindsKitten
This class represents the keyboard inputs.
"""
# import needed modules
import pyray
from game.shared.point import Point

#class declaration
class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    # default constructor
    def __init__(self, cell_size = 1):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size
                
    # get direction method returns a new Point based upon keys pressed
    def get_direction(self): 
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        # default to x and y coords zero in case there is no key press
        dx = 0
        dy = 0

        # if key is pressed, change dx or dy value
        if pyray.is_key_down(pyray.KEY_LEFT):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_RIGHT):
            dx = 1

        if pyray.is_key_down(pyray.KEY_UP):
            dy = 1
        
        if pyray.is_key_down(pyray.KEY_DOWN):
            dy = -1

        # make new Point our of dx, dy values
        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        # return new Point
        return direction

        