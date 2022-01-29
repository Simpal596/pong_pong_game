from turtle import Turtle
from random import randint


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.penup()
        self.color("blue")
        self.goto(0, 0)
        # self.angle = randint(0, 360)
        self.angle = 306

    def direction(self):
        self.setheading(self.angle)
        print(self.angle)

    def move(self):
        print(f"before fd {self.ycor()}")
        self.fd(10)
        print(f"after fd {self.ycor()}")

    def wall_collision(self):
        if self.ycor() < -340 or self.ycor() > 340:
            if 0 < self.heading() < 90:
                self.angle -= 90
                print(f"new angle 1 :{self.angle}")
                print(self.ycor())
                self.setheading(self.angle)
            elif 90 < self.heading() < 180:
                self.angle += 90
                print(f"new angle 2 :{self.angle}")
                print(self.ycor())
                self.setheading(self.angle)
            elif 180 < self.heading() < 270:
                self.angle -= 90
                print(f"new angle 3 :{self.angle}")
                print(self.ycor())
                self.setheading(self.angle)
            elif 270 < self.heading() < 360:
                self.angle += 90
                print(f"new angle 4 :{self.angle}")
                print(self.ycor())
                self.setheading(self.angle)
            else:
                self.angle += 180
                print(f"new angle 5 :{self.angle}")
                print(self.ycor())
                self.setheading(self.angle)

    def bat_collision(self, pos_list):
        for pos in pos_list:
            if self.distance(pos) <= 10:
                self.angle += 90
                print(f"new angle 4 :{self.angle}")
                print(self.ycor())
                self.setheading(self.angle)

