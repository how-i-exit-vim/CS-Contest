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
nb = nb[:-c] + '.' + nb[-c:]
nb = nb.lstrip("0")
nb = nb.strip(".")
if nb == "":
    nb = "0"
nb = nb.strip(" ")
print(nb)

