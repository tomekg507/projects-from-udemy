from turtle import Turtle

class EndGame(Turtle):
    def __init__(self):
        super().__init__()

    def win(self, font):
        self.write('You have won! :)', align='center', font=font)
        self.penup()

    def lose(self, font):
        self.write('You have lost! :(', align='center', font=font)
        self.penup()