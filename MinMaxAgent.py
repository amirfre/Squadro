from Squadro import Squadro
from State import State
import numpy as np
MAXSCORE = 1000

class MinMaxAgent2:

    def __init__(self, player, depth = 2, environment: Squadro = None):
        self.player = player
        if self.player == 1:
            self.opponent = 2
        else:
            self.opponent = 1
        self.depth = depth
        self.environment : Squadro = environment

    def get_Action(self,events, state: State,train = False):
        value, bestAction = self.minMax(state)
        return bestAction

    def minMax(self, state:State):
        visited = set()
        depth = 0
        return self.max_value(state, visited, depth)
        
    def max_value (self, state:State, visited:set, depth):
        
        value = -MAXSCORE

        # stop state
        if depth == self.depth or self.environment.is_end_of_game(state):
            value = self.evaluate(state)
            return value, None
        
        # start recursion
        bestAction = None
        legal_actions = self.environment.get_legal_actions(state)
        for action in legal_actions:
            newState = self.environment.get_next_state(action, state)
            if newState not in visited:
                visited.add(newState)
                newValue, newAction = self.min_value(newState, visited,  depth + 1)
                if newValue > value:
                    value = newValue
                    bestAction = action

        return value, bestAction 

    def min_value (self, state:State, visited:set, depth):
        
        value = MAXSCORE

        # stop state
        if depth == self.depth or self.environment.is_end_of_game(state):
            value = self.evaluate(state)
            return value, None
        
        # start recursion
        bestAction = None
        legal_actions = self.environment.get_legal_actions(state)
        for action in legal_actions:
            newState = self.environment.get_next_state(action, state)
            if newState not in visited:
                visited.add(newState)
                newValue, newAction = self.max_value(newState, visited,  depth + 1)
                if newValue < value:
                    value = newValue
                    bestAction = action

        return value, bestAction 
    
    def evaluate(self, state:State):
        red = 1
        yellow = 2
        # step_row_left_np = np.array([0, 3, 1, 2, 1, 3]) # row left
        # step_row_right_np = np.array([0, 1, 3, 2, 3, 1]) 
        # step_col_up_np  = np.array([0, 1, 3, 2, 3, 1]) 
        # step_col_down_np = np.array([0, 3, 1, 2, 1, 3])# row right
        
        board = state.board
        red_pieces = np.sum(abs(board) == red)
        
        red_pos_left = np.where(board == red)
        red_pos_left_distance = np.sum( 6 + red_pos_left[1])
        red_pos_right = np.where(board == -red)
        red_pos_right_distance = np.sum(6 - red_pos_right[1])
        red_score = -(red_pieces * 100 + red_pos_left_distance  + red_pos_right_distance)

        yellow_pieces = np.sum(abs(board) == yellow)
        yellow_pos_up = np.where(board == yellow)
        yellow_pos_up_distance = np.sum(6 + yellow_pos_up[0])
        yellow_pos_down = np.where(board == -yellow)
        yellow_pos_down_distance = np.sum(6 - yellow_pos_down[0])
        yellow_score = -(yellow_pieces * 100 + yellow_pos_up_distance+ yellow_pos_down_distance)

        if self.player == 1:
            return red_score - yellow_score
        else:
            return yellow_score - red_score
            
        
        
        
        # player_distance = 0

        # opponent_distance = 0



        # for row in board:
        #     for piece in row:
        #         if piece == player:
        #             player_pieces += 1
        #             player_distance += row.index(piece)
        #         elif piece == 'O':
        #             opponent_pieces += 1
        #             opponent_distance += row.index(piece)

        # if player_pieces == 0:
        #     return -10000
        # elif opponent_pieces == 0:
        #     return 10000
        # else:
        #     return (player_pieces - opponent_pieces) + (player_distance - opponent_distance)

