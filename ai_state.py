"""
Hinger Project
Coursework 001 for: CMP-7058A Artificial Intelligence

Includes a State class for Task 1

@author: E6 (100501127)
@date: 29/09/2025

"""
from copy import deepcopy


class State:
    def __init__(self, grid):
        self.grid = grid

    def __str__(self):
        """Returns a readable grid similar to input in brief but without lines"""
        result = ""
        for row in self.grid:
            result += ' '.join(str(cell) for cell in row)
            result += '\n'
        return str(f"{result}")

    def moves(self):
        """Returns a list of all possible states by reducing every active state by 1"""
        for rowIndex, row in enumerate(self.grid, start=0):
            print('\n')
            for columnIndex, cell in enumerate(row, start=0):
                if cell > 0:
                    clone = deepcopy(self.grid)
                    clone[rowIndex][columnIndex] = cell - 1
                    yield clone

    def getNeighbours(self, rowIndex, columnIndex):
        """Return a list of neighbouring states by looping through all 8 surrounding positions"""
        neighbours = []
        for x in range(rowIndex - 1, rowIndex + 2):
            for y in range(columnIndex - 1, columnIndex + 2):
                if (x, y) == (rowIndex, columnIndex):
                    continue  # skip the cell itself
                if 0 <= x < len(self.grid) and 0 <= y < len(self.grid[rowIndex]):  # stay inside grid
                    neighbours.append((x, y))
        return neighbours

    def numRegions(self):
        """Returns the number of active regions in the grid"""
        visited = set()
        regions = 0
        for rowIndex, row in enumerate(self.grid, start=0):
            for columnIndex, cell in enumerate(row, start=0):
                if self.grid[rowIndex][columnIndex] > 0 and (rowIndex, columnIndex) not in visited:
                    queue = [(rowIndex, columnIndex)]
                    visited.add((rowIndex, columnIndex))
                    #Do bfs
                    while queue:
                        row, column = queue.pop(0)
                        for nx, ny in self.getNeighbours(row, column):
                            if self.grid[nx][ny] > 0 and (nx, ny) not in visited:
                                visited.add((nx, ny))
                                queue.append((nx, ny))
                    regions += 1
        return regions

    def numHingers(self):
        """Returns the number of hingers in the grid"""
        hingers = 0
        hinger_cell = set()
        for rowIndex, row in enumerate(self.grid, start=0):
            for columnIndex, cell in enumerate(row, start=0):
                prev_regions = self.numRegions()
                if self.grid[rowIndex][columnIndex] >= 1:
                    self.grid[rowIndex][columnIndex] = cell - 1
                    current_regions = self.numRegions()
                    self.grid[rowIndex][columnIndex] = cell + 1
                    if current_regions > prev_regions:
                        hingers += 1
                        hinger_cell.add((rowIndex, columnIndex))
        return hingers

def tester():
    sa = State([
        [1, 1, 0, 0, 2],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1]
    ])

    # run str
    print(sa)

    # run moves
    # for n in State(sa).moves():
    #     print(n)

    # run numRegions
    print(f'number of regions: {sa.numRegions()}')

    # run numHingers
    print(f'number of hingers: {sa.numHingers()}')

if __name__ == '__main__':
    tester()