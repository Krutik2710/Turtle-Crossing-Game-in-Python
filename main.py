import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
STARTING_POSITION = (0, -280)
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
tim=Player()
screen.listen()
screen.onkey(tim.go_up,"Up")
game_is_on = True
i=0
car=CarManager()
score=Scoreboard()
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.car_move()
    if tim.ycor()>280:
        tim.goto(STARTING_POSITION)
        score.increase_score()

    for cars in car.all_cars:
        if tim.distance(cars)<20:
            game_is_on=False
            score.game_over()

screen.exitonclick()