from sys import stdin


def display(matrix):
    #print("-" * 2 * len(matrix[0]))
    for line in matrix:
        #for i in range(len(line)):
        #    if line[i] == 0:
        #        line[i] = "_"
        print(line[0], end="")
        for x in line[1:]:
            print(" " + str(x), end="")
        print()
    #print("-" * 2 * len(matrix[0]))

# OK?
def read_matrix():
    size = stdin.readline()
    x, y = [int(nb) for nb in size.split()]
    M = []
    for i in range(x):
        line = stdin.readline()
        line = [int(nb) for nb in line.split()]
        if y != len(line):
            raise Exception("bande de batards")
        M.append(line)
    return M

# Ok
def symmetric(M):
    M2 = []
    for i in range(len(M)):
        M2.append(M[i][::-1])
    return M2

# OK
def rot90(M):
    return [[M[j][i] for j in range(len(M))] for i in range(len(M[0])-1,-1,-1)]

# Fully working
def get_isotopes(bug):
    isotopes = []
    B1 = bug
    B2 = symmetric(bug)
    isotopes.append(B1)
    isotopes.append(B2)
    for i in range(4):
        B1 = rot90(B1)
        B2 = rot90(B2)
        isotopes.append(B1)
        isotopes.append(B2)
    return isotopes

# shape(m) = shape(bug)
def is_bugged(M, bug):
    for i in range(len(bug)):
        for j in range(len(bug[i])):
            if bug[i][j] == 1 and M[i][j] == 0:
                return False
    return True

# Get a cut of the matric of size (sx, sy) at the point x, y
def cut_matrix(M, x, y, sx, sy):
    M2 = []
    for i in range(sx):
        sub = M[x+i][y:y+sy]
        M2.append(sub)
    return M2

# Paste B into M at position x, y
def paste(M, B, x, y):
    for i in range(len(B)):
        for j in range(len(B[0])):
            if B[i][j] == 1:
                M[x+i][y+j] = B[i][j]

# create a matrix full of 0 of size x, y
def zeros(x, y):
    M2 = []
    for i in range(x):
        M2.append([0] * y)
    return M2 

# get all submatrix of size x, y in M
def get_all_slices(M, x, y):
    S = []
    for i in range(len(M) - x + 1):
        for j in range(len(M[0]) - y + 1):
            M2 = cut_matrix(M, i, j, x, y)
            S.append((i, j, M2))
    return S


def trim(bug):
    while (sum(bug[0]) == 0) and len(bug) > 0:
        bug.pop(0)
    while (sum(bug[-1]) == 0) and len(bug) > 0:
        bug.pop(-1)
    bug = rot90(bug)
    while (sum(bug[0]) == 0) and len(bug) > 0:
        bug.pop(0)
    while (sum(bug[-1]) == 0) and len(bug) > 0:
        bug.pop(-1)
    return bug 


if __name__ == "__main__":
    nb_bugs = int(stdin.readline())
    bugs = [] 
    
    for i in range(nb_bugs):
        M = read_matrix()
        if M == zeros(len(M),len(M[0])):
            continue
        M2 = trim(M)
        bugs += get_isotopes(M2)
    
    M = read_matrix() # Matrice finale
    F = zeros(len(M), len(M[0]))

    for bug in bugs:
        slices = get_all_slices(M, len(bug), len(bug[0]))
        for x, y, s in slices:
            if is_bugged(s, bug):
                paste(F, bug, x, y)
    display(F)

