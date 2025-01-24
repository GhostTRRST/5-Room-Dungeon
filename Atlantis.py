'''
    project: 5 room dungeon

    Author: Jaydriel Montes Connolly <jmontes-connolly2709545@woonsocketschools.com>
    Author: Nolan Pierce <npierce2709337@woonsocketschools.com>
    Author: Nathan Sayphrarath <nsayphrarath2709522@woonsocketschools.com>
'''
import random, os, time

# Character creation and game variables
isPlaying = False
isCreating = True
Continue = False

# item variables
invis = 0
fish = 0
Scales = 0

# Tracks pressure plate is pressed to unlock the last room
Pressure = False

# Tracks if you're dead or not
Dead = False

#Attribute variables
Health = 0
Agility = 0
Intelligence = 0
Strength = 0

# Attribute points
Points = 0

# Counter to see how many times someone has been to a room
Room2C = 0
Room3C = 0
Room4C = 0

# String variables, name and character type
Type = ""
name = ""

# 10 sided dice
def dice10():
    roll = random.randint(1, 10)
    print(f"You rolled a {roll}!")
    print()

    return roll


# 20 sided dice
def dice20():

    roll = random.randint(1, 20)
    print(f"You rolled a {roll}!")

    return roll


#Enemy dice10, player doesn't see this
def Edice5():

    roll = random.randint(1, 5)

    return roll

# rolls 12 sided dice
def dice12():
    roll2 = random.randint(1, 12)
    print(f"you rolled a {roll2}!")

    return roll2

# Warrior class
def Warrior():
    global Health, Strength, Agility, Intelligence
    Health = 10
    Strength = 12
    Agility = 8
    Intelligence = 8

    Points = 2

    choice = input("""You Get two free points to add to any two attributes!
                       
You may add points to Health, Agility, Strength, or Intelligence!

Health could potentially increase your lifespan, Strength will help you with anything requiring force, Agility will help you in anything that requires athleticism, and Intelligence will help with some dice rolls.

Know that for combat, your damage will be based off your main attribute! For the warrior its strength, for the occultist its intelligence, and for the archer its agility.

Please Type the first letter of the two attributes you would like to add points to! (Ex. SI or HA) : """)

    # Add points to attributes
    if choice == "HA":
        Agility = Agility + 1
        Health = Health + 1
        Points = Points - 2
    elif choice == "HI":
        Intelligence = Intelligence + 1
        Health = Health + 1
        Points = Points - 2
    elif choice == "HS":
        Health = Health + 1
        Strength = Strength + 1
        Points = Points - 2
    elif choice == "SH":
        Strength = Strength + 1
        Health = Health + 1
        Points = Points - 2
    elif choice == "SA":
        Strength = Strength + 1
        Agility = Agility + 1
        Points = Points - 2
    elif choice == "SI":
        Strength = Strength + 1
        Intelligence = Intelligence + 1
        Points = Points - 2
    elif choice == "AH":
        Agility = Agility + 1
        Health = Health + 1
        Points = Points - 2
    elif choice == "AI":
        Agility = Agility + 1
        Intelligence = Intelligence + 1
        Points = Points - 2
    elif choice == "AS":
        Agility = Agility + 1
        Strength = Strength + 1
        Points = Points - 2
    elif choice == "IH":
        Intelligence = Intelligence + 1
        Health = Health + 1
        Points = Points - 2
    elif choice == "IA":
        Intelligence = Intelligence + 1
        Agility = Agility + 1
        Points = Points - 2
    elif choice == "IS":
        Intelligence = Intelligence + 1
        Strength = Strength + 1
        Points = Points - 2

    time.sleep(2)
    print()
    print(f"Your health is {Health}")
    print(f"Your strength is {Strength}")
    print(f"Your agility is {Agility}")
    print(f"Your Intelligence is {Intelligence}")

    return Health, Strength, Agility, Intelligence
# Archer class
def Archer():
    global Health, Strength, Agility, Intelligence
    Health = 8
    Strength = 8
    Agility = 12
    Intelligence = 10


    Points = 2

    choice = input("""You Get two free points to add to any two attributes!

You may add points to Health, Agility, Strength, or Intelligence!

Health could potentially increase your lifespan, Strength will help you with anything requiring force, Agility will help you in anything that requires athleticism, and Intelligence will help with some dice rolls.

Know that for combat, your damage will be based off your main attribute! For the warrior its strength, for the occultist its intelligence, and for the archer its agility.

Please Type the first letter of the two attributes you would like to add points to! (Ex. SI or HA) : """)
    # Add points to attributes
    if choice == "HA":
        Agility = Agility + 1
        Health = Health + 1
        Points = Points - 2
    elif choice == "HI":
        Intelligence = Intelligence + 1
        Health = Health + 1
        Points = Points - 2
    elif choice == "HS":
        Health = Health + 1
        Strength = Strength + 1
        Points = Points - 2
    elif choice == "SH":
        Strength = Strength + 1
        Health = Health + 1
        Points = Points - 2
    elif choice == "SA":
        Strength = Strength + 1
        Agility = Agility + 1
        Points = Points - 2
    elif choice == "SI":
        Strength = Strength + 1
        Intelligence = Intelligence + 1
        Points = Points - 2
    elif choice == "AH":
        Agility = Agility + 1
        Health = Health + 1
        Points = Points - 2
    elif choice == "AI":
        Agility = Agility + 1
        Intelligence = Intelligence + 1
        Points = Points - 2
    elif choice == "AS":
        Agility = Agility + 1
        Strength = Strength + 1
        Points = Points - 2
    elif choice == "IH":
        Intelligence = Intelligence + 1
        Health = Health + 1
        Points = Points - 2
    elif choice == "IA":
        Intelligence = Intelligence + 1
        Agility = Agility + 1
        Points = Points - 2
    elif choice == "IS":
        Intelligence = Intelligence + 1
        Strength = Strength + 1
        Points = Points - 2

    time.sleep(2)
    print()
    print(f"Your health is {Health}")
    print(f"Your strength is {Strength}")
    print(f"Your agility is {Agility}")
    print(f"Your Intelligence is {Intelligence}")

    return Health, Strength, Agility, Intelligence

# Wizard class
def Wizard():
    global Health, Strength, Agility, Intelligence
    Health = 8
    Strength = 10
    Agility = 8
    Intelligence = 12
    Points = 2

    choice = input("""You Get two free points to add to any two attributes!

You may add points to Health, Agility, Strength, or Intelligence!

Health could potentially increase your lifespan, Strength will help you with anything requiring force, Agility will help you in anything that requires athleticism, and Intelligence will help with some dice rolls.

Know that for combat, your damage will be based off your main attribute! For the warrior its strength, for the occultist its intelligence, and for the archer its agility.

Please Type the first letter of the two attributes you would like to add points to! (Ex. SI or HA) : """)

    # Add points to attributes
    if choice == "HA":
        Agility = Agility + 1
        Health = Health + 1
        Points = Points - 2
    elif choice == "HI":
        Intelligence = Intelligence + 1
        Health = Health + 1
        Points = Points - 2
    elif choice == "HS":
        Health = Health + 1
        Strength = Strength + 1
        Points = Points - 2
    elif choice == "SH":
        Strength = Strength + 1
        Health = Health + 1
        Points = Points - 2
    elif choice == "SA":
        Strength = Strength + 1
        Agility = Agility + 1
        Points = Points - 2
    elif choice == "SI":
        Strength = Strength + 1
        Intelligence = Intelligence + 1
        Points = Points - 2
    elif choice == "AH":
        Agility = Agility + 1
        Health = Health + 1
        Points = Points - 2
    elif choice == "AI":
        Agility = Agility + 1
        Intelligence = Intelligence + 1
        Points = Points - 2
    elif choice == "AS":
        Agility = Agility + 1
        Strength = Strength + 1
        Points = Points - 2
    elif choice == "IH":
        Intelligence = Intelligence + 1
        Health = Health + 1
        Points = Points - 2
    elif choice == "IA":
        Intelligence = Intelligence + 1
        Agility = Agility + 1
        Points = Points - 2
    elif choice == "IS":
        Intelligence = Intelligence + 1
        Strength = Strength + 1
        Points = Points - 2
    time.sleep(2)
    print()
    print(f"Your health is {Health}")
    print(f"Your strength is {Strength}")
    print(f"Your agility is {Agility}")
    print(f"Your Intelligence is {Intelligence}")

    return Health, Strength, Agility, Intelligence

#Combat function
def combat(Health, Ehealth, Pdamage, Edamage, Ename):

    print("You will roll to see who will be attacking first!")
    print()
    time.sleep(2)
    Pdice = dice20()
    print()
    time.sleep(2)
    global Type

    if Pdice >= 13 and Type == "Dagon Warrior" :
        print("You go first!")
        time.sleep(2)
        print()
        if Pdice + Strength > 14:
            print("You swing your trident and slash his chest!")
            Ehealth = Ehealth - Pdamage
            time.sleep(2)
            print()
            print(f"Their remaining health is {Ehealth}")
            time.sleep(2)
            print()
            print("Their turn to swing!")
            Health = Health - Edamage
            print()
            print(f"Your remainnoing health is {Health}")
            time.sleep(2)
            print()
            print("Your turn again! You pierce their stomach!")
            Ehealth = Ehealth - Pdamage
            print()
            print(f"Their remaining health is {Ehealth}")
        elif Pdice + Strength < 12:
            print()
            print("You miss :((. His turn to swing!")
            Health = Health - Edamage

            print(f"Your remaining health is {Health}")

    elif Pdice < 13:

        print("The enemy combatant is attacking first!")
        time.sleep(2)
        print()
        print(f"{Ename} hits you!")
        print()

        Health = Health - Edamage

        print(f"Your remaining health is {Health}")
        time.sleep(2)
        print()
        print("Your turn to swing!")
        Ehealth = Ehealth - Pdamage
        time.sleep(2)
        print()
        print(f"Their remaining health is {Ehealth}")
        time.sleep(2)
        print()
        print("Their swing!")
        Health = Health - Edamage
        time.sleep(2)
        print()
        print(f"Your remaining health is {Health}")

    elif Pdice >= 13 and Type == "Cthulan Occultist" :
        print("You go first!")
        time.sleep(2)
        print()
        if Pdice + Intelligence > 14:
            print("You cast a spell and engulf him in flames!")
            Ehealth = Ehealth - Pdamage
            time.sleep(2)
            print()
            print(f"Their remaining health is {Ehealth}")
            time.sleep(2)
            print()
            print("His turn to swing!")
            Health = Health - Edamage
        elif Pdice + Strength < 12:
            print("You miss :((. His turn to swing!")
            Health = Health - Edamage

            print(f"Your remaining health is {Health}")

    elif Pdice < 13:
        print("The enemy combatant is attacking first!")
        print()
        time.sleep(2)
        print(f"{Ename} hits you!")

        Health = Health - Edamage
        print()
        print(f"Your remaining health is {Health}")
        time.sleep(2)
        print()
        print("Your turn to cast a spell!")
        Ehealth = Ehealth - Pdamage
        time.sleep(2)
        print()
        print(f"Their remaining health is {Ehealth}")
        time.sleep(2)
        print()
        print("Their swing!")
        Health = Health - Edamage
        time.sleep(2)
        print()
        print(f"Your remaining health is {Health}")

    elif Pdice >= 13 and Type == "NightGaunt Archer":
        print("You go first!")
        time.sleep(2)
        print()
        if Pdice + Agility > 14:
            print("You draw your bow and fire arrows at their torso!")
            Ehealth = Ehealth - Pdamage
            time.sleep(2)
            print()
            print(f"Their remaining health is {Ehealth}")
            time.sleep(2)
            print()
            print("Their turn to attack!")
            Health = Health - Edamage

        elif Pdice + Strength <= 12:
            print("You miss :((. His turn to swing!")
            Health = Health - Edamage
 
            print(f"Your remaining health is {Health}")

    elif Pdice < 13:
        print("The enemy combatant is attacking first!")
        time.sleep(2)
        print()
        print(f"{Ename} hits you!")
        print()

        Health = Health - Edamage
        print(f"Your remaining health is {Health}")
        time.sleep(2)
        print()
        print("Your turn to fire your bow!")
        Ehealth = Ehealth - Pdamage
        time.sleep(2)
        print()
        print(f"Their remaining health is {Ehealth}")
        time.sleep(2)
        print()
        print("Their swing!")
        Health = Health - Edamage
        time.sleep(2)
        print()
        print(f"Your remaining health is {Health}")

    if Health < 1:
        global Dead
        Dead = True

    elif Ehealth < 1:
        print(f"YOU WIN THE BATTLE! Congratulations {name}!")

    elif Ehealth > 1 and Health > 1:

        global Continue
        Continue = True

        if Continue == True:
            print()
            time.sleep(2)
            print("KEEP FIGHTING!!!") 
            Ehealth = Ehealth - Pdamage
            print()
            time.sleep(2)
            print(f"Their remaining health is {Ehealth}!")
            print()
            time.sleep(2)
            print("THEY SWING AT YOU!!!!!")
            Health = Health - Edamage
            print()
            time.sleep(2)
            print(f"Your remaining health is {Health}")



    return Health

# First room
def room1():
    time.sleep(1)
    os.system("clear")
    time.sleep(1)
    print("""You are in a dimly lit room entirely made out of silver. The walls are smooth on all sides aside from the four doors around the room and the vines covering them
There are paintings depicting ancient gods on each. One of poseidon, Ceto, Neptune, and Cthulu""")
    time.sleep(2)
    print()
    search = input("""You notice something off about the paintings. Do you wish to examine them? Type 'yes' or 'no' to examine them! : """)

    # Logic to search paintings for mermaid scales
    if search == "yes":
        time.sleep(1)
        print()
        print("You search each painting one by one. You examine the one depicting poseidon last and noticed a hole behind it!")
        time.sleep(2)
        print()
        print("In the hole you find what seem to be scales but not from any ocean creature you've ever seen. You decide to take them with you!")
        global Scales
        Scales = Scales + 1
        print()
        time.sleep(2)
        print("You found some mermaid scales! You may use this to boost you agility for a short time!")
    elif search == "no":
        print()
        time.sleep(1)
        print("You decide its a waste of time since there is probably no point anyway 🤷.")

    print()
    time.sleep(1)
    roommove1 = input("""What room would you like to go to?
Room 2,3,4 or 5: """)

    if roommove1 == "5" and Pressure == False:
        print("Sorry, this room is locked.  You must go through all the other rooms to unlock this one.")
        print()
        room01()

    elif roommove1 == "2":
        print()
        room2()

    elif roommove1 == "3":
        print()
        room3()
    
    elif roommove1 == "4":
        print()
        room4()

    elif Pressure == True and roommove1 == "5":
        print()
        room5()

#Player Creation
def playerCreation():
    global name
    name = input("Please name your character! : ")
    time.sleep(2)
    print()
    global Type
    Type = input("""What Type of class would you like to be? You may choose from the following selection!


       \033[34mCthulan Occultist \033[0m(Boost in intelligence, debuff in health. You start with a staff)
       
       The Cthulan Occultist was born into his religion worshipping the ancient gods Cthulu and Azathoth. Their whole lives revolve around these gods. 

       These are a small group and pretty much shunned from the outside world because of their beliefs and their practice of black magic. They mainly resided in caves close to oceans.   

       \033[32mNightGaunt Archer \033[0m(Boost in agility, debuff in strength. You start with a bow)
        
        These creatures are tall and have very smooth skin, they are born with wings but their wings are pretty much inoperable.

        They worship a god by the name of Nodens and these creatures are not originally from this dimension.

       \033[31mDagon Warrior \033[0m(Boost in strength, debuff in agility.  You start off with a Trident) 

        These creatures are a hostile and ancient race and reside deep in the ocean. They contribute their entire lives to taking back the land and eradicating humans.

        There is a smaller race known as the 'deep ones' that worship these creatures.



        What would you like to choose? : """)
    time.sleep(2)
    os.system("clear")

    # Warrior Class
    if Type == "Dagon Warrior":

        print(f"{name} the {Type}!")
        time.sleep(2)
        print()
        print(f"{Warrior()}")

    # Wizard Class
    elif Type == "Cthulan Occultist":

        print(f"{name} the {Type}!")
        time.sleep(2)
        print()
        print(f"{Wizard()}")


    # Archer Class
    elif Type == "NightGaunt Archer":

        print(f"{name} the {Type}!")
        time.sleep(2)
        print()
        print(f"{Archer()}")
    #If an unavailable input is Typed, it restarts the class selection function
    else:
        print("There is no option for that, please select one of the available classes.")
        time.sleep(3)
        os.system("clear")
        playerCreation()



    new = input("Would you like to create a new character? Please Type yes or no : ")
    if new == "yes":
        os.system("clear")
        playerCreation()
    elif new == "no":
        os.system("clear")
        global isPlaying
        isPlaying = True
        print("\033[33m", "The Five Room Dungeon", "\033[0m")
        print()
        print("Welcome to...", "\033[34m", "Atlantis 🌊", "\033[0m")
        print()
        print("""ZzZzZz...WOAH! Where am I? This is weird...Looks like I'm in a dome...underwater.  There is so many doors 
        but only one is locked.  There is \033[32m vines \033[0m everywhere, looks like I have to be really careful with where I'm stepping.
        *Sniff* *Sniff* Eughhh it \033[32m stinks🤢 \033[0m in here. HELPPP!! \033[33m *5 minutes later⌛* \033[0m 
        Looks like that isn't helping.  Do I have to go through these doors to escape? \033[31m  *ROARRRRRRR* \033[0m 
        WHAT WAS THAT?! Yea...I am not going through those doors.  Is that a sign? I wonder what it says.  
        "Welcome to \033[34m Atlantis🌊.  \033[0m As you can see there are 3 unlocked doors but only one is locked.  
        You have to go through all three doors to unlock the locked door to escape this dome😈"  Looks like I have to go through 
        these doors... 
        """)
        time.sleep(12)

        while isPlaying is True:
            room1()

#Doesn't let you go back to a room if you have already completed it or are currently in that room
def room01():
    print("You're back to room 1")
    roommove1 = input("""What room would you like to go to?
Room 2,3,4 or 5: """)

    if roommove1 == "5" and Pressure == False:
        print("Sorry, this room is locked.  You must go through all the other rooms to unlock this one.")
        print()
        room01()

    elif roommove1 == "2":
        print()

        global Room2C

        #You cannot go back to this room if you are in it or already completed it
        if Room2C > 0:
            print("You cannot go here, you are either already in or have already completed this room")
            time.sleep(1)
            room01()
        elif Room2C < 1:
            room2()


    elif roommove1 == "3":
        print()

        global Room3C

        # You cannot go back to this room if you are in it or already completed it
        if Room3C > 0:
            print("You cannot go here, you are either already in or have already completed this room")
            time.sleep(1)
            room01()
        elif Room3C < 1:
            room3()


    elif roommove1 == "4":
        print()
        # You cannot go back to this room if you are in it or already completed it
        global Room4C

        if Room4C > 0:
            print("You cannot go here, you are either already in or have already completed this room")
            time.sleep(1)
            room01()
        elif Room4C < 1:
            room4()


    elif Pressure == True and roommove1 == "5":
        print()
        room5()



# Second room
def room2():
    time.sleep(1)
    os.system("clear")
    print("You entered a room with a large cliff with vines on the other side that may be covering something useful")
    print()
    cliffJump = input("Would you like to jump over the large cliff? (yes/no) :  ")
    print()
    if cliffJump == "yes" or cliffJump == "Yes":
        print("""The game is going to roll a 20 sided dice for you.  If you get a number higher than 15, you made it over. 
If not, then you are dead...""")
        print()
        time.sleep(3)
        Pdice3 = dice20()

        if Pdice3 + Agility >= 15:
            print()
            print("Congratulations!!! You made it over the cliff and see a chest!.")
            time.sleep(2)
            print("You start seaching through the chest and under all the junk you see something!")
            print()
            time.sleep(2)
            print("You got a fish from the chest!!!")
            global fish
            fish = fish + 1
            print()
            global Room2C
            Room2C = Room2C + 1
            room01()

        else:
            print()
            global Dead
            Dead = True
            print("You have fell:(   RIP☠️😵")
            global isPlaying
            isPlaying = False
            print()
            time.sleep(1)
            playAgain = input("Do you want to play again?")
            if playAgain == "yes" or "Yes":
                time.sleep(1)
                os.system("clear")
                playerCreation()


            elif playAgain == "no" or "No":
                print()
                isPlaying = False

    else:
        print()
        print("Scaredy cat! You went back to room 1.")
        print()
        time.sleep(2)
        print()

        room01()

# Third Room
def room3():
    time.sleep(1)
    os.system("clear")
    print("""You enter the room which is seemingly pitch black. You decide to continue and the room gets lit up by bioluminescent algae
    .
At the other side of the room there stands a man with long dirty blonde hair. He seems to be wearing a suit made of shark scales. In one hand an emerald sword and in the other a chain holding a shark.

You are not aloud to leave until you bypass him, whether through combat or other means. What to you choose to do.""")
    print()
    Fight = input("Would you like to try your hand at combat? Remember, if you have a fish you may use it to feed the shark to avoid combat. 'yes' or 'no' to fight, you may also use the fish if you have it by typing 'use' : ")
    print()
    if Fight == "yes" and Type == "Dagon Warrior":
        combat(Health, 20, Strength, 3, "Aquaman")
        if Dead == True:
            print(f"you died in combat, Game Over! you lost :(")
            time.sleep(1)
            again = input("Would you like to play again? : ")

            if again == "yes":
                time.sleep(1)
                os.system("clear")
                playerCreation()
            elif again == "no":
                os.system("clear")
                print("Okay! Thank you for playing!")
                isPlaying = False
        else:
            os.system("clear")
            print(f"Congratulations {name}, you defeated Aquaman! You won yourself an invisibility potion(Which you found on his body)!")
            global invis
            invis = invis + 1
            global Room3C
            Room3C = Room3C + 1

            room01()
    elif Fight == "yes" and Type == "Cthulan Occultist":

        combat(Health, 20, Intelligence, 5, "Aquaman")
        if Dead == True:
            print(f"you died in combat, Game Over! you lost :(")
            time.sleep(1)
            again = input("Would you like to play again? : ")

            if again == "yes":
                time.sleep(1)
                os.system("clear")
                playerCreation()
            elif again == "no":
                os.system("clear")
                print("Okay! Thank you for playing!")
                isPlaying = False
        else:
            os.system("clear")
            print(f"Congratulations {name}, you defeated Aquaman! You won yourself an invisibility potion(Which you found on his body)!")
            invis = invis + 1
            Room3C = Room3C + 1

            room01()
    elif Fight == "yes" and Type == "NightGaunt Archer":

        combat(Health, 20, Agility, 5, "Aquaman")
        if Dead == True:
            print(f"you died in combat, Game Over! you lost :(")
            time.sleep(1)
            again = input("Would you like to play again? : ")

            if again == "yes":
                time.sleep(1)
                os.system("clear")
                playerCreation()
            elif again == "no":
                os.system("clear")
                print("Okay! Thank you for playing!")
                isPlaying = False
        else:
            os.system("clear")
            print(f"Congratulations {name}, you defeated Aquaman! You won yourself an invisibility potion(Which you found on his body)!")
            invis = invis + 1
            Room3C = Room3C + 1

            room01()

    elif Fight == "use" and fish > 0:
        print("""You give your fish to Aquaman and he takes this as a token of peace!
He gives you an invisibility potion as a token of gratitude!""")
        invis = invis + 1
        Room3C = Room3C + 1
        room01()

    elif Fight == "use" and fish < 1 and Type == "Dagon Warrior":
        print("You dont have an item to give to aquaman and he gets angry at you for teasing him!!")
        combat(Health, 20, Strength, 5, "Aquaman")
        os.system("clear")
        print(f"Congratulations {name}, you defeated Aquaman! You won yourself an invisibility potion(Which you found on his body)!")
        invis = invis + 1
        Room3C = Room3C + 1
        room01()

    elif Fight == "use" and fish < 1 and Type == "Cthulan Occultist":
        print("You dont have an item to give to aquaman and he gets angry at you for teasing him!!")
        combat(Health, 20, Intelligence, 5, "Aquaman")
        os.system("clear")
        print(f"Congratulations {name}, you defeated Aquaman! You won yourself an invisibility potion(Which you found on his body)!")
        invis = invis + 1
        Room3C = Room3C + 1
        room01()

    elif Fight == "use" and fish < 1 and Type == "NightGaunt Archer":
        print("You dont have an item to give to aquaman and he gets angry at you for teasing him!!")
        combat(Health, 20, Agility, 5, "Aquaman")
        os.system("clear")
        print(f"Congratulations {name}, you defeated Aquaman! You won yourself an invisibility potion(Which you found on his body)!")
        invis = invis + 1
        Room3C = Room3C + 1
        room01()


    elif Fight == "no" and Type == "Dagon Warrior":
        print("Unfortunately there is no other way around it, you are forced to fight!")
        time.sleep(1)
        combat(Health, 20, Strength, 5, "Aquaman")
        os.system("clear")
        print(f"Congratulations {name}, you defeated Aquaman! You won yourself an invisibility potion (Which you found on his body)!")
        invis = invis + 1
        Room3C = Room3C + 1
        room01()

    elif Fight == "no" and Type == "Cthulan Occultist":
        print("Unfortunately there is no other way around it, you are forced to fight!")
        time.sleep(1)
        combat(Health, 20, Intelligence, 5, "Aquaman")
        os.system("clear")
        print(f"Congratulations {name}, you defeated Aquaman! You won yourself an invisibility potion (Which you found on his body)!")
        invis = invis + 1
        Room3C = Room3C + 1
        room01()

    elif Fight == "no" and Type == "NightGaunt Archer":
        print("Unfortunately there is no other way around it, you are forced to fight!")
        time.sleep(1)
        combat(Health, 20, Agility, 5, "Aquaman")
        os.system("clear")
        print(f"Congratulations {name}, you defeated Aquaman! You won yourself an invisibility potion (Which you found on his body)!")
        invis = invis + 1
        Room3C = Room3C + 1
        room01()


# room 4
def room4():
    time.sleep(1)
    os.system("clear")
    print("You enter the dim lit room and hear the door slam behind you and squirming above you, its a trap! There are knights of Atlantis throwing tridents at you! Quick make it to the other side or use an item to sneak over!")
    print()
    solution = input("""Would you like to try your luck and sprint across or use and item? Type 'run' to sprint across or 'use' to use an item! 
The items you may use are the invisibility potion or mermaid scales if you have them! : """)
    if solution == "run":
        Pdice2 = dice10()
        global Agility
        if Pdice2 + Agility >= 17:
            print()
            print("You made it across swiftly with no injuries!! You hear a noise sounding like a pressure plate go down. Perhaps a door has been unlocked?")
            global Pressure
            Pressure = True
            print()
            time.sleep(2)
            room01()
            global Room4C
            Room4C = Room4C + 1

        else:
            print()
            print("You got impaled by MANY tridents and you will NOT be living :(")
            global isPlaying
            isPlaying = False
            print()
            time.sleep(1)
            playAgain = input("Do you want to play again? : ")
            if playAgain == "yes" or "Yes":
                time.sleep(1)
                os.system("clear")
                playerCreation()


    global Scales
    if solution == "use" and invis < 1 and Scales < 1:
        print()
        print("Sorry, you don't have any of these items!")
        print()
        time.sleep(1)
        room01()


    elif solution == "use" and invis > 0 and Scales < 1:
        print()
        print("You made it across and pressed the pressure plate with no injuries! The platforms on either side lower and the knights stop throwing their tridents!")
        Pressure = True
        print()
        time.sleep(1)
        Room4C = Room4C + 1
        room01()

    elif solution == "use" and Scales > 0 and invis < 1:
        print("You used your mermaid scales to boost your agility to help you get a bigger chance of making it over! (Your agility was boosted by 3 points)")
        print()
        time.sleep(1)
        Agility = Agility + 2
        Scales = Scales - 1

        Pdice = dice20()

        if Pdice + Agility >= 13:
            print("You made it across swiftly with no injuries!! You hear a noise sounding like a pressure plate go down. Perhaps a door has been unlocked?")
            Pressure = True
            print()
            time.sleep(2)
            room01()
            Room4C = Room4C + 1

        else:
            print()
            print("You got impaled by MANY tridents and you will NOT be living :(")
            isPlaying = False
            print()
            time.sleep(1)
            playAgain = input("Do you want to play again? : ")
            if playAgain == "yes" or "Yes":
                time.sleep(1)
                os.system("clear")
                playerCreation()

    elif solution == "use" and Scales > 1 and invis > 1:
        itemUse = input("You seem to have both items! please select which one you would like to use for this room! Type 'invis' to use the potion and 'scales' to use the scales! : ")

        if itemUse == "invis":
            print()
            print("You made it across and pressed the pressure plate with no injuries! The platforms on either side lower and the knights stop throwing their tridents!")
            Pressure = True
            print()
            time.sleep(1)
            Room4C = Room4C + 1
            room01()

        elif itemUse == "scales":
            print("You used your mermaid scales to boost your agility to help you get a bigger chance of making it over! (Your agility was boosted by 3 points")
            time.sleep(1)
            Agility = Agility + 3

            Pdice2 = dice20()

            if Pdice2 + Agility >= 13:
                print("You made it across swiftly with no injuries!! You hear a noise sounding like a pressure plate go down. Perhaps a door has been unlocked?")
                Pressure = True
                print()
                time.sleep(2)
                room01()
                Room4C = Room4C + 1

# Room 5
def room5():
    time.sleep(1)
    os.system("clear")

    print("You've made it to the last room!!  ")
    print()
    time.sleep(2)
    print(""" You waded through the cool, swirling waters, stepping cautiously into the sunken room of Atlantis. 

    The ruins stretched out in every direction, grand marble columns now fractured and coated in algae, their once-gilded surfaces dull and weathered by centuries beneath the sea.

    Fish darted in and out of shattered archways, their scales flickering like liquid silver in the faint light filtering down from above. 

Towering statues of forgotten gods loomed, their faces half-eroded, as if the very city itself had been consumed by time and the ocean’s wrath.

 The air was thick with the scent of salt and decay, the silence almost suffocating, broken only by the distant rumble of shifting tides.

  Ahead, at the heart of the lost city, a grand temple rose from the water, its gates wide open, as though inviting the challenger within.
  
  A chill ran down the figure’s spine, for they knew that beyond those gates, Poseidon awaited—his voice like thunder beneath the waves, calling them to face the wrath of the deep.
""")
    fightPoseidon = input("Do you want to fight the last boss to escape this dome?(yes/no) : ")
    global isPlaying
    if fightPoseidon == "yes" and Type == "Dagon Warrior":
        EnemyDamage = Edice5()
        print("I hope your ready to fight!")
        combat(Health, 40, Strength, EnemyDamage, "Poseidon")
        if Dead == True:
            print(f"you died in combat, Game Over! you lost :(")
            time.sleep(1)
            again = input("Would you like to play again? : ")

            if again == "yes":
                time.sleep(1)
                os.system("clear")
                playerCreation()
            elif again == "no":
                os.system("clear")
                print("Okay! Thank you for playing!")
                isPlaying = False

        os.system("clear")
        print(f"""YOU DEFEATED POSEIDON! CONGRATULATIONS {name}!
              
you go to his corpse and pick up his almighty trident! You are now the ruler of atlantis!

You were tasked with eradicating Poseidon and did so perfectly. Even though you found the exit you decide to stay down in the depths treating Atlantis as your home.

You are just a pawn in Chthulu's plan and will be used as such, like you have been your entire life. Await your next orders.
""")
        print()
        time.sleep(2)
        print("Thank you for playing our game!")
        time.sleep(2)
        isPlaying = False
        isCreating = False

    elif fightPoseidon == "yes" and Type == "Cthulan Occultist":
        EnemyDamage = Edice5()
        print("I hope your ready to fight!")
        combat(Health, 40, Intelligence, EnemyDamage, "Poseidon")
        if Dead == True:
            print(f"you died in combat, Game Over! you lost :(")
            time.sleep(2)
            again = input("Would you like to play again? : ")

            if again == "yes":
                time.sleep(1)
                os.system("clear")
                playerCreation()
            elif again == "no":
                os.system("clear")
                print("Okay! Thank you for playing!")
                isPlaying = False
        os.system("clear")
        print(f"""YOU DEFEATED POSEIDON! CONGRATULATIONS {name}!
              
you go to his corpse and pick up his almighty trident! You are now the ruler of atlantis!

You were tasked with eradicating Poseidon and did so perfectly. Even though you found the exit you decide to stay down in the depths treating Atlantis as your home.

You are just a pawn in Chthulu's plan and will be used as such, like you have been your entire life. Await your next orders.
""")
        print()
        print("Thank you for playing our game!")
    elif fightPoseidon == "yes" and Type == "NightGaunt Archer":
        print()
        time.sleep(2)
        EnemyDamage = Edice5()
        print()
        print("I hope your ready to fight!")
        combat(Health, 40, Agility, EnemyDamage, "Poseidon")
        os.system("clear")
        print(f"""YOU DEFEATED POSEIDON! CONGRATULATIONS {name}!
              
you go to his corpse and pick up his almighty trident! You are now the ruler of atlantis!

You were tasked with eradicating Poseidon and did so perfectly. Even though you found the exit you decide to stay down in the depths treating Atlantis as your home.

You are just a pawn in Chthulu's plan and will be used as such, like you have been your entire life. Await your next orders.
""")
        print()
        time.sleep(2)
        print("Thank you for playing our game!")
        time.sleep(2)
        isPlaying = False
        isCreating = False

    elif fightPoseidon == "no" and Type == "Dagon Warrior":
        EnemyDamage = Edice5()
        print("Unfortunately that's not an option here, this is the end of the line and you're forced to fight!")
        time.sleep(2)
        os.system("clear")
        combat(Health, 40, Strength, EnemyDamage, "Poseidon")
        if Dead == True:
            print(f"you died in combat, Game Over! you lost :(")
            time.sleep(1)
            again = input("Would you like to play again? : ")

            if again == "yes":
                time.sleep(1)
                os.system("clear")
                playerCreation()
            elif again == "no":
                os.system("clear")
                print("Okay! Thank you for playing!")
                isPlaying = False
                isCreating = False

        os.system("clear")
        print(f"""YOU DEFEATED POSEIDON! CONGRATULATIONS {name}!
              
you go to his corpse and pick up his almighty trident! You are now the ruler of atlantis!

You were tasked with eradicating Poseidon and did so perfectly. Even though you found the exit you decide to stay down in the depths treating Atlantis as your home.

You are just a pawn in Chthulu's plan and will be used as such, like you have been your entire life. Await your next orders.
""")
        print()
        time.sleep(2)
        print("Thank you for playing our game!")
        time.sleep(2)
        isPlaying = False
        isCreating = False

    elif fightPoseidon == "no" and Type == "Cthulan Occultist":
        EnemyDamage = Edice5()
        print("Unfortunately that's not an option here, this is the end of the line and you're forced to fight!")
        time.sleep(2)
        os.system("clear")
        combat(Health, 40, Intelligence, EnemyDamage, "Poseidon")
        if Dead == True:
            print(f"you died in combat, Game Over! you lost :(")
            time.sleep(1)
            again = input("Would you like to play again? : ")

            if again == "yes":
                time.sleep(1)
                os.system("clear")
                playerCreation()
            elif again == "no":
                os.system("clear")
                print("Okay! Thank you for playing!")
                isPlaying = False

        os.system("clear")
        print(f"""YOU DEFEATED POSEIDON! CONGRATULATIONS {name}!
              
you go to his corpse and pick up his almighty trident! You are now the ruler of atlantis!

You were tasked with eradicating Poseidon and did so perfectly. Even though you found the exit you decide to stay down in the depths treating Atlantis as your home.

You are just a pawn in Chthulu's plan and will be used as such, like you have been your entire life. Await your next orders.
""")
        print()
        time.sleep(2)
        print("Thank you for playing our game!")
        time.sleep(2)
        isPlaying = False
        isCreating = False

    elif fightPoseidon == "no" and Type == "NightGaunt Archer":
        EnemyDamage = Edice5()
        print("Unfortunately that's not an option here, this is the end of the line and you're forced to fight!")
        time.sleep(2)
        os.system("clear")
        combat(Health, 40, Agility, EnemyDamage, "Poseidon")
        if Dead == True:
            print(f"you died in combat, Game Over! you lost :(")
            time.sleep(1)
            again = input("Would you like to play again? : ")

            if again == "yes":
                time.sleep(1)
                os.system("clear")
                playerCreation()
            elif again == "no":
                os.system("clear")
                print("Okay! Thank you for playing!")
                isPlaying = False

        os.system("clear")
        print(f"""YOU DEFEATED POSEIDON! CONGRATULATIONS {name}!
              
You go to his corpse and pick up his almighty trident! You are now the ruler of atlantis!

You were tasked with eradicating Poseidon and did so perfectly. Even though you found the exit you decide to stay down in the depths treating Atlantis as your home.

You are just a pawn in Chthulu's plan and will be used as such, like you have been your entire life. Await your next orders.
""")

        print()
        time.sleep(2)
        print("Thank you for playing our game!")
        time.sleep(2)
        isPlaying = False
        isCreating = False




# Character selection
while isCreating is True:
    playerCreation()

# Intro
print("\033[33m", "The Five Room Dungeon", "\033[0m")
print()
print("Welcome to...", "\033[34m", "Atlantis 🌊", "\033[0m")
print()
print("""ZzZzZz...WOAH! Where am I? This is weird...Looks like I'm in a dome...underwater.  There is so many doors 
but only one is locked.  There is \033[32m vines \033[0m everywhere, looks like I have to be really careful with where I'm stepping.
*Sniff* *Sniff* Eughhh it \033[32m stinks🤢 \033[0m in here. HELPPP!! \033[33m *5 minutes later⌛* \033[0m 
Looks like that isn't helping.  Do I have to go through these doors to escape? \033[31m  *ROARRRRRRR* \033[0m 
WHAT WAS THAT?! Yea...I am not going through those doors.  Is that a sign? I wonder what it says.  
"Welcome to \033[34m Atlantis🌊.  \033[0m As you can see there are 3 unlocked doors but only one is locked.  
You have to go through all three doors to unlock the locked door to escape this dome😈"  Looks like I have to go through 
these doors... 
""")
time.sleep(12)

#Starts the game
while isPlaying is True:
    room1()
