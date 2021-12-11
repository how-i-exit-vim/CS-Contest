from sys import stdin
from functools import cache

raw_data = stdin.read()
data = raw_data.split()
data.pop(0)
data = list(map(int, data))

def div(a, b):
    return (b != 0) and ((a % b) == 0) 

def combine(a, b):
    res = []
    for i in a:
        for j in b:
            res.append(i + j)
            res.append(i - j)
            res.append(-i + j)
            res.append(-i - j)
            res.append(i * j)
            res.append(i * -j)
            if div(i, j):
                res += [i // j]
            if div(i, -j):
                res += [i // -j]
    return list(set(res))

def slices(data):
    for i in range(2, len(data)):
        for j in range(0, len(data)-i+1):
            yield (data[:j], data[j:j+i], data[j+i:])

def evaluate(data, cache={}):
    res = []
    for a, b, c in slices(data):
        if len(a) == 0:
            if (len(b) > 2):
                if str(b) not in cache:
                    cache[str(b)] = evaluate(b)
                b = cache[str(b)]
            elif (len(b) == 2):
                b = combine([b[0]], [b[1]])
            if (len(c) > 2):
                if str(c) not in cache:
                    cache[str(c)] = evaluate(c)
                c = cache[str(c)]
            elif (len(c) == 2):
                c = combine([c[0]], [c[1]])
            res += combine(b, c)
        elif len(c) == 0:
            if (len(a) > 2):
                if str(a) not in cache:
                    cache[str(a)] = evaluate(a)
                a = cache[str(a)]
            elif (len(a) == 2):
                a = combine([a[0]], [a[1]])
            if (len(b) > 2):
                if str(b) not in cache:
                    cache[str(b)] = evaluate(b)
                b = cache[str(b)]
            elif (len(b) == 2):
                b = combine([b[0]], [b[1]])
            res += combine(a, b)
        else:
            if (len(a) >= 2):
                if str(a) not in cache:
                    cache[str(a)] = evaluate(a)
                a = cache[str(a)]
            elif (len(a) == 2):
                a = combine([a[0]], [a[1]])
            if (len(b) >= 2):
                if str(b) not in cache:
                    cache[str(b)] = evaluate(b)
                b = cache[str(b)]
            elif (len(b) == 2):
                b = combine([b[0]], [b[1]])
            if (len(c) >= 2):
                if str(c) not in cache:
                    cache[str(c)] = evaluate(c)
                c = cache[str(c)]
            elif (len(c) == 2):
                c = combine([c[0]], [c[1]])
            res += combine(a, combine(b, c))
            res += combine(combine(a, b), c)
    return list(set(res))

# MAIN PROGRAM

obtainable = evaluate(data)

first_valid = 1
while (True):
    if (first_valid not in obtainable):
        break
    else:
        first_valid += 1
    
print(first_valid)

