import pygame, sys, os, time, util
from pygame.event import clear
from pygame.locals import *
import bombs


# to do list
# need to update image to choose from a list to creat animation
# you can place one bomb every x amount of seconds
# put movement in a array to allow for multiple angles

class Player(pygame.sprite.Sprite):
    """ Parent class that User controls """

    def __init__(self, speed=None):
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
        self.rect.x = 70
        self.rect.y = 70

    def update(self, location=None):

        " Move the player position based on the the speed variable and the location argument"
        if location is "up":
            self.rect.y -= self.speed
        elif location is "down":
            self.rect.y += self.speed
        elif location is "right":
            self.rect.x += self.speed
        elif location is "left":
            self.rect.x -= self.speed





class PlayerTwo(Player):
    """ Actual object that Player two interacts with   """

    # change this for animation
    def __init__(self):
        """ Constructor """
        Player.__init__(self)
        self.speed = 10

        self.image, self.rect = util.load_image(os.path.join('images', 'player-two.png'))
        self.rect.x = 910
        self.rect.y = 770

    def update(self, location=None):

        " Move the player position based on the the speed variable and the location argument"
        if location is "up":
            self.rect.y -= self.speed
        elif location is "down":
            self.rect.y += self.speed
        elif location is "right":
            self.rect.x += self.speed
        elif location is "left":
            self.rect.x -= self.speed

