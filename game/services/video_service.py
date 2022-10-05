"""
file: video_service.py
authors: authors of RobotFindsKitten
This class represents the game field display.
"""
# import pyray for raytracing, etc
import pyray

# class declaration
class VideoService: 
    """Outputs the game state. The responsibility of the class of objects is to draw the game state 
    on the screen. 
    """

    # default constructor
    def __init__(self, caption, width, height, cell_size, frame_rate, debug = False):
        """Constructs a new VideoService using the specified debug mode.
        
        Args:
            debug (bool): whether or not to draw in debug mode.
        """
        self._caption = caption
        self._width = width
        self._height = height
        self._cell_size = cell_size
        self._frame_rate = frame_rate
        self._debug = debug

    # close_window shuts down game
    def close_window(self):
        """Closes the window and releases all computing resources."""
        pyray.close_window()

    # clear buffer method clears the buffer, readying for new drawing
    def clear_buffer(self):
        """Clears the buffer in preparation for the next rendering. This method should be called at
        the beginning of the game's output phase.
        """
        pyray.begin_drawing()
        pyray.clear_background(pyray.BLACK)
        if self._debug == True:
            self._draw_grid()
    
    # draw_actor method draws the actor onscreen by color, text, position, and font size
    def draw_actor(self, actor):
        """Draws the given actor's text on the screen.

        Args:
            actor (Actor): The actor to draw.
        """ 
        text = actor.get_text()
        x = actor.get_position().get_x()
        y = actor.get_position().get_y()
        font_size = actor.get_font_size()
        color = actor.get_color().to_tuple()
        pyray.draw_text(text, x, y, font_size, color)
        
    # draw actors method separates the actors in a list and sends it to draw_actor method 
    # one at a time
    def draw_actors(self, actors):
        """Draws the text for the given list of actors on the screen.

        Args:
            actors (list): A list of actors to draw.
        """ 
        for actor in actors:
            self.draw_actor(actor)
    
    # flush_buffer method writes the buffer contents to game screen
    def flush_buffer(self):
        """Copies the buffer contents to the screen. This method should be called at the end of
        the game's output phase.
        """ 
        pyray.end_drawing()

    # get_cell_size method returns the video screen's cell size
    def get_cell_size(self):
        """Gets the video screen's cell size.
        
        Returns:
            Grid: The video screen's cell size.
        """
        return self._cell_size

    # returns video screen's height
    def get_height(self):
        """Gets the video screen's height.
        
        Returns:
            Grid: The video screen's height.
        """
        return self._height

    # returns width of screen
    def get_width(self):
        """Gets the video screen's width.
        
        Returns:
            Grid: The video screen's width.
        """
        return self._width

    # returns True if game window is still open, False if being closed
    def is_window_open(self):
        """Whether or not the window was closed by the user.

        Returns:
            bool: True if the window is closing; false if otherwise.
        """
        return not pyray.window_should_close()

    # opens a new game window
    def open_window(self):
        """Opens a new window with the provided title.

        Args:
            title (string): The title of the window.
        """
        pyray.init_window(self._width, self._height, self._caption)
        pyray.set_target_fps(self._frame_rate)

    # draws a grid on game screen
    def _draw_grid(self):
        """Draws a grid on the screen."""
        for y in range(0, self._height, self._cell_size):
            pyray.draw_line(0, y, self._width, y, pyray.GRAY)
        for x in range(0, self._width, self._cell_size):
            pyray.draw_line(x, 0, x, self._height, pyray.GRAY)