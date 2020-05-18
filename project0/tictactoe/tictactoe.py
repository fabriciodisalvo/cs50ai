"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    if board == initial_state():
        return "X"

    play_count = 0
    for row in board:
        for column in row:
            if column is not None:
                play_count += 1

    if play_count % 2 == 0: 
        return "X" 
    else: 
        return "O"


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    possible_actions_set = set()
    for row in range(len(board)):
        for column in range(len(board[row])):
            if board[row][column] is None:
                possible_actions_set.add((row,column))
    return possible_actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if new_board[action[0]][action[1]] is None:
        new_board[action[0]][action[1]] = player(board)
    else:
        raise Exception('Not a valid Action')
    print(board)
    print(new_board) 


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_boards = (((0,0),(0,1),(0,2)),
                        ((1,0),(1,1),(1,2)),
                        ((2,0),(2,1),(2,2)),
                        ((0,0),(1,0),(2,0)),
                        ((0,1),(1,1),(2,1)),
                        ((0,2),(1,2),(2,2)),
                        ((0,0),(1,1),(2,2)),
                        ((0,2),(1,1),(2,0)))

    for player in (X, O):
        for i in winning_boards:
            if board[i[0][0]][i[0][1]] == player:
                # print(str(player) + " is in place " 
                #     + str(i[0][0]) + "," + str(i[0][1]) 
                #     + ", so we check:" 
                #     + str(i[1][0]) + "," + str(i[1][1]) 
                #     + " and " 
                #     + str(i[2][0]) + "," + str(i[2][1]) )
                if board[i[1][0]][i[1][1]] == player and board[i[2][0]][i[2][1]] == player:
                    return player
    return None

def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    tested_board = winner(board)
    if tested_board is not None:
#        print("NO SIGUE")
        return True    
    play_count = 0
    for row in board:
        for column in row:
            if column is not None:
                play_count += 1
            if column is None:
#                print("SIGUE")
                return False
    if play_count == 9:
#        print("NO SIGUE")
        return True




def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == X:
        return 1
    if winner(board) == O:
        return -1
    return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if terminal(board) == True:
        return None
    
