"""
file: cast.py
authors: authors of RobotFindsKitten
This class represents the entirety of the game cast, actors,
banners, and artifacts
"""

# class declaration
class Cast:
    """A collection of actors. 

    The responsibility of a cast is to keep track of a collection of actors. It has methods for 
    adding, removing and getting them by a group name.

    Attributes:
        _actors (dict): A dictionary of actors { key: group_name, value: a list of actors }
    """

    # default constructor
    def __init__(self):
        """Constructs a new Actor."""
        self._actors = {}
        
    # add actor method to add actore to group    
    def add_actor(self, group, actor):
        """Adds an actor to the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to add.
        """
        # if group isn't in the dictionary keys, create one
        if not group in self._actors.keys():
            self._actors[group] = []
            
        # if actor isn't in the actor's group, add it in
        if not actor in self._actors[group]:
            self._actors[group].append(actor)

    # get list of actors in a group
    def get_actors(self, group):
        """Gets the actors in the given group.
        
        Args:
            group (string): The name of the group.

        Returns:
            List: The actors in the group.
        """
        results = []
        if group in self._actors.keys():
            results = self._actors[group].copy()
        return results
    
    # get all actors method returns all actors in a list
    def get_all_actors(self):
        """Gets all of the actors in the cast.
        
        Returns:
            List: All of the actors in the cast.
        """
        results = []
        for group in self._actors:
            results.extend(self._actors[group])
        return results

    # get first actor method returns the first in the group parameter
    def get_first_actor(self, group):
        """Gets the first actor in the given group.
        
        Args:
            group (string): The name of the group.
            
        Returns:
            List: The first actor in the group.
        """
        result = None
        if group in self._actors.keys():
            result = self._actors[group][0]
        return result

    # remove actor method simply removes an actor
    def remove_actor(self, group, actor):
        """Removes an actor from the given group.
        
        Args:
            group (string): The name of the group.
            actor (Actor): The actor to remove.
        """
        if group in self._actors:
            self._actors[group].remove(actor)