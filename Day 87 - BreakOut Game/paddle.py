from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, y_position):
        super().__init__()
        self.shape('square')
        self.color('black')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=7)
        self.goto(x=0, y=y_position)

    def go_left(self):
        x_cord = self.xcor() - 30
        y_cord = self.ycor()
        self.goto(x=x_cord, y=y_cord)
    def go_right(self):
        x_cord = self.xcor() + 30
        y_cord = self.ycor()
        self.goto(x=x_cord, y=y_cord)