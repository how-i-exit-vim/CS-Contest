from sys import stdin

def calc(nombres):
    l = []
    part_entiere = 0
    decimale1 = 0
    decimale2 = 0
    for a in nombres:
        if '.' in a:
            if a[0] == ".":
                a = "0" + a
            n, d = a.split(".")
            n = int(n)
            d = d[:2]
            d1 = 0
            d2 = 0
            if len(d) == 2:
                d1 = int(d[0])
                d2 = int(d[1])
            elif len(d) == 1:
                d1 = int(d[0])
            
            # Add 1 per 1
            decimale1    += d1
            decimale2    += d2
            part_entiere += n
            
            decimale1    += decimale2 // 10
            part_entiere += decimale1 // 10
            decimale1 %= 10
            decimale2 %= 10

        else:
            part_entiere += int(a)
    return f"{part_entiere}.{decimale1}{decimale2}"

for i in range(1000):
    for j in range(100):
        c = i + j
        k = str(c)
        ist = str(i)
        jst = str(j)
        ist = ist[:-2] + "." + ist[-2:] 
        jst = jst[:-2] + "." + jst[-2:] 
        nb = k[:-2] + "." + k[-2:]
        if nb[0] == ".":
            nb = "0" + nb
        if nb[-2] == ".":
            nb = nb + "0"
        nbf = calc((ist, jst))
        if not nb == nbf:
            print(f"{ist} + {jst} = {nb} != {nbf}")
