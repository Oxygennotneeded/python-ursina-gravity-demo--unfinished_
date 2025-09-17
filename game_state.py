class GameState:
    def __init__(self):
        #used to determine if menus are currently open or closed
        self.properties_menu_instance = None #to prevent menus from piling ontop of eachother
        self.add_planet_menu_instance = None
        
        #-----Planet related state variables-----
        #a dictionary for creating and storing the planet objects along with their id's
        self.planets= {}
        #use this when adding planet always go in order of creation
        self.next_planet_id = 0
        #not really important might remove
        self.planet_list = [] #list of all planets in the scene

state = GameState()