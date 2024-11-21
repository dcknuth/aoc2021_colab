# Day 12 part 1
import networkx as nx

DEBUG = False
#filename = 'test12.txt'
#filename = 'test12-2.txt'
#filename = 'test12-3.txt'
filename = 'input12.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

g = nx.Graph()
for l in ls:
    n1, n2 = l.split('-')
    g.add_edge(n1, n2)

path_list = [['start']]
full_paths = []
while len(path_list) > 0:
    cur_path = path_list.pop()
    if cur_path[-1] == 'end':
        full_paths.append(cur_path)
    else:
        for n in g.neighbors(cur_path[-1]):
            if DEBUG:
                print(f'Node is {cur_path[-1]} with neighbor {n}')
            if n.isupper() or n not in cur_path:
                new_path = cur_path.copy()
                new_path.append(n)
                path_list.append(new_path)

print(f'Number of paths is {len(full_paths)}')

# part 2
from collections import Counter
path_list = [['start']]
full_paths = []
while len(path_list) > 0:
    cur_path = path_list.pop()
    if cur_path[-1] == 'end':
        full_paths.append(cur_path)
    else:
        path_counts = Counter()
        two_count = False
        for n in cur_path:
            path_counts[n] += 1
            if n.islower() and path_counts[n] == 2:
                two_count = True    
        for n in g.neighbors(cur_path[-1]):
            if n.isupper() or n not in cur_path or (not two_count and \
                                                    n != 'start'):
                new_path = cur_path.copy()
                new_path.append(n)
                path_list.append(new_path)

print(f'Number of paths, part2, is {len(full_paths)}')