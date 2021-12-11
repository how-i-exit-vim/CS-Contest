from sys import stdin
from copy import deepcopy as dp


# valuation p adique
def v(p, n):
    if n % p != 0 or n == 0:
        return 0
    else:
        return v(p, n//p) + 1

A = 0
B = 0

def play_old(A, B):
    a = v(2, A)
    b = v(2, B)
    if a % 2 == 1 and a < b:
        return "A"
    if b % 2 == 1 and b < a:
        return "B"
    if b > a:
        return "B"
    else:
        return "A"

def play(A, B):
    if A % 2 == 1 and B % 2 == 1: # CAS 1 : Impair impair, on joue nptq
        R = "Z"
    elif A % 2 == 0 and B % 2 == 1: # CAS 2 : Un impair
        R = "A"
    elif B % 2 == 0 and A % 2 == 1:
        R = "B"
    elif B % 4 == 0 and A % 4 == 0: # CAS 3 (CHIANT) : tout modulo 4
        return play_old(A, B)
    elif B % 2 == 0 and B % 4 != 0: # CAS 4: Un modulo 2
        R = "B"
    elif A % 2 == 0 and A % 4 != 0:
        R = "A"
    else:
        exit(1) # impossible
    return R

def gameover():
    global A
    global B
    if A % 2 == 1 and B % 2 == 1:
        return True
    if A == 0 and B == 0:
        return True
    return False

def move(e):
    global A
    global B
    if e == "A":
        B += A//2
        A //= 2
    elif e == "B":
        A += B//2
        B //= 2
    return e

height = stdin.readline()
A, B = [int(i) for i in height.split()]
if gameover():
    exit(0)

for _ in range(100): 
    #print(played)
    #print(history)
    cp = play(A, B)
    move(cp)
    print(cp)
    #print(A, B)
    if gameover():
        break

    e = stdin.readline()
    e = e.rstrip()

    move(e)
    #print(A, B)
    if gameover():
        break
    

