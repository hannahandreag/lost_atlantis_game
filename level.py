import pygame
from settings import tile_size, screen_width
from tile import Tile
from player import Player

# level class
class Level:
    def __init__(self, level_data, surface):
        self.display_surface = surface
        self.tiles = pygame.sprite.Group()
        self.spikes = pygame.sprite.Group()
        self.fire = pygame.sprite.Group()
        self.end = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.setup_level(level_data)

        self.world_shift = 0

        # music
        pygame.mixer.music.load("sounds/music/glide.mp3")
        pygame.mixer.music.play(-1) # -1 --> loop

    # creating the different tiles
    def setup_level(self, layout):
        for row_index, row in enumerate(layout):
            for cell_index, cell in enumerate(row):
                x = cell_index * tile_size
                y = row_index * tile_size
                if cell == "x":
                    tile = Tile((x,y), (tile_size, tile_size), "graphics/sand_sprite.png", 0, self.display_surface)
                    self.tiles.add(tile)
                elif cell == "p":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                elif cell == "s":
                    spike = Tile((x,y), (tile_size, tile_size), "graphics/seaweed_sprite.png", 1, self.display_surface)
                    self.spikes.add(spike)
                elif cell == "f":
                    fire = Tile((x,y), (tile_size,tile_size), "graphics/seashell_sprite.png", 2, self.display_surface)
                    self.fire.add(fire)
                elif cell == "e":
                    end = Tile((x,y), (tile_size,tile_size), "graphics/coin_sprite.png", 3, self.display_surface)
                    self.end.add(end)

    # scrolling
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x > screen_width - (screen_width / 2) and direction_x > 0:
            self.world_shift = -5
            player.speed = 0
        elif player_x < screen_width / 2 and direction_x < 0:
            self.world_shift = 5
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 5

    # updates
    def run(self):
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)

        self.spikes.update(self.world_shift)
        self.spikes.draw(self.display_surface)

        self.fire.update(self.world_shift)
        self.fire.draw(self.display_surface)

        self.end.update(self.world_shift)
        self.end.draw(self.display_surface)

        self.scroll_x()

        self.player.draw(self.display_surface)
        self.player.update(self.tiles, self.spikes, self.fire, self.end)


