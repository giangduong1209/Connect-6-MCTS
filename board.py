from constant import SIZE, B, W, EMPTY, EDGE

class Board:
	def __init__(self):#, turn):
		self.move_count = 2
		#self.turn = turn
		self.board = []
		self.win_player = "Draw"
		self.__clear_board()
		
	def __clear_board(self):
		self.board = [[EMPTY for i in range(SIZE)] for j in range(SIZE)]
		for i in range(SIZE):
			for j in range(SIZE):
				if i == 0 or i == 20 or j == 0 or j == 20:
					self.board[i][j] = EDGE

	def put_down(self, x, y, stone): #move
		self.board[x][y] = stone

	def is_full(self):
		return all([i.count(EMPTY) == 0 for i in self.board])

	def is_won(self):
		for i in self.__get_horizontal() + self.__get_vertical() + self.__get_diagonal_up() + self.__get_diagonal_down():
			if self.__check(i):
				return True
		return False
		
	def is_over(self):
		return (self.board.is_full() or self.board.is_won())
		
	def get_legal_moves(self):
		return [(i, j) for j in range (SIZE) for i in range(SIZE) if self.board[i][j] == EMPTY]
		
	def is_move_legal(self, move):
		return move in set(get_legal_moves())

	def __str__(self):
		def stone(i):
			if i == B:
				return "X"
			elif i == W:
				return "O"
			elif i == EMPTY:
				return "."
			else:
				return "+"

		# return "\n".join([" ".join([stone(j) for j in i]) for i in self.board])
		b = []
		t = 1
		for i in self.board:
			l = []
			if self.board.index(i) != 0 and self.board.index(i) != 20: 
				if t < 10:
					l.append("   " + str(t))
				else:
					l.append("  " + str(t))
				t += 1
				for j in i:
					l.append(stone(j))
				b.append(" ".join(l))
			else:
				l.append("    ")
				for j in i:
					l.append(stone(j))
				b.append(" ".join(l))
		return "\n".join(b)
			
	def __check(self, line):
		b = EDGE
		n = 0

		for i in line:
			if EMPTY == i:
				n = 0
			elif b == i:
				n += 1
			else:
				n = 1
			if n == 6:
				self.win_player = "Black" if i == B else "White"
				return True
			b = i
		return False

	def __get_horizontal(self):
		return [i[1:] for i in self.board[1:SIZE - 1]]

	def __get_vertical(self):
		return [[self.board[j][i] for j in range(1, SIZE)] for i in range(1, SIZE - 1)]

	def __get_diagonal(self, ix, iy, dx, dy):
		line = []
		x, y = ix, iy
		s = self.board[x][y]
		while s != EDGE:
			line.append(s)
			x += dx
			y += dy
			s = self.board[x][y]
		return line

	def __get_diagonal_up(self):
		lines = []
		for i in range(6, SIZE - 1):
			lines.append(self.__get_diagonal(i, 1, -1, 1))
		for i in range(2, SIZE - 6):
			lines.append(self.__get_diagonal(SIZE - 2, i, -1, 1))
		return lines

	def __get_diagonal_down(self):
		lines = []
		for i in range(1, SIZE - 6):
		   lines.append(self.__get_diagonal(i, 1, 1, 1))
		for i in range(2, SIZE - 6):
			lines.append(self.__get_diagonal(1, i, 1, 1))
		return lines

	
