# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room


    # These display lines of dialogue.

    "Time - 10:30am"

    you "Ugh, I need to get up..."

    menu:
        "Stay in Bed":
            you "Nah I'll stay in bed..."
        "Stay in Bed":
            you "Nah I'll stay in bed..."
        "Get out":
            you "..."
            you "Nahhh"
    menu:
        "Stay in Bed":
            you "Yeah I'll stay in bed..."
        "Stay in Bed":
            you "Yeah I'll stay in bed..."
        "Get out":
            you "No! I don't want to."    
    menu:
        "Stay in Bed":
            you "Yeah I'll stay in bed..."
            "..."
            you "okay I'll hop out I guess..."
            jump outOfBedNEU
        "Stay in Bed":
            you "Yeah I'll stay in bed..."
            "..."
            you "okay I'll hop out I guess..."
            jump outOfBedNEU
        "Get out":
            you "..."
            you "Nope"        
    menu:
        "GET OUT!":
            you "OKAY!!! GOD... I'll get up"
            you "sheeeesh"
            jump outOfBedNEG

label outOfBedNEU:

    "You are now out of bed"
    "..."
    "..."
    "man yesterday was kinda shit..."
    jump bedroom0

label outOfBedNEG:
    
    "You are out of bed... (finally)"
    you "CHRIST NOT YOU TOO, SHUT UP FOR ONCE IN A WHILE"
    "..."
    "..."
    "..."
    you "I hated yesterday, fuck them," 
    you "sigh*"
    jump bedroom0

label bedroom0:

    $ topics = ['Make Bed, Set Alarm, Put Shoes Away']

    menu:
        "Make Bed" if "Make Bed" in topics:

            "You make your bed, its a bit of a struggle."
            you "at least it's done now."
            jump bedroom0

        "Set Alarm" if "Set Alarm" in topics:
            you "uhmmm, 8:45 should do"
            jump bedroom0

        "Put Shoes Away" if "Put Shoes Away" in topics:
            you "they caaan goooooooo"
            you "over here"
            jump bedroom0







    # This ends the game.

    return
