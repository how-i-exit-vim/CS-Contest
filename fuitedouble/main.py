from sys import stdin

height = int(stdin.readline())
level = 0
force = 0

def malediction():
    global height
    a = list(range(1, height + 1))
    a.reverse()
    b = []
    for i in range(height):
        if a[i] > height//2:
            if a[i] % 2 == 0:
                b.append(a[i]-1)
                b.append(a[i]//2)
        else:
            if a[i]+1 not in b or 2*a[i] not in b:
                b.append(a[i])
    return b

malade = []
if height % 2 == 1:
    level = 1
else: 
    malade = malediction()
    if level+1 not in malade:  
        level = 1
    else:
        level = 2

print(level)
for a in stdin:
    
    level = int(a)
    if level >= height:
        break
    
    if height % 2 == 1:
        cp = "o"
    else:
        if level+1 not in malade:  
            cp = "o"
        else:
            cp = "j'en peux plus"


    if cp == "o":
        level += 1
    else:
        level *= 2

    print(level)
    

