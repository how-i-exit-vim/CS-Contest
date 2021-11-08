import sys

ms = []

for a in sys.stdin:
    m = [int(c) for c in a.split()]
    ms.append(m)

rowSum = ms[1]
colSum = ms[0]

M = len(rowSum)
N = len(colSum)

result = [[0]*N for _ in range(M)]

for i in range(M):
    for j in range(N):
        result[i][j] = min(rowSum[i], colSum[j])
        rowSum[i] -= result[i][j]
        colSum[j] -= result[i][j]

x = result
for i in x:
    for j in range(len(i)):
        print(i[j], end="")
        if j != len(i)-1:
            print(" ", end="")
    print("")
