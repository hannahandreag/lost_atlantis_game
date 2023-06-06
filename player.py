import pygame
from settings import screen_height, screen_width


screen = pygame.display.set_mode((screen_width, screen_height))
pygame.font.init()

# game text
font1 = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 100)
text = font1.render("game over", True, (255, 255, 255), (60, 0, 100)) # text color, background colour
end_text = font1.render(" you won! ", True, (255, 255, 255), (60, 0, 100))

# player class
class Player(pygame.sprite.Sprite):
    def __init__(self, pos):
        super().__init__()
        # self.image = pygame.Surface((32, 64))
        # self.image.fill("red")
        self.image = pygame.image.load("graphics/octopus_sprite.png")
        self.image = pygame.transform.scale(self.image, (64, 64))
        self.offset = (-40, -40)

        self.rect = self.image.get_rect(topleft=pos)

        # sound effecting
        self.collide_sound = pygame.mixer.Sound("sounds/effects/bubble.wav")

        # hit box
        self.hitbox = self.rect.inflate(self.offset[0], self.offset[1])

        self.direction = pygame.math.Vector2(0,0)
        self.speed = 6
        self.alive = True

    # function for movement
    def get_input(self):
        keys = pygame.key.get_pressed()
        if self.alive:
            if keys[pygame.K_RIGHT]:
                self.direction.x = 1
            elif keys[pygame.K_LEFT]:
                self.direction.x = -1
            elif keys[pygame.K_UP]:
                self.direction.y = -1
            elif keys[pygame.K_DOWN]:
                self.direction.y = 1
            else:
                self.direction.x = 0
                self.direction.y = 0


    # functions for collisions
    def horizontal_movement_collision(self, tiles):
        self.hitbox.x += self.direction.x * self.speed

        for tile in tiles.sprites():
            if tile.rect.colliderect(self.hitbox):
                if self.direction.x < 0: # moving to the left
                    self.hitbox.left = tile.rect.right
                elif self.direction.x > 0: # moving to the right
                    self.hitbox.right = tile.rect.left

    def vertical_movement_collision_down(self, tiles):
        self.hitbox.y += self.direction.y * self.speed
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.hitbox):
                if self.direction.y > 0:
                    self.hitbox.bottom = tile.rect.top
                    self.direction.y = 0

    def vertical_movement_collision_up(self, tiles):
        self.hitbox.y += self.direction.y * self.speed
        for tile in tiles.sprites():
            if tile.rect.colliderect(self.hitbox):
                if self.direction.y < 0:
                    self.hitbox.top = tile.rect.bottom
                    self.direction.y = 0

    def spike_collision_up(self, spikes):
        for spike in spikes.sprites():
            if spike.rect.colliderect(self.hitbox):
                pygame.mixer.Sound.play(self.collide_sound)
                self.hitbox.bottom = spike.rect.top
                self.alive = False
                screen.blit(text, (280,325))

    def spike_collision_down(self, spikes):
        for spike in spikes.sprites():
            if spike.rect.colliderect(self.hitbox):
                pygame.mixer.Sound.play(self.collide_sound)
                self.hitbox.top = spike.rect.bottom
                self.alive = False
                screen.blit(text, (280,325))

    def spike_collision_right(self, spikes):
        for spike in spikes.sprites():
            if spike.rect.colliderect(self.hitbox):
                pygame.mixer.Sound.play(self.collide_sound)
                self.hitbox.left = spike.rect.right
                self.alive = False
                screen.blit(text, (280,325))

    def spike_collision_left(self, spikes):
        for spike in spikes.sprites():
            if spike.rect.colliderect(self.hitbox):
                pygame.mixer.Sound.play(self.collide_sound)
                self.hitbox.right = spike.rect.left
                self.alive = False
                screen.blit(text, (280,325))

    def bullet_collision(self, bullets):
        for bullet in bullets:
            if bullet.rect.colliderect(self.hitbox):
                pygame.mixer.Sound.play(self.collide_sound)
                self.alive = False
                screen.blit(text, (280,325))

    def end_collision(self, end):
        for end in end.sprites():
            if end.rect.colliderect(self.hitbox):
                pygame.mixer.Sound.play(self.collide_sound)
                self.alive = False
                screen.blit(end_text, (240,325))

    # updates
    def update(self, tiles, spikes, fire, end):
        self.get_input()
        self.horizontal_movement_collision(tiles)
        self.vertical_movement_collision_down(tiles)
        self.vertical_movement_collision_up(tiles)
        self.spike_collision_up(spikes)
        self.spike_collision_down(spikes)
        self.spike_collision_right(spikes)
        self.spike_collision_left(spikes)
        self.end_collision(end)

        # bullet collision
        for e in fire:
            if len(e.bullets) > 0:
                self.bullet_collision(e.bullets)

        self.rect = self.hitbox.inflate(self.offset[0] * -1, self.offset[1] * -1)

        if not self.alive:
            self.speed = 0


