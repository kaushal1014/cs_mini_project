# Tic Tac Toe game with GUI
# using tkinter

# importing all necessary libraries
import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy
import os, sys

# sign variable to decide the turn of which player
sign = 0

# Creates an empty board
global board
board = [[" " for x in range(3)] for y in range(3)]

# Check l(O/X) won the match or not
# according to the rules of the game


def winner(b, l):
	return ((b[0][0] == l and b[0][1] == l and b[0][2] == l) or
			(b[1][0] == l and b[1][1] == l and b[1][2] == l) or
			(b[2][0] == l and b[2][1] == l and b[2][2] == l) or
			(b[0][0] == l and b[1][0] == l and b[2][0] == l) or
			(b[0][1] == l and b[1][1] == l and b[2][1] == l) or
			(b[0][2] == l and b[1][2] == l and b[2][2] == l) or
			(b[0][0] == l and b[1][1] == l and b[2][2] == l) or
			(b[0][2] == l and b[1][1] == l and b[2][0] == l))


# Check if the player can push the button or not


def isfree(i, j):
	return board[i][j] == " "

# Check the board is full or not


def isfull():
	flag = True
	for i in board:
		if(i.count(' ') > 0):
			flag = False
	return flag


# Decide the next move of system


def pc(player_x, player_y):
    pmove = [[player_x, player_y]]
    possiblemove = []
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == ' ':
                possiblemove.append([i, j])

    for let in ['O', 'X']:
        for i in possiblemove:
            boardcopy = deepcopy(board)
            boardcopy[i[0]][i[1]] = let
            if winner(boardcopy, let):
                return i
    corner = []
    if pmove[0] in [[0, 0], [0, 2]]:
        	pmove[0][0]+=1
        	return pmove[0]
    if pmove[0] in [[2, 0], [2, 2]]:
        	pmove[0][0]-=1
        	return pmove[0]
    if len(corner) > 0:
        move = random.randint(0, len(corner) - 1)
        return corner[move]
    edge = []
    for i in possiblemove:
        if i in [[0, 1], [1, 0], [1, 2], [2, 1]]:
            edge.append(i)
    if len(edge) > 0:
        move = random.randint(0, len(edge) - 1)
        return edge[move]


# Configure text on button while playing with system
def get_text_pc(i, j, gb, l1, l2):
    global sign
    if board[i][j] == ' ':
        if sign % 2 == 0:
            board[i][j] = "X"
        else:
            board[i][j] = "O"
        sign += 1
        button[i][j].config(text=board[i][j])
    x = True
    if winner(board, "X"):
        retry(gb)
        x = False
        box = messagebox.showinfo("Winner", "Player won the match")
    elif winner(board, "O"):
        retry(gb)
        x = False
        box = messagebox.showinfo("Winner", "Computer won the match")
    elif isfull():
        retry(gb)
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
    if x:
        if sign % 2 != 0:
            move = pc(i, j)
            get_text_pc(move[0], move[1], gb, l1, l2)



# Create the GUI of game board for play along with system


def gameboard_pc(game_board, l1, l2):
	global button
	button = []
	for i in range(3):
		m = 3+i
		button.append(i)
		button[i] = []
		for j in range(3):
			n = j
			button[i].append(j)
			get_t = partial(get_text_pc, i, j, game_board, l1, l2)
			button[i][j] = Button(
				game_board, bd=5, command=get_t, height=4, width=8)
			button[i][j].grid(row=m, column=n)
	game_board.mainloop()

# Initialize the game board to play with system


def withpc(game_board):
	game_board.destroy()
	game_board = Tk()
	game_board.title("Tic Tac Toe")
	l1 = Button(game_board, text="Player : X", width=10)
	l1.grid(row=1, column=1)
	l2 = Button(game_board, text="Computer : O",
				width=10)

	l2.grid(row=2, column=1)
	gameboard_pc(game_board, l1, l2)

def restart():
    os.execv(sys.executable, ['python'] + sys.argv)

def retry(game_board):

    g1 = Button(game_board, text="Retry", width=10,command=restart)
    g1.grid(row=1, column=1)
    g2 = Label(game_board, text="Good Game!",width=10)
    g2.grid(row=2, column=1)


# main function


def play():
    menu = Tk()
    menu.geometry("500x200")  # Adjusted the height for a better appearance
    menu.title("Tic Tac Toe")

    wpc = partial(withpc, menu)

    head = Label(menu, text="---Welcome to Tic Tac Toe---",
                 bg="#3498db", fg="white",
                 font=('Arial', 18, 'bold'), pady=10)  # Changed background color to a shade of blue

    B1 = Button(menu, text="Play", command=wpc,
                bg="#2ecc71", fg="white",
                font=('Arial', 14), bd=3)  # Changed background color to a shade of green

    head.pack(side='top', fill='x')  # Filled the label horizontally
    B1.pack(pady=20)  # Added some padding to the button

    menu.mainloop()


