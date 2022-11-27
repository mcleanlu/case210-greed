from game.casting.actor import Actor
from game.shared.point import Point
import random

class Gem(Actor):
    
    """    
    The Gems class' purpose is to move the "*" symbol from the top to the bottom.

    Attributes:

        none
    """
    def __init__(self):
        super().__init__()
        
    def movement(self, max_y):
        """Gem moves from point a to point b, first starting in a random generated position on the x axis, and then moves within the given range of the canvas. Speed of gems are also defined.
        
        Args:
            max_x (int): The maximum x value.
            max_y (int): The maximum y value.
        """
        x = self._position.get_x()
        y = (self._position.get_y() + 6) % max_y
        self._position = Point(x, y)

    def vertical_position(self):
        x = random.randint(1, 59) * 10
        self._position = Point(x,self._position.get_y())