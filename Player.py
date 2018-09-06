import pygame, sys, os, time, util
from pygame.event import clear
from pygame.locals import *
import bombs


# to do list
# need to update image to choose from a list to creat animation
# you can place one bomb every x amount of seconds
# put movement in a array to allow for multiple angles \
# mess with drop bombs so that player can onyl drop one bombs per 2 sec 

class Player(pygame.sprite.Sprite):
    """ Parent class that User controls """

    def __init__(self, speed=None):
        pygame.sprite.Sprite.__init__(self)  # initiate the sprite class

    def pickup(pickups):
        bombs.add_effects(pickups)

    def test_collision(rect, list_rect):
        collide_list = []
        for r in list_rect:
            if rect.colliderect(r):
                collide_list.append(r)
        return collide_list
                
class PlayerOne(Player):
    """ Actual object that Player one interacts with   """

    # change this for animation
    def __init__(self):
        """ Constructor """
        Player.__init__(self)
        self.speed = 5 # variables that controls how fast the player moves 

        self.image, self.rect = util.load_image(os.path.join('images', 'player-one.png'))
        self.rect.x = 70 # set initial x position 
        self.rect.y = 70 # set initial y position
        self.direction_list = []

        self.max_bombs = 1 # keeps track of how many bombs the player is currently holding
        self.current_bombs = 1 # keeps track of how many bombs the player is currently holding

    def drop_bomb(self):
        """ Drop bombs"""
        if self.current_bombs > -100:
            self.current_bombs -= 1
            b = bombs.Bomb(self.rect.x, self.rect.y)
            return b

        def refill_bombs(self):
            pass 

    def update(self, list_rect, location): # and test for collison # keeps track of bombs

        " Move the player position based on the the speed variable and the location argument"
        if location is "up":
            self.rect.top -= self.speed # move the rect 
            collide_list = Player.test_collision(self.rect, list_rect) # test if there was a collision
            for r in collide_list: # prevent moving the rect if there was a collision
                self.rect.top = r.bottom
            
        elif location is "down":
            self.rect.bottom += self.speed
            collide_list = Player.test_collision(self.rect, list_rect) # test if there was a collision
            for r in collide_list: # prevent moving the rect if there was a collision
                self.rect.bottom = r.top
                
        elif location is "right":
            self.rect.right += self.speed
            collide_list = Player.test_collision(self.rect, list_rect) # test if there was a collision
            for r in collide_list: # prevent moving the rect if there was a collision
                self.rect.right = r.left
                
        elif location is "left":
            self.rect.left -= self.speed
            collide_list = Player.test_collision(self.rect, list_rect) # test if there was a collision
            for r in collide_list: # prevent moving the rect if there was a collision
                self.rect.left = r.right

        # place bombs 







class PlayerTwo(Player):
    """ Actual object that Player two interacts with   """

    # change this for animation
    def __init__(self):
        """ Constructor """
        Player.__init__(self)
        self.speed = 5

        self.image, self.rect = util.load_image(os.path.join('images', 'player-two.png'))
        self.rect.x = 910
        self.rect.y = 770

    def update(self, list_rect, location=None):

        " Move the player position based on the the speed variable and the location argument"
        if location is "up":
            self.rect.top -= self.speed # move the rect 
            collide_list = Player.test_collision(self.rect, list_rect) # test if there was a collision
            for r in collide_list: # prevent moving the rect if there was a collision
                self.rect.top = r.bottom
            
        elif location is "down":
            self.rect.bottom += self.speed
            collide_list = Player.test_collision(self.rect, list_rect) # test if there was a collision
            for r in collide_list: # prevent moving the rect if there was a collision
                self.rect.bottom = r.top
                
        elif location is "right":
            self.rect.right += self.speed
            collide_list = Player.test_collision(self.rect, list_rect) # test if there was a collision
            for r in collide_list: # prevent moving the rect if there was a collision
                self.rect.right = r.left
                
        elif location is "left":
            self.rect.left -= self.speed
            collide_list = Player.test_collision(self.rect, list_rect) # test if there was a collision
            for r in collide_list: # prevent moving the rect if there was a collision
                self.rect.left = r.right


    def get_speed():
        return self.speed
    
