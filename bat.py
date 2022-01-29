from turtle import Turtle


class Bat:
    def __init__(self):
        self.bat_segment_list = []
        self.bat_list_making()

    def bat_list_making(self):
        for i in range(4):
            self.segment = Turtle("square")
            self.segment.penup()
            self.segment.color("white")
            self.segment.speed("fastest")
            self.bat_segment_list.append(self.segment)

    def bat_positioning(self, pos_list):
        i = 0
        for pos in pos_list:
            self.bat_segment_list[i].setpos(pos)
            i += 1

    def bat_up(self):
        for i in range(len(self.bat_segment_list)-1, 0, -1):
            x = self.bat_segment_list[i-1].xcor()
            y = self.bat_segment_list[i-1].ycor()
            self.bat_segment_list[i].setpos(x, y)
        self.bat_segment_list[0].setheading(90)
        self.bat_segment_list[0].fd(20)

    def bat_down(self):
        for i in range(0, len(self.bat_segment_list)-1):
            x = self.bat_segment_list[i+1].xcor()
            y = self.bat_segment_list[i+1].ycor()
            self.bat_segment_list[i].setpos(x, y)
        self.bat_segment_list[len(self.bat_segment_list)-1].setheading(270)
        self.bat_segment_list[len(self.bat_segment_list)-1].fd(20)
