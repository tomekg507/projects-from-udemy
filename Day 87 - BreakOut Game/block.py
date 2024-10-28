from turtle import Turtle

class Block(Turtle):
    def __init__(self, x_position, y_position):
        super().__init__()
        self.shape('square')
        self.color('blue')
        self.penup()
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.goto(x=x_position, y=y_position)
