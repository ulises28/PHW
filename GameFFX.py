from sys import exit

#This function asks if the persons wants to play
def NewGame():
    option = input("> ")

    if option == "Y" or option == "y":
        print("Game has started")
    elif option == "N" or option == "n":
        print("Maybe next time, bye!")
        exit(0)
    else:
        print("Incorrect option, please type Y or N")
        NewGame()
#This function will allow the player to select the character and the weapon
def Characters_and_Weapons():
    print ()











Name = input("Please enter your name: ")
print(f"Hello {Name}, Do you want to start a new game? (Y/N): ")
NewGame()
