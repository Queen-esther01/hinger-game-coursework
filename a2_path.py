"""
Hinger Project
Coursework 001 for: CMP-7058A Artificial Intelligence

Includes functions for retrieving safe paths for Task 2

@author: E6 (100501127, 100527347)
@date: 29/09/2025

"""

from copy import deepcopy


from ai_state import State




def path_BFS(start,end):
    return

def path_DFS(start, end):

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
    end = [[1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]]
    
    start = [
        [1, 1, 0, 0, 2],
        [1, 1, 0, 0, 0],
        [0, 0, 1, 1, 1],
        [0, 0, 0, 1, 1]]
    
    path = path_DFS(start, end)
    
    print(path)

    return

# if __name__ == '__main__':
tester()