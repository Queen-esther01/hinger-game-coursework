"""
Hinger Project
Coursework 001 for: CMP-7058A Artificial Intelligence

Includes functions for retrieving safe paths for Task 2

@author: E6 (100501127, 100527347)
@date: 29/09/2025

"""
from copy import deepcopy
from a1_state import State


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
    queue = [(start, [start])]


    def grid_tuple(grid):
        return tuple(map(tuple, grid))

    visited = {grid_tuple(start)}

    while queue:
        currentgrid, path = queue.pop()  # DFS: LIFO pop for the deepest state


        if currentgrid == end:
            return path  # The goal has been reached, search now stops, returns path

        currentstate = State(currentgrid)

        for nextgrid in currentstate.moves():

            nextgridtuple = grid_tuple(nextgrid)

            if nextgridtuple not in visited:
                visited.add(nextgridtuple)

                newpath = path + [nextgrid]

                queue.append((nextgrid, newpath))

    # If the stack is empty and the set goal was not found
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