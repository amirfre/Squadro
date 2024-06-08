import pygame
from Graphics import *
from Squadro import Squadro

class Human_Agent:

    def __init__(self, player: int, env: Squadro, graphics: Graphics = None) -> None:
        self.player = player
        self.mode = 0
        self.graphics = graphics
        self.env = env

    def get_Action (self, events= None,  state = None):
        for event in events:
            if event.type == pygame.MOUSEBUTTONDOWN:
                # pygame.time.delay(200)
                pos = pygame.mouse.get_pos()
                row_col = self.graphics.calc_row_col(pos) 
                row, col = row_col
                if self.player == 1:
                    action = row
                else:
                    action = col
                if self.env.is_legal(action=action, state=self.env.state):
                    return action
                return None
            else:
                return None