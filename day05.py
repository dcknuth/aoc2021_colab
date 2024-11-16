# Day 5 part 1
from collections import Counter

#filename = 'test05.txt'
filename = 'input05.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

lines = []
for l in ls:
    p1, p2 = l.split(' -> ')
    x1, y1 = map(int, p1.split(','))
    x2, y2 = map(int, p2.split(','))
    lines.append([x1, y1, x2, y2])

point_counts = Counter()
for line in lines:
    x1, y1, x2, y2 = line
    if x1 == x2:
        if y1 <= y2:
            for y in range(y1, y2+1):
                point_counts[(y, x1)] += 1
        else:
            for y in range(y2, y1+1):
                point_counts[(y, x1)] += 1
    elif y1 == y2:
        if x1 <= x2:
            for x in range(x1, x2+1):
                point_counts[(y1, x)] += 1
        else:
            for x in range(x2, x1+1):
                point_counts[(y1, x)] += 1

overlaps = 0
for key in point_counts.keys():
    if point_counts[key] > 1:
        overlaps += 1

print('Number of points where at least two lines overlap is', overlaps)


# part 2
point_counts = Counter()
for line in lines:
    x1, y1, x2, y2 = line
    #print(f'{x1=} {x2=} {y1=} {y2=}')
    if x1 == x2:
        if y1 <= y2:
            for y in range(y1, y2+1):
                point_counts[(y, x1)] += 1
        else:
            for y in range(y2, y1+1):
                point_counts[(y, x1)] += 1
    elif y1 == y2:
        if x1 <= x2:
            for x in range(x1, x2+1):
                point_counts[(y1, x)] += 1
        else:
            for x in range(x2, x1+1):
                point_counts[(y1, x)] += 1
    else:
        if y2 > y1:
            y_step = 1
        else:
            y_step = -1
        if x2 > x1:
            x_step = 1
        else:
            x_step = -1
        cur_x = x1
        cur_y = y1
        for i in range(abs(y2 - y1)+1):
            point_counts[(cur_y, cur_x)] += 1
            cur_x += x_step
            cur_y += y_step

overlaps = 0
for key in point_counts.keys():
    if point_counts[key] > 1:
        overlaps += 1

print('Number of points where at least two lines overlap is', overlaps)
