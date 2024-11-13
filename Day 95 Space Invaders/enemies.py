from turtle import Turtle

class Enemies:
    def __init__(self):
        self.all_enemies = []
        self.speed = 0.1

    def create_enemies(self):
        for i in range(0,8):
            for j in range(0,3):
                enemy = Turtle()
                enemy.shape('square')
                enemy.color('white')
                enemy.penup()
                enemy.goto(-400 + 40*i,200 + 40*j)
                self.all_enemies.append(enemy)



