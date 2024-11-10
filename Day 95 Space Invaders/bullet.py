from turtle import Turtle

class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.penup()
        self.shapesize(1, 0.1)

    def move(self):
        x = self.position()[0]
        y = self.position()[1]
        self.goto(x, y+20)