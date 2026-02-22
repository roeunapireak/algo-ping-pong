from pygame import *
from spriteClass import GameSprite, Player

background = (200,255,255)
width = 700
height = 500

window = display.set_mode( (width, height) )
display.set_caption('Ping Pong Game')

clock = time.Clock()

ball = GameSprite('./images/ball.png', 
                  width/2, height/2, 
                  50,50, 1)

racket1 = Player('./images/racket_left.png', 
                  5, 240, 
                  70, 150, 
                  3)

racket2 = Player('./images/Modified/racket_left.png', 
                  620, 240, 
                  70, 150, 
                  3)

font.init()
font1 = font.Font(None, 35)
player1_lose = font1.render('PLAYER 1 LOSES!', True, (180, 0, 0))
player2_lose = font1.render('PLAYER 2 LOSES!', True, (180, 0, 0))
speed_x = ball.speed
speed_y = ball.speed

game = True

finish = True

while game:

    if finish:
            
        window.fill(background)

        ball.reset(window)

        ball.rect.x += speed_x
        ball.rect.y += speed_y

        racket1.reset(window)
        racket1.update_racket1()

        racket2.reset(window)
        racket2.update_racket2()

        if ball.rect.y >= 440 or ball.rect.y <= 0 :
                speed_y *= -1
        if sprite.collide_rect(racket2,ball) or sprite.collide_rect(racket1,ball): 
                speed_x *= -1

        if ball.rect.x <= 0: 
            window.blit(player1_lose, (200, 200))
            finish = False

        if ball.rect.x >= 600: 
            window.blit(player2_lose, (200, 200))
            finish = False
    else:
          
        time.delay(3000) 

        ball.kill()
        

        ball = GameSprite('./images/ball.png', 
                  width/2, height/2, 
                  50,50, 1)

        finish = True


    for e in event.get():
        if e.type == QUIT:
            game = False

    display.update()
    clock.tick(60)