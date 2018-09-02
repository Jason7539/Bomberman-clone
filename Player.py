import pygame, sys, os, time, util
from pygame.event import clear
from pygame.locals import *
import bombs
# to do list
# need to update image to choose from a list to creat animation 
# you can place one bomb every x amount of seconds 

class Player(pygame.sprite.Sprite):
    """ Parent class that User controls """
    
    def __init__(self, speed = None):
        pygame.sprite.Sprite.__init__(self)  # initiate the sprite class
        bomb = bombs.Bomb()

    def pickup(pickups):
        bombs.add_effects(pickups)



class PlayerOne(Player):
    """ Actual object that Player one interacts with   """

    # change this for animation 
    def __init__(self):
        """ Constructor """
        
        Player.__init__(self)
        self.speed = 10
        
        self.image, self.rect = util.load_image(os.path.join('images', 'player-one.png'))


    def update(self, location = None):
        if location = "up":
            pass
        elif location = "right":
            pass
        
        

        self.rect.y += 7
        
 

class PlayerTwo(Player):
    def __init__(self):

        Player.__init__(self)
        self.image, self.rect = util.load_image(os.path.join('images', 'player-two.png'))
        self.speed = 10
        
