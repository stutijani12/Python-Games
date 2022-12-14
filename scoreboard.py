from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier",24,"normal")



class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("scorelist.txt", "r") as file:
            contents = int(file.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.high_score = contents
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score}  High Score :{self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score = self.score + 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("scorelist.txt", "w") as file:
                file.write(f"{self.high_score}")
        self.update_scoreboard()
        self.score = 0


