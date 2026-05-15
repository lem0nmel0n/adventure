def main():
    print("""
your heroic duties are complete.
the world is safe, dexter stinkman is defeated,
and your roommate is still snoring.

you brush your teeth one last time (cause why not???),
collapse face-first into bed, and dream about free pizza.

[ NEXT MORNING ]

you hear a knocking at the front door.

[1] answer it civilly
[2] kick the door down
[3] don't open it.
""")
    answer = input("> ").strip()
    
    while answer not in "123": #if the answer isnt 1, 2 or 3, its invalid.
        print("invalid answer. try again.")
        print()
        answer = input("> ").strip()
        

    if answer == "1": #answering the door civilly ending
        print("""
you politely open the front door  
and are immediately blinded by flashing lights and cameras.  

The Chairman of the World Nobel Committee proudly hands you a certificate  
and a shiny gold coin-sized thing with a person's face on it.

"congratulations," he says, tears in his eyes,  
"for saving civilization armed only with a toothbrush,  
we present you with the **NOBEL PEACE PRIZE**."

you raise it high. somewhere, dexter stinkman is crying into a pillow.  
somewhere else, your roommate is finally doing the grocery shopping.

you’ve done it, hero. against all odds,  
you really, *really* did the bare minimum.
""")
    
    elif answer == "2": #kicking the door down ending
        print("""
you kick the door down,
and are immediately blinded by flashing lights and cameras.

you see The Chairman of the World Nobel Committee at your door, 
who takes a small, startled step back.
he's awkwardly holding a shiny gold coin-sized thing with a person's face on it.

"uh.. did we get the wrong house?" he asks, turning to face the 20 people behind him.

you clearly didn't make a good first impression.
they quickly scurry away. 

you spend your afternoon fixing the door. 
you may not have gotten the nobel peace prize, 
but deep down, we both know you saved the world.

you've done it, hero. against all the odds.
the world may not cheer your name, but i know i will.
""")
    elif answer == "3": #not answering the door ending
        print("""
you stare at the door.  
the knocking gets louder. the cameras flash through the windows.  
but you’re tired. you’ve had a long day.  

you crawl back into bed and pull the blanket over your head.  

the Chairman of the World Nobel Committee waits outside for a while.  
eventually, he sighs, shrugs, and leaves.  
the crowd gradually disappears. the flashing stops. the world moves on.

you dream of free pizza. of victory. of a full fridge.

you’ve done it, hero. not loudly. not gloriously.  
but you still saved the day.
""")



