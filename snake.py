import tkinter as tk
import random

#Window
snake = tk.Tk()
snake.title("Snake Game")
snake.geometry("400x400")
canvas = tk.Canvas(snake, bg="black", width=400,height=400);
canvas.pack()


snake.mainloop()
 # początkowa pozycja i punkty
snake = [(100, 100), (90,100), (80,100)]
snake_direction = "right"
points = (200,200)


