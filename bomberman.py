import pygame, sys, os, time
from pygame.event import clear
from pygame.locals import *
import Player

# to do list
# maybe make a start screen play, options etc 

# makes the game window centered 
os.environ['SDL_VIDEO_CENTERED'] = '1'


def main():
    # initializes pygame 
    pygame.init()

    # clock object used to control fps 
    clock = pygame.time.Clock()

    # tuple representing the x and y value of the window
    # x = 1050, y = 910
    screen_size = (15 * 70, 13 * 70)

    # create a window where the background will be drawn with the same size of the background
    screen = pygame.display.set_mode(screen_size, RESIZABLE)

    # upload the background
    background = pygame.image.load(os.path.join("images", "background.png"))

    #new background to clear
    new_background = pygame.image.load(os.path.join("images", "background.png"))
    # new_background = pygame.Surface((1050, 910))
    # new_background.fill((Color("gold")))

    # load the hard blocks images
    hard_blocks = pygame.image.load(os.path.join("images", "hard-block.png"))

    # turn this into a method
    # draw the hard blocks on the background

    # # draw to top borders
    top_x = 0
    for i in range(0, 14):
        background.blit(hard_blocks, (top_x, 0))
        top_x += 70

    # draw the right border
    right_y = 0
    for i in range(0, 13):
        background.blit(hard_blocks, (top_x, right_y))
        right_y += 70

    # draw the left border
    left_y = 0
    for i in range(0, 13):
        background.blit(hard_blocks, (0, left_y))
        left_y += 70

    # draw the bottom border
    left_y -= 70
    bottom_x = 0
    for i in range(0, 14):
        background.blit(hard_blocks, (bottom_x, left_y))
        bottom_x += 70

    # draw background on the screen
    screen.blit(background, (0, 0))

    # create game objects
    p1 = Player.PlayerOne()
    one_group = pygame.sprite.Group(p1)

    # variable that updates player movement
    location = ""

    # main loop
    while 1:
        # makes the game run at 60 fps
        clock.tick(60)
        for event in pygame.event.get():
            # quit the game and exit the program if the close button is clicked
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # read and respond when a key is pressed down
            elif event.type == KEYDOWN:
                # pause the game
                if event.key == K_ESCAPE:
                    pygame.time.delay(1000)

                # control player movement
                if event.key == K_w:
                    location = "up"
                elif event.key == K_s:
                    location = "down"
                elif event.key == K_a:
                    location = "left"
                elif event.key == K_d:
                    location = "right"

            elif event.type == KEYUP:
                # process controls player movement when a key is let go
                if event.key == K_w:
                    location = ""
                elif event.key == K_s:
                    location = ""
                elif event.key == K_a:
                    location = ""
                elif event.key == K_d:
                    location = ""



        one_group.update(location)
        one_group.clear(screen, new_background)
        one_group.draw(screen)


        pygame.display.update()

        pygame.event.pump() # clear the event queue


main()