from turtle import Screen
import time
from paddle import Paddle
from ball import Ball
from block import Block

#---------------SCREEN--------------
screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

#--------------PADDLE AND BALL---------------
paddle = Paddle(y_position=-250)
ball = Ball()

#--------------BLOCKS----------------------
blocks = []
for j in range(0,3):
    for i in range(0,6):
        block = Block(x_position=i*120-300, y_position=40*j+150)
        blocks.append(block)
print(blocks)
#--------------KEY_BINDINGS-----------
screen.listen()
screen.onkey(key='d', fun=paddle.go_right)
screen.onkey(key='a', fun=paddle.go_left)

game_is_on = True
while game_is_on:
    screen.update() #THIS is connected with screen.tracer(0), so things happen immediately
    time.sleep(0.01)
    ball.move()

    #End of the game
    if paddle.distance(ball) < 20:
        ball.bounce(direction='top')
    if len(blocks) == 0:
        game_is_on = False

    for block in blocks:
        if block.distance(ball) < 40:
            block.goto(x=1000, y=1000)
            blocks.remove(block)
            ball.bounce(direction='bottom')
    if ball.xcor() >= 390:
        ball.bounce(direction='left')
    elif ball.xcor() <= -390:
        ball.bounce(direction='right')
    elif ball.ycor() >= 290:
        ball.bounce(direction='bottom')
    elif ball.ycor() <=-290:
        # game_is_on = False
        ball.bounce(direction='top')

screen.exitonclick()