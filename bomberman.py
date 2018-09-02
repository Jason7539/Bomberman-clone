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
    screen = pygame.display.set_mode(screen_size)

    # upload the background
    background = pygame.image.load(os.path.join("images", "background.png")) 

    # load the hard blocks images 
    hard_blocks = pygame.image.load(os.path.join("images", "hard-block.png"))

    # draw the hard blocks on the background
    background.blit(hard_blocks, (0,0))

    # draw background on the screen 
    screen.blit(background, (0,0))

    
    #create game objects
    p1 = Player.PlayerOne()
    one_group = pygame.sprite.Group(p1)
    
    one_group.draw(screen)
    #main loop
    while 1:
        #makes the game run at 60 fps 
        clock.tick(60)
        for event in pygame.event.get():
            # quit the game and exit the program if the close button is clicked 
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        one_group.update()
        one_group.draw(screen)
        
        pygame.display.update()


main()


