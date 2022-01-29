from turtle import Turtle


class Dash(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, -350)
        self.setheading(90)
        self.pendown()
        self.pensize(width=5)
        for i in range(18):
            self.fd(20)
            self.penup()
            self.fd(20)
            self.pendown()
