# Day 13 part 1
import numpy as np

#filename = 'test13.txt'
filename = 'input13.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

y_max = x_max = 0
dots = []
start_folds = 0
for i, l in enumerate(ls):
    if l == '':
        start_folds = i+1
        break
    else:
        x, y = list(map(int, l.split(',')))
        dots.append([y, x])
        if y > y_max:
            y_max = y
        if x > x_max:
            x_max = x
folds = []
for l in ls[start_folds:]:
    fold = list(l.split())
    axis, n = fold[2].split('=')
    n = int(n)
    folds.append([axis, n])

m = [[0 for x in range(x_max+1)] for y in range(y_max+1)]
for y, x in dots:
    m[y][x] = 1
m = np.array(m, dtype=int)

def doFold(m, fold):
    axis, n = fold
    if axis == 'y':
        new_top = m[:n]
        new_bottom = m[n+1:]
        # pad if needed
        if new_top.shape[0] > new_bottom.shape[0]:
            n_rows = new_top.shape[0] - new_bottom.shape[0]
            new_bottom = np.pad(new_bottom, ((0, n_rows), (0, 0)),
                                mode='constant')
        elif new_top.shape[0] < new_bottom.shape[0]:
            n_rows = new_bottom.shape[0] - new_top.shape[0]
            new_top = np.pad(new_top, ((n_rows,0), (0, 0)),
                             mode='constant')
        # mirror bottom
        new_bottom = new_bottom[::-1]
        new_m = new_top + new_bottom
    if axis == 'x':
        new_left = m[:, :n]
        new_right = m[:, n+1:]
        # pad if needed
        if new_left.shape[1] > new_right.shape[1]:
            n_cols = new_left.shape[1] - new_right.shape[1]
            new_right = np.pad(new_right, ((0,0), (0, n_cols)),
                               mode='constant')
        elif new_left.shape[1] < new_right.shape[1]:
            n_cols = new_right.shape[1] - new_left.shape[1]
            new_left = np.pad(new_left, ((0, 0), (n_cols, 0)),
                              mode='constant')
        # mirror
        new_right = new_right[:, ::-1]
        # combine
        new_m = new_left + new_right
    return(new_m)

m = doFold(m, folds.pop(0))
dot_count = np.count_nonzero(m > 0)
print('Number of dots after one fold is', dot_count)

# part 2, finish folding and print
for fold in folds:
    m = doFold(m, fold)
m = m.tolist()
for row in m:
    for x in row:
        if x > 0:
            print('#', end='')
        else:
            print(' ', end='')
    print()
