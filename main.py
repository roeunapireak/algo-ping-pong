from pygame import *
from spriteClass import GameSprite

background = (200,255,255)
width = 700
height = 500

window = display.set_mode( (width, height) )
display.set_caption('Ping Pong Game')

clock = time.Clock()

ball = GameSprite('./images/ball.png', 
                  width/2, height/2, 
                  50,50, 3)

game = True

while game:

    window.fill(background)

    ball.reset(window)


    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)