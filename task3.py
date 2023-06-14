"""
Given a Tic-Tac-Toe 3x3 board (can be unfinished).
Write a function that checks if the are some winners.
If there is "x" winner, function should return "x wins!"
If there is "o" winner, function should return "o wins!"
If there is a draw, function should return "draw!"
If board is unfinished, function should return "unfinished!"

Example:
    [['-', '-', 'o'],
     ['-', 'x', 'o'],
     ['x', 'o', 'x']]
    Return value should be "unfinished"

    [[-, -, o],
     [-, o, o],
     [x, x, x]]

     Return value should be "x wins!"

"""
from typing import List


def tic_tac_toe_checker(board: List[List]) -> str:
    for row in board:
        if row.count('x') == 3:
            return "x wins!"
        elif row.count('o') == 3:
            return  "o wins!"

    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i]:
            if board[0][i] == 'x':
                return "x wins!"
            elif board == 'o':
                return  "o wins!"

    if board[0][0] == board[1][1] == board [2][2] and board[0][0] != '-':
        if board[0][0] == 'x':
            return "x wins!"
        elif board[0][0] == 'o':
            return  "o wins!"
    if board[0][2] == board[1][1] == board [2][0] and board[0][0] != '-':
        if board[0][2] == 'x':
            return "x wins!"
        elif board[0][2] == 'o':
            return  "o wins!"

    for row in board:
        if '-' in row:
            return 'unfinished!'
    return 'draw!'
