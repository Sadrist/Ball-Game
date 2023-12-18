from tkinter import *
import time
import random

screen = Tk()
screen.title("ball")
screen.resizable(False, False)

width = 1000
height = 1000

canvas = Canvas(
    screen,
    bg="gray",
    width=width,
    height=height
)
canvas.pack()
screen.update()


class Ball:
    def __init__(self, canvas, color, platform, score):
        self.canvas = canvas
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        possibilities = [-5, -4, -3, -2, -1, 1, 2, 3, 4, 5]
        self.x = random.choice(possibilities)
        self.y = -2
        width_ball = 25
        height_ball = 25
        self.b_drawing = self.canvas.create_oval(0, 0, width_ball, height_ball, fill=color)
        self.canvas.move(self.b_drawing, (width / 2 - width_ball / 2), (height / 2 - height_ball / 2))
        self.platform = platform
        self.score = score
        self.hit_bottom = False

    def draw(self):
        self.canvas.move(self.b_drawing, self.x, self.y)
        b_position = self.canvas.coords(self.b_drawing)
        if b_position[1] <= 0:
            self.y = 2
        elif b_position[3] >= self.canvas_height:
            self.hit_bottom = True
            self.canvas.create_text(400, 200, fill = "black", text = "YOU LOSE!!!", font = ("Arial", 40, "bold"))
        if self.reflection(b_position):
            self.y = -4
        elif b_position[0] <= 0:
            self.x = 2
        elif b_position[2] >= self.canvas_width:
            self.x = -2

    def reflection(self, b_position):
        p_position = canvas.coords(self.platform.p_drawing)
        if p_position[0] <= b_position[2] and p_position[2] >= b_position[0]:
            if p_position[1] <= b_position[3] <= p_position[3]:
                self.score.refresh()
                return True
        else:
            return False


class Platform:
    def __init__(self, canvas):
        self.canvas = canvas
        self.canvas.bind_all("<KeyPress-w>", self.move_right)
        self.canvas.bind_all("<KeyPress-s>", self.move_left)
        self.canvas.bind_all("<KeyPress-a>", self.move_left)
        self.canvas.bind_all("<KeyPress-d>", self.move_right)
        self.canvas_width = self.canvas.winfo_width()
        self.canvas_height = self.canvas.winfo_height()
        self.x = 0
        self.y = 0
        p_width = 100
        p_height = 20
        self.p_drawing = self.canvas.create_rectangle(0, 0, p_width, p_height, fill="black")
        self.canvas.move(self.p_drawing, (width / 2 - p_width / 2), (height / 2 - p_height / 2) + 200)

    def draw(self):
        self.canvas.move(self.p_drawing, self.x, self.y)
        p_position = self.canvas.coords(self.p_drawing)
        if p_position[0] <= 0:
            self.x = 0
        if p_position[2] >= self.canvas_width:
            self.x = 0

    def move_right(self, event):
        p_position = self.canvas.coords(self.p_drawing)
        if p_position[2] < self.canvas_width:
            self.x = 5

    def move_left(self, event):
        p_position = self.canvas.coords(self.p_drawing)
        if p_position[0] > 0:
            self.x = -5

class Score:
    def __init__(self,  canvas, colour):
        self.canvas = canvas
        self.score = 0
        self.text = self.canvas.create_text(50, 17, fill = colour, text = f"Score: {self.score}", font = ("Arial", 17, "bold"))

    def refresh(self):
        self.score += 1
        self.canvas.itemconfig(self.text, text = f"Score: {self.score}")


platform = Platform(canvas)
score = Score(canvas, "red")
ball = Ball(canvas, "red", platform, score)

while True:
    if not ball.hit_bottom:
        ball.draw()
        platform.draw()
    else:
        time.sleep(3)
        break
    screen.update_idletasks()
    screen.update()
    time.sleep(0.01)

# Далее в классе Ball, необходимо создать метод для отрисовки, например метод draw. Этот метод должен отображать
# движение мяча, но сначала нам нужно задасто движение со скоростью 0 по обеим осям, чтобы мячик просто отрисовался.
#
# Чтобы его увидеть, нам необходимо создать экземпляр класса мячика, и в цикле у объекта мячика запустить метод draw
