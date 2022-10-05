"""
file: artifact.py 
author: Jerry Lane
purpose: The Artifact class holds the infomation on an Actor that is
also an artifact. It holds a single variable as its member - message.
"""
# since an Artifact inherits from Actor, import Actor
from game.casting.actor import Actor 
from game.shared.point import Point

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """
    Parameters: none
    Return: nothing
    The Artifact class holds the description of the artifact actor in its 
    member 'message.'
    """

    # constructor method for Artifact
    def __init__(self):
        """
        Parameters: none
        Return: nothing
        The constructor method merely sets the default message of an Artifact
        instantiation to nothing ("").
        """
        # inherit the constructor elements of the Actor class
        super().__init__()

        # initialize an empty message
        self._message = ""

    # set_message method to set description of the artifact instantiation
    def set_message(self, message):
        """
        Parameters: message - descriptive text of artiface
        Return: nothing
        The set_message method does just that; it sets the descriptive message of
        an artifact instantiation.
        """
        # internal _message variable set to the parameter message
        self._message = message

    # get_message method will return the description contained in _message
    def get_message(self):
        """
        Parameter: none
        Return: _message - the descriptive text set by the set_message method
        The get_message method returns the private _message variable descriptive 
        text.
        """
        # return the _message variable's descriptive text
        return self._message