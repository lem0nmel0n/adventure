import time
def main(): #this is the ending if you lose the connect 4 game.
    print("""
you try to forget about failure. disappointment. defeat.

you brush your teeth one last time,
and collapse face-first into bed.

you have raging nightmares,
about connect4 games and villains hiding in your laundry.

[ NEXT MORNING ]

you hear people yelling in your room.
wake up? (yes/no)""")

    answer = input("> ")
    count = 0
    while answer[0] != "y": #asks you to wake up if you say no
        print("you probably should wake up.")
        count += 1
        print()
        answer = input("> ")

    print("""
you sit up.

...

there are handcuffs on your wrists.
""")
    time.sleep(4) #waits for 4 seconds
    
    print("\033[F\033[K", end="") #deletes previous line

    print("""[ FRONT OF HOUSE ]  

you are hauled off by police. 
your roommate looks helplessly. they can't pay the rent by themselves.

“you’re under arrest for:  
- harboring a known villain,  
- miserably failing at board games to the detriment of humanity,  
- and allowing the global takeover of civilization,”  
a policeman says, lifting you into their vehicle.

dexter stinkman wins. the world is falling apart.
you're in handcuffs. your roommate is sobbing on the sidewalk.

it's cruel. it's unjust. it sucks.
you *tried*. but this time, it wasn't enough.

you nailed it, hero.""")
