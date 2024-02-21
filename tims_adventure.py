import time
import sys
from colorama import init
from colorama import Fore, Back, Style

name = "main"
weapon = False


def victory_screen():
    print("")
    print("After defeating the therizinosaurus, no dino in Ark dared mess with Tim")
    time.sleep(3)
    print("")
    print("Tim decided to stop looking for a way out, he had fallen in love with Ark")
    time.sleep(3)
    print("")
    print("With the bones of his enemies, he constructed a compound for his new life.")
    time.sleep(4)
    print("")
    print("Tim lived happily ever after, with his new Sarco wife")
    time.sleep(2)
    print("")
    print("Credits: Dan.  ish-credits: Tim, Jimmy")


def quetzal_room():
    print("")
    print("Tim flees in terror and suddenly hears a deafening roar from above!")
    time.sleep(3)
    print("")
    print("It's a Quetzal!  The giant bird is swooping down towards Tim!")
    time.sleep(2)
    print("")
    print(
        "Without time to think, Tim leaps onto the Quetzals back and away from the jaws of the therizinosaurus"
    )
    time.sleep(4)
    print("")
    print(
        "Tim was finally safe, soaring above the skies of Ark, he realises the beauty and begins to enjoy it."
    )
    time.sleep(3)
    print("")
    print(
        "However, his relief is short lived as the Quetzal turns over and shakes Tim off!"
    )
    time.sleep(3)
    print("")
    print(
        "With a scream, Tim braced for impact, his world spinning as he tumbled through the air, "
    )
    print(
        "hoping against hope for a miracle to save him from the jaws of certain doom."
    )
    time.sleep(5)
    print("")
    print("A miracle.... did not occur.")
    sys.exit()


def boss_battle():
    directions = ["backward", "flee", "fight"]
    print("")
    print("Tim leaves Jimmy behind and heads toward a clearing to set up his own camp.")
    time.sleep(3)
    print("")
    print("As he begins to settle down for the night, he once again hears the")
    time.sleep(2)
    print("same bone-chilling roar as before.  But this time, closer.")
    time.sleep(2)
    print("")
    print(
        "Out of the woods comes out a therizinosaurus! it's razer sharp claws half the length of Tim himself."
    )
    time.sleep(3)
    print("")
    print("Tim is close to the woods, he can flee or fight.  What will you do?")
    user_input = ""
    while user_input not in directions:
        print("Options: flee, fight")
        user_input = input()
        if user_input == "fight":
            if weapon:
                print("")
                print(
                    "Tim's heart raced as he faced off with the terrifying therizinosaurus."
                )
                time.sleep(3)
                print("")
                print(
                    "With his rifle and riot shield, Tim ran from tree to tree, shooting and dodging."
                )
                time.sleep(3)
                print("")
                print(
                    "The therizinosaurus swiped at Tim with all his might and lost his footing!"
                )
                time.sleep(3)
                print("")
                print(
                    "Tim realized his chance, charged out of woods and put a bullet between its eyes."
                )
                time.sleep(3)
                print("")
                print(
                    "Tim triumphly stood on the head of the therizinosaurus and spit in its mouth for good measure."
                )
                time.sleep(5)
                victory_screen()
            else:
                print("")
                print(
                    "Tim's heart raced as he faced off with the terrifying therizinosaurus."
                )
                time.sleep(3)
                print("")
                print(
                    "With nothing but his fists and courage, Tim charges the therizinosaurus!"
                )
                time.sleep(2)
                print("")
                print("The therizinosaurus looks confused as the unarmed man charges")
                time.sleep(2)
                print("")
                print(
                    "With an easy stab of a finger, Tim is impaled, and carried back, alive,"
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
    print("Tim wearily opens the chest and is shocked by what he sees inside.")
    time.sleep(3)
    print("")
    print("Inside the chest is a longneck rifle and a riot shield!")
    time.sleep(2)
    print("")
    print("Tim is ecstatic at his discover, knowing he may need these items later.")
    time.sleep(2)
    print("He heads back to the traveler with his new gear.")
    time.sleep(5)
    meet_traveler()


def weapon_room():
    directions = ["backward", "open"]
    global weapon
    weapon = True
    print("")
    print("Tim decides to go left towards a friendly looking path.")
    time.sleep(3)
    print("")
    print("Unfortunately, the path ends in a dead end quite quickly.")
    time.sleep(2)
    print("")
    print("however, Tim see's something shimmer in the rocks.")
    time.sleep(2)
    print("")
    print(
        "Tim has found an eerie looking chest with a human skull and cross bones on top."
    )
    time.sleep(3)
    print("")
    print("Tim is uneasy about opening the chest.")
    time.sleep(2)
    print("")
    print("Does Tim go back to the traveler, or open the chest?")
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
    print("Venturing into the well-lit cave, Tim's curiosity overshadowed his caution.")
    time.sleep(3)
    print("")
    print(
        "He steps into the cave, Tim feels optimistic he may have found a home for the night!"
    )
    time.sleep(3)
    print("")
    print("As Tim begins to smile, he notices the human bones in the corner.")
    time.sleep(3)
    print("")
    print("Just then, he is knocked to the ground by the Sarco's powerful jump.")
    time.sleep(2)
    print("Tim is horrified as he realizes he is about to be eaten!")
    time.sleep(3)
    print("")
    print(
        "To Tim's shock and horror, the Sarco does not eat him, he instead removes Tim's pants!"
    )
    time.sleep(4)
    print("")
    print(
        "The sarco lets out a satisfied moan while Tim lets out an ear piercing screech as the Sarco enters."
    )
    time.sleep(3)
    print("")
    print(
        "Hours later, as Tim lies on the cold floor of the cave, anally bleeding to death,"
    )
    time.sleep(3)
    print("he can't help but think back on his screech.")
    print("")
    time.sleep(5)
    print(
        "Tim dies alone, having been savaged.  But mostly, he regrets his girly scream."
    )
    sys.exit()


def warning_room():
    directions = ["backward", "forward"]
    print("")
    print("Tim decides to take the travelers advice and takes the path to the right.")
    print("")
    time.sleep(2)
    print("As he ventures down the path, it slowly turns into a dark, ominous path.")
    print("")
    time.sleep(3)
    print(
        "The dense foliage blocks out the sun and the shadows seem to move in the dim light."
    )
    time.sleep(3)
    print("")
    print(
        "Just as Tim begins to lose his nerve, he spots a welcoming looking cave filled with light."
    )
    time.sleep(2)
    print("")
    print(
        "But out of the corner of his eye, Tim see's a weathered sign reading 'Do Not Continue'"
    )
    time.sleep(2)
    print("")
    print("Will Tim enter the cave? Or head back to the traveler?")
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
        "After Tim's close call with the silhoutted monster, he stumbles upon a fellow travelers camp."
    )
    time.sleep(3)
    print("")
    print("The traveler, Jimmy, welcomes Tim, but his eyes hold a hint of suspicion.")
    time.sleep(2)
    print("")
    print("'Be careful out there, this land is unforgiving' Jimmy said.")
    time.sleep(2)
    print("")
    print(
        "after sharing information, Tim asks Jimmy which direction he should travel in."
    )
    print("")
    time.sleep(2)
    print("'Go right, trust me, it's your best chance of survival' Jimmy tells Tim.")
    print("")
    print("Tim leaves the traveler, unsure if he should trust him.")
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
        "Running away from the monstrous silhouette, Tim finds a well used path and takes it."
    )
    print("")
    time.sleep(3)
    print(
        "As Tim makes his way down the path, he begins to hear a sharp noise near the fallen tree in front of him."
    )
    time.sleep(2)
    print("")
    print(
        "Tim approaches and the tree begins to move!  With a lift of his head, the Titanoboa"
    )
    print("reveals his piercing fangs, as long as Tim's body, with a sharp hiss.")
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
            print("Tim decides to be brave and take on the Titanoboa!")
            print("Tim lunges at the Titanoboa with nothing but his fists!")
            print(
                "It proves to be a fatal mistake as the Titanoboa strikes before Tim makes his first step."
            )
            print(
                "With a fang through his chest, Tim is easily picked up, and swallowed."
            )
            sys.exit()
        else:
            print("Please enter a valid option.")


def intro_boss():
    directions = ["forward", "backward", "left"]
    print("")
    print(
        "As Tim ventures deeper into the untamed wilderness, he stumbles upon a tranquil clearing."
    )
    print("")
    time.sleep(3)
    print("Tim begins to relax, until the calm is shattered with a bone-chilling roar.")
    print("")
    time.sleep(3)
    print(
        "Peering through the dense foliage, Tim catches a glimpse of a towering silhouette"
    )
    print("")
    print("Tim can't get a good look, but he see's large, razor-sharp claws and runs!")
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
        "Tim awakens to the pecks of Dodo's on a mysterious beach, surrounded by towering cliffs and the sound of crashing waves."
    )
    time.sleep(2)
    print("")
    print(
        "A horrifying realization overcomes Tim.  He is inside his most hated game, Ark!"
    )
    print("")
    time.sleep(2)
    print(
        "he must navigate this unfamiliar landscape, forging his path amidst towering dinosaurs and unknown dangers, with your help."
    )
    print("")
    print("Tim is ready to go, will you continue on or head back?")
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
        print("Embark on Tim's epic journey through the wild and untamed world of Ark")
        print("Where survival is key and danger lurks around every corner.")
        time.sleep(3)
        print("")
        print(
            "Join him as he navigates through towering forests, treacherous mountains,"
        )
        print("and encounters creatures both fierce and majestic.")
        time.sleep(4)
        print("")
        print(
            "Will Tim conquer the challenges that await him and emerge victorious in this thrilling adventure?"
        )
        time.sleep(3)
        print("")
        print(
            "You will control Tim and can choose to walk in multiple directions to find your way."
        )
        print("")
        print("Before we get started, what is your name?")
        name = input()
        print("Hello " + name + "! your name is now Tim! Goodluck Tim!")
        print("")
        print("")
        intro_scene()
