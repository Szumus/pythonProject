import tkinter as tk
from tkinter.colorchooser import askcolor

class PaintApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Paint App")
        self.root.geometry("800x600")

        self.canvas = tk.Canvas(root, bg="white")
        self.canvas.pack(fill=tk.BOTH, expand=True)

        self.drawing = False
        self.last_x = None
        self.last_y = None

        self.color = "black"
        self.line_width = 2
        self.eraser_mode = False

        self.color_button = tk.Button(root, text="Wybierz kolor", command=self.choose_color)
        self.color_button.pack()

        self.line_width_slider = tk.Scale(root, label="Grubość linii", from_=1, to=10, orient="horizontal", command=self.set_line_width)
        self.line_width_slider.set(self.line_width)
        self.line_width_slider.pack()

        self.eraser_button = tk.Button(root, text="Tryb Gumki", command=self.toggle_eraser)
        self.eraser_button.pack()

        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.draw)
        self.canvas.bind("<ButtonRelease-1>", self.stop_drawing)

    def start_drawing(self, event):
        self.drawing = True
        self.last_x = event.x
        self.last_y = event.y

    def draw(self, event):
        if self.drawing:
            x = event.x
            y = event.y
            if self.last_x is not None and self.last_y is not None:
                if self.eraser_mode:
                    self.canvas.create_line(self.last_x, self.last_y, x, y, fill="white", width=self.line_width)
                else:
                    self.canvas.create_line(self.last_x, self.last_y, x, y, fill=self.color, width=self.line_width)
                self.last_x = x
                self.last_y = y

    def stop_drawing(self, event):
        self.drawing = False
        self.last_x = None
        self.last_y = None

    def choose_color(self):
        color = askcolor()[1]
        if color:
            self.color = color

    def set_line_width(self, value):
        self.line_width = int(value)

    def toggle_eraser(self):
        self.eraser_mode = not self.eraser_mode

if __name__ == "__main__":
    root = tk.Tk()
    app = PaintApp(root)
    root.mainloop()
