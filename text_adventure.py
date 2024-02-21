import time
import sys
from colorama import init
from colorama import Fore, Back, Style

name = "main"
weapon = False


def victory_screen():
    print("")
    print("After defeating the therizinosaurus, no dino in Ark dared mess with " + name)
    time.sleep(3)
    print("")
    print(
        name
        + " decided to stop looking for a way out, they had fallen in love with Ark"
    )
    time.sleep(3)
    print("")
    print(
        "With the bones of their enemies, they constructed a beautiful house for their new life."
    )
    time.sleep(4)
    print("")
    print(name + " lived happily ever after")
    time.sleep(2)
    print("")
    print("Credits: Dan Armstrong")


def quetzal_room():
    print("")
    print(name + " flees in terror and suddenly hears a deafening roar from above!")
    time.sleep(3)
    print("")
    print("It's a Quetzal!  The giant bird is swooping down towards you!")
    time.sleep(2)
    print("")
    print(
        "Without time to think, you leap onto the Quetzals back and away from the jaws of the therizinosaurus!"
    )
    time.sleep(4)
    print("")
    print(
        name
        + " was finally safe, soaring above the skies of Ark, they realized the beauty and began to enjoy it."
    )
    time.sleep(3)
    print("")
    print(
        "However, the relief is short lived as the Quetzal turns over and shakes "
        + name
        + " off!"
    )
    time.sleep(3)
    print("")
    print(
        "With a scream, "
        + name
        + " braced for impact, their world spinning as they tumbled through the air, "
    )
    print(
        "hoping against hope for a miracle to save them from the jaws of certain doom."
    )
    time.sleep(5)
    print("")
    print("A miracle.... did not occur.")
    sys.exit()


def boss_battle():
    directions = ["backward", "flee", "fight"]
    print("")
    print(
        name
        + " leaves Jimmy behind and heads toward a clearing to set up their own camp."
    )
    time.sleep(3)
    print("")
    print("As you begin to settle down for the night, you once again hears the")
    time.sleep(2)
    print("same bone-chilling roar as before.  But this time, closer.")
    time.sleep(2)
    print("")
    print(
        "Out of the woods comes out a therizinosaurus! it's razer sharp claws half the length of your body!"
    )
    time.sleep(3)
    print("")
    print(name + " is close to the woods, they can flee or fight.  What will they do?")
    user_input = ""
    while user_input not in directions:
        print("Options: flee, fight")
        user_input = input()
        if user_input == "fight":
            if weapon:
                print("")
                print(
                    name
                    + "'s heart raced as they faced off with the terrifying therizinosaurus."
                )
                time.sleep(3)
                print("")
                print(
                    "With your rifle and riot shield, you run from tree to tree, shooting and dodging."
                )
                time.sleep(3)
                print("")
                print(
                    "The therizinosaurus swiped at you with all its might and lost its footing!"
                )
                time.sleep(3)
                print("")
                print(
                    name
                    + " realized it's their chance, charged out of woods and was able to take it down!"
                )
                time.sleep(3)
                print("")
                print(name + " triumphantly stands on the therizinosaurus")
                time.sleep(5)
                victory_screen()
            else:
                print("")
                print(
                    name
                    + "'s heart raced as they faced off with the terrifying therizinosaurus."
                )
                time.sleep(3)
                print("")
                print(
                    "With nothing but your fists and courage, you charge the therizinosaurus!"
                )
                time.sleep(2)
                print("")
                print(
                    "The therizinosaurus looks confused as the unarmed, small human charges"
                )
                time.sleep(2)
                print("")
                print(
                    "With an easy stab of a finger, you are impaled, and carried back, alive,"
                )
                print("for the therizinosaurus children to eat")
                time.sleep(3)
            sys.exit()
        elif user_input == "flee":
            quetzal_room()
        else:
            print("Please enter a valid option.")


def open_chest():
    print("")
    print(name + " wearily opens the chest and is shocked by what they see inside!")
    time.sleep(3)
    print("")
    print("Inside the chest is a longneck rifle and a riot shield!")
    time.sleep(2)
    print("")
    print(
        name
        + " is ecstatic at their discovery, knowing they may need these items later."
    )
    time.sleep(2)
    print("You head back to the traveler with your new gear.")
    time.sleep(5)
    meet_traveler()


def weapon_room():
    directions = ["backward", "open"]
    global weapon
    weapon = True
    print("")
    print(name + " decides to go left, towards a friendly looking path.")
    time.sleep(3)
    print("")
    print("Unfortunately, the path ends in a dead end quite quickly.")
    time.sleep(2)
    print("")
    print("however, you see something shimmer in the rocks.")
    time.sleep(2)
    print("")
    print(
        "You have found an eerie looking chest with a human skull and cross bones on top."
    )
    time.sleep(3)
    print("")
    print(name + " feels uneasy about opening the chest.")
    time.sleep(2)
    print("")
    print("Does " + name + " go back to the traveler, or open the chest?")
    user_input = ""
    while user_input not in directions:
        print("Options: backward, open")
        user_input = input()
        if user_input == "backward":
            meet_traveler()
        elif user_input == "open":
            open_chest()
        else:
            print("Please enter a valid option.")


def death_room():
    print("")
    print(
        "Venturing into the well-lit cave, "
        + name
        + "'s curiosity overshadowed their caution."
    )
    time.sleep(3)
    print("")
    print(
        "You step into the cave. "
        + name
        + " feels optimistic they may have found a home for the night!"
    )
    time.sleep(3)
    print("")
    print("As you begin to smile, you notice the human bones in the corner.")
    time.sleep(3)
    print("")
    print("Just then, you are knocked to the ground by the Sarco's powerful jump.")
    time.sleep(2)
    print(name + " is horrified as they realize they are about to be eaten!")
    time.sleep(3)
    print(
        "With a quick snap of the Sarco's powerful jaws, your adventure comes to an end."
    )
    sys.exit()


def warning_room():
    directions = ["backward", "forward"]
    print("")
    print(
        name + " decides to take the travelers advice and take the path to the right."
    )
    print("")
    time.sleep(2)
    print("As you ventures down the path, it slowly turns into a dark, ominous path.")
    print("")
    time.sleep(3)
    print(
        "The dense foliage blocks out the sun and the shadows seem to move in the dim light."
    )
    time.sleep(3)
    print("")
    print(
        "Just as you begins to lose your nerve, you spot a welcoming looking cave filled with light."
    )
    time.sleep(2)
    print("")
    print(
        "But out of the corner of your eye, you see a weathered sign reading 'Do Not Continue'"
    )
    time.sleep(2)
    print("")
    print("Will " + name + " enter the cave? Or head back to the traveler?")
    user_input = ""
    while user_input not in directions:
        print("Options: forward, backward")
        user_input = input()
        if user_input == "backward":
            meet_traveler()
        elif user_input == "forward":
            death_room()
        else:
            print("Please enter a valid option.")


def meet_traveler():
    directions = ["backward", "left", "forward", "right"]
    print("")
    print(
        "After your close call with the silhoutted monster, you stumble upon a fellow travelers camp."
    )
    time.sleep(3)
    print("")
    print("The traveler, Jimmy, welcomes you, but his eyes hold a hint of suspicion.")
    time.sleep(2)
    print("")
    print("'Be careful out there, this land is unforgiving' Jimmy said.")
    time.sleep(2)
    print("")
    print(
        "after sharing information, you ask Jimmy which direction you should travel in."
    )
    print("")
    time.sleep(2)
    print("'Go right, trust me, it's your best chance of survival' Jimmy tells you.")
    print("")
    print(name + " leaves the traveler, unsure if they should trust him.")
    user_input = ""
    while user_input not in directions:
        print("Options: backward, left, forward, right")
        user_input = input()
        if user_input == "backward":
            intro_boss()
        elif user_input == "left":
            weapon_room()
        elif user_input == "forward":
            boss_battle()
        elif user_input == "right":
            warning_room()
        else:
            print("Please enter a valid option.")


def titanboa():
    directions = ["backward", "fight"]
    print("")
    print(
        "Running away from the monstrous silhouette,"
        + name
        + " finds a well used path and takes it."
    )
    print("")
    time.sleep(3)
    print(
        "As you makes your way down the path, you begins to hear a sharp noise near the fallen tree in front of you."
    )
    time.sleep(2)
    print("")
    print(
        "You approach and the tree begins to move!  With a lift of his head, the Titanoboa"
    )
    print("reveals his piercing fangs, as long as your body, with a sharp hiss.")
    print("")
    time.sleep(4)
    print("The Titanoboa coils its body ready to strike.  Will you run or fight?")
    user_input = ""
    while user_input not in directions:
        print("Options: backward, fight")
        user_input = input()
        if user_input == "backward":
            intro_boss()
        elif user_input == "fight":
            print(name + " decides to be brave and take on the Titanoboa!")
            print("")
            print("You lunge at the Titanoboa with nothing but your fists!")
            print("")
            time.sleep(3)
            print(
                "It proves to be a fatal mistake as the Titanoboa strikes before you make your first step."
            )
            print("")
            print(
                "With a fang through your chest, you are easily picked up, and swallowed."
            )
            sys.exit()
        else:
            print("Please enter a valid option.")


def intro_boss():
    directions = ["forward", "backward", "left"]
    print("")
    print(
        "As you venture deeper into the untamed wilderness, you stumble upon a tranquil clearing."
    )
    print("")
    time.sleep(3)
    print(
        name
        + " begins to relax, until the calm is shattered with a bone-chilling roar."
    )
    print("")
    time.sleep(3)
    print(
        "Peering through the dense foliage, you catches a glimpse of a towering silhouette"
    )
    print("")
    print("you can't get a good look, but you see large, razor-sharp claws and run!")
    user_input = ""
    while user_input not in directions:
        print("Options: forward, backward, left")
        user_input = input()
        if user_input == "forward":
            titanboa()
        elif user_input == "backward":
            intro_scene()
        elif user_input == "left":
            meet_traveler()
        else:
            print("Please enter a valid option.")


def intro_scene():
    directions = ["forward"]
    print("")
    print(
        "You awakens to the pecks of Dodo's on a mysterious beach, surrounded by towering cliffs and the sound of crashing waves."
    )
    time.sleep(2)
    print("")
    print("A horrifying realization overcomes you.  You are inside the game, Ark!")
    print("")
    time.sleep(2)
    print(
        "You must navigate this unfamiliar landscape, forging your path amidst towering dinosaurs and unknown dangers."
    )
    print("")
    print(name + ", are you ready to go?")
    userInput = ""
    while userInput not in directions:
        print("Options: forward")
        userInput = input()
        if userInput == "forward":
            intro_boss()
        else:
            print("Please enter a valid direction")


if name == "main":
    while True:
        print("")
        print("Embark on this epic journey through the wild and untamed world of Ark")
        print("Where survival is key and danger lurks around every corner.")
        time.sleep(3)
        print("")
        print(
            "Make decision as you navigate through towering forests, treacherous mountains,"
        )
        print("and encounters creatures both fierce and majestic.")
        time.sleep(4)
        print("")
        print(
            "Will you conquer the challenges that await you and emerge victorious in this thrilling adventure?"
        )
        time.sleep(3)
        print("")
        print("You can choose to walk in multiple directions to find your way.")
        print("")
        print("Before we get started, what is your name?")
        name = input()
        print("Hello " + name + ", goodluck on your adventure!")
        print("")
        print("")
        intro_scene()
