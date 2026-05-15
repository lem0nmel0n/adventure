import time
def main(next_move):
    if next_move == "1": #this is the "punching dexter if you tie" ending
        print("""
you wonder if you failed. if being tied was the same as losing.

you brush your teeth one last time,
and collapse face-first into bed.

you dream about winning. about villains flailing in bushes.
about finishing that comic you started. 

[ NEXT MORNING ]

you hear sirens outside. 

your heroic duties are...complete, i guess.
the world is safe, dexter stinkman is stuck in a bush, 
and your roommate is eating breakfast.

outside, the police untangle and arrest a very embarassed villain.

you did it, hero. you may be a mediocre connect 4 opponent,
but the world isn't destroyed. and that's all that matters.
""")

    if next_move == "2": #this is the "trying to befriend dexter" ending. it is pretty similar to the losing ending.
        print("""
you try to forget about rejection. being friendless. failure.

you brush your teeth one last time,
and collapse face-first into bed.

you have raging nightmares,
about full connect4 boards and people not liking you.

[ NEXT MORNING ]

you hear people yelling in your room.
wake up? (yes/no)""")

    answer = input("> ")
    count = 0
    while answer[0] != "y": #if you say no, it just keeps asking you to wake up.
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
    input("enter to continue..")
    
    print("\033[F\033[K", end="") # clears the last line

    print("""[ FRONT OF HOUSE ]  

you are hauled off by police. 
your roommate looks helplessly. they can't pay the rent by themselves.

“you’re under arrest for:  
- harboring a known villain,  
- trying to befriend a known villain,  
- and allowing the global takeover of civilization,”  
a policeman says, lifting you into their vehicle.

for dexter stinkman, being tied was as good as winning. 
the world is falling apart.
you're in handcuffs. your roommate is sobbing on the sidewalk.

it's cruel. it's unjust. it sucks.
you *tried*. but this time, it wasn't enough.

you nailed it, hero.""")