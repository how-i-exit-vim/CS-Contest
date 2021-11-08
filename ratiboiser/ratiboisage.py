from sys import stdin
from math import log

raw_data = stdin.read()
data = ' '.join(raw_data.split())
data = data.replace('\n', ' ')
data = [int(num) for num in data.split(' ')][2:]

world = []
for i in range(int(len(data)/3)):
    human = [data[3 * i], data[3 * i + 1], data[3 * i + 2]]
    world.append(human)

def kill(world):
    weaks = []
    i = 0
    while (i < len(world)):
        human = world[i]
        if (human[1] == human[2] == -1):
            weaks.append(world.pop(i)[0])
        else:
            i += 1
    return weaks

def weaken(world, dead):
    for i in range(len(world)):
        for j in range(2):
            if world[i][j+1] in dead:
                world[i][j+1] = -1

kill_waves = []
while (len(world) > 1):
    dead = kill(world)
    kill_waves.append(len(dead))
    weaken(world, dead)

print(*kill_waves)
