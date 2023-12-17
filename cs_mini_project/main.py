from tictactoe.tic_tac_toe import play
from hangman.hangman import hg
from rps.rock import rpsgame
#from connectfour.gui import run
import tkinter as tk


if __name__ == '__main__':
    def create_buttons():
        root = tk.Tk()
        root.title("Games Menu")

        button_style = {'padx': 15, 'pady': 10, 'bg': '#2ecc71', 'fg': 'white', 'font': ('Arial', 12)}

        button_frame = tk.Frame(root, padx=20, pady=20)
        button_frame.pack()

        tk.Button(button_frame, text="Tic Tac Toe", command=play, **button_style).pack(fill=tk.X, pady=5)
        tk.Button(button_frame, text="Hangman", command=hg, **button_style).pack(fill=tk.X, pady=5)
        tk.Button(button_frame, text="Rock Paper Scissors", command=rpsgame, **button_style).pack(fill=tk.X, pady=5)
        tk.Button(button_frame, text="Connect 4", command='run', **button_style).pack(fill=tk.X, pady=5)

        root.mainloop()

        # Run the improved button program
    create_buttons()


