from turtle import Screen
from player import Player
from bullet import Bullet
import time

#-------------SCREEN --------------
screen = Screen()
screen.title('Space Invaders Game')
screen.bgcolor('black')

#-------------PLAYER---------------
player = Player()

#--------------MOVING --------------
bullet = []

def shoot():
    global bullet
    bullet = Bullet()

screen.listen()
screen.onkeypress(key='a', fun=player.go_left)
screen.onkeypress(key='d', fun=player.go_right)
screen.onkeypress(key='space', fun=shoot)

while True:
    screen.update()
    time.sleep(0.1)
    if bullet:
        bullet.move()



screen.mainloop()

