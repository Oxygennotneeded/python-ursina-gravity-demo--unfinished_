from ursina import *

class PLANET(Entity):

    def __init__(self, planet_color=color.orange, position = (0,0,0), scale = 1, mouse_position = False):
        super().__init__(
            model='sphere',
            texture='white_cube',
            color= planet_color,
            position=position,
            scale=scale
        )
        