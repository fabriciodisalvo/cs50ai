from tictactoe import *

board_1 = [[EMPTY, EMPTY, EMPTY],
           [EMPTY, X, EMPTY],
           [EMPTY, EMPTY, EMPTY]]

board_2 = [[EMPTY, EMPTY, EMPTY],
           [EMPTY, X, O],
           [EMPTY, EMPTY, EMPTY]]

board_3 = [[EMPTY, EMPTY, EMPTY],
           [X, X, O],
           [EMPTY, EMPTY, EMPTY]]

board_4 = [[EMPTY, O, EMPTY],
           [X, X, O],
           [EMPTY, EMPTY, EMPTY]]

board_5 = [[EMPTY, O, EMPTY],
           [X, X, O],
           [EMPTY, X, EMPTY]]

board_6 = [[EMPTY, O, O],
           [X, X, O],
           [EMPTY, X, EMPTY]]

board_7 = [[X, O, O],
           [X, X, O],
           [EMPTY, X, EMPTY]]

board_8 = [[X, O, O],
           [X, X, O],
           [O, X, EMPTY]]

board_9 = [[X, O, O],
           [X, X, O],
           [O, X, X]]

boardX = [[EMPTY, X, O],
          [X, O, O],
          [EMPTY, X, EMPTY]]

boardO = [[EMPTY, X, O],
          [X, O, O],
          [EMPTY, EMPTY, X]]

boardT = [[X, O, EMPTY],
          [EMPTY, EMPTY, EMPTY],
          [EMPTY, EMPTY, EMPTY]]

test_boards = [initial_state(), board_1, board_2, board_3, board_4,
               board_5, board_6, board_7, board_8, board_9]

board = initial_state()


def auto_player(board):
    while True:
        if terminal(board):
            print()
            print('   THE WINNER IS : ' + str(winner(board)))
            break
        action = minimax(board)
        board = result(board, action)
    return winner(board), board


for i in range(5):
    print('ATTEMPT : ' + str(i))
    auto_player(initial_state())
