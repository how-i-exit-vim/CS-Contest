import sys

ms = []
for a in sys.stdin:
    a = a[:-3]
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
