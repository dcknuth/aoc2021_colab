# Day 10 part 1
from collections import Counter

DEBUG = 5
#filename = 'test10.txt'
filename = 'input10.txt'
OPEN = ['(', '[', '{', '<']
CLOSE = [')', ']', '}', '>']
VALUES = {')':3, ']':57, '}':1197, '>':25137}
C_VALS = {')':1, ']':2, '}':3, '>':4}

with open(filename) as f:
    ls = f.read().strip().split('\n')

cp_list = []
illegals = Counter()
for l in ls:
    c_points = 0
    lifo = []
    bad_line = False
    for c in l:
        if c in OPEN:
            lifo.append(c)
        elif c in CLOSE:
            matching = lifo.pop()
            expecting = CLOSE[OPEN.index(matching)]
            if c != expecting:
                if DEBUG < 5:
                    print(f'Expected {expecting} but got {c}')
                illegals[c] += 1
                bad_line = True
                break
        else:
            print(f'Error: unknown symbol {c}')
    if not bad_line:
        while len(lifo) > 0:
            c_points *= 5
            matching = lifo.pop()
            expecting = CLOSE[OPEN.index(matching)]
            c_points += C_VALS[expecting]
        cp_list.append(c_points)

points = 0
for key in illegals.keys():
    points += illegals[key] * VALUES[key]
print(f'{points=}')

# part 2
# adding to part 1 to score completion characters
# get the middle score as given in the instructions
cp_list.sort()
c_score = cp_list[len(cp_list)//2]
print(f'{c_score=}')
