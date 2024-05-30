from State import State
import numpy as np
# from Graphics import *
import torch

class Squadro:
    def __init__(self, state:State = None) -> None:
        if state == None:
            self.state = self.initState()
        else:
            self.state = state
        self.step_row_left = [0, 3, 1, 2, 1, 3] # row left
        self.step_row_right = [0, 1, 3, 2, 3, 1] 
        self.step_col_up  = [0, 1, 3, 2, 3, 1] 
        self.step_col_down = [0, 3, 1, 2, 1, 3]# row right
        

    def initState(self):
        board = np.zeros([7,7])
        board[6,1] = 2 # yellow
        board[6,2] = 2
        board[6,3] = 2
        board[6,4] = 2
        board[6,5] = 2
        board[1,6] = 1 # red
        board[2,6] = 1
        board[3,6] = 1
        board[4,6] = 1
        board[5,6] = 1
        state = State(board, 1)
        self.set_legal_actions(state)
        return state

    def find_arrow_in_row (self, row, state):
        board_row = state.board[row,:]
        cols = np.where(abs(board_row) == 1)[0] 
        if len(cols) > 0:
            return row, cols[0]
        return row, None
        
    def find_arrow_in_col (self, col, state):
        board_col = state.board[:, col]
        rows = np.where(abs(board_col) == 2)[0]
        if len(rows) > 0:
            return rows[0], col
        return None, col

    def move(self, action ,state: State):
        if state.player == 1: #red
            row, col = self.find_arrow_in_row(action,state)
            arrow = state.board[row,col]
            if arrow == 1:
                step = -self.step_row_left[row]
                new_col = col + step
                if new_col == 0:
                    arrow = arrow * -1
            elif arrow == -1:
                step = self.step_row_right[row]
                new_col = col + step
                if new_col == 6:
                    arrow = 0
                    state.score1+=1
            
            self.eat((row,col), (row, new_col), state)
            state.board[row,col] = 0
            state.board[row, new_col] = arrow
            state.player = 2
            
        else:
            row, col = self.find_arrow_in_col(action, state)
            arrow = state.board[row,col]
            if arrow == 2:
                step = -self.step_col_up[col]
                new_row = row + step
                if new_row == 0:
                    arrow = arrow * -1
            elif arrow == -2:
                 step = self.step_col_down[col]
                 new_row = row + step
                 if new_row == 6:
                    arrow = 0
                    state.score2+=1
            if state.board[new_row, col] != 0:
                
                state.board[new_row, 6] = 1
            self.eat((row,col), (new_row, col), state)
            state.board[row,col] = 0
            state.board[new_row, col] = arrow
            state.player = 1
    
        self.set_legal_actions(state)
            

    def eat(self,row_col,new_row_col,state: State):
        row, col = row_col
        new_row, new_col = new_row_col

        if state.player == 1:
            # arr = state.board[row, min(col, new_col): max(col, new_col)]
            for c in range(min(col, new_col), max(col, new_col)+1):
                if abs(state.board[row, c]) == 2:
                    state.board[row, c] = 0
                    state.board[6, c] = 2
        else:
            for r in range(min(row,  new_row), max(row, new_row)+1):
                if abs(state.board[r, col]) == 1:
                    state.board[r, col]=0
                    state.board[r, 6] = 1

    def is_legal(self, action, state: State):
        # if state.player == 1: #red
        #     row, col = self.find_arrow_in_row(action, state)
        #     return col is not None
        # else:
        #     row, col = self.find_arrow_in_col(action, state)
        #     return row is not None
        if action in state.legal_actions:
            return True
        return False

        # return abs(state.board[row_col]) == state.player
   
    def get_legal_actions(self, state: State):
        return state.legal_actions
        
    
    def set_legal_actions(self, state: State):
        arrows = np.where(abs(state.board) == state.player)
        if state.player == 1:
            legal_actions = list(arrows[0])
        else:
            legal_actions = list(arrows[1])
        state.legal_actions = legal_actions


    def is_end_of_game(self, state: State):
        return state.score1 == 4 or state.score2 == 4

    def get_next_state(self, action, state:State) -> State:
        next_state = state.copy()
        self.move(action, next_state)
        self.set_legal_actions(next_state)
        return next_state

    def get_all_next_states (self, state: State) -> tuple:
        legal_actions = state.legal_actions
        next_states = []
        for action in legal_actions:
            next_states.append(self.get_next_state(action, state))
        return next_states, legal_actions
    
    def toTensor (self, list_states, device = torch.device('cpu')) -> tuple:
        list_board_tensors = []
        list_legal_actions = []
        for state in list_states:
            board_tensor, legal_actions = state.toTensor(device) 
            list_board_tensors.append(board_tensor)
            list_legal_actions.append(torch.tensor(legal_actions))
        return torch.vstack(list_board_tensors), torch.vstack(list_legal_actions)
    
    def reward (self, state : State, action = None) -> tuple:
        if action:
            next_state = self.get_next_state(action, state)
        else:
            next_state = state
        if (self.is_end_of_game(next_state)):
            if state.score1 == 4:
                player = 1
            else:
                player = 2

            if player == 1:
                return 1, True  
            else:
                return -1, True  
        return 0, False
    
    def revarse (self):
        self.step_row_left, self.step_row_right = self.step_row_right, self.step_row_left
        self.step_col_up, self.step_col_down = self.step_col_down, self.step_col_up
        
        