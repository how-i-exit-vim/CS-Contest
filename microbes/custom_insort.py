def viral_infection(microbe, immune_system):
    if len(immune_system) == 0:
        immune_system.append(microbe)
    else:
        viral_infection_rec(microbe, immune_system, 0, len(immune_system))

def viral_infection_rec(microbe, immune_system, left, right):
    n = (left + right)//2
    delta = right - left
    studying = immune_system[n]
    if (delta == 1):
        if (microbe > studying):
            immune_system[n] = microbe
        else:
            if(n == 0):
                immune_system.insert(0, microbe)
                return
            else:
                immune_system[n-1] = microbe
    elif microbe <= studying:
        viral_infection_rec(microbe, immune_system, left, n)
    else:
        viral_infection_rec(microbe, immune_system, n, right)

a = [1, 1, 1]
viral_infection(1, a)
print(a)
