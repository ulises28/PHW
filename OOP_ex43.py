from sys import exit
from random import randint
from textwrap import dedent

#-------------------- Scene -------------------------------------------------
class Scene(object):
    def enter(self):
    #This is like a generic scene, only created to follow the structure
        pass

class Death(Scene):
    def enter(self):
        print("You made a bad decision!!! *Blood explosion* JAJAJAJAJAJA")
        exit(1)
        
class Corridor (Scene):
    def enter(self):
        print(dedent("""
        Let see how smart you're , you need need to take some decision 
        to defeat the aliens who have invaded the ship and reach the planet
        below. 
        So, how you want to start this journey? 
        [You just need to enter the number and the press ENTER]
        
        1) Find a gun to fight against them.
        2) Start the fight! there is no time to be wasted.
        3) Hide! The best strategy is to stay asaid from the aliens an find a way out.
        4) Do nothing, expect that someone will to save you.
        """))
        Option = input("> ")
        if Option == '1':
            print(dedent("""
            Smart move, you need something to fight againts the aliens,
            you run as fast as possible to the armory.
            """))
            return 'Leaser_Weapon'
        elif Option == '2':
            print(dedent("""
            This will be very dificult, without weapons you run to the bridge
            in order to find an available ship to reach the planet below.
            """))
            return 'Bridge_Fight_No_Weapon'
        elif Option == '3':
            print(dedent("""
            The hero remains still until he realices the alines can see him with the 
            heat sensor they have , you run as fast as possible where the ship are,
            but a lot of aliens start to hunt you.
            """))
            return 'Escape_Hidding'
        elif Option == '4':
            print(dedent("""
            Nobody will come to safe you, also the heros never expect to be saved, 
            seems that a bad decision has been taken.
            """))
            return 'Dead'
        else:
            print(dedent("""
            That is not an option. Remember, "you need to be smart".
            You can't even read instructions...
            """)) 
            return 'Dead'
        
class LeaserWeapon (Scene):
    def enter(self):
        print(dedent("""
        You have reached the armory, there are plenty of weapons, but you can only carry one.
        Choose wisely, because there are advantages and disavantages for each one:
        1) Choose the always reliable laser handgun,
        -- This weapon will allow you to run fast but the laser charge wont last too much.
        2) Choose the bazooka, 
        -- You will only have one shoot, but with a huge destructive power.
        3) Choose asault rifle
        -- A good balance between weight and power capacity, but... the normal bullet will kill the aliens?
        """))
        Option = input("> ")
        if Option == '1':
            print(dedent("""
            You took the reliable option, please use the laser with measure.
            """))
            return 'The_bridge'
        elif Option == '2':
            print(dedent("""
            You only have one, shoot... 
            You don't waste time and trigger the missile to the aliens. 
            You need to enter a number between 1-5 
            If you guess the correct number you missile will kill the alines,
            otherwise you will enter the bridge unarmed.
            """))
            randomShot = randint(1,5)
            Misile_Hit = input('> ')
            if int(Misile_Hit) == randomShot:
                print(dedent("""
                Awsome!!! you hit the target 
                there are fragments of aliens everywhere
                but nothing to worry about
                you cross the bridge without problems
                """))
                return 'Escape_Pod'
            else:
                print(f"You missed the shot (the expected value was {randomShot} )")
                print(dedent("""                              
                This will be very dificult, without weapons you run into the bridge
                in order to find an available ship to reach the planet below.
                """))
                return 'Bridge_Fight_No_Weapon'
        elif Option == '3':
            print(dedent("""
            Well you took the assault rifle and plenty of ammo
            You go to the bridge and start shooting...
            But you realice the normal bullets can't penetrate
            the Aliens skin.
            """))
            return 'Bridge_Fight_No_Weapon'
        else:
            print(dedent("""
            That is not an option.. remember, "you need to be smart"...
            """)) 
            return 'Dead'
        
class Bridge (Scene):
    def enter(self):
         print("This is another battle scene with a Gothon where the hero...")
         
class BridgeNW(Scene):
    def enter(self):
        pass
        
class EscapeH(Scene):
    def enter(self):
        pass

class Escape (Scene):
    def enter(self):
         print("This is where the hero escapes but only after guessing the right ecape pod")
         
class Finished(Scene):
    def enter(self):
        print("You won, good job!")
        return 'Finished'
        
#-------------------- Engine -------------------------------------------------
class Engine(object):
    def __init__(self, scene_map):
        self.scene_map = scene_map
        
    def play(self):                                         #This function will determine the start and end of the game
        current_scene = self.scene_map.opening_scene()      #Set current_scene to --> from self.scene_map get the function opening_scene with self parameters
        last_scene = self.scene_map.next_scene('Finished')  #Set last_scene to --> from self.scene_map get the function next_scene with self, Finished parameters
        
        while current_scene != last_scene:                  #Loop that will run intul current_scene gets the value 'Finished'
            next_scene_name = current_scene.enter()         #Set next_scene_name to --> From current_scene.enter() get enter function with self parameter 
            current_scene = self.scene_map.next_scene(next_scene_name) #Set current_scene to the value function next_scene on MAP class will retrieve based on the enter function returned previosuly.
            
        current_scene.enter()                               #If the loop has ended (current_scene = 'Finished') the player has won
        
#-------------------- Map ----------------------------------------------------
class Map():

    Scenes_Relationship = {
    'Central_Corridor' : Corridor(),
    'Leaser_Weapon' : LeaserWeapon(),
    'The_bridge' : Bridge(),
    'Bridge_Fight_No_Weapon' : BridgeNW(),
    'Escape_Hidding' : EscapeH(),
    'Escape_Pod' : Escape(),
    'Dead' : Death(),
    'Finished' : Finished()
    }

    def __init__(self, start_scene):
        self.start_scene = start_scene
        
    def next_scene(self, scene_name):
        conv = Map.Scenes_Relationship[scene_name]
        return conv
        
    def opening_scene(self):
        return Map.Scenes_Relationship[self.start_scene]
#------------------- Main -----------------------------------------------------
print("Let's play! (y/n)")
Star_NewGame = input()
if Star_NewGame.upper() == 'Y':
    print("Here we go!")
#    print("Choose where you want to start by pressing the number + 'ENTER' :")
#    print("""
#    1. Death Valley.
#    2. Central Corridor.
#    3. Go for the laser gun.
#    4. Bridge.
#    """)
#    Scenario_Option = input()
#    Scenario_List = [Death, Corridor, LeaserWeapon, Bridge, Escape]
# 
#    print(Scenario_List[int(Scenario_Option) - 1])
#    Scene_Selection = Scenario_List[int(Scenario_Option) - 1]
#    Start_Scenario = Scene_Selection()
#    Start_Scenario.enter()
#
    G_Map = Map('Central_Corridor')    # Set G_Map to an instance of class Map with self and Central_Corridor string parameter.
    G_Engine = Engine(G_Map)              # Set G_Engine to an instance of class Engine with self and G_Map variable parameter.
    G_Engine.play()                       # From G_Engine, get the function play and call it with the self parameter.  
    
elif Star_NewGame.upper() == 'N':
    print("Maybe next time")
    exit(1)
else:
    print("Ehhhh?! Ok bye")
    exit(1)