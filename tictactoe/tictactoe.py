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
    
    # Get the number of X's on the board
    x_count = sum([row.count(X) for row in board])
    # Get the number of O's on the board
    o_count = sum([row.count[O] for row in board])

    # If more Xs than Os, it's O's turn
    if x_count > o_count:
        return O
    # Otherwise, it's X's turn
    return X

    # raise NotImplementedError


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    actions = set()
    # Check for empty cells in the board
    # Checking rows
    for i in range(3):
        # Checking columns
        for j in range(3):
            # If that cell is empty, add to the list of actions
            if board[i][j] == EMPTY:
                actions.add((i, j))

    return actions

    # raise NotImplementedError


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    # Get the coordinates of the action
    i = action[0]
    j = action[1]
    # Raise error if move is invalid
    if not board[i][j] == EMPTY:
        raise ValueError('Move is invalid')

    # Create a deepcopy of the board
    board_copy = copy.deepcopy(board)
    # Update the board state based on the action (by getting the current player and setting the value of the desired cell)
    board_copy[i][j] = player(board)
    # Return the new board state
    return board_copy

    # raise NotImplementedError


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
