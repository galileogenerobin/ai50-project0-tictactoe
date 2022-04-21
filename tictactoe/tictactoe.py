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
    
    # Get the number of X's on the board; we use list comprehension so we can sum the count of X for each row in the board
    x_count = sum([row.count(X) for row in board])
    # Get the number of O's on the board; ditto above
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
    # Check for horizontal
    for row in board:
        if row.count(X) == 3:
            return X
        if row.count(O) == 3:
            return O
    
    # Check for vertical
    for i in range(3):
        # List comprehension to get a list of all items in the i index of each row == our column
        column = [row[i] for row in board]
        if column.count(X) == 3:
            return X
        if column.count(O) == 3:
            return O

    # Check for diagonal; hard coding coordinates while I can't think of a more elegant way to do this yet
    # Basically if all cells in the diagonal are equal and not empty, the value in those cells is the winning player
    if board[0][0] == board [1][1] == board [2][2] and not board[0][0] == EMPTY:
        return board[0][0]
    if board[0][2] == board [1][1] == board [2][0] and not board[0][2] == EMPTY:
        return board[0][2]

    # Otherwise, no winners yet
    return None
    # raise NotImplementedError


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # Let's utilize our winner function; i.e. if there's already a winner, the game is over
    # Or if there are no more EMPTY cells on the board
    if winner(board) or sum([row.count[EMPTY] for row in board]) == 0:
        return True
    
    # Else, game is still ongoing
    return False
    # raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # Let's utilize our winner function
    if winner(board) == X:
        return 1
    elif winner(board) == O:
        return -1
    else:
        return 0

    # raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
