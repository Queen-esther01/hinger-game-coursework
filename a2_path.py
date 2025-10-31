"""
Hinger Project
Coursework 001 for: CMP-7058A Artificial Intelligence

Includes functions for retrieving safe paths for Task 2

@author: E6 (100501127, 100527347)
@date: 29/09/2025

"""

import sys
from copy import deepcopy
from a1_state import State
import heapq

from a3_agent import Agent


def grid_tuple(grid):
    return tuple(map(tuple, grid))

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
    
def dls_path(current_grid, end, limit, path):
    if current_grid == end:
        return path
    
    if len(path) > limit:
        return None  # Path is too long, stop search
    current_state = State(current_grid)
    
    for next_grid in current_state.moves():
        if next_grid not in path: 
            solution = dls_path(next_grid, end, limit, path + [next_grid])
            if solution is not None:
                return solution                    
        return None


def path_BFS(start, end):
    """
        Returns safe paths from start to end using Breadth First Search (BFS)
        - Return if the corresponding end cell is larger than start cell, game is invalid
        - Return if state is not binary, game is invalid
    """
    for rowIndex in range(len(start)):
        for columnIndex in range(len(start[rowIndex])):
            if start[rowIndex][columnIndex] < end[rowIndex][columnIndex] or start[rowIndex][columnIndex] > 1 or end[rowIndex][columnIndex] > 1:
                return None

    if start == end:
        return []

    start_regions = State(deepcopy(start)).numRegions()
    queue = [(deepcopy(start), [])]
    visited = []
    agent = Agent((len(start), len(start[0])))
    while len(queue) > 0:
        state, path = queue.pop(0)
        for move in agent.get_all_valid_moves(state):
            next_state = agent.apply_action(move, state)
            next_regions = State(deepcopy(next_state)).numRegions()
            if next_regions > start_regions:
                continue
            if next_state in visited:
                continue
            visited.append(next_state)
            new_path = path + [move]
            if next_state == end:
                return new_path
            queue.append((next_state, new_path))
    return None

def path_DFS(start,end):
    checks(start, end)
    queue = [(start, [start])]
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
    return None

def path_IDDFS(start, end, depthchoice=50):
    for limit in range(depthchoice + 1):
        print(f"Searching with Depth Limit: {limit}") #here wwe can track progress

        initial_path = [start]    
        result_path = dls_path(start, end, limit, initial_path)
        
        if result_path is not None:
            return result_path
    return None

def path_astar(start, end):
    checks(start, end)
    if start == end:
        return None
    
    def calculate_h(grid):
        """
        Heuristic h(n): Sum of all active cell values.
        This is admissible because each move reduces the sum by at most 1.
        It is the gold standard for an admissible heuristic. It is easy to compute, guaranteed to be admissible, and highly effective.
        """
        total_sum = 0
        for row in grid:
            total_sum += sum(row)
        return total_sum

    initial_hnvalue = calculate_h(start)
    initial_gnvalue = 0
    initial_fnvalue =  initial_hnvalue + initial_gnvalue
    initial_path = [start]
    start_tuple = grid_tuple(start)
    queue = [(initial_fnvalue, initial_gnvalue, start_tuple, initial_path)]
    g_costs = {start_tuple: initial_gnvalue}

    while queue:
        fns = []
        for i in queue:
            fns.append(queue[i][0])
        leastfn = min(fns)
        for i in queue:
            if queue[i][0] == leastfn:
                fnvalue, gnvalue, current_tuple, path = queue.pop(i) # Pop the state with the LOWEST fnvalue
                current_grid = list(list(row) for row in current_tuple)
               
                if current_grid == end:
                    return path
                
                current_state = State(current_grid)
                
                for next_grid in current_state.moves():
                    next_tuple = grid_tuple(next_grid)
            
                new_gn_value = gnvalue + 1
                #check for shorter path to an already visited state
                if next_tuple not in g_costs or new_gn_value < g_costs[next_tuple]:
                    g_costs[next_tuple] = new_gn_value
                    new_hn_value = calculate_h(next_grid)
                    new_fn_value = new_gn_value + new_hn_value
                    new_path = path + [next_grid]
                    heapq.heappush(queue, (new_fn_value, new_gn_value, next_tuple, new_path))
    return None

def compare(start, end):
    bfs_result = path_BFS(start, end)
    dfs_result = path_DFS(start, end)
    
    iddfs_result = path_IDDFS(start, end)
    astar_result = path_astar(start, end)
    return print(f"bfs-{sys.getsizeof(bfs_result)} bytes; dfs-{sys.getsizeof(dfs_result)} bytes; iddfs-{sys.getsizeof(iddfs_result)} bytes; astar-{sys.getsizeof(astar_result)} bytes;")

def safe_path(start, end):
    """
    Through the combination of on;ly generating valid successors and A* algorithm,
    The A*'s core logic is best used to ensure that the path found is the best or shortest safe path '
    """
    checks(start, end)
    if start == end:
        return None
    
    def calculate_h(grid):
        total_sum = 0
        for row in grid:
            total_sum += sum(row)
        return total_sum
    
    
    initial_hnvalue = calculate_h(start)
    initial_gnvalue = 0
    initial_fnvalue =  initial_hnvalue + initial_gnvalue
    initial_path = [start]
    start_tuple = grid_tuple(start)
    queue = [(initial_fnvalue, initial_gnvalue, start_tuple, initial_path)]
    g_costs = {start_tuple: initial_gnvalue}

    while queue:
        fnvalue, gnvalue, current_tuple, path = heapq.heappop(queue) # Pop the state with the LOWEST fnvalue
        current_grid = list(list(row) for row in current_tuple)
        
        if current_grid == end:
            return path

        #heck if we found a shorter path to this state already
        #handles cases where a state is re-added with a higher g_cost 
        if gnvalue > g_costs.get(current_tuple, float('inf')):
             continue
        
        current_state = State(current_grid)
        for next_grid in current_state.moves():
            next_tuple = grid_tuple(next_grid)
            
         
            new_gn_value = gnvalue + 1
            
            #check if this new path to next_grid is shorter than any known path
            if new_gn_value < g_costs.get(next_tuple, float('inf')):
                
                g_costs[next_tuple] = new_gn_value
                new_hn_value = calculate_h(next_grid)
                new_fn_value = new_gn_value + new_hn_value
                new_path = path + [next_grid]
                
                heapq.heappush(queue, (new_fn_value, new_gn_value, next_tuple, new_path))
    return None

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
    # print(path_BFS(start,end))
    print(path_DFS(start,end))
    # a_safe_path = safe_path(start, end)
    #
    # if a_safe_path:
    #     print("A* Safe Path Found (Minimum Moves):")
    #     for i, grid in enumerate(a_safe_path):
    #         print(f"\nMove {i+1}:")
    #         for row in grid:
    #             print(row)
    # else:
    #     print("No solution found within the search space.")

if __name__ == '__main__':
    tester()
