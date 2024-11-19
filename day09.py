# Day 9 part 1

#filename = 'test09.txt'
filename = 'input09.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

hmap = [[int(x) for x in l] for l in ls]

risk_sum = 0
low_points = []
for y, row in enumerate(hmap):
    for x, node in enumerate(row):
        # up
        if y > 0:
            if node >= hmap[y-1][x]:
                continue
        # down
        if y < len(hmap)-1:
            if node >= hmap[y+1][x]:
                continue
        # left
        if x > 0:
            if node >= hmap[y][x-1]:
                continue
        # right
        if x < len(row)-1:
            if node >= hmap[y][x+1]:
                continue
        # add as lowest
        risk_sum += node + 1
        low_points.append((y, x))

print(f'Risk sum is {risk_sum}')

# part 2
# Added a low points list to part one to use here
basins = dict()
while len(low_points) > 0:
    cur_lp = low_points.pop()
    frontier = [cur_lp]
    visited = dict()
    while len(frontier) > 0:
        cur_p = frontier.pop()
        y, x = cur_p
        # up
        if y > 0:
            if hmap[y-1][x] != 9 and (y-1, x) not in visited and \
                (y-1, x) not in frontier:
                frontier.append((y-1, x))
        # down
        if y < len(hmap)-1:
            if hmap[y+1][x] != 9 and (y+1, x) not in visited and \
                (y+1, x) not in frontier:
                frontier.append((y+1, x))
        # left
        if x > 0:
            if hmap[y][x-1] != 9 and (y, x-1) not in visited and \
                (y, x-1) not in frontier:
                frontier.append((y, x-1))
        # right
        if x < len(hmap[y])-1:
            if hmap[y][x+1] != 9 and (y, x+1) not in visited and \
                (y, x+1) not in frontier:
                frontier.append((y, x+1))
        visited[(y, x)] = True
    basins[(len(visited), cur_lp)] = len(visited)

basin_list = sorted(basins.keys(), reverse=True)
product = 1
for i in range(3):
    product *= basins[basin_list[i]]
print(f'Product is {product}')
