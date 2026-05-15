import endings

VOWELS = ["a", "o", "u", "e", "i"]

#a list of possible actions
#for example you can say collect or grab and the game will interpret it as if you said "take"

ACTIONS = {
    "take":
    ["pick", "take", "grab", "collect", "snatch", "steal", "swipe", "get"],
    "move": ["move", "go", "walk", "run"],
    "eat": ["chomp", "eat", "consume", "devour", "ingest"],
    "read": ["read", "see"],
    "open": ["open"],
    "look": ["look", "look around"],
    "import": ["from __fridge__ import breakfast"],
    "explode": ["explode", "kaboom", "bomb"],
    "exit": ["exit", "quit", "leave"],
    "tasks": ["task", "tasks"],
    "inventory": ["inventory"],
    "help": ["help", "assistance"],
    "brush": ["brush", "clean"]
}

#tasks you gotta complete
tasks = {
    "breakfast": False,
    "brushed teeth": False,
}
#random bits i need for the game. for example i need to check if the fridge exploded or if the player has the key
game_state = {
    "fridge_open": False,
    "exploded": False,
    "has_key": False,
    "safe_open": False,
    "safe_note": False,
}


def intro():  #this is how i introduce the game to the player :]
	print("""welcome to your house.
your roommate was meant to save the world, but they slept in. 
guess who’s in charge now?

complete your tasks, explore the chaos, and get out in time to stop the villain.

(psst.. down here. use "help" for a list of commands. you might need it)""")


#OK SO THESE ARE FOR SCENE HEADERS. THE ANNOUNCE EVENT ONLY HAPPENS ONCE DURING THE FINAL BATTLE
#THE SCENE HEADER APPEARS WHEN YOU ENTER A ROOM
#AND THE ACTIONIFY ONE [terrible naming btw] IS FOR EVERYTHING ELSE [for example you finished a task]


def announce_event(title):
	print(f">>{title.upper()}<<")
	print()


def scene_header(room):
	print(f"==={room.upper()}===")
	print()


def actionify(action):
	print(f"[ {action.upper()} ]")
	print()


#A DICTIONARY THAT IM USING AS A MAP.
#BASICALLY EACH ROOM HAS ITEMS, A DESCRIPTION, AND ROOMS THAT YOU CAN ACESS BY TRAVELLING FROM THE CURRENT ROOM

places = {
    "living room": {
        "west":
        "hallway 1",
        "items": ["remote", "pizza box"],
        "desc":
        """you are in the living room. there is a 3 seater couch with cheap cushions and a TV at one end.
the remote is buried in a pot plant and the air conditioning is on. an empty pizza box is in the corner.
to the west, the living room door leads to the first hallway."""
    },
    "your room": {
        "north":
        "west of hallway 2",
        "items": ["comic book"],
        "desc":
        """you are in your room. you see your unmade bed and a closet.
there's a table in the corner, multiple drawings up on the wall, and a faint smell of coffee. 
to the north, your bedroom door leads to a passage."""
    },
    "roommate room": {
        "north":
        "east of hallway 2",
        "items": ["key"],
        "desc":
        """you are in your roommate's room. tell me that isn't creepy. 
they went to bed AGES ago, and are still snoring like a foghorn. their cape is folded neatly on the bed alongside that dorky superhero mask they wear.
to the north, the second hallway is visible."""
    },
    "bathroom": {
        "south":
        "west of hallway 2",
        "desc":
        """you are in the bathroom. the leaky tap slowly drips.
there is an empty toothbrush holder in front of the dirty mirror. your toothbrush isn't here, because you left it in your 10cm-thick reinforced steel anti-theft safe.
the door to the south reveals the end of the second hallway."""
    },
    "kitchen": {
        "east":
        "hallway 1",
        "south":
        "middle of hallway 2",
        "items": ["note"],
        "desc":
        """you are in the kitchen. the shelves are empty, and so are all the cupboards.
the fridge is completely jammed shut, and there is a note on it. 
the first hallway is to the east. to the south, you see the second hallway."""
    },
    "laundry": {
        "east": "west of hallway 2",
        "villain": "yes",
    },
    "hallway 1": {
        "east":
        "living room",
        "west":
        "kitchen",
        "south":
        "east of hallway 2",
        "desc":
        """you are in a narrow hallway. 
to the east, you see the living room, home of the mighty three-seater couch. 
a door to the west leads to the kitchen. to the south, the start of the second hallway is visible."""
    },
    "east of hallway 2": {
        "south":
        "roommate room",
        "north":
        "hallway 1",
        "west":
        "middle of hallway 2",
        "desc":
        """you are at the corner of the second and first hallway. 
the current hallway goes west. to the north, you see the first hallway. your roommate's bedroom is to the south."""
    },
    "middle of hallway 2": {
        "north":
        "kitchen",
        "west":
        "west of hallway 2",
        "east":
        "east of hallway 2",
        "desc":
        """you are in the middle of the second hallway, which extends both east and west. 
there is an entrance to the kitchen on the north."""
    },
    "west of hallway 2": {
        "west":
        "laundry",
        "east":
        "middle of hallway 2",
        "south":
        "your room",
        "north":
        "bathroom",
        "desc":
        """you are at the west end of the second hallway, which continues east.
the laundry room is to the west. your room is south, opposite the bathroom."""
    },
}


#gets the action the player meant using the actions dictionary. returns empty if its not possible
def get_action(user_action):
	for key, val in ACTIONS.items():
		if user_action in val:
			return key
	return ""


#this prints all the items in the current room.
def print_items(items):
	for item in items:
		if item:
			if item[-1] == "s":
				print(f"you see {item}.")
			elif item[0] in VOWELS:
				print(f"you see an {item}.")
			else:
				print(f"you see a {item}.")


#similar to the get_action() function. it gets the item the player meant if the item is in the inventory or room.
#it doesnt return empty, instead returns the user_item if the item isn't a thing.
def get_items(user_item):
	all_items = places[current_room].get("items", [])

	for i in all_items:
		first_half = i.split()[0]
		if first_half in user_item:
			return i

	for i in inventory:
		first_half = i.split()[0]
		if first_half in user_item:
			return i

	return user_item


def remove_item(current_room, i):  #for removing items when i need to
	places[current_room]["items"].remove(i)


def new_scene():
	print()
	scene_header(current_room)  #print the scene header
	if "desc" in places[current_room].keys():  #prints the description
		print(places[current_room]["desc"])
	print_items(items)


def guess_code():  #this is the riddle for the safe.
	actionify("note")
	print("""over the road i dared to stride,
to meet the world on another side.
what creature am i?""")
	print()
	print("enter your answer below:")
	print()
	answer = input("> ")

	while "chicken" not in answer.lower():  #if you get the wrong answer
		print("that doesn't sound right. try again.")
		print()
		answer = input("> ")

	places["your room"]["items"].append("toothbrush")
	places["bathroom"][
	    "desc"] = """you are in the bathroom. the leaky tap slowly drips.
there is an empty toothbrush holder in front of the dirty mirror.
the door to the south reveals the end of the second hallway."""

	return "the safe opens with a click. you see your toothbrush"


'''THE FUNCTIONS FOR EACH ACTION'''


def handle_move(direction, room):
	if not direction:  #if the direction is empty
		return "you've gotta enter a direction to go somewhere.", room

	if not direction in places[room]:  #if the direction ain't possible
		return "not a valid direction, dude.", room

	if (room == "west of hallway 2"
	    and direction == "west"):  #if the player wants to go to the laundry room
		if all(tasks.values()):  #if they completed all the tasks
			if not game_state["has_key"]:  #if they dont have the key
				return "dang it, the laundry room is locked. find the key first.", room
		else:  #they didn't do all the tasks.
			msg = "dang it, the laundry room is locked. you need to.."

			if not tasks["breakfast"]:
				msg += "\n--> eat breakfast"
			if not tasks["brushed teeth"]:
				msg += "\n--> brush your teeth"
			if not game_state["has_key"]:
				msg += "\n--> find the key"

			return msg, room  #returns game response + current_room

	new_room = places[room][direction]
	return f"you travel {direction}", new_room


def print_help():  #prints all possible commands, helpful for beginners
	actionify("commands")

	print("--> go north/south/east/west")
	print("--> take <item>")
	print("--> eat <item>")
	print("--> read <item>")
	print("--> open <item>")
	print("--> explode <item>")
	print("--> brush <item>")
	print("--> inventory (to check your inventory)")
	print("--> look around (to check your surroundings)")
	print("--> tasks (to display your tasks)")
	return ""


def print_tasks():  #prints all tasks
	actionify("tasks")

	print("--> eat breakfast")
	print("--> brush your teeth")
	print("--> grab your socks from the laundry room")


def print_inventory():  #prints every item in the inventory
	if "inventory" in action:
		actionify("inventory")
		msg = ""
		if inventory:  #if there's stuff in the inventory
			for item in inventory:
				print("--> " + item)
		else:
			print("you got nothin' buddy.")


def handle_exit():  #quits the game.
	print()
	print(
	    "are you sure you wanna quit playing?")  #asks the player before quitting
	print()
	user_exit = input("> ").lower()
	if user_exit.startswith("y"):
		exit()
	else:
		return "glad to know you're staying."


def handle_look():  #prints the current room's description
	print(places[current_room]["desc"])
	print_items(items)
	return


def take_item(item):  #adds item to inventory
	if item == "key":  #if they picked up a key
		game_state["has_key"] = True

	if item not in food:
		inventory.append(item)
		places[current_room]["items"].remove(item)
		return f"you took the {item}"
	else:  #print this if they try to add food to their inventory
		return "where are you gonna stuff that, your pockets?"


def read_item(item, items):
	if "note" in item:  #if the user wants to read a note
		if "note" in items or "note" in inventory:  #the only time there is a note in the room's items is in the kitchen
			actionify("note")
			return "\"hey dude, i may have a̶c̶i̶d̶e̶n̶t̶l̶y̶ a̶c̶c̶i̶d̶e̶t̶a̶l̶y̶  non-deliberately super-glued the fridge shut. just get the explosives from the living room to get it open.\""
		elif current_room == "kitchen" and game_state[
		    "fridge_open"]:  #if the fridge is open print a different note
			actionify("note")
			return "just type \"from __fridge__ import breakfast\""
		elif ("safe" in inventory or "safe" in items
		      ) and game_state["safe_note"]:  #prints a different note for the safe
			return guess_code()
		return "there is no note here."

	if "comic" in item:
		if "comic book" in inventory:
			actionify("comic book")
			print('you read the comic. it\'s...oddly familiar.')
			print("panel 1: your room.")
			print("panel 2: you, standing around, holding this very comic.")
			print("caption: STOP READING AND GET ON WITH THE GAME!!")
			return
		return "you've gotta pick it up first!"


def explode_item(current_room):
	if "explosives" in inventory:
		game_state["exploded"] = True
		if "note" in places[current_room]["items"]:
			places[current_room]["items"].remove("note")

		places["kitchen"][
		    "desc"] = """you are in the kitchen. the shelves are empty, and so are all the cupboards.
the fridge is smoldering and the door is in pieces.
the first hallway is to the east. to the south, you see the second hallway."""

		if "note" in inventory:
			inventory.remove("note")
		return "you have exploded the fridge."
	return "you don't have explosives."


def open_item(item, items, room):
	if "fridge" in item:
		if game_state["exploded"]:
			game_state["fridge_open"] = True
			return "the fridge opens. \nunfortunately, it's wiped clean! it's completely empty, aside from another note with messy scribbling."
		return "the fridge doesn't budge. read the note."

	if "pizza" in item:
		if "explosives" in inventory and "explosives" in items:
			return "there are 3 lonely crumbs in the pizza box."
		places[room]["items"].append("explosives")
		return "you have found explosives in the pizza box."

	if "safe" in item:
		if not game_state["safe_open"]:
			game_state["safe_note"] = True
			return """the safe doesn't open.
the password for it is a 7 letter word, and there's a note stuck to it with a riddle."""
		else:
			return "the safe is already open."

	if "closet" in item:
		places[room]["items"].append("safe")
		return "you have opened your closet. there is an anti-theft safe"


def eat_item(item, current_room):
	if item not in food:
		return f"don't even think about it."
	remove_item(current_room, item)
	food.remove(item)
	return f"you ate the {item}"


def import_food():
	if current_room == "kitchen" and game_state["exploded"]:
		places["kitchen"]["items"] = ["eggs", "toast", "plate"]
		return "you have imported breakfast"
	return "invalid command!"


def handle_brush(current_room):
	if "toothbrush" in inventory:
		if current_room == "bathroom":
			actionify("toothbrushing complete")
			tasks["brushed teeth"] = True
			return "you've brushed your teeth! finally."
		else:
			return "you can't brush your teeth here. go to the bathroom."
	else:
		return "you don't have a toothbrush."


#assigns each function to it's relevant action. the function is called through the dictionary
action_functions = {
    "move": handle_move,
    "help": print_help,
    "tasks": print_tasks,
    "inventory": print_inventory,
    "exit": handle_exit,
    "look": handle_look,
    "import": import_food
}


def action_center(action, item, direction, current_room, items):
	if not action:
		return f"\"{user_action}\" isn't a valid command. type \"help\" for a list."

	if "move" == action:
		return handle_move(direction, current_room)

	if action in action_functions.keys():
		return action_functions[action](
		)  #calls the function from the actions dictionary
	'''ITEM BASED ACTIONS'''
	if "take" in action and item in items:
		return take_item(item)

	if "read" in action and item in ["note", "comic book"]:
		return read_item(item, items)

	if "explode" in action and "fridge" in item and current_room == "kitchen":
		if not game_state["exploded"]:
			return explode_item(current_room)
		else:
			return "you already exploded the fridge"

	if "eat" in action and item in items:
		return eat_item(item, current_room)

	if "brush" in action and "teeth" in item:
		if not tasks["brushed teeth"]:
			return handle_brush(current_room)
		else:
			return "you already brushed your teeth"

	if "open" in action:
		if (item in items or item in inventory
		    or ("fridge" in item and current_room == "kitchen")
		    or ("closet" in item and current_room == "your room")):
			return open_item(item, items, current_room)

	if item in items:
		return f"you can't {action} the {item}"
	return f"you can't {action} item \"{user_item}\""


current_room = "your room"  #used for the map dictionary
previous_room = ""  #this is so that i dont display the scene header if im still in the same room
inventory = []
food = ["eggs", "toast", "plate"]
msg = ""
print("\033[1;34m")
actionify("START GAME")
intro()

while True:  #the main game loop
	msg = ""
	items = places[current_room].get("items", [])

	if current_room != previous_room:
		previous_room = current_room  #sets the new previous room
		new_scene()

	print()
	user_input = input("> ").lower()  #takes user input [yay!]
	next_move = user_input.split(" ")  #splits the user's input into a list
	user_action = next_move[
	    0] if "from __fridge__ import breakfast" not in user_input else user_input

	if len(next_move) > 1:
		user_item = ' '.join(next_move[1:]).replace("the ", "")
		direction = next_move[1]  #the direction is the second part
	else:
		user_item = direction = ""

	item = get_items(user_item)
	action = get_action(user_action)

	action_result = action_center(action, item, direction, current_room, items)

	if "move" in action:
		msg, current_room = action_result
	else:
		msg = action_result

	if not food:
		if not tasks["breakfast"]:
			print()
			actionify("breakfast complete")
			msg = "you've finished breakfast! finally."
			tasks["breakfast"] = True

	if msg:  #kinda self explanatory, only prints the game's response if there is a response to print
		print(msg)

	if "villain" in places[current_room].keys():
		break
endings.main()
