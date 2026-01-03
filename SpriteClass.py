from pygame import *

class GameSprite(sprite.Sprite):
    ''' constructor ''' 
    def __init__(self, player_image, player_x, player_y, image_width, image_height, player_speed):
        super().__init__()
        self.image = transform.scale(image.load(player_image), (image_width, image_height))
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
        self.speed = player_speed

        self.window = None

    def reset(self, window):
        self.window = window
        self.window.blit(self.image, (self.rect.x, self.rect.y))


class Player(GameSprite):
    
    def update_left(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 2:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < 435:
            self.rect.y += self.speed

    def update_right(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 2:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < 435:
            self.rect.y += self.speed

