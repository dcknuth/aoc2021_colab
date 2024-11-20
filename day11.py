# Day 11 part 1

#filename = 'test11.txt'
filename = 'input11.txt'
M_SIZE = 10

with open(filename) as f:
    ls = f.read().strip().split('\n')

m = [[int(x) for x in y] for y in ls]

def step(m):
    # add 1 to everything
    new_m = [[x+1 for x in y] for y in m]
    # look for a process flashes
    flashed = []
    flash = True
    while flash:
        flash = False
        for y in range(M_SIZE):
            for x in range(M_SIZE):
                if new_m[y][x] > 9 and (y, x) not in flashed:
                    flashed.append((y, x))
                    flash = True
                    # up
                    if y > 0:
                        if x > 0:
                            new_m[y-1][x-1] += 1
                        new_m[y-1][x] += 1
                        if x < M_SIZE - 1:
                            new_m[y-1][x+1] += 1
                    # down
                    if y < M_SIZE - 1:
                        if x > 0:
                            new_m[y+1][x-1] += 1
                        new_m[y+1][x] += 1
                        if x < M_SIZE - 1:
                            new_m[y+1][x+1] += 1
                    # left
                    if x > 0:
                        new_m[y][x-1] += 1
                    # right
                    if x < M_SIZE - 1:
                        new_m[y][x+1] += 1
    num_flashes = len(flashed)
    while len(flashed) > 0:
        y, x = flashed.pop()
        new_m[y][x] = 0
    return(num_flashes, new_m)

total_flashes = 0
num_flashes = 0
for n in range(100):
    num_flashes, m = step(m)
    total_flashes += num_flashes
print(f'{total_flashes=}')

# part 2
steps = 100
while num_flashes != 100:
    num_flashes, m = step(m)
    steps += 1
print('All octopuses flash at step', steps)
