
import random

class Player:
    name = ""
    H = 100
    STR = 5
    DEX = 5
    FRT = 5
    
    def __init__(self, name, H, STR, DEX, FRT):
        self.name = name
        self.H = H
        self.STR = STR
        self.DEX = DEX
        self.FRT = FRT

    def get_health(self):
        return self.H

class Enemy:
    name = ""
    H = 0 
    STR = 0
    DEX = 0
    FRT = 0
   
    def __init__(self, name, H, STR, DEX, FRT):
        self.name = name
        self.H = H
        self.STR = STR
        self.DEX = DEX
        self.FRT = FRT
        
    def get_health(self):
        return Enemy.H
    
class Goblin(Enemy):
    name = "Goblin"
    H = 25
    STR = 10
    DEX = 3
    FRT = 3
    
    def __init__(self):
        super().__init__(name="Goblin", H=25, STR=5, DEX=3, FRT=3)

def prompt():
    x = input()
    return x



def CombatGoblin():
    while Player.H >= 0:
        print("You are fighting a Goblin.")
        print("""What will you do?
        1: Attack
        2: Wait""")
        command = prompt()
        
        if command == "1":
            dexcheck = random.randint(1, 2)
            dexroll = random.randint(1, 5)
            if dexcheck == 1:
                Goblin.DEX = Goblin.DEX - dexroll
                if Goblin.DEX <= Player.STR:
                    dmgboost = random.randint(1, 3)
                    Goblin.H -= Player.STR+dmgboost-Goblin.FRT
                    print("You strike the Goblin for {} damage.".format(Player.STR-Goblin.FRT))
                if Goblin.DEX >= Player.STR:
                   print("The Goblin dodges the attack.")
                enemyturn = random.choice('12')
                if enemyturn == "1":
                        dexcheck = random.randint(1, 2)
                        dexroll = random.randint(1, 5)
                        if dexcheck == 1:
                            Player.DEX = Player.DEX - dexroll
                            if Player.DEX <= Goblin.STR:
                                dmgboost = random.randint(1, 3)
                                Player.H -= Goblin.STR+dmgboost-Player.FRT
                                print("The Goblin strikes you for {} damage.".format(Goblin.STR-Player.FRT))
                            if Player.DEX >= Goblin.STR:
                                print("You dodge the attack.")
                        if dexcheck == 2:
                            Player.DEX = Player.DEX + dexroll
                            if Player.DEX <= Goblin.STR:
                                dmgboost = random.randint(1, 3)
                                Player.H -= Goblin.STR+dmgboost-Player.FRT
                                print("The Goblin strikes you for {} damage.".format(Goblin.STR-Player.FRT))
                            if Player.DEX >= Goblin.STR:
                                print("You dodge the attack")
                
                if enemyturn == "2":
                    print("The Goblin waits patiently")

            if dexcheck == 2:
                Goblin.DEX = Goblin.DEX + dexroll
                if Goblin.DEX <= Player.STR:
                    dmgboost = random.randint(1, 3)
                    Goblin.H -= Player.STR+dmgboost-Goblin.FRT
                    print("You strike the Goblin for {} damage.".format(Player.STR-Goblin.FRT))
                if Goblin.DEX >= Player.STR:
                    print("The Goblin dodges the attack.")
                enemyturn = random.choice('12')
                if enemyturn == "1":
                    dexcheck = random.randint(1, 2)
                    dexroll = random.randint(1, 5)
                    if dexcheck == 1:
                        Player.DEX = Player.DEX - dexroll
                        if Player.DEX <= Goblin.STR:
                            dmgboost = random.randint(1, 3)
                            Player.H -= Goblin.STR+dmgboost-Player.FRT
                            print("The Goblin strikes you for {} damage.".format(Goblin.STR-Player.FRT))
                        if Player.DEX >= Goblin.STR:
                            print("You dodge the attack.")
                    if dexcheck == 2:
                            Player.DEX = Player.DEX + dexroll
                            if Player.DEX <= Goblin.STR:
                                dmgboost = random.randint(1, 3)
                                Player.H -= Goblin.STR+dmgboost-Player.FRT
                                print("The Goblin strikes you for {} damage.".format(Goblin.STR-Player.FRT))
                            if Player.DEX >= Goblin.STR:
                                print("You dodge the attack")
                if enemyturn == "2":
                    print("The Goblin waits patiently")

                                
        if command == "2":
            print("You wait patiently.")
            enemyturn = random.choice('12')
            if enemyturn == "1":
                dexcheck = random.randint(1, 2)
                dexroll = random.randint(1, 5)
                if dexcheck == 1:
                    Player.DEX = Player.DEX - dexroll
                    if Player.DEX <= STR:
                        Player.H -= Goblin.STR+dmgboost-Player.FRT
                        print("The Goblin strike you for {} damage.".format(Goblin.STR))
                    if Player.DEX >= STR:
                        print("You dodge the attack.")
                if dexcheck == 2:
                    Player.DEX = Player.DEX + dexroll
                    if Player.DEX <= Goblin.STR:
                        Player.H -= Goblin.STR+dmgboost-Player.FRT
                        print("The Goblin strikes you for {} damage.".format(Goblin.STR-Player.FRT))
                    if Player.DEX >= Goblin.STR:
                        print("You dodge the attack")
                
            if enemyturn == "2":
                print("The Goblin waits patiently")

        if Goblin.H <= 0:
           Victory()

        if Player.H <= 0:
            GameOver()
                      
def GameOver():
    print("You have been slain")
    input()

def Victory():
    print("The Enemy has been slain")
    input()

CombatGoblin()
