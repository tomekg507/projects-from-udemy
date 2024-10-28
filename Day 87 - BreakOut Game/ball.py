from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('black')
        self.penup()
        self.x_move = 10
        self.y_move = 10

    def move(self):
        x_cord = self.xcor() + self.x_move
        y_cord = self.ycor() + self.y_move
        self.goto(x=x_cord, y=y_cord)

    def bounce(self, direction):
        if direction in ['top', 'bottom']:
            self.y_move *= -1
        else:
            self.x_move *= -1

