import pygame
from settings import screen_width

# bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, pos, direction):
        super().__init__()
        self.image = pygame.image.load("graphics/pearl_sprite.png")
        self.image = pygame.transform.scale(self.image, (40,40))
        self.rect = self.image.get_rect(topleft=pos)
        self.rect.x -= 20
        self.speed = 1
        self.direction = pygame.math.Vector2(0, direction * self.speed)

    # update
    def update(self, x_shift):
        self.rect.y += self.direction.y
        self.rect.x += x_shift
        if self.rect.x > screen_width or self.rect.x < 0:
            self.kill()
