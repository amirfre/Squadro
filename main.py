import pygame
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
WIDTH = 650
HEIGHT = 650
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.init()
 
graphics = Graphics()
env = Squadro()
# graphics.draw_Board()
pygame.display.set_caption("Squadro")
player1 = None
player2 = None

#player1 = Human_Agent(1, env, graphics)
#player1 = Random_Agent(player = 1,env=env)
#player1 = MinMaxAgent(player=1, depth=4,environment = env)
# player1 = AlphaBetaAgent(player=1, depth = 3,environment = env)
# player1 = DQN_Agent(player = 1, env=env, train=False, parametes_path='Data/best_random_params_2.pth')

#player2 = Human_Agent(2, env, graphics)
#player2 = Random_Agent(player = 2,env=env)
#player2 = MinMaxAgent(player=2, depth = 3,environment = env)
#player2 = AlphaBetaAgent(player=2, depth=3,environment = env)
# player2 = DQN_Agent(player = 2, env=env, train=False, parametes_path='Data/best_random_params_29.pth')


# player = player1

# Loop until the user clicks the close button.
# run = True
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
print(env.get_legal_actions(env.state))

def switchPlayers(player):
    if player == player1:
       return player2
    else:
        return player1


def main (p1, p2):
    global player1, player2
    player1=p1
    player2=p2   
    player = player1
    run = True
        # -------- Main Program Loop -----------
    while(run):
        # --- Main event loop
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                run = False

        action = player.get_Action(events=events, state = env.state)
        if action:
            env.move(action, env.state)
            player = switchPlayers(player)
            if env.is_end_of_game(env.state):
                run = False
            
        

        # graphics.draw_Arrow(1,1,1)
        graphics.draw_State(env.state)

        
    
        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.update()
    
        # --- Limit to 60 frames per second
        clock.tick(30)
    
    print (env.state.score1, env.state.score2)

    # # Close the window and quit.
    # pygame.quit()
       


def GUI ():
    global player1, player2
    player1 = Human_Agent(1, env, graphics)
    player2 = Human_Agent(2, env, graphics)
    # player1 = MinMaxAgent(player = 1,depth = 3, environment=environment)
    # player2 = MinMaxAgent(player = 2,depth = 3, environment=environment)
    # player1 = MinMaxAgent2(player = 1,depth = 3, environment=environment)
    # player2 = MinMaxAgent2(player = 2,depth = 3, environment=environment)
    # player1 = AlphaBetaAgent(player = 1,depth = 3, environment=environment)
    # player2 = AlphaBetaAgent(player = 2,depth = 3, environment=environment)
    # player1 = RandomAgent(environment)
    # player2 = RandomAgent(environment)
    # player1 = FixAgent(environment, player=1)
    # player2 = FixAgent(environment, player=2, train=True)
    # player1 = FixAgent2(environment, player=1, train=True)
    # player2 = FixAgent2(environment, player=2)

    # model = DQN(environment)
    # model = torch.load(file)
    # player1 = DQNAgent(model, player=1, train=False)
    # player2 = DQNAgent(model, player=2, train=False)

    colors = [['violet', 'gray', 'gray', 'gray'], ['violet', 'gray', 'gray', 'gray']]
    player1_chosen = 0
    player2_chosen = 0
    clock = pygame.time.Clock()
    run = True
    while(run):
        clock.tick(60)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                if 200<pos[0]<400 and 500<pos[1]<540:
                    main(player1, player2) 
                if 85<pos[0]<285 and 200<pos[1]<240:
                    player1 = Human_Agent(1, env, graphics)
                    player1_chosen=0
                if 350<pos[0]<550 and 200<pos[1]<240:
                    player1 = Human_Agent(1, env, graphics)
                    player2_chosen=0
                if 85<pos[0]<285 and 250<pos[1]<290:
                    player1 = MinMaxAgent2(player=1, depth=3,environment = env)
                    player1_chosen=1
                if 350<pos[0]<550 and 250<pos[1]<290:
                    player2 = MinMaxAgent2(player=2, depth = 3,environment = env)
                    player2_chosen=1

                if 85<pos[0]<285 and 300<pos[1]<340:
                    player1 = AlphaBetaAgent(player=1, depth = 3,environment = env)
                    player1_chosen=2
                if 350<pos[0]<550 and 300<pos[1]<340:
                    player2 = AlphaBetaAgent(player=2, depth = 3,environment = env)
                    player2_chosen=2

                if 85<pos[0]<285 and 350<pos[1]<390:
                    player1 = DQN_Agent(player = 1, env=env, train=False, parametes_path='Data/best_random_params_2.pth')
                    player1_chosen=3
                if 350<pos[0]<550 and 350<pos[1]<390:
                    player2 = DQN_Agent(player = 2, env=env, train=False, parametes_path='Data/best_random_params_2.pth')
                    player2_chosen=3




        colors = [['gray', 'gray', 'gray', 'gray'], ['gray', 'gray', 'gray', 'gray']]
        colors[0][player1_chosen]='violet'
        colors[1][player2_chosen]='violet'




        win.fill('LightGray')
        write(win, "Welcome to Squadro!", pos=(190, 50), color=BLACK, background_color=None)

        write(win, 'Player 1',(135,150),color=BLACK)
        pygame.draw.rect(win, colors[0][0], (85,200,200,40))
        write(win, 'Human', (140,200),color=BLACK)
        pygame.draw.rect(win, colors[0][1], (85,250,200,40))
        write(win, 'Min_Max', (130,250),color=BLACK)
        pygame.draw.rect(win, colors[0][2], (85,300,200,40))
        write(win, 'Alpha_Beta', (120,300),color=BLACK)
        pygame.draw.rect(win, colors[0][3], (85,350,200,40))
        write(win, 'DQN', (155,350),color=BLACK)

        write(win, 'Player 2',(400,150),color=BLACK)
        pygame.draw.rect(win, colors[1][0], (350,200,200,40))
        write(win, 'Human', (405,200),color=BLACK)
        pygame.draw.rect(win, colors[1][1], (350,250,200,40))
        write(win, 'Min_Max', (395,250),color=BLACK)
        pygame.draw.rect(win, colors[1][2], (350,300,200,40))
        write(win, 'Alpha_Beta', (385,300),color=BLACK)
        pygame.draw.rect(win, colors[1][3], (350,350,200,40))
        write(win, 'DQN', (420,350),color=BLACK)

        
        pygame.draw.rect(win, 'gray', (266,500,100,40))
        write(win, 'Play', (290,497),color=BLACK)


        pygame.display.update()

    pygame.quit()

def write (surface, text, pos = (50, 20), color = BLACK, background_color = None):
    font = pygame.font.SysFont("Rockwell Condensed", 36)
    text_surface = font.render(text, True, color, background_color)
    surface.blit(text_surface, pos)


if __name__ == '__main__':
    GUI()


    