from turtle import Turtle

class Barrier:
    def __init__(self):
        self.barrier = []

    def create_barrier(self, x):
        for i in range(0,8):
            for j in range(0,3):
                part_of_barrier = Turtle()
                part_of_barrier.shape('square')
                part_of_barrier.color('white')
                part_of_barrier.penup()
                part_of_barrier.goto(x + 25 * i, -200 + 25 * j)
                self.barrier.append(part_of_barrier)