class Weapons():

    Armory = {
        # The values of each weapon list are ammo capacity[0], damage[1], accuracy[2], movement speed[3], self damage[4]
        'laserGun': [13, 10, 80, 80, 0],
        'laserMachineGun': [60, 30, 40, 50, 0],
        'laserMiniGun': [150, 40, 20, 20, 0],
        'laserKnife': ['NoAplicable', 100, 100, 100, 10],
        'atomBomb': [1, 1000, 100, 10, 1000],
        'godHand': [100000, 100000, 100000, 100000, -100000]
    }

    def __init__(self, weapon_Equiped):
        self.weaponEquiped = weapon_Equiped

    def IncreaseAmmo(self):
        # To select an element for the list (Armory['gunName'][0])
        if isinstance((Weapons.Armory[self.weaponEquiped][0]), int):
            Weapons.Armory[self.weaponEquiped][0] *= 2
            print(Weapons.Armory[self.weaponEquiped])
        else:
            print("The knife doesn't need bullets (bullets dropped...)")

    def IncreaseDamage(self):
        # To select an element for the list (Armory['gunName'][1])
        if isinstance((Weapons.Armory[self.weaponEquiped][1]), int):
            Weapons.Armory[self.weaponEquiped][1] *= 2
            if ((Weapons.Armory[self.weaponEquiped][1]) >= 2000) and (not(self.weaponEquiped == 'godHand')):
                (Weapons.Armory[self.weaponEquiped][1]) = 2000
                print("You have reached the limit of the damage. Blow them out!!!!")
            print(Weapons.Armory[self.weaponEquiped])
        else:
            print("Incorrect value, the damage is measured by numbers")

    def IncreaseAccuracy(self):
        # To select an element for the list (Armory['gunName'][2])
        if isinstance((Weapons.Armory[self.weaponEquiped][2]), int):
            Weapons.Armory[self.weaponEquiped][2] *= 2
            if ((Weapons.Armory[self.weaponEquiped][2]) >= 500) and (not(self.weaponEquiped == 'godHand')):
                (Weapons.Armory[self.weaponEquiped][2]) = 500
                print("You have reached the limit of the accuracy. Go for those headshots!!!!")
            print(Weapons.Armory[self.weaponEquiped])
        else:
            print("Incorrect value, the accuracy is measured by numbers")

    def IncreaseSpeed(self):
        # To select an element for the list (Armory['gunName'][3])
        if isinstance((Weapons.Armory[self.weaponEquiped][2]), int):
            Weapons.Armory[self.weaponEquiped][3] *= 2
            if ((Weapons.Armory[self.weaponEquiped][3]) >= 500) and (not(self.weaponEquiped == 'godHand')):
                (Weapons.Armory[self.weaponEquiped][3]) = 500
                print("You have reached the limit of the speed. Run like hell!!!!")
            print(Weapons.Armory[self.weaponEquiped])
        else:
            print("Incorrect value, the speed is measured by numbers")

    def DecreaseSelfDamage(self):
        # To select an element for the list (Armory['gunName'][4])
        if isinstance((Weapons.Armory[self.weaponEquiped][0]), int):
            Weapons.Armory[self.weaponEquiped][4] -= 100
            if ((Weapons.Armory[self.weaponEquiped][4]) <= -1000) and (not(self.weaponEquiped == 'godHand')):
                (Weapons.Armory[self.weaponEquiped][4]) = -1000
                print("You have reached the limit of armour. you're bullet proof!!!!")
            print(Weapons.Armory[self.weaponEquiped])
        else:
            print("Incorrect value, the armour is measured by numbers")

#print("---- Knife -----")
#knife = Weapons('laserKnife')
#knife.IncreaseAmmo()

#print("\n---- LaserGun -----")
#gun = Weapons('laserGun')
#gun.IncreaseAmmo()

#print("\n---- MachineGun -----")
#machgun = Weapons('laserMachineGun')
#machgun.IncreaseAmmo()

#print("\n---- God -----")
#god = Weapons('godHand') 
#god.IncreaseAmmo()
#god.IncreaseDamage()
#god.IncreaseAccuracy()
#god.IncreaseSpeed()
#god.DecreaseSelfDamage()
#god.IncreaseAmmo()
#god.IncreaseDamage()
#god.IncreaseAccuracy()
#god.IncreaseSpeed()
#god.DecreaseSelfDamage()

#print("\n---- Nuclear bomb -----")
#nuke = Weapons('atomBomb')
#nuke.IncreaseAmmo()
#nuke.IncreaseDamage()
#nuke.IncreaseAccuracy()
#nuke.IncreaseSpeed()
#nuke.DecreaseSelfDamage()
#nuke.IncreaseAmmo()
#nuke.IncreaseDamage()
#nuke.IncreaseAccuracy()
#nuke.IncreaseSpeed()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()
#nuke.DecreaseSelfDamage()