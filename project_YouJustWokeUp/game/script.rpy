 # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You", color="1f1fff")


# The game starts here.

label start:

    scene bg room

    # These display lines of dialogue.

    "Player wakes up in their room to the sound of an alarm."

    you "Ugh, I need to get up..."

    default bedroom_menu1 = set()

    menu loop1menu1:
        set bedroom_menu1 #POTENTIAL fuckywucky line
        "Turn off alarm":
            "You reach over and smack the alarm a few times until it stops beeping."
            jump loop1menu1
        "Make bed":
            "You haphazardly pull your sheets up until they're somewhat neat."
            jump loop1menu1
        "Exit room":
            "You leave your bedroom."
            jump hallway1
            
label hallway1:

    "You exit out into the hallway."

    you "I need to go outside today."

    default hallway_menu1 = set()

    menu loop1menu2:
        set hallway_menu1 #POTENTIAL fuckywucky line
        "Look in the mirror":
            jump mirror1
        "Go to the living room":
            "You walk into your living room."
            jump livingroom1

label mirror1:

    you "My reflection."

    default mirror_menu1 = set()

    menu loop1menu3:
        set mirror_menu1
        "Examine reflection":
            "Your reflection. You seem tired. You should head to bed early tonight."
            jump loop1menu3
        "Stop looking at reflection":
            jump hallway1


label livingroom1:

    default livingroom_menu1 = set()

    menu loop1menu4:
        set livingroom_menu1
        "Look at photos":
            "Your friends and familt. You haven't spoken to them in a while."
            jump loop1menu4
        "Examine plants":
            "Potted plants. They're starting to wilt. You should water them later."
            "You need to go outside now though."
            jump loop1menu4
        "Look at TV":
            "Nothing interesting playing."
            jump loop1menu4
        "Exit living room":
            jump frontdoor1

label frontdoor1:
    "You enter your front foyer."
    default frontdoor_menu1 = set()

    menu loop1menu5:
        set frontdoor_menu1
        "Grab shoes":
            "You grab your blue sneakers."
            jump loop1menu5
        "Examine door":
            "Your front door. It seems like a nice day outside. You should go outside."
            jump loop1menu5
        "Examine window":
            "A window. You should go outside."
            jump loop1menu5
        "Exit front door":
            "First loop ended."

label bedroom2:   
    scene bg room

    you "Wait... huh??"

    "You find yourself in the your bedroom again, wait..."

    you "I swear I just exited outside"
    you "..."
    you "Something feels off.."
    "I'm not to sure about this either"

    default bedroom_menu2 = set()

    menu loop2menu1:
        set bedroom_menu2 #POTENTIAL fuckywucky line
        "Turn off alarm":
            "You notice the alarm, its sound much worser than it did before"
            you "I turned this off and reseted it, I swear"
            "..."
            you "Did I?"
            jump loop2menu1
        "Make bed":
            "Your bed was made, not anymore apparently"
            you "uggggggh you're joking, huuuuu fine I'll make it again"
            "And so you make it again, don't understand why, it was made before"
            you "and your not helping brain, so shush"
            "..."
            jump loop2menu1
        "Exit room":
            "You leave your bedroom."
            "again"
            jump hallway2

label hallway2:

    "You exit out into the hallway."

    you "Hmmm... something doesn't feel right indeed"

    "Darting around the room, you feel like you're in a cage, looking for a way out"

    default hallway_menu2 = set()

    menu loop2menu2:
        set hallway_menu2
        "Look in the mirror":
            jump mirror2
        "Go to the living room":
            "You walk into your living room."
            jump livingroom2

label mirror2:

    you "My reflection..."
    you "It looks a bit off"
    "Maybe... I..."

    default mirror_menu2 = set()

    menu loop2menu3:
        set mirror_menu2 #POTENTIAL fuckywucky line
        "Examine reflection":
            "Your reflection. It seems fine at first but you notice."
            you "its more distorted?, I'm confused"
            "..."
            jump loop2menu3
        "Stop looking at reflection":
            jump hallway1

label livingroom2:

    default livingroom_menu2 = set()

    menu loop2menu4:
        set livingroom_menu2
        "Look at photos":
            you "I... why, the photos"
            "you look at the photos, slightly distorted, not enough for anyone else to notice"
            "But for you it's immediate"
            jump loop2menu4
        "Examine plants":
            "One of the leaves is darker than the rest"
            you "I gave them water, I do remember that!"
            you "Ain't lookin to good on the leaves either"
            you "I've got to get out of here"
            jump loop2menu4
        "Look at TV2":
            "Nothing interesting playing"
            you "Wait, what was that?!,"
            you "..."
            "..."
            you " I swear I saw something on the tv"
            "Stop scaring yourself, your acting stupid"
            you "Wow, okay did not need that remark"
            "..."
            "Did you?"
            "..."
            you "uh..."
            jump loop2menu4
        "Exit living room":


label frontdoor2:
    "You enter your front foyer. Yet like everything, it feels off"
    default frontdoor_menu2 = set()

    menu loop2menu5:
        set frontdoor_menu2
        "Grab shoes":
            "You grab your blu..."
            you "Theres a tear in one shoe..."
            "..."
            "..."
            you "...I liked them..."
            "...I"
            "You put the shoes back"
            you "not feeling great rn"
            jump loop2menu5
        "Examine door":
            you "Door looks even more beaten up "
            jump loop2menu5
        "Examine window":
            "It seems darker than before, maybe go investigate."
            jump loop2menu5
        "Exit front door":
            "Second loop ended."
return