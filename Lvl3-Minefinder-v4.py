import tkinter as tk
from tkinter import messagebox
import random


class Minesweeper:
    def __init__(self, master, rows, columns, num_mines):
        self.master = master
        self.rows = rows
        self.columns = columns
        self.num_mines = num_mines


        self.board = [[0 for _ in range(columns)] for _ in range(rows)]
        self.buttons = [[None for _ in range(columns)] for _ in range(rows)]


        self.generate_mines()
        self.calculate_numbers()


        self.create_grid()


    def generate_mines(self):
        mines = random.sample(range(self.rows * self.columns), self.num_mines)
        for mine in mines:
            row = mine // self.columns
            col = mine % self.columns
            self.board[row][col] = -1


    def calculate_numbers(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col] != -1:
                    for i in range(-1, 2):
                        for j in range(-1, 2):
                            if 0 <= row + i < self.rows and 0 <= col + j < self.columns:
                                if self.board[row + i][col + j] == -1:
                                    self.board[row][col] += 1


    def create_grid(self):
        for row in range(self.rows):
            for col in range(self.columns):
                button = tk.Button(
                    self.master,
                    width=2,
                    height=1,
                    font=('Arial', 12),
                    relief='raised',
                    command=lambda r=row, c=col: self.on_click(r, c)
                )
                button.grid(row=row, column=col)
                self.buttons[row][col] = button


    def on_click(self, row, col):
        if self.board[row][col] == -1:
            self.buttons[row][col].config(text="X", state='disabled')
            self.game_over()
        elif self.board[row][col] == 0:
            self.buttons[row][col].config(text="", state='disabled')
            self.reveal_empty(row, col)
        else:
            self.buttons[row][col].config(text=str(self.board[row][col]), state='disabled')


    def reveal_empty(self, row, col):
        if 0 <= row < self.rows and 0 <= col < self.columns and self.buttons[row][col]['state'] == 'normal':
            if self.board[row][col] == 0:
                self.buttons[row][col].config(text="", state='disabled')
                for i in range(-1, 2):
                    for j in range(-1, 2):
                        self.reveal_empty(row + i, col + j)
            else:
                self.buttons[row][col].config(text=str(self.board[row][col]), state='disabled')


    def game_over(self):
        for row in range(self.rows):
            for col in range(self.columns):
                if self.board[row][col] == -1:
                    self.buttons[row][col].config(text="X", state='disabled')


def square_clicked(event):
    square = event.widget
    square.config(bg='#e2ecf4')


def grid(master):
    for i in range(10):
        for j in range(10):
            square = tk.Frame(master, width=50, height=50, bg='#2b3f6b', highlightbackground='#e2ecf4', highlightthickness=1)
            square.grid(row=i, column=j)
            square.bind('<Button-1>', square_clicked)


def create_minesweeper_frame(parent):
    minesweeper_frame = tk.Frame(parent, bg='#e2ecf4')
    minesweeper_frame.pack(side=tk.TOP, padx=10, pady=10)


    minesweeper = Minesweeper(minesweeper_frame, 10, 10, 10)  # Adjust the parameters as needed
    minesweeper_frame.update()


def game_window():
    master = tk.Toplevel(root)
    master.title("Mine Finder")
    master.geometry("515x595")


    game_window_base = tk.Canvas(master, width=300, height=300, bg='#fff')
    game_window_base.pack()


    game_window_base.create_rectangle(11, 11, 504, 70, outline="#e2ecf4", fill="#e2ecf4")


    def back():
        master.destroy()


    back_button = tk.Button(game_window_base, text="Back", font=('@Binate', 15, 'bold'), relief='solid', bg="#e2ecf4", command=back)
    back_button.pack(side=tk.TOP, padx=10, pady=10)


    create_minesweeper_frame(master)  # Add Minesweeper frame


def how_to_play():
    messagebox.showinfo("How to Play", "1. Click one of the tiles within the grid to start the game\n2. The number in each box represents the number of 'mines' in the surrounding 8 tiles\n3. Right-click to place a flag to signal a mine\n4. Left-click to dig up a tile (only if you believe there is no mine)")


root = tk.Tk()
root.title("Mine Finder")


canvas = tk.Canvas(root, width=300, height=300, bg='#2b3f6b')
canvas.pack()


canvas.create_rectangle(10, 10, 293, 293, outline="#fff", fill="#fff")
canvas.create_rectangle(20, 60, 284, 283, outline="#e2ecf4", fill="#e2ecf4")


canvas.create_rectangle(10, 10, 293, 293, outline="#fff", fill="#fff")
canvas.create_rectangle(55, 30, 250, 130, outline="#e2ecf4", fill="#e2ecf4")
canvas.create_rectangle(55, 140, 250, 270, outline="#e2ecf4", fill="#e2ecf4")


title = tk.Label(canvas, text="Mine Finder", font=('@Binate', 24, 'bold'), bg="#e2ecf4")
title.pack()
canvas.create_window(150, 80, window=title)


play_button = tk.Button(canvas, text="Play", font=('@Binate', 18, 'bold'), relief='solid', bg="#e2ecf4", command=game_window)
canvas.create_window(150, 175, window=play_button)


htp_button = tk.Button(canvas, text="How to play", font=('@Binate', 18, 'bold'), relief='solid', bg="#e2ecf4", command=how_to_play)
canvas.create_window(150, 238, window=htp_button)


root.mainloop()
