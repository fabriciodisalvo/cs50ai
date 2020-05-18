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


test_boards = [initial_state(), board_1, board_2, board_3, board_4, board_5, board_6, board_7, board_8, board_9]

for board in test_boards:
    print(player(board))
    print(actions(board))
    print(winner(board))
    terminal(board)
    print(utility(board))


# result(initial_state(), (1,1))

# result(board_2, (1,1))
