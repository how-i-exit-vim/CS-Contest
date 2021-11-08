import sys

l = []
for a in sys.stdin:
    l.append(a[:-1])

dmax = 0
for x in l:
    if "." in x:
        n, d = x.split('.')
        dmax = max(dmax, len(d))

res = 0
for x in l:
    if "." in x:
        n, d = x.split('.')
        x = n + d + "0"*(dmax - len(d))
    else:
        x = x + "0"*dmax
    res += int(x)

res = str(res)
if dmax != 0:
    n, d = res[:-dmax], res[-dmax:]
    d = d.rstrip("0")
    res = n + '.' + d
    if res[0] == ".":
        res = "0" + res
    if res[-1] == ".":
        res = res[:-1]

print(res)
