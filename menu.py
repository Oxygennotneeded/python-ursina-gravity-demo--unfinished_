from ursina import *
import planet
from game_state import state

class ADD_PLANET_MENU(Entity):

    def __init__(self):
        super().__init__(
            parent = camera.ui,
            position = Vec2(0, 0),
            model = 'quad',
            scale = (0.9, 0.9),
            color=color.dark_gray,
            radius = 0.2,
            z = -1
        )
        self.title = Text(parent = self, text = 'Planet Creation',color=color.white, y = 0.4)

        self.add_planet_button = Button(
            parent=self,
            text='Add planet',
            color=color.blue,
            highlight_color = color.green,
            scale=(0.15, 0.1),
            x=-0.4, 
            y=0.4 - 0.05,
            z = -2,
            on_click = lambda: self.add_planet()                  
        )

        #self.add_planet_button.on_click = self.add_planet

        self.exit_button = Button(
            parent=self,
            text = 'X',
            color=color.red,
            highlight_color=color.yellow,
            scale = (0.04, 0.04),
            x = 0.5,
            y = 0.5,
            z = -2
        )
        self.exit_button.on_click = lambda: self.destroy_menu()

    def add_planet(self):
        created_planet = planet.PLANET(position = (1, 0 ,0), mouse_position = True)
        state.planet_list.append(created_planet)
        state.add_planet_menu_instance = None
        destroy(self, state.add_planet_menu_instance)

    def destroy_menu(self):
            

            state.add_planet_menu_instance = None
            destroy(self)
    
    
class PROPERTIES_MENU(Entity):
    def __init__(self):
        super().__init__(
            parent=camera.ui,
            position=mouse.position + Vec2(0.1, 0),
            model='quad',
            scale=(.2, .4),
            color=color.dark_gray,
            radius=0.2,
            z = -1
        )
        

        self.title = Text(parent=self, text='Properties', color=color.white, y=0.4)

        self.add_planet_button = Button(
            parent=self,
            text='Add planet',
            color=color.blue,
            scale=(.8, .2),
            y=0.1,
            z = -2,
            on_click = lambda: self.open_planet_menu()
        )
        
    
    
    def open_planet_menu(self):
        
        
        if state.add_planet_menu_instance == None:
            state.add_planet_menu_instance = ADD_PLANET_MENU()
            destroy(self)
            

        else:
            destroy(state.add_planet_menu_instance)
