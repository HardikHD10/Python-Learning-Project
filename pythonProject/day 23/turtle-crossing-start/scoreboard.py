from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super(Scoreboard, self).__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Game Level : {self.level} ", align="left", font=("Courier", 20, "normal"))

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()

    def game_finish(self):
        self.goto(0,0)
        self.write("Gameover", align="center", font=("Courier", 20, "normal"))

