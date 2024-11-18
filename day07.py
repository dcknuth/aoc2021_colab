# Day 7 part 1

#filename = 'test07.txt'
filename = 'input07.txt'

with open(filename) as f:
    ls = f.read().strip().split(',')

crabs = [int(x) for x in ls]

min_p = min(crabs)
max_p = max(crabs)
min_fuel = 1000000000
best_p = -1
for cur_p in range(min_p, max_p+1):
    total_fuel = 0
    for crab in crabs:
        total_fuel += abs(cur_p - crab)
    if total_fuel < min_fuel:
        min_fuel = total_fuel
        best_p = cur_p
print(f'Min fuel position is {best_p} with {min_fuel=}')

# part 2
# We could probably brute force this also, but we could also use the sum
#  formula n * (n+1)/2 with the same loop
min_p = min(crabs)
max_p = max(crabs)
min_fuel = 1000000000
best_p = -1
for cur_p in range(min_p, max_p+1):
    total_fuel = 0
    for crab in crabs:
        total_fuel += abs(cur_p - crab) * (1+abs(cur_p - crab)) / 2
    if total_fuel < min_fuel:
        min_fuel = total_fuel
        best_p = cur_p
print(f'Min fuel position is {best_p} with {min_fuel=}')
