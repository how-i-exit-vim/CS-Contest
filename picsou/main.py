import sys

nb = 0
c = 0
ms = [] # nb list

for a in sys.stdin:
    a = a[:-1]
    d = ""
    if "." in a:
        n, d = a.split(".")
        c = max(c, len(d))
        a = n+d
    ms.append((a, len(d)))

for (i,d) in ms:
    i = i + "0"*(c-d)
    nb += int(i)

nb = str(nb)
n, d = nb[:-c], nb[-c:]
n = n.lstrip("0")
d = d.rstrip("0")
nb = n + '.' + d
nb = nb.strip(".")

if nb == "":
    nb = "0"
nb = nb.strip(" ")
print(nb)

