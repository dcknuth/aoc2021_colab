# Day 14 part 1
from collections import Counter

filename = 'test14.txt'
#filename = 'input14.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

start = ls[0]
subs = dict()
for l in ls[2:]:
    pair, ins = l.split(' -> ')
    subs[pair] = ins

def doStep(s, subs):
    new_s = []
    for i in range(len(s)-1):
        new_s.append(s[i])
        if s[i:i+2] in subs:
            new_s.append(subs[s[i:i+2]])
    new_s.append(s[-1])
    return(''.join(new_s))

s = start
for x in range(10):
    s = doStep(s, subs)

e_counts = Counter()
for c in s:
    e_counts[c] += 1
e_list = list(e_counts.items())
e_list.sort(key=lambda x: x[1])
print(f'Answer is {e_list[-1][1] - e_list[0][1]}')

# part 2
# this would get too long using the method above, so let's save the first 12
#  steps and look for patterns
def doStep(s, subs):
    new_s = []
    for i in range(len(s)-1):
        new_s.append(s[i])
        if s[i:i+2] in subs:
            new_s.append(subs[s[i:i+2]])
    new_s.append(s[-1])
    return(''.join(new_s))

s = start
results = []
results.append([s, {'N':2, 'C':1, 'B':1}])
for x in range(20):
    s = doStep(s, subs)
    e_counts = Counter()
    for c in s:
        e_counts[c] += 1
    results.append([s, e_counts])
# list results
for i, result in enumerate(results):
    cur_s, cur_count = result
    e_list = list(cur_count.items())
    e_list.sort(key=lambda x: x[1])
    print('Round:', i, end=' ')
    if len(cur_s) < 560:
        print(cur_s)
    for x in e_list:
        print(f'{x[0]}:{x[1]}', end=' ')
    print()
# list just the delta in answers and hope for a formula
for i, result in enumerate(results):
    cur_s, cur_count = result
    e_list = list(cur_count.items())
    e_list.sort(key=lambda x: x[1])
    print('Round:', i)
    ans = e_list[-1][1] - e_list[0][1]
    print(f'Greatest {e_list[-1][1]} least {e_list[0][1]} {ans=}')

# Now just follow the progression of pairs for a bit
def pairStep(pairs, subs):
    new_pairs = []
    for pair in pairs:
        new_pairs.append(''.join([pair[0], subs[pair]]))
        new_pairs.append(''.join([subs[pair], pair[1]]))
    return(new_pairs)

# Looks at some pair progressions
for pair in subs.keys():
    cur_pairs = [pair]
    print("Starting pair", cur_pairs)
    for i in range(5):
        cur_pairs = pairStep(cur_pairs, subs)
        print(cur_pairs)
    print()
# NB, BN, BB, BC all have "seen before" loops within four iterations.
#  Can we use this for something? Maybe LCM from first seen to next will
#  produce a stable step. CN is seen again in the next step, so 1. CC is
#  seen again in two steps, so 2 and so forth?
# Maybe step until each of the pairs in the original is seen again?
original = ['NN', 'NC', 'CB']
for i in range(1,20):
    result = results[i][0]
    found_all = True
    for p in original:
        if p not in result:
            found_all = False
            break
    if found_all:
        print("First time all original pairs found is", i)
# This never happens because NN never shows up again
# Maybe detect and loop until all dead ends are eliminated from the orig
#  then get the LCM? For the example, NN is out after one step, but not
#  seeing a pattern for the max value from step 2 on
