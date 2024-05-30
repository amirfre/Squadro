import random
from Graphics import *
from State import State

class Random_Agent():
    def __init__(self, env : Squadro, player = None) -> None:
        self.env = env

    def get_Action (self, events = None, graphics=None, state: State = None, epoch = 0, train = None):
            action = random.choice(state.legal_actions)
            return action