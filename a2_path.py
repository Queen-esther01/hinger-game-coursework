"""
Hinger Project
Coursework 001 for: CMP-7058A Artificial Intelligence

Includes functions for retrieving safe paths for Task 2

@author: E6 (100501127)
@date: 29/09/2025

"""

# Ignore this, I am using to test
# def breadthFirstSearch(array):
#     queue = [array[0][0]]
#     visited = []
#     current = array[0][0]
#     while len(queue) != 0:
#         visited = queue.pop(0)
#         # array.push(current.name)
#         for value of queue[0]:
#             queue.push(nodes)
#         }
#     }
#     console.log(array)
#     return array


def path_BFS(start,end):
    """ returns safe paths from start to end """
    if len(start) != len(end) or len(start[0]) != len(end[0]):
        return None
    for rowIndex in range(len(start)):
        for columnIndex in range(len(start[rowIndex])):
            if start[rowIndex][columnIndex] > 1 or end[rowIndex][columnIndex] > 1:
                return None

    return

def path_DFS(start,end):
    return

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
    path_BFS(start,end)

if __name__ == '__main__':
    tester()