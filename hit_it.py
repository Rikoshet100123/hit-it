from turtle import *
from random import randint
font_00 = ('Arial', 40, 'bold')

class Sprite(Turtle):
    def __init__(self, x, y, step, shape, color):
        super().__init__()
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.shape(shape)
        self.color(color)
        self.step = step

    

class Player(Sprite):
    def __init__(self):
        super().__init__(0, -180, 10, 'circle', 'orange')
        self.scr = self.getscreen()
        self.scr.listen()

        self.scr.onkey(self.stepRight, 'Right')
        self.scr.onkey(self.stepleft, 'left')
        self.scr.onkey(self.stepup, 'up')
        self.scr.onkey(self.stepdown, 'down')

        self.lives = 3
        self.score = 0
        self.score_win = 3

    def start(self):
        self.goto(0, -180)
    
    def stepup(self):
        self.goto(self.xcor(), self.ycor() + self.step)

    def stepdown(self):
        self.goto(self.xcor() , self.ycor() - self.step) 

    def stepleft(self):
        self.goto(self.xcor() - self.step, self.ycor())

    def stepRight(self):
        self.goto(self.xcor() + self.step, self.ycor())   

    def hit(self, obj):
        return self.distance(obj.xcor(), obj.ycor()) < 30



class Target(Sprite):
    def __init__(self):
        super().__init__(0, 200, 0, 'triangle', 'green')
        self.left(90)
        self.start()

    def start(self):
        self.goto(randint(-180, 180), randint(150,170))


class Enemy(Sprite):
    def __init__(self):
        super().__init__(randint(-200, 200), randint(-170, 200), 15, 'square', 'red')
        self.turn()

    def turn(self):
        self.x_end = randint(-200, 200)
        self.y_end = randint(-170, 200)
        self.setheading(self.towards(self.x_end, self.y_end))
        
    def move(self):
        self.forward(self.step)
        if self.distance(self.x_end, self.y_end) < self.step:
            self.turn()
    
player = Player()
target = Target()
enemy_00 = Enemy()
enemy_01 = Enemy()
enemy_02 = Enemy()
enemy_03 = Enemy()

is_run = True
while is_run:
    enemy_00.move()
    enemy_01.move()
    enemy_02.move()
    enemy_03.move()

    if player.hit(target):
        player.score += 1
        player.start()
        target.start()

    if player.hit(enemy_00) or player.hit(enemy_01) or player.hit(enemy_02) or player.hit(enemy_03):
        player.lives -= 1 
        player.start() 
    
    if player.score == player.score_win or player.lives == 0:
        is_run = False
    
player.hideturtle()
target.hideturtle()
enemy_00.hideturtle()
enemy_01.hideturtle()
enemy_02.hideturtle()
enemy_03.hideturtle()

if player.lives == 0:
    player.goto(-170, 20)
    player.color('red')
    player.write('game over!', font = font_00)
else:
    player.goto(-80, 20)
    player.color('green')
    player.write('you win', font = font_00)
