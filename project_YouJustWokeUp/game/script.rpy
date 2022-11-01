 # The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define you = Character("You", color="1f1fff")



label start:

    scene bedroomloopone
    with fade

    play music "audio/yjwu_soundtrack.mp3"

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
            scene madebed
            jump loop1menu1
        "Exit room":
            "You leave your bedroom."
            jump hallway1
            
label hallway1:

    scene hallwayloopone
    with fade

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

    scene mirrorloopone
    with fade

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

    scene livingroomloopone
    with fade

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

    scene frontdoorloopone
    with fade

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
            "You head outside."
        

# ////
# END OF LOOP 1
# ////

label bedroom2:   
    scene unmadebed
    with fade

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
            scene madebedtwo
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
    scene hallwaylooptwo
    with fade

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
    scene mirrorlooptwo
    with fade

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
            jump livingroom2

label livingroom2:
    scene livingroomlooptwo
    with fade

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
        "Exit living room"


label frontdoor2:
    scene frontdoorlooptwo
    with fade

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
            "You head outside."

# ////
# END OF LOOP 2
# ////

label bedroom3:
 
    scene bedroomloopthree
    with fade
 
    you "I need to get out of here."
 
    default bedroom_menu3 = set()
 
    menu loop3menu1:
        set bedroom_menu3 #POTENTIAL fuckywucky line
        "Insepct alarm":
            "It's not plugged in. Why did you unplug it?"
            jump loop3menu1
        "Make bed":
            "What's the point?"
            jump loop3menu1
        "Exit room":
            jump hallway3
           
label hallway3:
 
    scene hallwayloopthree
    with fade
 
    you "I need to leave."
 
    default hallway_menu3 = set()
 
    menu loop3menu2:
        set hallway_menu3 #POTENTIAL fuckywucky line
        "Look in the mirror":
            jump mirror3
        "Go to the living room":
            jump livingroom3
 
label mirror3:
 
    scene mirrorloopthree
    with fade
 
    you "It's... me?"
 
    default mirror_menu3 = set()
 
    menu loop3menu3:
        set mirror_menu3
        "Examine reflection":
            "You don't seem yourself, are you feeling ok?"
            jump loop3menu3
        "Stop looking at reflection":
            jump hallway3
 
 
label livingroom3:
 
    scene livingroomloopthree
    with fade
 
    default livingroom_menu3 = set()
 
    menu loop3menu4:
        set livingroom_menu3
        "Look at photos":
            "The photos are empty. Where did they all go?"
            jump loop3menu4
        "Examine plants":
            "They're dead. You killed them."
            jump loop3menu4
        "Look at TV":
            "You feel like you're being watched."
            jump loop3menu4
        "Exit living room":
            jump frontdoor3
 
label frontdoor3:
 
    scene frontdoorloopthreeone
    pause 0.5
    scene frontdoorloopthreetwo
    pause 0.5
    scene frontdoorloopthreeone
    pause 0.5
    scene frontdoorloopthreetwo
    pause 0.5
    scene frontdoorloopthreeone
    pause 0.5
    scene frontdoorloopthreetwo
    pause 0.5
    scene frontdoorloopthreeone
    pause 0.5
    scene frontdoorloopthreetwo
    pause 0.5

    default frontdoor_menu3 = set()
 
    menu loop3menu5:
        set frontdoor_menu3
        "Examine door":
            "You need to leave."
            jump loop3menu5
        "Examine window":
            "There's something out there."
            jump loop3menu5
        "Exit front door":
            "You enter your room."

#////
#END OF LOOP 3
#////

label bedroom4:

    scene bedroomloopfour
    with fade

    default bedroom_menu4 = set()

    menu loop4menu1:
        set bedroom_menu4 #POTENTIAL fuckywucky line
        "Inspect alarm":
            "43:79am"
            jump loop4menu1
        "Make bed":
            "..."
            jump loop4menu1
        "Exit room":
            jump hallway4
            
label hallway4:

    scene hallwayloopfour
    with fade

    default hallway_menu4 = set()

    menu loop4menu2:
        set hallway_menu4 #POTENTIAL fuckywucky line
        "Look in the mirror":
            jump mirror4
        "Go to the living room":
            jump livingroom4

label mirror4:

    scene mirrorloopfour
    with fade

    you "My reflection."

    default mirror_menu4 = set()

    menu loop4menu3:
        set mirror_menu4
        "Look in the mirror":
            "It's you."
            jump loop4menu3
        "Stop looking at reflection":
            jump hallway4


label livingroom4:

    scene livingroomloopfour
    with fade

    default livingroom_menu4 = set()

    menu loop4menu4:
        set livingroom_menu4
        "Look at photos":
            "They're gone."
            jump loop4menu4
        "Examine plants":
            "They're gone."
            jump loop4menu4
        "Look at TV":
            "They're gone."
            jump loop4menu4
        "Exit living room":
            jump frontdoor4

label frontdoor4:

    scene frontdoorloopfour
    with fade

    default frontdoor_menu4 = set()

    menu loop4menu5:
        set frontdoor_menu4
        "Examine door":
            "You need to go outside."
            jump loop4menu5
        "Examine open window":
            "Outside is hell. There's nothing for you there."
            jump loop4menu5
        "Decide":
            jump decision

label decision:

    scene frontdoorloopfour

    default decision_menu1 = set()

    menu loop4menu6:
        set decision_menu1
        "Exit front door":
            jump goodend
            "You exit your front door..."
        "Go back to bed":
            jump badend
            "You retreat to bed..."

label goodend:

    scene goodendbg
    with fade

    "The window showed a hellscape outside, pulsating monsters made of eyes and flesh."
    "These delusions were just that. Delusions. The mind playing tricks on itself."
    "Despite it all, you persevered."
    "You're outside now."
    
return

label badend:

    scene badendbg
    with fade

    "This looping nightmare is eating at your mind."
    "You buckle under the weight of it all and retreat to where you feel some semblance of safety." 
    "Closing the door to your bedroom, you crawl beneath your covers. Perhaps you'll return to try again sometime."

return