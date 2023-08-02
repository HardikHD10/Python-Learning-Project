import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

user = Player()
cars = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(user.go_up,"Up")

game_is_on = True
while game_is_on:
     time.sleep(0.5)
     screen.update()
     cars.create_cars()
     cars.move()
     scoreboard.update_scoreboard()

     for car in cars.all_cars:
          if car.distance(user) < 20 :
               game_is_on = False
               scoreboard.game_finish()


     if user.is_gameover():
          user.go_to_start()
          cars.level_up()
          scoreboard.increase_score()


screen.exitonclick()

