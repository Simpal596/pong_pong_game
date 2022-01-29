from turtle import Turtle


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score_player1 = 0
        self.score_player2 = 0
        self.penup()
        self.color("white")
        self.hideturtle()
        self.score_1()
        self.score_2()


    def score_1(self):
        self.goto(-120, 280)
        self.write(arg=f"{self.score_player1}", font=("Arial", 50, "normal"))

    def score_2(self):
        self.goto(100, 280)
        self.write(arg=f"{self.score_player2}", font=("Arial", 50, "normal"))

    def score_update(self, score):
        score += 1
        self.clear()
        self.write(arg=f"{score}", font=("Arial", 50, "normal"))

