import pygame
import random
from bullet import Bullet

r_num = random.randint(1, 100)

# tile cass
class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size, image, type, surface):
        super().__init__()
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect(topleft=pos)
        self.type = type
        self.surface = surface

        # shooting
        self.bullets = pygame.sprite.Group()
        self.firing = True
        self.fire_now = random.randint(0, 60)
        self.fire_count = 0

    # firing
    def fire(self):
        global r_num
        bullet = Bullet((self.rect.centerx, self.rect.centery), 1)
        self.bullets.add(bullet)

    # updates
    def update(self, x_shift):
        global r_num
        self.rect.x += x_shift

        # generating random bullets
        self.fire_count += 1
        if self.fire_count == self.fire_now and self.type == 2:
            self.fire()
            self.fire_count = 0
            self.fire_now = random.randint(0, 360)

        self.bullets.update(x_shift)
        self.bullets.draw(self.surface)


