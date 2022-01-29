from turtle import Screen
from bat import Bat
from ball import Ball
from dash import Dash
from score import Score
# from time import sleep
POSITION_1 = [(-740, 0), (-740, -20), (-740, -40), (-740, -60)]
POSITION_2 = [(730, 0), (730, -20), (730, -40), (730, -60)]

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.title("pong_pong_game 🎾")
my_screen.setup(width=1500, height=700)

bat_1 = Bat()
bat_1.bat_positioning(pos_list=POSITION_1)

bat_2 = Bat()
bat_2.bat_positioning(pos_list=POSITION_2)

my_screen.listen()
my_screen.onkeypress(fun=bat_1.bat_up, key="w")
my_screen.onkeypress(fun=bat_1.bat_down, key="s")
my_screen.onkeypress(fun=bat_2.bat_up, key="Up")
my_screen.onkeypress(fun=bat_2.bat_down, key="Down")

ball = Ball()
dash_line = Dash()
score = Score()

is_game_on = True
ball.direction()
while is_game_on:
    ball.move()
    ball.wall_collision()
    ball.bat_collision(pos_list=POSITION_1)
    ball.bat_collision(pos_list=POSITION_2)


my_screen.exitonclick()
