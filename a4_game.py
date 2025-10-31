"""
Hinger Project
Coursework 001 for: CMP-7058A Artificial Intelligence

Core gameplay loop for the Hinger game

@author: E6 (100501127, 100527347)
@date: 29/09/2025

"""
from a3_agent import Agent

def play(state, agentA, agentB):
    """Play a game of Hinger between two agents"""
    while agentA.game_over(state) == False and agentB.game_over(state) == False:
        move_a = agentA.move(state, maximizing_player=True)
        if agentA.is_hinger(state, move_a):
            print('Agent A is hinger!', state)
            return 'Agent A'
        state_a = agentA.apply_action(move_a, state)

        move_b = agentB.move(state_a, maximizing_player=False)
        if agentB.is_hinger(state_a, move_b):
            return 'Agent B'
        state_b = agentB.apply_action(move_b, state_a)
        state = state_b

    return None

def tester():
    # Example1 - Winning Board Agent A (update Agent(2, 3))
    start = [
        [1, 1, 1],
        [0, 0, 0],
    ]
    # Example2 - Winning Board Agent B (update Agent(4, 5))
    # start = [
    #     [0, 0, 0, 0, 1],
    #     [1, 1, 0, 0, 0],
    #     [0, 1, 1, 1, 1],
    #     [0, 1, 1, 1, 1]
    # ]
    # Example3 - Winning Board Agent A (update Agent(2, 5)
    # start = [
    #     [1, 1, 1, 1, 1],
    #     [1, 1, 1, 1, 1]
    # ]
    agent_a = Agent((2, 3))
    agent_b = Agent((2, 3))
    print(play(start, agent_a, agent_b))

if __name__ == '__main__':
    tester()