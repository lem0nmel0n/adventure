from .board import Board
from .game import Game

from dataclasses import dataclass

@dataclass
class Player:
	name: str
	piece: str
def run():
	players = [Player("your", "X"), Player("dexter stinkman's ", "O")]
	game = Game(players, save_file=None)
	result = game.play()
	return result
	
if __name__ == "__main__":
	run()