import tkinter as tk
from tkinter import messagebox




def square_clicked(event):
    square = event.widget
    square.config(bg='#e2ecf4')






def grid(master):
    for i in range(10):
        for j in range(10):
            square = tk.Frame(master, width=50, height=50, bg='#2b3f6b', highlightbackground='#e2ecf4', highlightthickness=1)
            square.grid(row=i, column=j)
            square.bind('<Button-1>', square_clicked)








def game_window():
    master = tk.Toplevel(root)
    master.title("Mine Finder")
    master.geometry("515x595")


    game_window_base = tk.Canvas(master, width=300, height=300, bg='#fff')
    game_window_base.pack()


    game_window_base.create_rectangle(11, 11, 504, 70, outline="#e2ecf4", fill="#e2ecf4")


    # creating the back function
    def back():
        master.destroy()




    # creating the back button
    back_button = tk.Button(game_window_base, text="Back", font=('@Binate', 15, 'bold'), relief='solid', bg="#e2ecf4", command=back)
    back_button.pack(side=tk.TOP, padx=10, pady=10)




    # creating the grid
    grid_frame = tk.Frame(game_window_base, bg='#e2ecf4')
    grid_frame.pack(side=tk.TOP, padx=10, pady=10)
    grid(grid_frame)




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
