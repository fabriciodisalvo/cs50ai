"""
Tic Tac Toe Player
"""

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
    for cell in cell_list(board):
        if cell_reader(board, cell) is not None:
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
    for cell in cell_list(board):
        if cell_reader(board, cell) is None:
            possible_actions_set.add(cell)
    return possible_actions_set


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    new_board = copy.deepcopy(board)
    if cell_reader(new_board, action) is None:
        new_board[action[0]][action[1]] = player(board)
        return new_board
    else:
        raise Exception('Not a valid Action')


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    winning_boards = (((0, 0), (0, 1), (0, 2)),
                      ((1, 0), (1, 1), (1, 2)),
                      ((2, 0), (2, 1), (2, 2)),
                      ((0, 0), (1, 0), (2, 0)),
                      ((0, 1), (1, 1), (2, 1)),
                      ((0, 2), (1, 2), (2, 2)),
                      ((0, 0), (1, 1), (2, 2)),
                      ((0, 2), (1, 1), (2, 0))
                      )

    for player in (X, O):
        for trifecta in winning_boards:
            if all(board[i][j] is player for (i, j) in trifecta):
                return player
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    tested_board = winner(board)
    if tested_board is not None:
        return True
    play_count = 0
    for cell in cell_list(board):
        if cell_reader(board, cell) is None:
            return False
        else:
            play_count += 1
    if play_count == 9:
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
    playing = player(board)
    optimal_result = 1
    if playing == O:
        optimal_result = -1
    if terminal(board):
        return None
    possible_outcomes = []
    if playing is X:
        for action in actions(board):
            outcome = max(-100, min_value(result(board, action)))
            possible_outcomes.append((action, outcome))
            if outcome == optimal_result:
                return action
        for i in possible_outcomes:
            if i[1] == 0:
                return i[0]
        return possible_outcomes[0][0]
    else:
        for action in actions(board):
            outcome = min(100, max_value(result(board, action)))
            possible_outcomes.append((action, outcome))
            if outcome == optimal_result:
                return action
        for i in possible_outcomes:
            if i[1] == 0:
                return i[0]
        return possible_outcomes[0][0]


def max_value(board):
    if terminal(board):
        return utility(board)
    v = -100
    for action in actions(board):
        v = max(v, min_value(result(board, action)))
    return v


def min_value(board):
    if terminal(board):
        return utility(board)
    v = 100
    for action in actions(board):
        v = min(v, max_value(result(board, action)))
    return v


def cell_list(board):
    positions = []
    for row_index, row in enumerate(board):
        for col_index, column in enumerate(row):
            positions.append((row_index, col_index))
    return positions


def cell_reader(board, cell):
    return board[cell[0]][cell[1]]
