import constants
from game.casting.actor import Actor
from game.shared.point import Point


class Snake(Actor):
    """
    A long limbless reptile. This snake is player 1.

    The responsibility of Snake is to move itself.

    Attributes:
        _segments(list): A list of segments for the snake.
        _set_color(color): The color of the snake
        _prepare_body: Gives the symbol of the head, sets the color to the snakes, and gives appropriate points
    """

    def __init__(self, head_symbol, color, x, y):
        super().__init__()
        self._segments = []
        self._color = color
        self._prepare_body(head_symbol, color, x, y)
        self.set_color = color

    def get_segments(self):
        return self._segments

    def move_next(self):

        for segment in self._segments:
            segment.move_next()

        for i in range(len(self._segments) - 1, 0, -1):
            trailing = self._segments[i]
            previous = self._segments[i - 1]
            velocity = previous.get_velocity()
            trailing.set_velocity(velocity)

    def get_head(self):
        return self._segments[0]

    def grow_tail(self, number_of_segments, color):
        for i in range(number_of_segments):
            tail = self._segments[-1]
            velocity = tail.get_velocity()
            offset = velocity.reverse()
            position = tail.get_position().add(offset)

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text("#")
            segment.set_color(color)
            self._segments.append(segment)

    def turn_head(self, velocity):
        self._segments[0].set_velocity(velocity)

    def _prepare_body(self, head_symbol, color, x, y):

        for i in range(constants.SNAKE_LENGTH):
            position = Point(x - i * constants.CELL_SIZE, y)
            velocity = Point(1 * constants.CELL_SIZE, 0)
            text = head_symbol if i == 0 else "#"
            color = color if i == 0 else color

            segment = Actor()
            segment.set_position(position)
            segment.set_velocity(velocity)
            segment.set_text(text)
            segment.set_color(color)
            self._segments.append(segment)
