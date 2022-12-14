from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",30, "normal")

class GameOver(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.gameisover = "Game Over"

    def game_over(self):
        self.write(self.gameisover, align=ALIGNMENT, font=FONT)
