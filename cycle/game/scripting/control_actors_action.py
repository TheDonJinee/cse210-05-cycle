import constants
from game.scripting.action import Action
from game.shared.point import Point


class ControlFirstActorsAction(Action):
    """
    An input action that controls the actor.
    
    The responsibility of ControlActorsAction is to get the direction and move the actor's head.

    Attributes:
        _keyboard_service (KeyboardService): An instance of KeyboardService.
    """

    def __init__(self, keyboard_service):
        """Constructs a new ControlActorsAction using the specified KeyboardService.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
        """
        self._keyboard_service = keyboard_service
        self._direction = Point(constants.CELL_SIZE, 0)
        self._move_left = 'a'
        self._move_right = 'd'
        self._move_up = 'w'
        self._move_down = 's'
        self._player_number = 0

    def execute(self, cast, script):
        """Executes the control actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """

        snake = cast.get_actor("snakes", self._player_number)

        # Move Left
        if self._keyboard_service.is_key_down(self._move_left):
            self._direction = Point(-constants.CELL_SIZE, 0)
            snake.grow_tail(1, snake._color)
        
        # Move Right
        if self._keyboard_service.is_key_down(self._move_right):
            self._direction = Point(constants.CELL_SIZE, 0)
            snake.grow_tail(1, snake._color)
        
        # Move up
        if self._keyboard_service.is_key_down(self._move_up):
            self._direction = Point(0, -constants.CELL_SIZE)
            snake.grow_tail(1, snake._color)
        
        # Move Down
        if self._keyboard_service.is_key_down(self._move_down):
            self._direction = Point(0, constants.CELL_SIZE)
            snake.grow_tail(1, snake._color)

        
        
        snake.turn_head(self._direction)
        

