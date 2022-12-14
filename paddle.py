from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.create_paddle()
        self.goto(x, y)

    def create_paddle(self):
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.penup()
        self.speed("fastest")

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
