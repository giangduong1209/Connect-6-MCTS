# import numpy as np
# def board_game():
#     board = np.zeros((19,19))
#     return board
    
# def drop_piece(board, row, col, piece):
    
#     board[row][col] = str(piece)

# def is_valid_location(board, col):
#     return board[18][col] == 0

# def get_next_open_row(board, col):
#     for r in range(19):
#         if board[r][col] == 0:
#             return r

# board = board_game()
# print(board)
# game_over = False
# turn = 0 
# while not game_over:
#     if turn == 0:
#         col = int(input("Player 1 make your selection (19,19): "))
#         if is_valid_location(board, col):
#             row = get_next_open_row(board, col)
#             drop_piece(board, row, col, 1)

#     else:
#         col = int(input("Player 2 make your selection (19,19): "))
#         if is_valid_location(board, col):
#             row = get_next_open_row(board, col)
#             drop_piece(board, row, col, 2)
#         print(board)
#     turn += 1
#     turn = turn % 2
class Connect_6()
