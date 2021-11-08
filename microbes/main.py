import sys

a = ""
c = sys.stdin.read(1)
while c != '0':
    a = a + c
    c = sys.stdin.read(1)

ms = []
a = a.strip()
m = [int(c) for c in a.split()]
ms = m

corps = []
for m in ms:
    if corps == [] or min(corps) > m:
        corps.append(m)
    else:
        corps.sort(reverse=True)
        for i in range(len(corps)):
            if corps[i] < m:
                corps[i] = m
                break

print(len(corps))
