from .board import Board
from random import randint, choice
import os
import time
import re

class Game:
	def __init__(self, players, rows=6, cols=7, save_file=None):
		if len(players) < 2:
			raise ValueError("At least two players are required.")
		self.players = players
		self.current_player_index = 0
		self.rows = rows
		self.cols = cols
		self.board = Board(self.rows, self.cols)
	def get_current_player(self):
		return self.players[self.current_player_index]

	def switch_player(self):
		self.current_player_index = (self.current_player_index + 1) % len(self.players)

	def clear(self):
		if os.name == 'nt':
				board = os.system('cls')
		else:
				board = os.system('clear')

	def villain_move(self):
		villain_piece = self.players[1].piece
		player_piece = self.players[0].piece

		'''
		these two blocks are for checking if the next move will be a 4 in a row
		if the player will win next turn, it'll block
		if the villain will win, it'll select that column
		'''
		for col in range(7):
			temporary = self.board.copy()
			if temporary.is_valid_move(col):
				temporary.drop_piece(col, villain_piece)
				if temporary.check_win(villain_piece):
					return col

		for col in range(7):
			temporary = self.board.copy()
			if temporary.is_valid_move(col):
				temporary.drop_piece(col, player_piece)
				if temporary.check_win(player_piece):
					return col
		'''
		these next two blocks of code are for checking 
		if either the villain can make 3 in a row or 
		if it can block the player from making 3 in a row. 
		'''
		for col in range(7):
			temporary = self.board.copy()
			if temporary.is_valid_move(col):
				temporary.drop_piece(col, villain_piece)
				if temporary.check_threes(villain_piece):
					print("three!", col)
					return col

		for col in range(7):
			temporary = self.board.copy()
			if temporary.is_valid_move(col):
				temporary.drop_piece(col, player_piece)
				if temporary.check_threes(player_piece):
					print("blocked!", col)
					return col

		col_list = [0,1,2,2,3,3,3,3,4,4,5,6] #favouring the middle columns over the edge columns

		for col in range(7): # for every column
			temporary = self.board.copy() #create a board copy
			if temporary.is_valid_move(col): 
				temporary.drop_piece(col, villain_piece) # the villain drops a piece 

				for col2 in range(7): #for every column [again]
					if temporary.is_valid_move(col2):
						temporary.drop_piece(col2, player_piece) #drop the player piece
						if temporary.check_win(player_piece): 
							col_list = [column for column in col_list if column != col2] #the columns that dont allow the player an instant win

		col = choice(col_list)
		while not self.board.is_valid_move(col):
			col = choice(col_list)
		return col


	def play(self):
		self.clear()
		self.board.print_board()
		while True:
			current_player = self.get_current_player()
			print(f"{current_player.name} turn.")
			if "your" in current_player.name:
				col = input("enter the column (0-6) to drop your piece: ")
				if not col:
					print()
					print("do you want to exit?")
					leave = input("> ").lower()
					print()
					if leave.startswith("y"):
						print("it was sad you couldn't stay.")
						exit()
				col = re.sub(r"\D", "", col)

				while not col.isnumeric():
					print()
					print("try entering a number.")
					print()
					col = input("enter the column (0-6) to drop your piece: ")
					col = re.sub(r"\D", "", col)
				col = int(col)

				if col > 6: col = 6
				while not self.board.is_valid_move(col):
					print("that ain't a valid move, dude. try again.")
					col = int(input("enter the column (0-6) to drop your piece: "))
					if col > 6: col = 6

				self.board.drop_piece(col, self.get_current_player().piece)
			else:
				col = self.villain_move()
				self.board.drop_piece(col, self.get_current_player().piece)
				time.sleep(1.5)

			self.clear()
			self.board.print_board()

			if self.board.check_win(self.get_current_player().piece):
				time.sleep(1)
				self.clear()
				self.board.print_board()
				time.sleep(1)
				if "your" in self.get_current_player().name:
					return "win"
				else:
					time.sleep(1)
					return "lose"
			elif self.board.is_full():
				return "tie"



			self.switch_player()
