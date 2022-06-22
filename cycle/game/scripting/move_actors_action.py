from game.scripting.action import Action

class MoveActorsAction(Action):
    ''''''

    def execute(self, cast, script):
        actors = cast.get_all_actors()
        for actors in actors:
            actors.move_next()