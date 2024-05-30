import pygame
from old.gameboard import Gameboard
from Graphics import  Graphics
from Squadro import Squadro
from State import State
from Human_Agent import Human_Agent
from MinMaxAgent import MinMaxAgent2
from Random_Agent import Random_Agent
from AlphaBetaAgent import AlphaBetaAgent
from DQN_Agent import DQN_Agent
import numpy as np

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
 
pygame.init()
 
graphics = Graphics()
env = Squadro()
# graphics.draw_Board()
pygame.display.set_caption("Amir's game")

#player1 = Human_Agent(1, env, graphics)
#player1 = Random_Agent(player = 1,env=env)
#player1 = MinMaxAgent(player=1, depth=4,environment = env)
# player1 = AlphaBetaAgent(player=1, depth = 3,environment = env)
player1 = DQN_Agent(player = 1, env=env, train=False, parametes_path='Data/best_random_params_2.pth')

#player2 = Human_Agent(2, env, graphics)
#player2 = Random_Agent(player = 2,env=env)
#player2 = MinMaxAgent(player=2, depth = 3,environment = env)
#player2 = AlphaBetaAgent(player=2, depth=3,environment = env)
player2 = DQN_Agent(player = 2, env=env, train=False, parametes_path='Data/best_random_params_29.pth')


player = player1

# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
print(env.get_legal_actions(env.state))

def switchPlayers(player):
    if player == player1:
       return player2
    else:
        return player1
    
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            done = True

    action = player.get_Action(events=events, state = env.state)
    if action:
        env.move(action, env.state)
        player = switchPlayers(player)
        done = env.is_end_of_game(env.state)
        
    

    # graphics.draw_Arrow(1,1,1)
    graphics.draw_State(env.state)

    
 
    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.update()
 
    # --- Limit to 60 frames per second
    clock.tick(2)
 
print (env.state.score1, env.state.score2)

# Close the window and quit.
pygame.quit()


    