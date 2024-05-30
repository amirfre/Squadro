import pygame
from PIL import Image

def pil_image_to_pygame_surface(pilImage):
    return pygame.image.fromstring(pilImage.tobytes(), pilImage.size, pilImage.mode).convert()