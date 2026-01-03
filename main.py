from pygame import *
# this is test

''' colors '''
background = (200,255,255)  # Red/Green/Blue


''' variables '''
width = 700
height = 500


window = display.set_mode( (width, height) )
window.fill(background)

clock = time.Clock()


game = True




''' game loop '''
while game: 

    for e in event.get():
        if e.type == QUIT:
            game = False


    display.update()
    clock.tick(60)



