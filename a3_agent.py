"""
Hinger Project
Coursework 001 for: CMP-7058A Artificial Intelligence

Includes functions for retrieving safe paths for Task 2

@author: E6 (100501127, 100527347)
@date: 29/09/2025

"""
from copy import deepcopy
from a1_state import State


class Agent:
    name = 'E6'
    modes = ['minimax', 'alphabeta']
    def __init__(self, size, name = 'E6'):
        self.name = name
        self.size = size

    def __str__(self, state):
        """Returns a readable grid similar to input in brief but without lines"""
        result = ""
        for row in state:
            result += ' '.join(str(cell) for cell in row)
            result += '\n'
        return str(f"{result}")

    def is_hinger(self, state, move):
        """Check if this move is a hinger cell"""
        if state[move[0]][move[1]] != 1:
            return False

        # Check if removing cell increases regions
        prev_regions = State(deepcopy(state)).numRegions()
        next_state = self.apply_action(move, state)
        new_regions = State(deepcopy(next_state)).numRegions()

        return new_regions > prev_regions

    @staticmethod
    def get_all_valid_moves(state):
        """Return a list of all valid moves"""
        result = []
        for rowIndex, row in enumerate(state, start=0):
            for columnIndex, cell in enumerate(row, start=0):
                if cell > 0:
                    result.append((rowIndex, columnIndex))
        return result

    @staticmethod
    def game_over(state):
        """Return true if game is over ie if there are no active cells"""
        for rowIndex, row in enumerate(state, start=0):
            for columnIndex, cell in enumerate(row, start=0):
                if cell > 0:
                    return False
        return True

    @staticmethod
    def apply_action(move, state):
        """Return a new state after applying the action"""
        clone = deepcopy(state)
        clone[move[0]][move[1]] = clone[move[0]][move[1]] - 1
        return clone

    def minimax(self, state, depth, maximizing_player):
        """Return best move based on minimax"""
        # The base cases that break recursion
        if self.game_over(state):
            return 0, None

        # Return the winning move immediately if any
        for move in self.get_all_valid_moves(state):
            if self.is_hinger(state, move):
                if maximizing_player:
                    return 10000, move
                else:
                    return -10000, move

        if maximizing_player:
            max_eval = float('inf')
            best_move = None
            for move in self.get_all_valid_moves(state):
                next_state = self.apply_action(move, state)
                eval, _ = self.minimax(next_state, depth - 1, False)
                # print(f"MAX: move {move}, eval={eval}, current_best={max_eval}")
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
            return max_eval, best_move

        else:  # minimizing player
            min_eval = -float('inf')
            best_move = None
            for move in self.get_all_valid_moves(state):
                next_state = self.apply_action(move, state)
                eval, _ = self.minimax(next_state, depth - 1, True)
                # print(f"MIN: move {move}, eval={eval}, current_best={min_eval}")
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
            return min_eval, best_move

    def alphabeta(self, state):
        """Return a move based on alphabeta"""
        return

    def move(self, state, mode='minimax', maximizing_player=True):
        """Return a move based on the mode, depth is how many moves deep to search"""
        assert (len(state) == self.size[0])
        assert (len(state[0]) == self.size[1])
        assert(mode in self.modes)
        if mode not in self.modes:
            return None
        if mode == 'minimax':
            score, best_move = self.minimax(state, depth=1, maximizing_player=maximizing_player)
            if best_move is None:
                return self.get_all_valid_moves(state)[0]
            return best_move
        elif mode == 'alphabeta':
            return self.alphabeta(state)
        else:
            return self.get_all_valid_moves(state)[0]


def tester():
    start = [
        [1, 1, 1],
        [0, 0, 0],
    ]
    start = [
        [1, 1, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    start = [
        [0, 0, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    start = [
        [1, 1, 1, 1, 1],
        [1, 1, 1, 1, 1],
    ]
    # print(Agent((2, 3)).move(start))
    print(Agent((2, 5)).move(start))

if __name__ == '__main__':
    tester()