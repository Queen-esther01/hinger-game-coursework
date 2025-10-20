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

    def __str__(self):
        """Returns a readable grid similar to input in brief but without lines"""
        result = ""
        for row in self.grid:
            result += ' '.join(str(cell) for cell in row)
            result += '\n'
        return str(f"{result}")

    def get_all_valid_moves(self, state):
        result = []
        for rowIndex, row in enumerate(state, start=0):
            for columnIndex, cell in enumerate(row, start=0):
                if cell > 0:
                    result.append([rowIndex, columnIndex])
        return result

    def evaluate(self, prev_state, new_state):
        """Return 1 if active regions increased, 0 otherwise"""
        prev_state_clone = deepcopy(prev_state)
        prev_state_class = State(prev_state_clone)
        prev_regions = prev_state_class.numRegions()

        new_state_clone = deepcopy(new_state)
        new_state_class = State(new_state_clone)
        new_regions = new_state_class.numRegions()

        if new_regions > prev_regions:
            return 1
        else:
            return 0

    def game_over(self, state):
        """Return true if game is over ie if there are no active cells"""
        for rowIndex, row in enumerate(state, start=0):
            for columnIndex, cell in enumerate(row, start=0):
                if cell > 0:
                    return False
        return True

    def apply_action(self, move, state):
        """Return a new state after applying the action"""
        clone = deepcopy(state)
        clone[move[0]][move[1]] = clone[move[0]][move[1]] - 1
        return clone

    def minimax(self, state, depth, maximizing_player, prev_state=None):
        """Return best move based on minimax"""
        # The base case that break recursion
        if depth == 0 or self.game_over(state):
            if prev_state is None:
                return 0, None
            return self.evaluate(state, prev_state), None

        if maximizing_player:
            max_eval = -1
            best_move = None
            for move in self.get_all_valid_moves(state):
                next_state = self.apply_action(move, state)
                eval, _ = self.minimax(next_state, depth - 1, False, state)
                # print(f"Trying move {move} max player, eval score = {eval}")
                if eval > max_eval:
                    max_eval = eval
                    best_move = move
            return max_eval, best_move

        else:  # minimizing player
            min_eval = 1
            best_move = None
            for move in self.get_all_valid_moves(state):
                next_state = self.apply_action(move, state)
                eval, _ = self.minimax(next_state, depth - 1, True, state)
                # print(f"Trying move {move} min player, eval score = {eval}")
                if eval < min_eval:
                    min_eval = eval
                    best_move = move
            return min_eval, best_move

    def alphabeta(self, state):
        """Return a move based on alphabeta"""
        return

    def move(self, state, mode='minimax'):
        """Return a move based on the mode"""
        # print(f"row {len(state)} column {len(state[0])}")
        # print(f"size {self.size}")
        assert (len(state) == self.size[0])
        assert (len(state[0]) == self.size[1])
        if mode not in self.modes:
            return None
        if mode == 'minimax':
            score, best_move = self.minimax(state, depth=4, maximizing_player=True)
            print(f'score: {score} best move: {best_move}')
            return best_move
        elif mode == 'alphabeta':
            return self.alphabeta(state)


def tester():
    start = [
        [1, 1, 1],
        [0, 0, 0],
    ]
    start = [
        [0, 1, 0, 0, 1],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1]
    ]
    # state = State(start)
    print(Agent((4,5)).move(start))
    # print(tester_state())

if __name__ == '__main__':
    tester()