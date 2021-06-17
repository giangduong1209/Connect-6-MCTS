import numpy as np
from player import *
from board import *
from constant import Constant
class Connect6State():
    def __init__(self, state, next_to_move=1):
        self.board = state
        self.board_size = Board
        self.next_to_move = next_to_move
    def game_result(self):
        # won_player = self.referee.__check()
        # if won_player:
        #     self.winner = won_player
        #     return True
        # return False
        return (self.board.isFull() or self.board.isGameOver())
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
        if self.next_to_move == Connect6State.x:
            next_to_move = Connect6State.o
        else:
            next_to_move = Connect6State.x

        return Connect6State(new_board, next_to_move)

    def get_legal_actions(self):
        indices = np.where(self.board == 0)
        return [
            Connect6State(coords[0], coords[1], self.next_to_move)
            for coords in list(zip(indices[0], indices[1]))
        ]
    def next_state(self, move):
        if(move != 0):
            return 
    def SwapPlayer(self, constant: Constant):
        self.SetPlayer(constant.Opponent(Player))
    
    def SetPlayer(self, player):
        self.legalmove = self.get_legal_actions(player)

