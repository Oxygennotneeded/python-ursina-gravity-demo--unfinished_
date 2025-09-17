class GameState:
    def __init__(self):
        self.properties_menu_instance = None #to prevent menus from piling ontop of eachother
        self.add_planet_menu_instance = None
        
        #-----Planet related state variables-----
        self.planet_list = [] #list of all planets in the scene

state = GameState()