from ursina import *
import planet

#---USER SETTINGS-------
hold_duration_threshold = 0.25

#---Boolean values----


#--Ursina shit
app = Ursina()
EditorCamera() 

num_planets = 2
planets_positions = [Vec3(0,0,0), Vec3(1,0,0)]
planet_list = []

for i in range(num_planets):
    new_planet = planet.PLANET(position=planets_positions[i])
    planet_list.append(new_planet)



def update():

    camera.x += held_keys['d'] * time.dt
    camera.x -= held_keys['a'] * time.dt
    camera.z += held_keys['w'] * time.dt
    camera.z -= held_keys['s'] * time.dt
    
    
app.run()
#all the cool shit
