from turtle import Turtle, Screen
from random import randint

FONT = ('Arial', 18, 'bold')

# Up
def u():
    if h[0] != 270:
        h[0] = 90
# Down
def d():
    if h[0] != 90:
        h[0] = 270
# Left
def l():
    if h[0] != 0:
         h[0] = 180
# Right
def r():
    if h[0] != 180:
            h[0] = 0

def gameover():

    screen.onkey(None, "Up")
    screen.onkey(None, "Left")
    screen.onkey(None, "Right")
    screen.onkey(None, "Down")

    tscore.clear()
    tfood.clear()
    tplayer.clear()

    tfood.hideturtle()
    tplayer.hideturtle()

    tscore.color("red")

    tscore.goto(0, 150)
    tscore.write("Game Over", align="center", font=FONT)

    tscore.goto(0, 50)
    tscore.write("Score:" + str(a[0]), align="center", font=FONT)

    tscore.goto(0, -200)
    tscore.write("(Click anywhere to return to the main menu)", align="center", font=FONT)

    screen.onscreenclick(home)

def food(tfood):

    x = randint(-160, 160)
    y = randint(-160, 160)

    tfood.goto(x, y)
    tfood.showturtle()

def move():
    x, y = tplayer.position()

    if -210 < x < 210 and -210 < y < 210:
        if not tfood.isvisible():
            food(tfood)

        tplayer.setheading(h[0])
        tplayer.stamp()
        tplayer.forward(20)


        if b[0] > a[0]:
            tplayer.clearstamps(1)
            pos.insert(0, [round(x), round(y)])
            pos.pop(-1)
        else:
            pos.insert(0, [round(x), round(y)])
            b[0] += 1

        if tplayer.distance(tfood) < 15:
            tfood.hideturtle()
            tfood.clear()
            a[0] += 1
            tscore.clear()
            tscore.write("Score:" + str(a[0]), align="center", font=FONT)

        flag = True
        x, y = tplayer.position()

        if len(pos) > 1:
            for i in range(1, len(pos)):
                if pos[i][0] - 5 < x < pos[i][0] + 5 and pos[i][1] - 5 < y < pos[i][1] + 5:
                    flag = False
                    break

        if flag:
            screen.ontimer(move, 25)
    else:
        screen.ontimer(gameover, 100)

def level_1():

    tmarker.penup()
    tmarker.goto(-220, 220)
    tmarker.pendown()
    tmarker.goto(220, 220)
    tmarker.goto(220, -220)
    tmarker.goto(-220, -220)
    tmarker.goto(-220, 220)
    tmarker.penup()

def start(x, y):
    screen.onscreenclick(None)

    tscore.clear()

    level_1()

    tplayer.home()
    tplayer.setheading(h[0])

    tscore.goto(100, -250)
    tscore.write("Score:" + str(a[0]), align="center", font=FONT)

    screen.onkey(u, "Up")
    screen.onkey(l, "Left")
    screen.onkey(r, "Right")
    screen.onkey(d, "Down")

    move()

def home(x=0, y=0):
    screen.onscreenclick(None)

    a[0] = 0
    b[0] = 0
    h[0] = 0

    pos[:] = []

    tscore.clear()
    tscore.home()
    tscore.color('lime')
    tscore.write("PLAY", align="center", font=FONT)

    screen.onscreenclick(start)

# head orientation
h = [0]

# score
a = [0]
b = [0]

# position
pos = []

# turtles
tfood = Turtle('circle', visible=False)
tfood.speed('fastest')
tfood.color('red')
tfood.penup()

tscore = Turtle(visible=False)
tscore.speed('fastest')
tscore.penup()

tplayer = Turtle("square", visible=False)
tplayer.speed('slow')
tplayer.color("green")
tplayer.penup()

tmarker = Turtle(visible=False)
tmarker.speed('fastest')
tmarker.pensize(20)
tmarker.color("grey")

# # # # # # # # # # # # # # # # # # # # # #
# Main                                    #
# # # # # # # # # # # # # # # # # # # # # #
if __name__ == '__main__':
    screen = Screen()
    screen.title("Snake Game")
    screen.listen()

    home()

    screen.mainloop()