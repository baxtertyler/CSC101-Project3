# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Tyler Baxter
# Instructor: S. Einakian
# Section: 03

from tictactoeFuncs import *


class TicTacToeGame:
    # var initialization
    check_r = []
    check_c = []
    check_d = []
    # game start
    winner = ""
    mode = welcome()
    board = create_board()
    p1_letter = pick_letter(mode)
    p2_letter = ""
    if p1_letter == "X":
        p2_letter = "O"
    else:
        p2_letter = "X"
    if mode == 1:
        while not board_full(board):
            print("Player 1's turn:")
            get_input(board, p1_letter)
            print_board(board)
            if check_win(board):
                break
            print()
            print("Computer's turn:")
            get_comp_input(board, p2_letter)
            print_board(board)
            if check_win(board):
                break
            print()
    if mode == 2:
        while not board_full(board):
            print("Player 1's turn:")
            get_input(board, p1_letter)
            print_board(board)
            if check_win(board):
                break
            print()
            print("Player 2's turn:")
            get_input(board, p2_letter)
            print_board(board)
            if check_win(board):
                break
            print()
