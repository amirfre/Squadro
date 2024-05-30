import pygame
from enum import Enum
from PIL import Image
from PIL import ImageDraw
from utils import pil_image_to_pygame_surface

ARROW_IMAGE_FILE_NAME = "arrow.png"
ARROW_SCALE_DIMENTIONS = (19.22, 85.21)

class E_ArrowDirection(Enum):
    FORWARD = 1
    BACKWORD = 2

class E_ArrowRotation(Enum):
    UP = 0
    LEFT = 90
    DOWN = 180
    RIGHT = 270

class E_ArrowColor(Enum):
    RED = (255,0,0, 255)
    YELLOW = (255,255,0, 255)

class Arrow:
    def __init__(self, screen, rotation, moves_per_round, color, location):
        self.moves_per_round = moves_per_round
        self.direcrion=E_ArrowDirection.FORWARD
        self.color = color
        self.location = location

        original_arrow_image = Image.open(ARROW_IMAGE_FILE_NAME) 
        image_width, image_height = original_arrow_image.size
        image_center = (int(0.5 * image_width), int(0.5 * image_height))
        ImageDraw.floodfill(original_arrow_image, xy=image_center, value=color.value)

        self.image = pil_image_to_pygame_surface(original_arrow_image)
        image_background_color = self.image.get_at((0,0))
        self.image.set_colorkey(image_background_color)
        self.image.convert_alpha()
        self.image = pygame.transform.scale(self.image, ARROW_SCALE_DIMENTIONS)
        self.image = pygame.transform.rotate(self.image, rotation.value)

        screen.blit(self.image, self.location)

