from sys import stdin
from copy import deepcopy as dp
from functools import cache

# Create matrix from given dim
def create_matrix(height, width):
    M = []
    val = 0
    for i in range(height * 2 + 1):
        line = []
        for j in range(width * 2 + 1):
            if (i == 0) or (i == height * 2) or (j == 0) or (j == width * 2):
                line.append('X')
            elif (i % 2 != 1) or (j % 2 != 1):
                line.append(' ')
            else:
                line.append(val)
                val += 1
        M.append(line)
    return M

# Display matrix with "clean" view
def display(M):
    print('\\', *[n for n in range(len(M[0]))])
    for line in M:
        for el in line:
            if (type(el) == int):
                print(el % 10, ' ', end='')
            else:
                print(el, ' ',  end='')
        print()

# Index of case
def case(x, y):
    return (x * 2 + 1), (y * 2 + 1)

# Index of horizontal walls
def h_wall(x, y):
    return (x * 2 + 2), (y * 2 + 1)

# Insert horizontal wall
def insert_h_wall(matrix, x, y):
    x, y = h_wall(x, y)
    matrix[x][y-1] = 'X'
    matrix[x][y] = 'X'
    matrix[x][y+1] = 'X'

# Index of vertical walls
def v_wall(x, y):
    return (x * 2 + 1), (y * 2 + 2)

# Insert vertical wall
def insert_v_wall(matrix, x, y):
    x, y = v_wall(x, y)
    matrix[x-1][y] = 'X'
    matrix[x][y] = 'X'
    matrix[x+1][y] = 'X'

def get_sub_universe(matrix, el):
    sub_universe = set([el])
    for x in range(len(matrix)):
        if el in matrix[x]:
            y = matrix[x].index(el)
            break
    i = 2
    while (matrix[x-i+1][y] != 'X'):        # UP
        sub_universe.add(matrix[x-i][y])
        i += 2

    i = 2                                   # RIGHT
    while (matrix[x][y+i-1] != 'X'):
        sub_universe.add(matrix[x][y+i])
        i += 2

    i = 2                                   # DOWN
    while (matrix[x+i-1][y] != 'X'):
        sub_universe.add(matrix[x+i][y])
        i += 2

    i = 2                                   # LEFT
    while (matrix[x][y-i+1] != 'X'):
        sub_universe.add(matrix[x][y-i])
        i += 2

    return sub_universe

def get_all_sub_universes(matrix, universe):
    all_sub_universes = []
    for el in universe:
        all_sub_universes.append([el, get_sub_universe(matrix, el)])
    return all_sub_universes

def rec(sub_universes, cache={}):
    if (len(sub_universes) == 0):
        return 0
    sub_universes.sort(key=lambda t: len(t[1]), reverse=True)
    if (str(sub_universes) in cache):
        return cache[str(sub_universes)]
    ind = 1
    max = len(sub_universes[0][1])
    while (ind < len(sub_universes)) and (len(sub_universes[ind][1]) == max):
        ind += 1
    maxed_univ = sub_universes[:ind]

    results = []
    for univ in maxed_univ:
        sub_universes_copy = dp(sub_universes)
        sub_universes_copy.remove(univ)
        i = 0
        while i < len(sub_universes_copy):
            if (univ[0] in sub_universes_copy[i][1]):
                sub_universes_copy.pop(i)
            else:
                sub_universes_copy[i][1] = sub_universes_copy[i][1] - univ[1]
                i += 1
        results.append(1 + rec(sub_universes_copy))
    cache[str(sub_universes)] = min(results)
    return cache[str(sub_universes)]

def start_rec(matrix, universe):
    sub_universes = get_all_sub_universes(matrix, universe)
    sub_universes.sort(key=lambda t: len(t[1]), reverse=True)
    ind = 1
    max = len(sub_universes[0][1])
    
    while (ind < len(sub_universes)) and (len(sub_universes[ind][1]) == max):
        ind += 1

    maxed_univ = sub_universes[:ind]

    results = []
    for univ in maxed_univ:
        sub_universes_copy = dp(sub_universes)
        sub_universes_copy.remove(univ)
        i = 0
        while i < len(sub_universes_copy):
            if (univ[0] in sub_universes_copy[i][1]):
                sub_universes_copy.pop(i)
            else:
                sub_universes_copy[i][1] = sub_universes_copy[i][1] - univ[1]
                i += 1
        results.append(1 + rec(sub_universes_copy))
    return min(results)

# Main
if __name__=="__main__":    
    # Getting the height and width
    height = int(stdin.readline())
    width = int(stdin.readline())

    # The Universe
    universe = set([n for n in range(height * width)])

    # Creating the base matrix
    matrix = create_matrix(height, width)

    # Getting the horizontal walls
    N = int(stdin.readline())
    for _ in range(N):
        size = stdin.readline()
        x, y = [int(q) for q in size.split()]
        insert_h_wall(matrix, x-1, y-1)

    # Getting the vertical walls
    N = int(stdin.readline())
    for _ in range(N):
        size = stdin.readline()
        x, y = [int(q) for q in size.split()]
        insert_v_wall(matrix, x-1, y-1)

    display(matrix)

    # result = start_rec(matrix, universe)
    # print(result)

