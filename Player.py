import pygame, sys, os, time, util
from pygame.event import clear
from pygame.locals import *
import bombs

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
        self.rect.y += 7
        
 

class PlayerTwo(Player):
    def __init__(self):

        Player.__init__(self)
        self.speed = 10
        
