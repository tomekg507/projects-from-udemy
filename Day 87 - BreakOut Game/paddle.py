from turtle import Turtle

STARTING_POSITIONS = [(-60, -220), (-40, -220), (-20, -220), (0, -220), (20, -220), (40, -220), (60, -220)]


class Paddle:
    def __init__(self):
        self.parts = []
        self.create_paddle()

    def create_paddle(self):
        for position in STARTING_POSITIONS:
            self.add_part(position)

    def add_part(self, position):
        part = Turtle(shape='square')
        part.penup()
        part.goto(position)
        self.parts.append(part)

    def go_left(self):
        for part in self.parts:
            x_cord = part.xcor() - 20
            y_cord = part.ycor()
            part.goto(x=x_cord, y=y_cord)
    def go_right(self):
        for part in self.parts:
            x_cord = part.xcor() + 20
            y_cord = part.ycor()
            part.goto(x=x_cord, y=y_cord)