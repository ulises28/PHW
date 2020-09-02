from sys import exit

#-------------------- Scene -------------------------------------------------
class Scene(object):
    def __init__(self):
        pass
    
    def enter(self):
        pass

class Death (Scene):
    def enter(self):
        print("This is the death valley where are the defeated heros rest, this means you are DEATH!")
        
class Corridor (Scene):
    def enter(self):
         print("This is the starting point and has a Gothon already standing...")
        
class LeaserWeapon (Scene):
    def enter(self):
         print("This iw here the hero gest a neutron..")
        
class Bridge (Scene):
    def enter(self):
         print("This is another battle scene with a Gothon where the hero...")
        
class Escape (Scene):
    def enter(self):
         print("This is where the hero escapes but only after guessing the right ecape pod")
        
#-------------------- Engine -------------------------------------------------
class Engine(object):
    def __init__(self, scene_map):
        pass
        
    def play(self):
        pass
#-------------------- Map ----------------------------------------------------
class Map(object):
    def __init__(self, start_scene):
        self.start_scene = start_scene;
        
    def next_scene(self, scene_name):
        pass
        
    def opening_scene(self):
        print(f"Game started at {self.start_scene}")
#------------------- Main -----------------------------------------------------
print("Let's play! (y/n)")
Star_NewGame = input()
if Star_NewGame.upper() == 'Y':
    print("Here we go!")
    print("Choose where you want to start by pressing the number + 'ENTER' :")
    print("""
    1. Death Valley.
    2. Central Corridor.
    3. Go for the laser gun.
    4. Bridge.
    """)
    Scenario_Option = input()
    Scenario_List = [Death, Corridor, LeaserWeapon, Bridge, Escape]
 
    print(Scenario_List[int(Scenario_Option) - 1])
    Scene_Selection = Scenario_List[int(Scenario_Option) - 1]
    Scene_Selection
 
#    Start_Scenario = Map('Central_corridor')
#    Game = Engine(Start_Scenario)
#    Game.play();
    
elif Star_NewGame.upper() == 'N':
    print("Maybe next time")
    exit(1)
else:
    print("Ehhhh?! Ok bye")
    exit(1)