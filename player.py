from constant import SIZE, B, W, EMPTY, EDGE
import random
import mcts
class Player:
	def __init__(self, stone):
		self.stone = stone
		self.opponent = - stone

	def first_move(self):
		return (10, 10)

	def move(self, board):
		raise NotImplementedError
		
	def collectEmpty(self, board):
		return [(i, j) for j in range (SIZE) for i in range(SIZE) if board[i][j] == EMPTY]

class RandomPlayer(Player):
	def move(self, board):
		empty = self.collectEmpty(board)
		print(empty)
		candidates = random.sample(empty, 2)
		print(candidates)
		return candidates
		
class HumanPlayer(Player):
	def move(self, board):
		empty = self.collectEmpty(board)
		print(empty)
		candidates = ([int(input("Row 1:")),int(input("Column 1:"))], [int(input("Row 2:")),int(input("Column 2:"))])
		return candidates
