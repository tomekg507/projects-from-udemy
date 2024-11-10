from turtle import Turtle
from bullet import Bullet

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        # self.shapesize(1,1)

    def go_left(self):
        x = self.position()[0]
        y = self.position()[1]
        self.goto(x-20,y)

    def go_right(self):
        x = self.position()[0]
        y = self.position()[1]
        self.goto(x+20,y)

    def shoot(self):
        bullet = Bullet()
        bullet.goto(0,20)