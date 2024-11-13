from turtle import Screen, Turtle
from player import Player
from bullet import Bullets
from enemies import Enemies
from random import randint
import time


#------------------CONSTANTS--------------------
i = 0
j = 0
direction = 0
flag = True

#---------------- INITIALIZATION---------------
player = Player()
bullets = Bullets()
enemies = Enemies()

#--------------GAME OVER-----------------
def gameover():
    game_over = Turtle()
    game_over.color('white')
    game_over.write('Game Over', font=("Arial", "40", "bold"), align='center')


#------MOVING ENEMIES IN GIVEN DIRECTION AND RESETTING THE INDEX--------
def move_enemies(direction):
    for enemy in enemies.all_enemies:
        enemy.setheading(direction)
        enemy.forward(20)
    return 0

#--------------- ENEMY SHOOTS ----------------
def enemy_shoot():
    random_enemy = randint(0, len(enemies.all_enemies) - 1)
    xcor = enemies.all_enemies[random_enemy].xcor()
    ycor = enemies.all_enemies[random_enemy].ycor()
    bullets.enemy_bullets_create(xcor, ycor)

#----------------MAIN PART OF GAME------------------
def game():
    global i,j, direction, flag

    screen.update()

    # MOVING BULLETS
    if len(bullets.all_player_bullet) > 0:
        bullets.player_bullet_move()
    if len(bullets.all_enemy_bullets) > 0:
        bullets.enemy_bullet_move()

    # ENEMY SHOOTING
    if randint(1,10) == 1:
        enemy_shoot()

    # MOVING ENEMIES EVERY 4 ITERATION
    if i == 4:
        i = move_enemies(direction)
        j += 1
    # CHANGING DIRECTION EVERY 4*20 ITERATIONS
    if j == 20:
        direction = 180
    elif j == 40:
        move_enemies(270)
        direction = 0
        j = 0

    i += 1

    # ENEMY HIT
    for enemy in enemies.all_enemies:
        if len(bullets.all_player_bullet) > 0:
            if enemy.distance(bullets.all_player_bullet[0]) < 19:
                enemy.reset()
                enemies.all_enemies.remove(enemy)
                # removing players bullet on hit
                bullets.all_player_bullet[0].reset()
                del bullets.all_player_bullet[0]

    # PLAYER HIT
    for enemy_bullet in bullets.all_enemy_bullets:
        if enemy_bullet.distance(player) < 19:
            flag = False
            screen.ontimer(gameover, 50)

    # REPEATING EVERYTHING EVERY TIME
    if flag == True:
        screen.ontimer(game, 50)


#------------ ENEMIES AND KEYS------------------------
def home():
    screen.onkeypress(key='a', fun=player.go_left)
    screen.onkeypress(key='d', fun=player.go_right)
    # Player can only have 1 bullet at a time
    screen.onkeypress(key='space', fun=lambda: bullets.player_bullet_create(player.xcor(), player.ycor()) if len(bullets.all_player_bullet) < 1
                      else None)

    enemies.create_enemies()
    screen.update()
    game()

#-------------SCREEN --------------
screen = Screen()
screen.title('Space Invaders Game')
screen.bgcolor('black')
screen.tracer(False)
screen.listen()

home()

screen.mainloop()


