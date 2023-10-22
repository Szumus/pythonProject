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

#funkcje pomocnicze
def draw_snake():
    canvas.delete("snake")
    for segment in snake:
        x, y = segment
        canvas.create_rectangle(x, y, x + 10, y + 10, fill="green", tag="snake")

def draw_food():
    x, y = draw_food
    canvas.create_rectangle(x, y, x +10, y +10, fill="yellow")


def move_snake():
    global snake_direction
    x, y = snake[0]
    if snake_direction == "Up":
        y -= 10
    elif snake_direction == "Down":
        y += 10
    elif snake_direction == "Left":
        x -= 10
    else:
        x += 10
snake.insert(0,(x, y))
if snake[0] == food:
    generate_food()
else:
    snake.pop()

    if chcek_collision():
        canvas.delete("all")
        canvas.create_text(200, 200, text="Get better and try again")
    else:
        draw_snake()
        draw_food()
        snake.after(100,move_snake)

        def generate_food():
            global food
            x = random.randint(0,39) * 10
            y = random.randint(0,39) * 10
            food = (x, y)

def check_collision():
    x, y =snake[0]
    if x < 0 or x >= 400 or y < 0 or y>= 400 or snake[0] in snake[1:]:
        return True
    return False

def change_direction(event):
    global snake_direction
    if event.keysym == "Up" and snake_direction != "Down":
        snake_direction = "Up"
    elif event.keysym == "Down" and snake_direction != "Down":
        snake_direction = "Down"
    elif event.keysym == "Right" and snake_direction != "Left":
        snake_direction = "Right"
    elif event.keysym == "Left" and snake_direction!= "Right":
        snake_direction = "Left"

snake.bind("<KeyPress>", change_direction)


