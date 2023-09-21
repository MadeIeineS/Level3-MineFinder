import tkinter as tk
from tkinter import messagebox
import random

def square_clicked(event):
    square = event.widget
    row, col = square.grid_info()["row"], square.grid_info()["column"]
    if game_over:
        return
    if game_board[row][col] == -1:
        # Mine clicked, handle game over
        square.config(bg='red')
        reveal_mines()
        messagebox.showinfo("Game Over", "You clicked on a mine! Game over.")
        reset_game()
    elif game_board[row][col] == 0:
        # Clicked on an empty cell, reveal empty cells
        reveal_empty_cells(row, col)
    else:
        # Clicked on a numbered cell, reveal it
        square.config(bg='#e2ecf4')
        square.config(text=str(game_board[row][col]), font=('@Binate', 14, 'bold'))

def mine_clicked(event):
    if not game_over:
        reveal_mines()
        messagebox.showinfo("Game Over", "You clicked on a mine! Game over.")
        reset_game()

def grid(master):
    for i in range(10):
        for j in range(10):
            square = tk.Button(master, width=3, height=1, bg='#c0c0c0', highlightbackground='#000000', highlightthickness=1)
            square.grid(row=i, column=j, padx=2, pady=2)
            square.bind('<Button-1>', square_clicked)
            square.bind('<Button-3>', flag_square)
            squares[i][j] = square  # Store the reference to the square in the 2D list

def place_mines():
    mines = random.sample(range(100), 10)
    for mine in mines:
        row, col = mine // 10, mine % 10
        game_board[row][col] = -1  # -1 represents a mine

def calculate_numbers():
    for row in range(10):
        for col in range(10):
            if game_board[row][col] != -1:
                count = 0
                for dr in [-1, 0, 1]:
                    for dc in [-1, 0, 1]:
                        if 0 <= row + dr < 10 and 0 <= col + dc < 10 and game_board[row + dr][col + dc] == -1:
                            count += 1
                game_board[row][col] = count

def reveal_empty_cells(row, col):
    if row < 0 or row >= 10 or col < 0 or col >= 10 or revealed[row][col]:
        return
    revealed[row][col] = True
    square = squares[row][col]
    square.config(bg='#e2ecf4')
    if game_board[row][col] == 0:
        for dr in [-1, 0, 1]:
            for dc in [-1, 0, 1]:
                reveal_empty_cells(row + dr, col + dc)

def flag_square(event):
    square = event.widget
    if not game_over:
        square.config(bg='#e2ecf4')
        square.config(text="🚩", font=('@Binate', 14, 'bold'))

def reveal_mines():
    for row in range(10):
        for col in range(10):
            if game_board[row][col] == -1:
                square = squares[row][col]
                square.config(bg='red')

def reset_game():
    global game_board, revealed, game_over
    game_board = [[0 for _ in range(10)] for _ in range(10)]
    revealed = [[False for _ in range(10)] for _ in range(10)]
    place_mines()
    calculate_numbers()
    game_over = False

def open_game_window():
    game_window = tk.Toplevel(root)
    game_window.title("Minesweeper")
    
    global squares, game_board, revealed, game_over
    squares = [[None for _ in range(10)] for _ in range(10)]
    game_board = [[0 for _ in range(10)] for _ in range(10)]
    revealed = [[False for _ in range(10)] for _ in range(10)]
    game_over = False
    
    canvas = tk.Canvas(game_window, width=300, height=300, bg='#2b3f6b')
    canvas.pack()

    grid_frame = tk.Frame(canvas, bg='#2b3f6b')
    grid_frame.pack(side=tk.TOP, padx=5, pady=5)
    grid(grid_frame)

    reset_game()

def how_to_play():
    messagebox.showinfo(
        "How to Play",
        "1. Click one of the tiles within the grid to start the game\n"
        "2. The number in each box represents the number of 'mines' in the surrounding 8 tiles\n"
        "3. Right-click to place a flag to signal a mine\n"
        "4. Left-click to dig up a tile (only if you believe there is no mine)"
    )

root = tk.Tk()
root.title("Minesweeper")

canvas = tk.Canvas(root, width=300, height=400, bg='#2b3f6b')
canvas.pack()

canvas.create_rectangle(10, 10, 293, 390, outline="#fff", fill="#fff")
canvas.create_rectangle(20, 60, 284, 380, outline="#e2ecf4", fill="#e2ecf4")

title = tk.Label(canvas, text="Minesweeper", font=('@Binate', 24, 'bold'), bg="#e2ecf4")
title.pack(pady=20)

play_button = tk.Button(canvas, text="Play", font=('@Binate', 18, 'bold'), relief='solid', bg="#e2ecf4", command=open_game_window)
play_button.pack(pady=10)

print("Hello Kelsey")

htp_button = tk.Button(canvas, text="How to play", font=('@Binate', 18, 'bold'), relief='solid', bg="#e2ecf4", command=how_to_play)
htp_button.pack(pady=10)

squares = [[None for _ in range(10)] for _ in range(10)]
game_board = [[0 for _ in range(10)] for _ in range(10)]
revealed = [[False for _ in range(10)] for _ in range(10)]
game_over = False

root.mainloop()