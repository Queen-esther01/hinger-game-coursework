"""
Hinger Project
Coursework 001 for: CMP-7058A Artificial Intelligence

Includes functions for retrieving safe paths for Task 2

@author: E6 (100501127)
@date: 29/09/2025

"""
from copy import deepcopy
from ai_state import State


def possible_moves(grid):
    """Returns a list of all possible moves"""
    moves = []
    for rowIndex, row in enumerate(grid, start=0):
        print('\n')
        for columnIndex, cell in enumerate(row, start=0):
            if cell > 0:
                clone = deepcopy(grid)
                clone[rowIndex][columnIndex] = cell - 1
                moves.append(clone)
    return moves

def checks(start, end):
    if len(start) != len(end) or len(start[0]) != len(end[0]):
        return None
    if start == end:
        return None

def path_BFS(start,end):
    """ returns safe paths from start to end """
    checks(start,end)

    queue = [([0,0])]
    visited = set()
    flat = []
    safe_moves = set()
    regions = State(end).numRegions()
    for rowIndex in range(len(start)):
        for columnIndex in range(len(start[rowIndex])):
            """ 
                Extra Checks
                - Return if the corresponding end cell is larger than start cell, game is invalid
                - Return if state is not binary, game is invalid
            """
            # print(f"start: {start[rowIndex][columnIndex]} end: {end[rowIndex][columnIndex]}")
            if start[rowIndex][columnIndex] < end[rowIndex][columnIndex]:
                return None
            if start[rowIndex][columnIndex] > 1 or end[rowIndex][columnIndex] > 1:
                return None

            visited.add((rowIndex,columnIndex))
            flat.append(start[rowIndex][columnIndex])
            neighbors = State(start).getNeighbours(
                rowIndex,
                columnIndex
            )
            if start[rowIndex][columnIndex] > end[rowIndex][columnIndex]:
                start[rowIndex][columnIndex] = start[rowIndex][columnIndex] - 1
                if State(start).numRegions() > regions:
                    return None
                else:
                    safe_moves.add((rowIndex,columnIndex))

            # print(f"neighbors: {neighbors}")
            for neighbor in neighbors:
                if neighbor not in visited:
                    queue.append(neighbors)
    print(f'safe moves: {safe_moves}')
    return flat

def path_DFS(start,end):
    # The queue stores tuples containing the current_state_grid and list of grid states in the path
    queue = [(start, [start])]

    # We use a set to keep track of visited *grid states* to prevent cycles and re-visits.
    # Grids must be converted to an immutable type i.e a tuple of tuples to be stored in a set.
    def grid_to_tuple(grid):
        return tuple(map(tuple, grid))

    visited = {grid_to_tuple(start)}

    while queue:
        current_grid, path = queue.pop()  # DFS: LIFO pop for the deepest state

        # We check if the presentr state is the goal
        if current_grid == end:
            return path  # The goal has been reached, search now stops, returns path

        # Produce all possible next states (moves) from the current state
        current_state = State(current_grid)

        for next_grid in current_state.moves():

            next_grid_tuple = grid_to_tuple(next_grid)

            if next_grid_tuple not in visited:
                visited.add(next_grid_tuple)

                new_path = path + [next_grid]

                # We then push the new state and its path onto the stack
                # The search continues from this new, deeper state (depth first)
                queue.append((next_grid, new_path))

    # If the stack is empty and the goal was not found
    return None

def path_IDDFS(start, end):
    return

def path_astar(start, end):
    return

def compare():
    return

def tester():
    start = [
        [1, 1, 0],
        [0, 1, 0],
        [0, 0, 1]
    ]
    end = [
        [0, 1, 0],
        [0, 1, 0],
        [0, 0, 0]
    ]
    print(path_BFS(start,end))
    print(path_DFS(start,end))

if __name__ == '__main__':
    tester()