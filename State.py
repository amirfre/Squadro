import numpy as np
import torch

class State:
    def __init__(self, board= None, player = 1,legal_actions = []) -> None:
        self.board = board
        self.player = player
        self.score1 =0
        self.score2 =0
        self.legal_actions = legal_actions 

    def get_opponent (self):
        if self.player == 1:
            return 2
        return 1   
   
    def __eq__(self, other) ->bool:
        b1 = np.equal(self.board, other.board).all()
        b2 = self.player == other.player
        return np.equal(self.board, other.board).all() and self.player == other.player

    def __hash__(self) -> int:
        return hash(repr(self.board) + str(self.player))
    
    def copy (self):
        newBoard = np.copy(self.board)
        legal_actions = self.legal_actions.copy()
        new_state = State(board=newBoard, player=self.player, legal_actions=legal_actions)
        new_state.score1 = self.score1
        new_state.score2 = self.score2
        return new_state
    
    def reverse (self):
        
        board_signs = self.board.copy()
        board_signs = np.transpose(board_signs)
        board_signs[board_signs == -1] = -12
        board_signs[board_signs == 1] = 12
        board_signs[board_signs == 2] = 1
        board_signs[board_signs == -2] = -1
        board_signs[board_signs == -12] = -2
        board_signs[board_signs == 12] = 2
        
        if abs(self.player) ==1:
            player = self.player * 2
        elif abs(self.player) ==2:
            player = self.player / 2

        state = State(board=board_signs, player=player , legal_actions=self.legal_actions)
    
        state.score1, state.score2 = self.score2, self.score1
        return state

    def set_legal_actions(self):
        state = self
        arrows = np.where(abs(state.board) == state.player)
        if state.player == 1:
            legal_actions = list(arrows[0])
        else:
            legal_actions = list(arrows[1])
        state.legal_actions = legal_actions

    def toTensor (self, device = torch.device('cpu')):
        board_np = self.board.reshape(-1)
        board_tensor = torch.tensor(board_np, dtype=torch.float32, device=device)
        actions_np = np.array(self.legal_actions).reshape(-1,1)
        actions_tensor = torch.from_numpy(actions_np)
        return board_tensor, actions_tensor
    
    [staticmethod]
    def tensorToState (state_tuple, player):
        board_tensor = state_tuple[0]
        board = board_tensor.reshape([7,7]).cpu().numpy()
        legal_actions_tensor = state_tuple[1]
        legal_actions = legal_actions_tensor.cpu().numpy()
        legal_actions = list(map(tuple, legal_actions))
        return State(board, player=player, legal_actions=legal_actions)
