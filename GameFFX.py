from sys import exit

#This function asks if the persons wants to play
def NewGame():
    option = input("> ")

    if option == "Y" or option == "y":
        print("Game has started")
        Characters_and_Weapons(characters, weapons)
    elif option == "N" or option == "n":
        print("Maybe next time, bye!")
        exit(0)
    else:
        print("Incorrect option, please type Y or N")
        NewGame()
#This function will allow the player to select the character and the weapon
def Characters_and_Weapons(Character, Weapons):
    print("""
    Please select the character you will use to fight:

        (1) Tidus
        (2) Yuna
        (3) Aaron
    """)
    character_selection = input ("Type the number of the character you want to select: ")
    print("""
    Now please select the weapon you are going to use:

        (1) Sword
        (2) Magic wand
        (3) Shield
    """)
    weapon_selection = input ("Type the number of the weapon you want: ")
    selection_CW(character_selection,weapon_selection) #Will calls the funtion that sets the values

def selection_CW (c_selection, w_selection):

    if c_selection == "1":
        player.append(characters[0])
    elif c_selection == "2":
        player.append(characters[1])
    elif c_selection == "3":
        player.append(characters[2])
    else:
        print('Incorrect value, please input a value from 1 to 3 to select the character')

    if c_selection == "1":
        player.append(weapons[0])
    elif c_selection == "2":
        player.append(weapons[1])
    elif c_selection == "3":
        player.append(weapons[2])
    else:
        print('Incorrect value, please input a value from 1 to 3 to select the weapon')

    print(f"\nYou have selected the character {player[0]} and the weapon {player[1]}.")


characters = ["Tidus", "Yuna", "Aaron"]
weapons = ["Sword", "Magic wand", "Shield"]
player = []
Name = input("Please enter your name: ")
print(f"Hello {Name}, Do you want to start a new game? (Y/N): ")
NewGame()
