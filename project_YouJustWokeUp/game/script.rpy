 # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You", color="1f1fff")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room


    # These display lines of dialogue.

    "Player wakes up in their room to the sound of an alarm."

    you "Ugh, I need to get up..."

    default bedroom_menu1 = set()

    menu firstmenu1:
        set bedroom_menu1 #POTENTIAL fuckywucky line
        "Turn off alarm":
            "You reach over and smack the alarm a few times until it stops beeping."
            jump firstmenu1
        "Make bed":
            "You haphazardly pull your sheets up until they're somewhat neat."
            jump firstmenu1
        "Exit room":
            "You leave your bedroom."
            jump hallway1
            
label hallway1:

    "You exit out into the hallway."

    you "I need to go outside today."

    default hallway_menu1 = set()

    menu secondmenu1:
        set hallway_menu1
        "Look in the mirror":
            jump mirror1
        "Go to the living room":
            "You walk into your living room."
            jump livingroom1

label mirror1:

    you "My reflection."

    default mirror_menu1 = set()

    menu thirdmenu1:
        set mirror_menu1
        "Examine reflection":
            "Your reflection. You seem tired. You should head to bed early tonight."
            jump thirdmenu1
        "Stop looking at reflection":
            jump hallway1


label livingroom1:

    default livingroom_menu1 = set()

    menu fourthmenu1:
        set livingroom_menu1
        "Look at photos":
            "Your friends and familt. You haven't spoken to them in a while."
            jump fourthmenu1
        "Examine plants":
            "Potted plants. They're starting to wilt. You should water them later."
            "You need to go outside now though."
            jump fourthmenu1
        "Look at TV":
            "Nothing interesting playing."
            jump fourthmenu1
        "Exit living room":
            jump frontdoor1

label frontdoor1:
    "You enter your front foyer."
    default frontdoor_menu1 = set()

    menu fifthmenu1:
        set frontdoor_menu1
        "Grab shoes":
            "You grab your blue sneakers."
            jump fifthmenu1
        "Examine door":
            "Your front door. It seems like a nice day outside. You should go outside."
            jump fifthmenu1
        "Examine window":
            "A window. You should go outside."
            jump fifthmenu1
        "Exit front door":
            "First loop ended."
    # This ends the game.

return
