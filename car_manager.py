import random
from turtle import Screen,Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.all_cars=[]
        self.hideturtle()
        self.create_car()

    def create_car(self):
        choice=random.randint(1,6)
        if choice==1 :
            new_c=Turtle()
            new_c.penup()
            new_c.shape("square")
            new_c.color(random.choice(COLORS))
            new_c.shapesize(stretch_wid=1, stretch_len=2)
            new_c.ran_no = random.randint(-250,250)
            new_c.goto(400,new_c.ran_no)
            self.all_cars.append(new_c)



    def car_move(self):
        for cars in self.all_cars:
            cars.backward(MOVE_INCREMENT)

