from Random_Agent import Random_Agent
from Squadro import Squadro
from DQN_Agent import DQN_Agent
from AlphaBetaAgent import AlphaBetaAgent
from MinMaxAgent2 import MinMaxAgent2

class Tester:
    def __init__(self, env, player1, player2) -> None:
        self.env = env
        self.player1 = player1
        self.player2 = player2
        

    def test (self, games_num):
        env = self.env
        player = self.player1
        player1_win = 0
        player2_win = 0
        games = 0
        step = 0
        while games < games_num:
            step+=1
            action = player.get_Action(state=env.state, train = False)
            env.move(action, env.state)
            player = self.switchPlayers(player)
            if env.is_end_of_game(env.state) or step > 200:
                score1 = env.state.score1
                score2 = env.state.score2
                if score1 == 4:
                    player1_win += 1
                elif score2 == 4:
                    player2_win += 1
                env.state = env.initState()
                step = 0
                games += 1
                player = self.player1
        return player1_win, player2_win        

    def switchPlayers(self, player):
        if player == self.player1:
            return self.player2
        else:
            return self.player1

    def __call__(self, games_num):
        return self.test(games_num)

if __name__ == '__main__':
    env = Squadro()
    #player1 = DQN_Agent(player=2, env=env,parametes_path='Data/best_random_params_29.pth');
    player1 = Random_Agent(player=1, env=env)
    player2 = Random_Agent(player=2, env=env)#AlphaBetaAgent(player=2, depth=2,environment = env)
    test = Tester(env,player1=player1, player2= player2)
    print(test.test(100))
    