from pygame import *
from SpriteClass import GameSprite, Player

''' colors '''
background = (200,255,255)  # Red/Green/Blue


''' variables '''
width = 700
height = 500


window = display.set_mode( (width, height) )
# window.fill(background)

clock = time.Clock()


ball = GameSprite('./images/ball.png', width/2, height/2, 50,50, 3)
racket_left = Player('./images/racket_left.png', 2, height/2, 65,65, 3)
racket_right = Player('./images/Modified/racket_right.png', width-65, height/2, 65,65, 3)


game = True

ball_speed_x = ball.speed
ball_speed_y = ball.speed

font.init()
font1 = font.Font(None, 35)
lose_player_left = font1.render('LEFT PLAYER LOSES!', True, (180, 0, 0))
lose_player_right = font1.render('RIGHT PLAYER LOSES!', True, (180, 0, 0))

finish = True

''' game loop '''
while game: 

    if finish :
        window.fill(background)

        ball.reset(window)
        ball.rect.x -= ball_speed_x
        ball.rect.y -= ball_speed_y

        if ball.rect.y <= 2 or ball.rect.y >= 400:
            ball_speed_y *= -1
        if sprite.collide_rect(ball,racket_left) or sprite.collide_rect(ball, racket_right):
            ball_speed_x *= -1

        # win & lose 
        if ball.rect.x <= 0:
            window.blit(lose_player_left, ( (width/2)-90, (height/2)-30 ))
            finish = False

        if ball.rect.x >= (width-65):
            window.blit(lose_player_right, ( (width/2)-90, (height/2)-30 ))
            finish = False


        racket_left.reset(window)
        racket_left.update_left()

        racket_right.reset(window)
        racket_right.update_right()

    else:
        
        time.delay(1000)

        ball.rect.x = width/2
        ball.rect.y = height/2

        finish = True


    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()
    clock.tick(60)



