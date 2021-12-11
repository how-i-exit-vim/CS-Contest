from sys import stdin
from math import sqrt, atan2, degrees
from copy import deepcopy as dp
# import matplotlib.pyplot as plt

######################
### MATH FUNCTIONS ###
######################

def dotProduct(v1, v2):
    return (v1[0] * v2[0] + v1[1] * v2[1])

def crossProduct(v1, v2):
    return (v1[0] * v2[1] - v1[1] * v2[0])

def norme(v1):
    return sqrt(dotProduct(v1, v1))

def colinear(v1, v2):
    return (crossProduct(v1, v2) == 0)

def neg(v1):
    return (-v1[0], -v1[1])

# Measuure the angle between v1 {p1 -> p2} and v2 {p3 -> p4}, turing trigo-wise
def angle(p1, p2, p3=(0, 0), p4=(-1, 0)):
    v1 = (p2[0] - p1[0], p2[1] - p1[1])
    v2 = (p4[0] - p3[0], p4[1] - p3[1])
    dot = dotProduct(v1, v2)
    det = crossProduct(v1, v2)
    angle = degrees(atan2(det, dot))
    return (angle + 360) % 360

def angleVect(v1, v2):
    dot = dotProduct(v1, v2)
    det = crossProduct(v1, v2)
    angle = degrees(atan2(det, dot))
    return (angle + 360) % 360

def normalize(v1):
    return (v1[0]/norme(v1), v1[1]/norme(v1))

def getVect(points):
    l1 = points[:-1]
    l2 = points[1:]
    return [(p2[0] - p1[0], p2[1] - p1[1]) for p1, p2 in zip(l1, l2)]

#####################
### FAT ALGORITHM ###
#####################

# Fonction faites intégralement de nos soins ;)
def convexHull(points):
    border = []
    border.append(min(points, key=lambda p: p[0]))
    while (len(border) == 1) or (border[0] != border[-1]):
        if (len(border) == 1):
            candidates = dp(points)
            candidates.remove(border[-1])
            best = max(candidates, key=lambda p: angle(border[-1], p))
            border.append(best)
            candidates = dp(points)
        else:
            candidates.remove(border[-1])
            best = max(candidates, key=lambda p: angle(border[-1], p, border[-1], border[-2]))
            border.append(best)
    return border

if (__name__=='__main__'):
    ######################
    ### READING INPUTS ###
    ######################
    N = int(stdin.readline())
    data = []
    for i in range(N):
        p = stdin.readline()
        x, y = [float(x) for x in p.split()]
        data.append((x, y))
    data = list(set(data))

    ### Exiting if less than 3 distincts points
    if (len(data) < 3):
        print(0)

    ### If there's at least 3 distincts points
    else:
        hull = convexHull(data)
        
        # plt.figure()
        # plt.scatter([p[0] for p in data], [p[1] for p in data])
        # plt.plot([v[0] for v in hull], [v[1] for v in hull], "red")
        # plt.show()
        
        hull_vect = getVect(hull)

        # Removing every adjacent colinear vectors from the hull
        hull_vect_copy = dp(hull_vect)
        final_hull = [hull_vect_copy.pop(0)]
        while (len(hull_vect_copy) > 0):
            vect = hull_vect_copy.pop(0)
            if (not colinear(vect, final_hull[-1])):
                final_hull.append(vect)
                
        if (colinear(final_hull[0], final_hull[-1])):
            final_hull = final_hull[:-1]
        
        # Renaming for easier typing
        v = final_hull
        
        # Normalizing just in case
        v = list(map(normalize, v))
        
        # Checking if we can find "any" triangles
        if (len(v) < 3):
            print(0)

        else:
        
            triangles = 0
            n = len(v)
            for i in range(n-2):
                for j in range(i+1, n-1):
                    for k in range(j+1, n):
                        a, b, c = v[i], v[j], v[k]
                        flag = angleVect(b, neg(a)) + angleVect(c, neg(b))
                        if (flag >= 180):
                            continue
                        flag = angleVect(c, neg(b)) + angleVect(a, neg(c))
                        if (flag >= 180):
                            continue
                        flag = angleVect(a, neg(c)) + angleVect(b, neg(a))
                        if (flag >= 180):
                            continue
                        triangles += 1

            print(triangles)
