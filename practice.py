import pygame

# Initialize Pygame
pygame.init()

# Set the width and height of the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Scrolling Bullets Example")

# Set up the camera
camera_x = 0
camera_y = 0

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((32, 32))
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Update player's position relative to the camera's position
        self.rect.x += camera_x
        self.rect.y += camera_y

# Bullet class
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((8, 8))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

    def update(self):
        # Do not update bullet's position relative to the camera's position
        pass

# Create player
player = Player(400, 300)
all_sprites = pygame.sprite.Group(player)

# Create bullets
bullets = pygame.sprite.Group()
for i in range(10):
    bullet = Bullet(i * 50, 400)
    bullets.add(bullet)
    all_sprites.add(bullet)

# Game loop
running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Handle player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player.rect.x -= 5
    if keys[pygame.K_RIGHT]:
        player.rect.x += 5
    if keys[pygame.K_UP]:
        player.rect.y -= 5
    if keys[pygame.K_DOWN]:
        player.rect.y += 5

    # Scroll the camera with the player
    camera_x = -player.rect.x + screen_width // 2
    camera_y = -player.rect.y + screen_height // 2

    # Update all sprites
    all_sprites.update()

    # Clear the screen
    screen.fill((0, 0, 0))

    # Draw all sprites
    for sprite in all_sprites:
        screen.blit(sprite.image, (sprite.rect.x, sprite.rect.y))

    # Update the display
    pygame.display.flip()
    clock.tick(60)

# Quit the game
pygame.quit()
