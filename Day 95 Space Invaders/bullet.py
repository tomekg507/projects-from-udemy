from turtle import Turtle

class Bullets:
    def __init__(self):
        self.all_player_bullet = []
        self.all_enemy_bullets = []
        self.speed = 0.1

    def player_bullet_create(self,x,y):
        new_bullet = Turtle()
        new_bullet.color('white')
        new_bullet.shape('square')
        new_bullet.penup()
        new_bullet.shapesize(0.1, 1)
        new_bullet.goto(x,y)
        self.all_player_bullet.append(new_bullet)

    def player_bullet_move(self):
        for bullet in self.all_player_bullet:
            bullet.setheading(90)
            bullet.forward(20)
            if bullet.ycor() > 400:
                self.all_player_bullet.remove(bullet)

    def enemy_bullets_create(self,x,y):
        new_bullet = Turtle()
        new_bullet.color('white')
        new_bullet.shape('square')
        new_bullet.penup()
        new_bullet.shapesize(0.1, 1)
        new_bullet.goto(x,y)
        self.all_enemy_bullets.append(new_bullet)

    def enemy_bullet_move(self):
        for bullet in self.all_enemy_bullets:
            bullet.setheading(270)
            bullet.forward(20)
            if bullet.ycor() < -400:
                self.all_enemy_bullets.remove(bullet)