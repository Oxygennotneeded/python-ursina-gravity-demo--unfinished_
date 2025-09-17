from ursina import *
import planet
from game_state import state
from menu import ADD_PLANET_MENU, PROPERTIES_MENU

#---USER SETTINGS-------
#How long the click has to be for it to be considered a hold or a click of the mouse // may move to its own function later
hold_duration_threshold = 0.25 



#--Ursina 
app = Ursina()
#Sky Box texture //plan to change // is a placeholder
Sky(texture='textures\milky-way-stars-in-space-virtual-reality-360-degree-video-elements-of-this-image-furnished-by-nasa_StprBfkdx_thumbnail-108010-1961978930.png')
EditorCamera() 

#where most our inputs take place(unless in some sort of function or something)
def input(key):
    global right_click_start_time
    #if the key pressed is the right mouse button
    if key == 'right mouse down':
        # Record the start time.
        right_click_start_time = time.time()
    #when the right mouse button is released
    if key == 'right mouse up':
        #  Calculate the duration.
        duration = time.time() - right_click_start_time

        #  Check if it was a tap.
        if duration < hold_duration_threshold:

            #If this menu already exists, remove existing menu
            if state.properties_menu_instance: 
                destroy(state.properties_menu_instance)

            #Dont allow properties menu to exist when add planet menu exists
            elif state.add_planet_menu_instance:
                return
            
            #Create the properties menu and log its existance in our game state
            else:   
                state.properties_menu_instance = PROPERTIES_MENU() 
    #if we left click and the existence of the property menu is true destroy        
    if key == 'left mouse up' and state.properties_menu_instance:
        destroy(state.properties_menu_instance)

def update():
    
    #self explanitory moving 
    camera.x += held_keys['d'] * time.dt
    camera.x -= held_keys['a'] * time.dt
    camera.z += held_keys['w'] * time.dt
    camera.z -= held_keys['s'] * time.dt
    
    
app.run()

