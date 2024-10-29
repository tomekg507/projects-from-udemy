from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from block import Block
from endgame import EndGame

colors = ['blue', 'green', 'red', 'yellow']
FONT = ("Arial", 40, 'normal')


#---------------SCREEN--------------
screen = Screen()
screen.setup(width=800, height=600)
screen.tracer(0)

#--------------PADDLE AND BALL---------------
paddle = Paddle()
ball = Ball()

#--------------BLOCKS----------------------
blocks = []
for j in range(0,4):
    for i in range(0,8):
        block = Block(x_position=i*80-300, y_position=40*j+100, color=colors[j])
        blocks.append(block)

#--------------KEY_BINDINGS-----------
screen.listen()
screen.onkeypress(key='a', fun=paddle.go_left) #onkey - relese, onkeypress - pressed
screen.onkeypress(key='d', fun=paddle.go_right)

#-------------ENDGAME-------------------
endgame = EndGame()

#----------------GAME CODE-------------
game_is_on = True

while game_is_on:

    screen.update() #THIS is connected with screen.tracer(0), so things happen immediately
    time.sleep(ball.ball_speed)
    ball.move()

    #End of the game
    for part in paddle.parts:
        if part.distance(ball) < 21:
            ball.bounce(direction='top')
    if len(blocks) == 0:
        game_is_on = False
        screen.clear()
        endgame.win(FONT)

    for block in blocks:
        if block.distance(ball) < 41:
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
        game_is_on = False
        screen.clear()
        endgame.lose(FONT)

    screen.update()
screen.mainloop()