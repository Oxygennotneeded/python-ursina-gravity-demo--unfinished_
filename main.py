from ursina import *
import planet

#---USER SETTINGS-------
hold_duration_threshold = 0.25 #How long the click has to be for it to be considered a hold or a click of the mouse

#---global variables----
properties_menu_instance = None #to prevent menus from piling ontop of eachother
add_planet_menu_instance = None

#--Ursina 
app = Ursina()
Sky(texture='textures\milky-way-stars-in-space-virtual-reality-360-degree-video-elements-of-this-image-furnished-by-nasa_StprBfkdx_thumbnail-108010-1961978930.png')
EditorCamera() 

num_planets = 1
planets_positions = [Vec3(0,0,0), Vec3(1,0,0)]
planet_list = []

for i in range(num_planets):
    new_planet = planet.PLANET(position=planets_positions[i])
    planet_list.append(new_planet)

class ADD_PLANET_MENU(Entity):

    def __init__(self):
        global add_planet_menu_instance
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
        global add_planet_menu_instance

        created_planet = planet.PLANET(position = (1, 0 ,0), mouse_position = True)
        planet_list.append(created_planet)
        add_planet_menu_instance = None
        destroy(self, add_planet_menu_instance)

    def destroy_menu(self):
            global add_planet_menu_instance

            add_planet_menu_instance = None
            destroy(self)
    

class PROPERTIES_MENU(Entity):
    def __init__(self, menu_instance):
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
        global add_planet_menu_instance
        
        if add_planet_menu_instance == None:
            add_planet_menu_instance = ADD_PLANET_MENU()
            destroy(self)
            

        else:
            destroy(add_planet_menu_instance)

    
def input(key):
    global right_click_start_time, properties_menu_instance, add_planet_menu_instance

    if key == 'right mouse down':
        # Record the start time.
        right_click_start_time = time.time()

    if key == 'right mouse up':
        #  Calculate the duration.
        duration = time.time() - right_click_start_time

        #  Check if it was a tap.
        if duration < hold_duration_threshold:
            if properties_menu_instance:
                destroy(properties_menu_instance)

            elif add_planet_menu_instance:
                return

            else:   
                properties_menu_instance = PROPERTIES_MENU(properties_menu_instance) 
            
    if key == 'left mouse up' and properties_menu_instance:
        destroy(properties_menu_instance)

def update():
    
    camera.x += held_keys['d'] * time.dt
    camera.x -= held_keys['a'] * time.dt
    camera.z += held_keys['w'] * time.dt
    camera.z -= held_keys['s'] * time.dt
    
    
app.run()
#all the cool shit
