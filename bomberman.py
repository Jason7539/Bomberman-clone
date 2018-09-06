import pygame, sys, os, time
from pygame.event import clear
from pygame.locals import *
import Player, bombs

# to do list
# maybe make a start screen play, options etc
# test collide
# turn the map creation into a method
# maybe change border and put it in the game map
# work on bombs and placing bombs 


# makes the game window centered 
os.environ['SDL_VIDEO_CENTERED'] = '1'

# test collison
def test_collision(rect, list_rect):
    """ test whether rect collides with any rects in list rects and return that lsit of rects"""
    collide_list = []
    for r in list_rect:
        if rect.colliderect(r):
            collide_list.append(r)
    return collide_list
            

# move rect. if a rect collides with a list of rects based on movement
def move(rect, direction, list_rect, speed):
    # see where the collision occures 
    dict_direction = {"top" : False, "bottom" : False, "right" : False, "left" : False}

    # move the rect if it collides with list_rect stop the collision 
    if direction == "top": 
        rect.top += speed # move the rect 
        collide_list = test_collision(rect, list_rect) # test if it collide 

        for r in collide_list: # prevent the rect from colliding 
            rect.top = r.bottom
        
    elif direction == "down":
        rect.bottom += speed # move the rect 
        collide_list = test_collision(rect, list_rect) # test if it collide 

        for r in collide_list: # prevent the rect from colliding 
            rect.bottom = r.top
    elif direction == "left":
        rect.left += speed # move the rect 
        collide_list = test_collision(rect, list_rect) # test if it collide 

        for r in collide_list: # prevent the rect from colliding 
            rect.left = r.right
    elif direction == "right":
        rect.right += speed # move the rect 
        collide_list = test_collision(rect, list_rect) # test if it collide 

        for r in collide_list: # prevent the rect from colliding 
            rect.right = r.left




# intialize variables and main game loop 
def main():
    pygame.init() # initializes pygame
    pygame.display.set_caption("Bomberdude")
    # clock object used to control fps
    clock = pygame.time.Clock()

    # tuple representing the x and y value of the window
    # x = 1050, y = 910
    screen_size = (15 * 70, 13 * 70)

    # create a window where the background will be drawn with the same size of the background
    screen = pygame.display.set_mode(screen_size, RESIZABLE)

    # upload the background
    background = pygame.image.load(os.path.join("images", "background.png"))

    # new background used to clear old player model
    new_background = pygame.image.load(os.path.join("images", "background.png"))
    # new_background = pygame.Surface((1050, 910))
    # new_background.fill((Color("gold")))

    # load the hard blocks images
    hard_blocks = pygame.image.load(os.path.join("images", "hard-block.png"))

    # the size of hard blocks used work with borders
    x_block, y_block = hard_blocks.get_size()

    # turn this into a method
    # draw the hard blocks on the background
    # # draw to top borders
    top_x = 0
    for i in range(0, 14):
        background.blit(hard_blocks, (top_x, 0))
        top_x += x_block

    # draw the right border
    right_y = 0
    for i in range(0, 13):
        background.blit(hard_blocks, (top_x, right_y))
        right_y += x_block

    # draw the left border
    left_y = 0
    for i in range(0, 13):
        background.blit(hard_blocks, (0, left_y))
        left_y += x_block

    # draw the bottom border
    left_y -= x_block
    bottom_x = 0
    for i in range(0, 14):
        background.blit(hard_blocks, (bottom_x, left_y))
        bottom_x += x_block

    # draw the impassable blocks inside the borders
    # 2d list representing the inner map 0s symbolizes empty space and 1s are impassable blocks
    inner_map = [['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                 ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
                 ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                 ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
                 ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                 ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
                 ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                 ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
                 ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
                 ['0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0', '1', '0'],
                 ['0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0', '0']]


    # creates the inner blocks and rectangles associated with each one
    impassable_blocks = [] # list used to store the rectangle of impassable blocks
    y = 1 # keep track of what row we are printing
    for rows in inner_map:
        x = 1 # keeps track of which column
        for tile in rows:
            if tile == "0":
                pass
            elif tile == "1":
                background.blit(hard_blocks,( x * x_block, y *y_block)) # draw a block on the background
                impassable_blocks.append(Rect(x * x_block, y * y_block, x_block, y_block))
            x += 1

        y += 1




    # draw background on the screen
    screen.blit(background, (0, 0))

    # create user controlled objects
    p1 = Player.PlayerOne()
    one_group = pygame.sprite.Group(p1)

    p2 = Player.PlayerTwo()
    two_group = pygame.sprite.Group(p2)



    # variable that updates player movement
    location_one = ""
    location_two = ""

    # list that keep tracks and updates the bombs player1 drops
    p1_bombs = pygame.sprite.Group()

    # messing with bomb reload
    blomb = pygame.USEREVENT + 1
    exploded = 0
    # main loop
    while 1:
        # makes the game run at 60 fps
        clock.tick(60)

        for event in pygame.event.get():
            if event.type == pygame.USEREVENT + 1:
                print("boom")
            
            # quit the game and exit the program if the close button is clicked
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

            # read and respond when a key is pressed down
            elif event.type == KEYDOWN:
                # pause the game
                if event.key == K_ESCAPE:
                    main()
                    pygame.time.delay(1000)

                # control player one  movement
                if event.key == K_w:
                    location_one = "up"
                elif event.key == K_s:
                    location_one = "down"
                elif event.key == K_a:
                    location_one = "left"
                elif event.key == K_d:
                    location_one = "right"
                # place bombs
                if event.key == K_SPACE:
                    print("space")
                    # control that you only drop a bomb                     
                    print("Official = ",pygame.time.get_ticks())
                    p1_bombs.add(p1.drop_bomb())



                # control player two movement
                if event.key == K_UP:
                    location_two = "up"
                elif event.key == K_DOWN:
                    location_two = "down"
                elif event.key == K_LEFT:
                    location_two = "left"
                elif event.key == K_RIGHT:
                    location_two = "right"


            elif event.type == KEYUP:
                # process controls player one movement when a key is let go
                if event.key == K_w:
                    location_one = ""
                elif event.key == K_s:
                    location_one = ""
                elif event.key == K_a:
                    location_one = ""
                elif event.key == K_d:
                    location_one = ""

                # process controls for player two movement when a key is let go
                if event.key == K_UP:
                    location_two = ""
                elif event.key == K_DOWN:
                    location_two = ""
                elif event.key == K_LEFT:
                    location_two = ""
                elif event.key == K_RIGHT:
                    location_two = ""
                elif event.key == K_0 or event.key == K_KP0:
                    print("zero")
                    

        # prevents the player  one from going through the borders
        if location_one == "left" and p1.rect.x <= x_block:
            location_one = ""
        if location_one == "right" and p1.rect.x + p1.rect.width >= (screen.get_width() - x_block):
            location_one = ""
        if location_one == "up" and p1.rect.y <= y_block:
            location_one = ""
        if location_one == "down" and p1.rect.y + p1.rect.height >= (screen.get_height() - y_block):
            location_one = ""

        # prevents the player two from going through the borders
        if location_two == "left" and p2.rect.x <= x_block:
            location_two = ""
        if location_two == "right" and p2.rect.x + p2.rect.width >= (screen.get_width() - x_block):
            location_two = ""
        if location_two == "up" and p2.rect.y <= y_block:
            location_two = ""
        if location_two == "down" and p2.rect.y + p2.rect.height >= (screen.get_height() - y_block):
            location_two = ""

        # test collision test_collison(rect, location, rect_list)
        


        one_group.update(impassable_blocks, location_one)
        one_group.clear(screen, background)
        one_group.draw(screen)

        two_group.update(impassable_blocks, location_two)
        two_group.clear(screen, background)
        two_group.draw(screen)

        # keeps track of player one bombs 
        p1_bombs.update(pygame.time.get_ticks(), p1_bombs, screen, background)
        
        # get a list of active bombs 
        p1_active_bombs = p1_bombs.sprites()

        # remove the bomb from group list after it explodes 
        for booms in p1_active_bombs:
            if booms.exploding_state == 2:
                print(p1_bombs.sprites())
                booms.clear(screen, background)
                p1_bombs.remove(booms)
                print(p1_bombs.sprites())
                
        p1_bombs.draw(screen)

        # draw the player hitbox
        #pygame.draw.rect(screen, Color("gold"), p1.rect)
                                 

        pygame.display.update()
        

        pygame.event.pump()  # clear the event queue
        


main()
