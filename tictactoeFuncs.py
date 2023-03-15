# Project 3 - Tic-Tac-Toe Simulator
#
# Name: Tyler Baxter
# Instructor: S. Einakian
# Section: 03

from random import randint

# This function prints the welcome message and prompts the user for game mode
# none -> int
def welcome():
    print()
    print("Welcome to tic-tac-toe")
    print("    Win by getting having three in a row, column, or diagonal")
    print("    Players will alternate taking turns choosing a play location(1-9)")
    print("    until there is a draw or a player wins")
    print("This is what the board will look like:")
    print("", 1, " | ", 2, " | ", 3, " ")
    print("---------------")
    print("", 4, " | ", 5, " | ", 6, " ")
    print("---------------")
    print("", 7, " | ", 8, " | ", 9, " ")
    play = input("Would you like the play against the computer(1) or another player(2)? ")
    return int(play)

 
# This function creates a list to store the tic-tac-toe position data
# none -> list[]
def create_board():
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
    return board
   

# This function prints the current game board
# list[] -> none
def print_board(board):
    print("", board[0], " | ", board[1], " | ", board[2], " ")
    print("---------------")
    print("", board[3], " | ", board[4], " | ", board[5], " ")
    print("---------------")
    print("", board[6], " | ", board[7], " | ", board[8], " ")
   

# This function prompts the user if the want to play as X or O
# none -> string
def pick_letter(mode):
    p2 = ""
    if mode == 1:
        response = input("Play as X or O? ")
    else:
        response = input("Player 1: Play as X or O? ")
    response = response.upper()
    while not (response == "X" or response == "O"):
        print("invalid response, respond with X or O")
        if mode == 1:
            response = input("Play as X or O? ")
        else:
            response = input("Player 1: Play as X or O? ")
        response = response.upper()
    if response == "X":
        p2 = "O"
    else:
        p2 = "X"
    if mode == 2:
        print("Player 2: You will be", p2)
    return response


# This function prompts the user to choose a location for their turn
# list[], string -> list[]
def get_input(board, letter):
    turn = int(input("Where do you like to place your letter (pick in range of 1-9)? ")) - 1
    while turn > 8 or turn < 0:
        print("Invalid move! Location is already taken. Please try again. ")
        turn = int(input("Where do you like to place your letter (pick in range of 1-9)? ")) - 1
    while not(board[turn] == " "):
        print("Invalid move! Location is already taken. Please try again. ")
        turn = int(input("Where do you like to place your letter (pick in range of 1-9)? ")) - 1

    board[turn] = letter
    return board


# This function picks a random value for the computer to select
def get_comp_input(board, letter):
    c_input = randint(0, 8)
    while not board[c_input] == " ":
        c_input = randint(0, 10)
    board[c_input] = letter
    return board


# This function checks if the row is full
# list[] -> boolean, string
def check_rows(board):
    check = [False, ""]
    for i in range(0, 7, 3):
        if board[i] == board[i + 1] == board[i + 2]:
            if not board[i] == " ":
                check[0] = True
                check[1] = board[i]
    return check


# This function checks if the columns are filled with the same latter
# list[] -> boolean, string
def check_cols(board):
    check = [False, ""]
    for i in range(0, 3, 1):
        if board[i] == board[i + 3] == board[i + 6]:
            if not board[i] == " ":
                check[0] = True
                check[1] = board[i]
    return check


# This function checks if the diagonals are filler with the same letter
# list[] -> boolean, string
def check_diags(board):
    check = [False, ""]
    if board[0] == board[4] == board[8]:
        if not board[0] == " ":
            check[0] = True
            check[1] = board[0]
    if board[2] == board[4] == board[6]:
        if not board[2] == " ":
            check[0] = True
            check[1] = board[2]
    return check


# This function checks if the board is full
# list[] -> boolean
def board_full(board):
    full = True
    for idx in range(0, 9, 1):
        if board[idx] == " ":
            full = False
    return full


# This function checks if there is a winner
# list[] -> boolean
def check_win(board):
    check_r = check_rows(board)
    check_c = check_cols(board)
    check_d = check_diags(board)
    if check_r[0]:
        print("Player", check_r[1], "Wins!")
        return check_r[0]
    if check_c[0]:
        print("Player", check_c[1], "Wins!")
        return check_c[0]
    if check_d[0]:
        print("Player", check_d[1], "Wins!")
        return check_d[0]
