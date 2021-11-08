import sys
from numpy import array, transpose

def solve(r, c):
   matrix = [[0]*len(c) for _ in range(len(r))]
   visited = set()

   def minimum(r,c):
      min_total = float('inf')
   
      type = ''
      for i in range(len(r)):
         if(r[i] < min_total):
            index = i
            type = 'row'
            min_total = r[i]

      for i in range(len(c)):
         if(c[i] < min_total):
            min_total = c[i]
            type = 'col'
            index = i

      if(type == 'row'):
         r[index] = float('inf')

         for i in range(len(c)):
            if(c[i] != float('inf') and c[i] >= min_total):
               c[i] -= min_total
               matrix[index][i] = min_total
               break

      if(type == 'col'):
         c[index] = float('inf')
         for i in range(len(r)):
            if(r[i] != float('inf') and r[i] >= min_total):
               r[i] -= min_total
               matrix[i][index] = min_total
               break

      visited.add((index,type))

   while len(visited) != len(r)+len(c):
      minimum(r,c)

   return matrix

ms = []
for a in sys.stdin:
    m = [int(c) for c in a.split()]
    ms.append(m)

rowSum = ms[1]
colSum = ms[0]

x = solve(rowSum, colSum)

for i in x:
    for j in range(len(i)):
        print(i[j], end="")
        if j != len(i)-1:
            print(" ", end="")
    print("")
