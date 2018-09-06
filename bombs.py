import pygame, sys, os, time, util
from pygame.locals import *
# bombs have a damage radius
# pickups:
# increase amount of bombs you can place 
# increase the radius of bombs 
# bombs can only take out one block at a time 

class Bomb(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)  # initiate the sprite class
        
        self.raduis = 1
        self.expire_time = pygame.time.get_ticks() + 2000 # time that is five seconds after bomb is created, used to keep track of explosion
        self.exploding_time = 0 # keeps how long the bombs is exploding 
        self.delete_time = 0 # keeps track of when the bomb should be deleted 
        self.exploding_state = 0 # keeps track of whether the bomb is exploding
        # 0 - not exploding, 1 - exploding, 2 - delete 
        self.image, self.rect = util.load_image(os.path.join("images", "bomb.png"))
        self.rect.x = x
        self.rect.y = y

    # erases a bomb from a surface 
    def clear(self, screen, bg):
        # draw the background over the bomb 
        screen.blit(bg, self.rect, self.rect)
    
    def add_effects(effect):
        """takes a  Pickup object to modify the bomb"""
        name = effect.get_name()
        # if elif else         
        pass

    def activate(self):
        return pygame.time.get_ticks() + 5000

    def update(self, time, group, screen, bg):
        """ explodes bomb if current time is equal to expire time """
        # explodes 
        if self.expire_time <= time and self.exploding_state == 0:
            print("BOOM")
            old_x, old_y = self.rect.x, self.rect.y
            old_width, old_height = self.rect.width, self.rect.height


            # change the bomb so that its exploding             
##            self.image, self.rect = util.load_image(os.path.join("images", "background.png"))
##            self.rect.x, self.rect.y = old_x, old_y
##            self.rect.width, self.rect.height = old_width, old_height
            self.exploding_state = 1
            self.exploding_time = pygame.time.get_ticks() + 3000

        # exploding, last one second 
        elif self.exploding_time <= time and self.exploding_state == 1:
            print("exploded")
            self.delete_time = pygame.time.get_ticks() + 2000
            
            self.exploding_state = 2
            # change the rect of the bomb
            
        elif self.exploding_time <= time and self.exploding_state == 2:
            # return a number that gets tested in main
            pass

             

        


class PickUp():
    def __init__(self, name = "Default"):
        self.name = name
    
    def get_name():
        return self.name


# make different typ of pickups 
