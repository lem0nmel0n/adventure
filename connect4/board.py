import copy
import time

class Board:
	def __init__(self, rows, cols):
		self.rows = rows
		self.cols = cols
		self.board = [['.' for i in range(cols)] for i in range(rows)]
  
  # Load a specific board state
	def load_board(self, rows):
		# rows is a 2D list of strings containing the board state
		for row in rows:
			self.board.append(list(row))

	def copy(self):
		temporary = Board(self.rows, self.cols)
		temporary.board = [row[:] for row in self.board]
		return temporary

	def is_valid_move(self, col):
		if self.board[0][col] == ".":
			return True
		else:
			return False

  # Get the next open row in a column for a piece to be dropped
	def get_next_open_row(self, col):
		for index, row in enumerate(self.board):
			if index == 0 and row[col] != ".":
				return None
			if row[col] != ".":
				return index-1
			if index == 5:
				return index

  # Drop a piece into the board at the specified column
	def drop_piece(self, col, piece):
		open_row = self.get_next_open_row(col)
		self.board[open_row][col] = piece

	def check_threes(self, piece):
		#check if the current player creates a 3 in a row
		for row in range(self.rows):
			for col in range(self.cols-3):
				new = [self.board[row][col + i] for i in range(4)]
				if (piece * 3) in "".join(new) and new.count(".") == 1:
					return True

		for col in range(self.cols):  
			for row in range(self.rows-3):
				new = [self.board[row + i][col] for i in range(4)]
				if (piece * 3) in "".join(new) and new.count(".") == 1:
					return True

		for col in range(self.cols-3):  
			for row in range(self.rows-3):
				new = [self.board[row + i][col + i] for i in range(4)]
				if (piece * 3) in "".join(new) and new.count(".") == 1:
					return True

		for row in range(3, self.rows):  
			for col in range(self.cols-3):
				new = [self.board[row - i][col + i] for i in range(4)]
				if (piece * 3) in "".join(new) and new.count(".") == 1:
					return True
					
		return False

  # checks that the player has won vertically, horizontally, or diagonally
	def check_win(self, piece):
		for row in range(self.rows):
			for col in range(self.cols-3):
				new = [self.board[row][col + i] for i in range(4)]
				if new.count(piece) == 4:
					for i in range(4):
						self.board[row][col + i] = "☆" 
					return True

		for col in range(self.cols):  
			for row in range(self.rows-3):
					new = [self.board[row + i][col] for i in range(4)]
					if new.count(piece) == 4:
						for i in range(4):
							self.board[row + i][col] = "☆" 
						return True

		for col in range(self.cols-3):  
			for row in range(self.rows-3):
				new = [self.board[row + i][col + i] for i in range(4)]
				if new.count(piece) == 4:
					for i in range(4):
						self.board[row + i][col + i] = "☆" 
					return True

		for row in range(3, self.rows):  
			for col in range(self.cols-3):
				new = [self.board[row - i][col + i] for i in range(4)]
				if new.count(piece) == 4:
					for i in range(4):
						self.board[row - i][col + i] = "☆" 
					return True

		return False
  
  # Check if the board is full
	def is_full(self):
		new = set(col for col in self.board[0])
		return "." not in new

	def print_board(self):
		top = " ".join(list(map(str, range( 7))))
		print("| " + " ".join(str(i) for i in range(7)) + " |")
		for row in self.board:
			new_row = " ".join(row)
			print(f"| {new_row} |")
		bottom = "-" * 13
		print(f"| {bottom} |")