from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super(Player, self).__init__()
        self.shape("turtle")
        self.left(90)
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.is_gameover()
        self.go_to_start()


    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(),new_y)

    def is_gameover(self):
        if self.ycor() > FINISH_LINE_Y :
            return True
        else:
            return False

    def go_to_start(self):
        self.goto(STARTING_POSITION)



