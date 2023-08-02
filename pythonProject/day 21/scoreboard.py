from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update()


    def update(self):
        self.write(f"score = {self.score}", False, "center", ("Courier", 24, "bold"))

    def gameover(self):
        self.goto(0,0)
        self.write("Gameover",align="center",font=("Courier", 24, "bold"))

    def refresh(self):
        self.score += 1
        self.clear()
        self.update()


