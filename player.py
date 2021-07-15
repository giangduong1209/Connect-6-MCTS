from constant import SIZE, B, W, EMPTY, EDGE
import random
import mcts
class Player:
	def __init__(self, stone):
		self.stone = stone
		self.opponent = - stone

	def first_move(self):
		return (int(input("Row:")), int(input("Column:")))

	def move(self, board):
		raise NotImplementedError
		
	def collectEmpty(self, board):
		return [(i, j) for j in range (SIZE) for i in range(SIZE) if board[i][j] == EMPTY]

class RandomPlayer(Player):
	def move(self, board):
		empty = self.collectEmpty(board)
		candidates = random.sample(empty, 2)
		return candidates
		
class HumanPlayer(Player):
	def move(self, board):
		empty = self.collectEmpty(board)
		candidates = ([int(input("Row:")),int(input("Column:"))], [int(input("Row:")),int(input("Column:"))])
		return candidates
