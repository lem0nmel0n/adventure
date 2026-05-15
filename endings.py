from connect4 import program, board, game
import time
import os
import win, lose, tie

print("\033[1;34m")

def announce_event(title):
	print(f">>{title.upper()}<<")
def scene_header(room):
	print(f"==={room.upper()}===")
	print()
def actionify(action):
	print(f"[ {action.upper()} ]")
	print()
def goto_bedroom(): #asks you to go to your bedroom
	print("go to bedroom? (yes/no) ")
	bed = input("> ").lower()
	print()
	while "y" not in bed:
		print("come on dude, don't be stubborn.")
		print("go to bedroom? (yes/no) ")
		bed = input("> ").lower()
		print()
def clear(): #clears the screen
	if os.name == 'nt':
		board = os.system('cls')
	else:
		board = os.system('clear')

def main():
	clear()
	scene_header("LAUNDRY ROOM")
	print("""you are in the laundry. the laundry basket is overflowing and there are socks all over the place. your special striped ones are in the corner.

a figure emerges from behind the laundry basket. 
you instantly recognise his odd, villainous smile.
it's dexter stinkman, eager to put his plans for world-domination into motion.

he pulls out a connect 4 board, before placing it between the two of you.
""")

	announce_event("battle start")
	print()
	
	print("dexter stinkman challenges you!")
	print("are you ready? (yes/no) ")
	ready = input("> ").lower()
	while not ready.startswith("y"):
		print()
		print("fine, we'll wait.")
		print("are you ready yet? (yes/no) ")
		ready = input("> ").lower()
		

	result = program.run() #runs the connect 4 program
	time.sleep(1)
	
	clear()

	#result = "win" #i use this for testing the different endings

	if result == "win": #you win
		actionify("victory")
		time.sleep(1)
		print("after vanquishing arch-nemesis dexter stinkman at a gruelling game of connect 4, the world was finally safe. he retreated into the shadows, distraught at even the *thought* of defeat.")
		print()
		goto_bedroom()

	elif result == "tie": #you tied
		actionify("tie")
		time.sleep(1)
		print("looks like you tied with dexter. chose your next move wisely.")
		print("[1] punch him")
		print("[2] become best friends")
		print("[3] scream")
		next_move = input("\n> ").lower()
		print()
		while next_move not in "123":
			print("invalid answer. try again dude.")
			next_move = input("> ").lower()
			print()
		if next_move == "1": #you punch dexter stinkman
			actionify("punch")
			print("you stare at the villain. he stares back.\n")
			print("your knuckles protrude from your clenched fist before you swing at him.")
			print("somehow, dexter manages to get hit by the sloppy punch.")
			print("he slips on your lucky socks before tumbling out the window!")
			print()
			print("he lands in a bush with a hard thump, completely stuck.")
			print()
		elif next_move == "2": #you try to befriend stinkman
			actionify("attempt to become friends")
			print("in case you didn't notice, dexter is a lonely, non-showering, villain who hates people. he escapes through the window while you cry about not having friends.")
			print()
			print("that was never gonna work out, man.")
		elif next_move == "3": #you scream [with catastrophic consequences]
			actionify("scream")
			print("your throat is on fire as you scream.\n")
			print('"SHUT IT!!" he screams back. ')
			print("you see him panicking and picking up a conveniently placed baseball bat. ")
			print("\n...\n")
			print('you are suddenly and violently dead.')
			print("someone should have warned you about that.")
			print()
			quit()
		print("---")
		print()
		print("maybe just try to sleep off the disappointment.")
		goto_bedroom()

	else: #you lost
		actionify("defeat") 
		time.sleep(1)
		print("YOU LOST.")
		print("your connect 4 tutor sighs disappointedly through the window. \nyou can't believe it.")
		print("you lost. badly.")
		print()
		print("before you could even process your defeat, he vanished into the shadows, cackling. his plans for world domination are already in motion. ")
		print("and it's all. your. fault.")
		print()
		print("---")
		print()
		print("oh well. you're tired.")
		goto_bedroom()

	clear()
	print()
	#this code block calls the main functions of the win, lose and tie programs
	announce_event("ending")
	if result == "win":
		win.main()
	elif result == "tie":
		tie.main(next_move)
	else:
		lose.main()
