import tkinter as tk
from tkinter import messagebox
import random

# Minesweeper class represents the Minesweeper game logic and interface.
class Minesweeper:
    def __init__(self, master, rows, columns, num_mines, main_window):
        # Initialize Minesweeper game settings and create the grid.
        self.master = master
        self.rows = rows
        self.columns = columns
        self.num_mines = num_mines
        self.remaining_mines = num_mines
        self.main_window = main_window

        self.board = [[0 for _ in range(columns)] for _ in range(rows)]
        self.buttons = [[None for _ in range(columns)] for _ in range(rows)]

        self.game_over_flag = False

        self.create_grid()
        self.generate_mines()
        self.calculate_numbers()

    def generate_mines(self):
        # Randomly place mines on the grid.
        mines = random.sample(range(self.rows * self.columns), self.num_mines)
        for mine in mines:
            row = mine // self.columns
            col = mine % self.columns
            self.board[row][col] = -1
            self.buttons[row][col].config(command=lambda r=row, c=col: self.on_click(r, c))

    def calculate_numbers(self):
        # Calculate the number of mines surrounding each cell.
        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col] != -1:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if 0 <= row + i < self.rows and 0 <= col + j < self.columns:
                                if self.board[row + i][col + j] == -1:
                                    self.board[row][col] += 1

    def create_grid(self):
        # Create the graphical grid interface.
        for row in range(self.rows):
            for col in range(self.columns):
                button = tk.Button(
                    self.master,
                    width=2,
                    height=1,
                    font=("Arial", 12),
                    relief="raised",
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button

    def on_click(self, row, col):
        # Handle a cell click event.
        if self.game_over_flag:
            return

        if self.board[row][col] == -1:
            self.reveal_mines()  # Reveal all mines
            self.game_over()
        elif self.board[row][col] == 0:
            self.buttons[row][col].config(text="", state="disabled")
            self.reveal_empty(row, col)
        else:
            self.buttons[row][col].config(
                text=str(self.board[row][col]), state="disabled"
            )

    def reveal_empty(self, row, col):
        # Reveal empty cells and their neighbors.
        if (
            0 <= row < self.rows
            and 0 <= col < self.columns
            and self.buttons[row][col]["state"] == "normal"
        ):
            if self.board[row][col] == 0:
                self.buttons[row][col].config(text="", state="disabled")
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        self.reveal_empty(row + i, col + j)
            else:
                self.buttons[row][col].config(
                    text=str(self.board[row][col]), state="disabled"
                )

    def game_over(self):
        # Handle the game over condition.
        self.game_over_flag = True
        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col] == -1:
                    self.buttons[row][col].config(text="X", state="disabled", bg="#de4e5a")  
# Change background color to #de4e5a

        messagebox.showinfo("Game Over", "You lose!")
        self.main_window.deiconify()  # Show the main window
        self.master.destroy()  # Close the game window

    def reveal_mines(self):
        # Reveal all mines when the game ends.
        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col] == -1:
                    self.buttons[row][col].config(text="X", state="disabled", bg="#de4e5a")  
# Change background color to #de4e5a

# square_clicked function handles click events on grid squares.
def square_clicked(event, buttons, row, col):
    square = event.widget
    square.config(bg="#e2ecf4")
    buttons[row][col].invoke()

# grid function creates the grid of squares in the game window.
def grid(master, buttons):
    squares = []
    for i in range(10):
        square_row = []
        for j in range(10):
            square = tk.Frame(
                master,
                width=50,
                height=50,
                bg="#2b3f6b",
                highlightbackground="#e2ecf4",
                highlightthickness=1,
            )
            square.grid(row=i, column=j)
            square.bind("<Button-1>", lambda event, r=i, c=j: square_clicked(event, buttons, r, c))
            square_row.append(square)
        squares.append(square_row)
    return squares

# create_minesweeper_frame function creates the Minesweeper game frame.
def create_minesweeper_frame(parent, main_window):
    minesweeper_frame = tk.Frame(parent, bg="#e2ecf4")
    minesweeper_frame.pack(side=tk.TOP, padx=10, pady=10)
    buttons = Minesweeper(minesweeper_frame, 10, 10, 10, main_window)  # Pass the main window reference
    squares = grid(minesweeper_frame, buttons.buttons)
    buttons.squares = squares

# game_window function creates the game window and UI elements.
def game_window():
    master = tk.Toplevel(root)
    master.title("Mine Finder")
    master.geometry("515x595")

    game_window_base = tk.Canvas(master, width=300, height=300, bg="#fff")
    game_window_base.pack()

    game_window_base.create_rectangle(
        11, 11, 504, 70, outline="#e2ecf4", fill="#e2ecf4"
    )

    def back():
        master.withdraw()  # Hide the game window
        root.deiconify()  # Show the main window

    back_button = tk.Button(
        game_window_base,
        text="Back",
        font=("@Binate", 15, "bold"),
        relief="solid",
        bg="#e2ecf4",
        command=back,
    )
    back_button.pack(side=tk.TOP, padx=10, pady=10)

    create_minesweeper_frame(master, root)  # Pass the main window reference

# how_to_play function displays instructions on how to play the game.
def how_to_play():
  messagebox.showinfo(
    "How to Play",
    "1. Click one of the tiles within the grid to start the game\n"
    "2. 10 of the squares in the grid have been assigned the 'Mine' value, and once clicked, will end the game\n"
    "3. You'll have to try and guess your way to the end of the game, relying on instinct and luck, instead of logical thinking skills"
)

# Main application window.
root = tk.Tk()
root.title("Mine Finder")

# Main canvas for the game.
canvas = tk.Canvas(root, width=300, height=300, bg="#2b3f6b")
canvas.pack()

# Title label displayed at the top of the main window.
title = tk.Label(canvas, text="Mine Finder", font=("@Binate", 24, "bold"), bg="#e2ecf4")
title.pack()
canvas.create_window(150, 80, window=title)

# Play button to start the game.
play_button = tk.Button(
    canvas,
    text="Play",
    font=("@Binate", 18, "bold"),
    relief="solid",
    bg="#e2ecf4",
    command=game_window,
)
canvas.create_window(150, 175, window=play_button)

# How to play button to display game instructions.
htp_button = tk.Button(
    canvas,
    text="How to play",
    font=("@Binate", 18, "bold"),
    relief="solid",
    bg="#e2ecf4",
    command=how_to_play,
)
canvas.create_window(150, 238, window=htp_button)

# Start the main application.
root.mainloop()
