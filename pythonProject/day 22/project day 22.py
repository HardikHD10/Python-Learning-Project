from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

#Step 1 : Create the screen
screen = Screen()
screen.setup(height=600,width=800)
screen.bgcolor("Black")
screen.title("PONG GAME")
screen.tracer(0)

# creating paddles and ball
r_paddle = Paddle(350)
l_paddle = Paddle(-350)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")


flag = True
while(flag):
    scoreboard.update_scoreboard()
    time.sleep(ball.movespeed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    if (ball.distance(r_paddle) < 50  and ball.xcor() > 320) or (ball.distance(l_paddle)  < 50 and ball.xcor() < -320):
        ball.bounce_x()


    if ball.xcor() > 380 :
        ball.reset_position()
        ball.bounce_x()
        scoreboard.l_point()


    if ball.xcor() < -380:
        ball.reset_position()
        ball.bounce_x()
        scoreboard.r_point()


screen.exitonclick()
