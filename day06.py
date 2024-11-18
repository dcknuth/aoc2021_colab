# Day 6 part 1

#filename = 'test06.txt'
filename = 'input06.txt'
DEBUG = 5

with open(filename) as f:
    ls = f.read().strip().split(',')

fish = [int(x) for x in ls]

day = 1
while day < 81:
    new_fish = []
    for cur_fish in fish:
        if cur_fish == 0:
            new_fish.append(6)
            new_fish.append(8)
        else:
            new_fish.append(cur_fish - 1)
    fish = new_fish
    day += 1

print(f'Number of fish after 80 days is {len(fish)}')

# Day 2
# This will go to billions or trillions, so need another plan
# At each given day, we only need to follow one count of each number through
#  the rest of the days instead of each fish
from collections import Counter
fish_count = Counter()
day_count = 1
for cur_fish in ls:
    fish_count[int(cur_fish)] += 1
if DEBUG < 5:
    print(f'Initial state: {fish_count}')
while day_count < 257:
    new_fish = Counter()
    for cur_fish in fish_count.keys():
        if cur_fish != 0:
            new_fish[cur_fish-1] = fish_count[cur_fish]
    new_fish[6] += fish_count[0]
    new_fish[8] = fish_count[0]
    fish_count = new_fish
    if DEBUG < 5:
        print(f'After day {day_count}: {fish_count}')
    day_count += 1

num_fish = 0
for cur_fish in fish_count.keys():
    num_fish += fish_count[cur_fish]
print(f'Number of fish after 256 days is {num_fish}')
