class Player:
    def __init__(self, name, age, pclass, mp):
        self.name = name
        self.age = age
        self.pclass = pclass
        self.mana = mp

global Npc1 
global Npc2

Npc1 = Player("John", 20 , "Monk", 250)
Npc2 = Player("Siph", 378, "Warlock", 549)

WarlockSpell1 = {"name":"Fireball", "Damage":30, "MP Cost":10}
WarlockSpell2 = {"name":"Eldrich Blast", "Damage":15, "MP Cost":5}
WarlockSpell3 = {"name":"Jester", "Damage":5, "MP Cost":0}

def Gather_Info():
    X1 = input("What is your first name? : ")
    X2 = input("How old are you? ")

    global P1
    P1 = Player(X1, X2, "blank", 0)

    print ("What Class would you like to be? [ Warlock ], [ Monk ], or [ Fighter ]?")
    Class = input(" [ ")

    if Class == "Warlock":
        print ("You have decided to be a Warlock, the Master of Reality!\n")
        P1 = Player(X1, X2, "Warlock", 300)
    elif Class == "Monk":
        print ("You have decided to be a Monk, Fighters of Fate!\n")
        P1 = Player(X1, X2, "Monk", 250)
    elif Class == "Fighter":
        print ("You have decided to be a Fighter, a Keeper of Peace!\n")
        P1 = Player(X1, X2, "Fighter", 30)

    print("You have chosen to be a " + P1.pclass + "\n")
    print("You are now " + X1 + " the " + P1.pclass + "\n")

def Welcome():
    print("Welcome "+ P1.name +" to the world of Alferon!")
    print("Alferon is a world of Magic, Wars, and Betrayal.\n")
    print("And you, " + P1.name + " have been dropped into this world feet first!")
    print("You have found a small pouch of 30 GP (Gold Pieces) and can choose how to spend them.")
    global gp
    gp = 0
    gp = gp + 30
    print("You now have " + str(gp) + " gold!")

def Str1():
    print("\n\nYou awaken in a tavern - You seem to be on the floor which, ")
    print("while strange, doesn't bother you too much, since it's happened")
    print("before. \n\n")
    if P1.pclass == "Warlock":
        print("You have the following spells : " + WarlockSpell1["name"] + " :: " + WarlockSpell2["name"] + " :: " + WarlockSpell3["name"] + " . ")
    else:
       print("\nYou Don't have any spells available\n")
    print(Npc1.name + " The Barkeep : You seem to be rather lost there, stranger.\n")
    print(Npc1.name + " The Barkeep : You should get outta here - Guards are gonna come scoop you up if you don't.\n")

    print("\n Following the barkeeps advice - You do stand to leave - making sure to take your gold pouch with you.")
    print("\n Now outside, you appear to be in the middle of the city of Junx, based on the sign you can see from the tavern.")
    print("\n Which direction would you want to go? [R] [F] [L]")
    direction1 = input("[ ")

    if direction1 == "R":
        print("You've gone Right")
        R1()
    elif direction1 == "F":
        print("You've gone Forward")
        F1()
    elif direction1 == "L":
        print("You've gone Left")
        L1()

def R1():
    print("You've gone Right, And onto a road that leads you around the edge of the city.")
    print("On this road, you come across a Magic Shop called 'Magiks Hands' ")
    print("Would you like to go in? [ Y ] [ N ]")
    MagikHands = input(" [ ")
    if MagikHands == "Y":
        print("You've entered the shop, the man behind the counter speaking to you.")
        print(Npc2.name + " The Shopkeep : Welcome to my shop stranger!")
        print(Npc2.name + " The Shopkeep : How could I help you today?")
        print("End of Line")
    elif MagikHands == "N":
        print(" you decided to walk past the shop, no matter how tempting it is to go in.")
        print("End of Line")
def F1():
    print("You've gone Forward, And onto a road that leads you to the Castle.")
    print("End of Line")
def L1():
    print("You've gone Left, And onto a road that leads out of the City.")
    print("End of Line")
    

def main():
    print("Welcome Player!\n")
    Gather_Info()
    Welcome()
    Str1()


if __name__ == "__main__":
    main()