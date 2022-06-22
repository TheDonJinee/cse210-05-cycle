import constants

from game.casting.cast import Cast
from game.casting.score import Score
from game.casting.snake import Snake
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlFirstActorsAction
from game.scripting.control_actors_action_2 import ControlSecondActorsAction
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():

    # Create game casts
    cast = Cast()
    x = int(constants.MAX_X / 2)
    y = int(constants.MAX_Y / 2)
    x1 = int(constants.MAX_X / 4)
    y1 = int(constants.MAX_Y / 4)
    cast.add_actor("snakes", Snake("@", constants.GREEN, x, y))
    cast.add_actor("snakes", Snake("@", constants.RED, x1, y1))

    # Begin Game Play
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlFirstActorsAction(keyboard_service))
    script.add_action("input", ControlSecondActorsAction(keyboard_service))
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))

    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()
