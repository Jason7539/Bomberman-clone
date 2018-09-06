import pygame
def load_image(image):
    '''Load an image and return that image surface and the Rect.'''

    image = pygame.image.load(image).convert_alpha() # change pixel format 
    image_rect = image.get_rect()
    return image, image_rect




