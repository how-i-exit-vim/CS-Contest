from sys import stdin

raw_data = stdin.read()
data = raw_data.split('\n')[:-1]
data = [list(map(int, sub_list.split(' '))) for sub_list in data]

class environment():
    def __init__(self, height, width):
        self.cam_positions = []
        self.height = height
        self.width = width
        self.cam_grid = [[0 for _ in range(width)] for _ in range(height)]
        self.h_wall_grid = [[0 for _ in range(width)] for _ in range(height - 1)]
        self.v_wall_grid = [[0 for _ in range(width - 1)] for _ in range(height)]
        
    def display(self):
        print("[zone]", *self.cam_positions)
        for line in self.cam_grid:
            print(*line)
            
        print("[h_walls]")
        for line in self.h_wall_grid:
            print(*line)
            
        print("[v_walls]")
        for line in self.v_wall_grid:
            print(*line)
            
    def set_camera(self, y, x):
        self.cam_grid[y-1][x-1] = 0
        self.cam_positions.append((y-1, x-1))
        
    def set_h_wall(self, y, x):
        self.h_wall_grid[y-1][x-1] = 1
        
    def set_v_wall(self, y, x):
        self.v_wall_grid[y-1][x-1] = 1

    def is_h_wall(self, y, x, up):
        if ((y == 0) and (up)) or ((y == self.height - 1) and (not up)):
            return True
        delta = 0
        if up:
            delta = 1
        return self.h_wall_grid[y-delta][x] == 1 

    def is_v_wall(self, y, x, left):
        if ((x == 0) and (left)) or ((x == self.width - 1) and (not left)):
            return True
        delta = 0
        if left:
            delta = 1
        return self.v_wall_grid[y][x-delta] == 1

    def __propagate_up__(self, y, x, incr=False, delta=1):
        i = 0
        # up
        while (not self.is_h_wall(y-i, x, True)):
            i += 1
            if (incr):
                self.cam_grid[y-i][x] += delta
            else:
                self.cam_grid[y-i][x] = 0

    def __propagate_right__(self, y, x, incr=False, delta=1):
        i = 0
        # right
        while (not self.is_v_wall(y, x+i, False)):
            i += 1
            if (incr):
                self.cam_grid[y][x+i] += delta
            else:
                self.cam_grid[y][x+i] = 0

    def __propagate_bot__(self, y, x, incr=False, delta=1):
        i = 0
        # bottom
        while (not self.is_h_wall(y+i, x, False)):
            i += 1
            if (incr):
                self.cam_grid[y+i][x] += delta
            else:
                self.cam_grid[y+i][x] = 0

    def __propagate_left__(self, y, x, incr=False, delta=1):
        i = 0
        # left
        while (not self.is_v_wall(y, x-i, True)):
            i += 1
            if (incr):
                self.cam_grid[y][x-i] += delta
            else:
                self.cam_grid[y][x-i] = 0

    def propagate(self, y, x, incr=False):
        if (incr):
            self.cam_grid[y][x] += 1
        else:
            self.cam_grid[y][x] = 0
        self.__propagate_up__(y, x, incr)
        self.__propagate_right__(y, x, incr)
        self.__propagate_bot__(y, x, incr)
        self.__propagate_left__(y, x, incr)      

    def algo(self):
        for y in range(self.height):
            for x in range(self.width):
                self.propagate(y, x, True)

    def get_best(self):
        y = 0
        x = 0
        for yi in range(client.height):
            for xi in range(client.width):
                self.propagate(yi, xi, True, 1)
        
        return y, x

    def reduce(self, y, x):
        for xi in range(self.width):
            if(xi == x):
                continue
            self.__propagate_bot__(y, xi, True, -1)
            self.__propagate_up__(y, xi, True, -1)
        for yi in range(self.height):
            if (yi == y):
                continue
            self.__propagate_left__(yi, x, True, -1)
            self.__propagate_right__(yi, x, True, -1)

    def is_valid(self):
        k = lambda x: x <= 0
        f = lambda x: all(list(map(k, x)))
        return all(list(map(f, self.cam_grid)))

height = data.pop(0)[0]
width = data.pop(0)[0]
client = environment(height, width)

for _ in range(data.pop(0)[0]):
    wall = data.pop(0)
    client.set_h_wall(wall[0], wall[1])
    
for _ in range(data.pop(0)[0]):
    wall = data.pop(0)
    client.set_v_wall(wall[0], wall[1])

client.algo()
cam_amount = 0
while (not client.is_valid()):
    cam_amount += 1
    y, x = client.get_best()
    client.propagate(y, x)
    client.reduce(y, x)

print(cam_amount)
