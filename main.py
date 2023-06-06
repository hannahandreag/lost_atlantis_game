# imports
import pygame, sys
from guizero import App, PushButton, Text, Box
from settings import *

# main function
def game():
    from level import Level
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))
    clock = pygame.time.Clock()
    level = Level(level_map, screen)
    time_text = ""

    # text
    pygame.font.init()
    font = pygame.font.Font("fonts/PressStart2P-Regular.ttf", 32)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # will happen when the user clicks on the cross at the top of the screen
                pygame.quit()
                sys.exit()

        # stopwatch
        ticks = pygame.time.get_ticks()
        if level.player.sprite.alive:
            seconds = int(ticks/1000 % 60)
            minutes = int(ticks/60000 % 24)
        out = '{minutes:02d}:{seconds:02d}'.format(minutes=minutes, seconds=seconds)
        pygame.display.flip()

        time_text = font.render("time:" + str(out), True, (255, 255, 255), (0, 0, 0))

        # background colour
        screen.fill("#006fff")

        level.run()

        # timer text
        screen.blit(time_text, (0,0))

        pygame.display.update()

        clock.tick(fps)


# instructions screen
def run():
    game()
    app.destroy()

# guizero
def start_screen():
    app = App(title="instructions", width=500, height=400)
    app.bg = "#FF34B3"

    box_left = Box(app, height="fill", width = 50, align="left")
    box_right = Box(app, height="fill", width = 50, align="right")
    box_top = Box(app, width="fill", height=20, align="top")
    name = Box(app, width="fill", height=70, align="top")
    spacer = Box(app, width="fill", height=5, align="top")
    rule_title = Box(app, width="fill", height=50, align="top")
    spacer_2 = Box(app, width="fill", height=5, align="top")
    text_box = Box(app, width="fill", height= 150, align="top")
    spacer_3 = Box(app, width="fill", height= 10, align="top")
    spacer_4 = Box(app, width="fill", height= 50, align="bottom")


    button = PushButton(app, command=run, align="bottom", text="play")
    title_text = Text(name, text="Lost Atlantis", color="white", size=70)
    rule_title_text = Text(rule_title, text="how to play", color="white", size=30)
    text = Text(text_box, color="white", size=20, text="your goal is to find the treasure", align="top")
    text_1 = Text(text_box, color="white", size=20, text="use the arrow keys to move around", align="top")
    text_2 = Text(text_box, color="white", size=20, text="avoid the seaweed and shooting seashells", align="top")
    text_3 = Text(text_box, color="white", size=20, text="fastest time wins!", align="top")

    app.display()


start_screen()
