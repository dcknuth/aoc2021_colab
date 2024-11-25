# Day 15 part 1
import networkx as nx

filename = 'test15.txt'
filename = 'input15.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

m = [[int(x) for x in y] for y in ls]
g = nx.DiGraph()
for y in range(len(m)):
    for x in range(len(m[y])):
        # up
        if y > 0:
            g.add_edge((y, x), (y-1, x), weight=m[y-1][x])
        # down
        if y < len(m) -1:
            g.add_edge((y, x), (y+1, x), weight=m[y+1][x])
        # left
        if x > 0:
            g.add_edge((y, x), (y, x-1), weight=m[y][x-1])
        # right
        if x < len(m[y]) - 1:
            g.add_edge((y, x), (y, x+1), weight=m[y][x+1])

risk = nx.shortest_path_length(g, (0, 0), target=(len(m)-1, len(m[-1])-1),
                               weight='weight')
print(f'Total risk level is {risk}')

# part 2
import numpy as np
a = np.array(m, dtype=int)
full_array = a.copy()
# make the first row
next_a = a.copy()
for i in range(4):
    next_a = next_a + 1
    next_a[next_a > 9] = 1
    full_array = np.hstack((full_array, next_a.copy()))
# now add rows
next_a = full_array.copy()
for i in range(4):
    next_a = next_a + 1
    next_a[next_a > 9] = 1
    full_array = np.vstack((full_array, next_a.copy()))
# back to a list
m = full_array.tolist()

g = nx.DiGraph()
for y in range(len(m)):
    for x in range(len(m[y])):
        # up
        if y > 0:
            g.add_edge((y, x), (y-1, x), weight=m[y-1][x])
        # down
        if y < len(m) -1:
            g.add_edge((y, x), (y+1, x), weight=m[y+1][x])
        # left
        if x > 0:
            g.add_edge((y, x), (y, x-1), weight=m[y][x-1])
        # right
        if x < len(m[y]) - 1:
            g.add_edge((y, x), (y, x+1), weight=m[y][x+1])

risk = nx.shortest_path_length(g, (0, 0), target=(len(m)-1, len(m[-1])-1),
                               weight='weight')
print(f'Total risk level of expanded map is {risk}')
