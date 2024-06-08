import numpy as np
import pygame
import time
from enum import Enum
# from PIL import Image
# from PIL import ImageDraw
# from utils import pil_image_to_pygame_surface
from Squadro import Squadro
from State import State


ARROW_IMAGE_FILE_NAME = "arrow.png"
ARROW_SCALE_DIMENTIONS = (19.22, 85.21)
MARGIN_X = 36
MARGIN_Y = 35
CELL = 93
BACKGROUND_IMAGE_FILE_NAME = "backround.png"
SCREEN_LEFT_TOP_POSITION = (0,0)
SCREEN_SIZE = (650,650)

class Graphics:
    def __init__(self):
        self.image = pygame.image.load(ARROW_IMAGE_FILE_NAME) 
        self.screen = pygame.display.set_mode(SCREEN_SIZE)
        self.original_arrow_image = pygame.image.load(ARROW_IMAGE_FILE_NAME) 
        self.bg = pygame.image.load(BACKGROUND_IMAGE_FILE_NAME)

    def draw_Board(self):
        self.screen.blit(self.bg, SCREEN_LEFT_TOP_POSITION)

    def draw_State (self, state : State):
        self.draw_Board()        
        board = state.board
        rows,cols = board.shape
        for row in range(rows):
            for col in range(cols):
                if board[row, col] == 0:
                    continue
                pos = self.calc_Pos(row,col,board[row, col])
                arrow = board[row, col]
                self.draw_Arrow(arrow, pos) 

        TextFontP= pygame.font.SysFont("Rubik Black",20)
        player = 1
        if state.player == 1: 
            pygame.draw.rect(self.screen, (184,4,4), pygame.Rect(590, 605, 25, 25))

        else: 
            pygame.draw.rect(self.screen, (240,212,60), pygame.Rect(590, 605, 25, 25))
        TextPlayer2 = TextFontP.render("Current player:", 1, (255,255,255))
        # TextPlayer = TextFontP.render("Player " + str(player), 1, (255,255,255))
        # self.screen.blit(TextPlayer, (555, 600))
        self.screen.blit(TextPlayer2, (555, 585))


    def draw_Arrow (self, arrow, pos):
               
        self.red_arrow_left = pygame.image.load("red-arrow-left.png")
        self.yellow_arrow_up = pygame.image.load("yellow-arrow-up.png")
        self.red_arrow_right = pygame.image.load("red-arrow-right.png")
        self.yellow_arrow_down = pygame.image.load("yellow-arrow-down.png")
        
        match arrow:
            case 1: #red left
                self.screen.blit(self.red_arrow_left, pos)
            case -1: # red right
                self.screen.blit(self.red_arrow_right, pos)
            case 2: # yellow up
                self.screen.blit(self.yellow_arrow_up, pos)
            case -2: # yellow down
                self.screen.blit(self.yellow_arrow_down, pos)
                
    def calc_row_col(self, pos):
            x, y = pos
            col = x // CELL 
            row = y // CELL 
            return row, col
        


    def calc_Pos(self, row, col, arrow_num):
        match arrow_num:
            case 1:
                x = MARGIN_X + -33 + CELL * col 
                y = MARGIN_Y + 1 + CELL * row
            case 2:
                x = MARGIN_X + CELL * col
                y = MARGIN_Y + -34 + CELL * row
            case -1:
                x = MARGIN_X + -31 + CELL * col
                y = MARGIN_Y + 1 + CELL * row
            case -2:
                x = MARGIN_X +1+ CELL * col
                y = MARGIN_Y + -31 + CELL * row
        return x,y
    
    # def arrow_deatails (self, arrow_num):
    #     match arrow_num:
    #         case 1:
    #             return E_ArrowRotation.UP, E_ArrowColor.YELLOW #self.yellow_arrow_up
    #         case -1:
    #             return E_ArrowRotation.DOWN, E_ArrowColor.YELLOW
    #         case 2:
    #             return E_ArrowRotation.UP, E_ArrowColor.RED #self.red_arrow_left
    #         case -2:
    #             return E_ArrowRotation.RIGHT, E_ArrowColor.RED


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
