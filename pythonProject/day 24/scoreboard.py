from turtle import Turtle
class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.goto(0, 270)
        self.hideturtle()
        self.update()


    def update(self):
        self.clear()
        self.write(f"score : {self.score} Highscore : {self.highscore}", False, "center", ("Courier", 24, "bold"))

    def reset(self):
        if self.score > self.highscore :
            self.highscore = self.score
            with open("data.txt",mode="w") as data :
                data.write(f"{self.highscore}")
        self.score = 0
        self.update()

    # def gameover(self):
    #     self.goto(0,0)
    #     self.write("Gameover",align="center",font=("Courier", 24, "bold"))

    def refresh(self):
        self.score += 1
        self.update()


