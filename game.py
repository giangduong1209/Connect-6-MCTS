import numpy as np
def board_game():
    board = np.zeros((19,19))
    return board
    
def drop_piece(board, row, col, piece):
    
    board[row][col] = str(piece)

def is_valid_location(board, col):
    return board[18][col] == 0

def get_next_open_row(board, col):
    for r in range(19):
        if board[r][col] == 0:
            return r

board = board_game()
print(board)
game_over = False
turn = 0 
while not game_over:
    if turn == 0:
        col = int(input("Player 1 make your selection (19,19): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)

    else:
        col = int(input("Player 2 make your selection (19,19): "))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
        print(board)
    turn += 1
    turn = turn % 2
##########################################################

class Connect6BTMM():
    def game_result(self):
        # check if game is over
        rowsum = np.sum(self.board, 0)
        colsum = np.sum(self.board, 1)
        diag_sum_tl = self.board.trace()
        diag_sum_tr = self.board[::-1].trace()

        player_one_wins = any(rowsum == self.board_size)
        player_one_wins += any(colsum == self.board_size)
        player_one_wins += (diag_sum_tl == self.board_size)
        player_one_wins += (diag_sum_tr == self.board_size)

        if player_one_wins:
            return self.x

        player_two_wins = any(rowsum == -self.board_size)
        player_two_wins += any(colsum == -self.board_size)
        player_two_wins += (diag_sum_tl == -self.board_size)
        player_two_wins += (diag_sum_tr == -self.board_size)

        if player_two_wins:
            return self.o

        if np.all(self.board != 0):
            return 0.

        # if not over - no result
        return None

    def is_game_over(self):
        return self.game_result is not None

    def is_move_legal(self, move):
        # check if correct player moves
        if move.value != self.next_to_move:
            return False

        # check if inside the board on x-axis
        x_in_range = (0 <= move.x_coordinate < self.board_size)
        if not x_in_range:
            return False

        # check if inside the board on y-axis
        y_in_range = (0 <= move.y_coordinate < self.board_size)
        if not y_in_range:
            return False

        # finally check if board field not occupied yet
        return self.board[move.x_coordinate, move.y_coordinate] == 0

    def move(self, move):
        if not self.is_move_legal(move):
            raise ValueError(
                "move {0} on board {1} is not legal". format(move, self.board)
            )
        new_board = np.copy(self.board)
        new_board[move.x_coordinate, move.y_coordinate] = move.value
        if self.next_to_move == Connect6BTMM.x:
            next_to_move = Connect6BTMM.o
        else:
            next_to_move = Connect6BTMM.x

        return Connect6BTMM(new_board, next_to_move)

    def get_legal_actions(self):
        indices = np.where(self.board == 0)
        return [
            Connect6BTMM(coords[0], coords[1], self.next_to_move)
            for coords in list(zip(indices[0], indices[1]))
        ]