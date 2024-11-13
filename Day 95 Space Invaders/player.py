from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(0,-300)
        # self.shapesize(1,1)

    def go_left(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x-20,y)

    def go_right(self):
        x = self.xcor()
        y = self.ycor()
        self.goto(x+20,y)
    #
    # def shoot(self):
    #     bullet = Bullet()
    #     bullet.goto(0,20)