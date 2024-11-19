# Day 8 part 1

#filename = 'test08.txt'
filename = 'input08.txt'
looking_for = [2, 3, 4, 7]

with open(filename) as f:
    ls = f.read().strip().split('\n')

count = 0
for l in ls:
    all_segs, output = l.split(' | ')
    for cur_digit in output.split():
        if len(cur_digit) in looking_for:
            count += 1

print('Unique digits are', count)

# part 2
from collections import defaultdict
test_case = 'acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf'

def find_digits(in_digits, out_digits):
    lengths = defaultdict(list)
    decode = dict()
    for digit in in_digits:
        lengths[len(digit)].append(set(digit))
    # set unique lengths
    one = set(lengths[2][0])
    decode[''.join(sorted(list(one)))] = '1'
    four = set(lengths[4][0])
    decode[''.join(sorted(list(four)))] = '4'
    seven = set(lengths[3][0])
    decode[''.join(sorted(list(seven)))] = '7'
    eight = set(lengths[7][0])
    decode[''.join(sorted(list(eight)))] = '8'
    # find 6
    six = set()
    for i in range(len(lengths[6])):
        if len(lengths[6][i] - one) == 5:
            six = lengths[6].pop(i)
            break
    decode[''.join(sorted(list(six)))] = '6'
    # find 5
    five = set()
    for i in range(len(lengths[5])):
        if len(lengths[5][i] - six) == 0:
            five = lengths[5].pop(i)
            break
    decode[''.join(sorted(list(five)))] = '5'
    # find 3 and 2
    three = set()
    for i in range(len(lengths[5])):
        if len(lengths[5][i] - seven) == 2:
            three = lengths[5].pop(i)
            break
    two = lengths[5].pop()
    decode[''.join(sorted(list(three)))] = '3'
    decode[''.join(sorted(list(two)))] = '2'
    # find 9 and 0
    nine = set()
    for i in range(len(lengths[6])):
        if len(lengths[6][i] - three) == 1:
            nine = lengths[6].pop(i)
            break
    zero = lengths[6].pop()
    decode[''.join(sorted(list(nine)))] = '9'
    decode[''.join(sorted(list(zero)))] = '0'
    # decode the number and return it
    out_str = ''
    for d in out_digits:
        out_str = out_str + decode[''.join(sorted(d))]
    return(int(out_str))

in_digits, out_digits = test_case.split(' | ')
in_digits = list(in_digits.split())
out_digits = list(out_digits.split())
val = find_digits(in_digits, out_digits)
print('Test line value is', val)

total = 0
for l in ls:
    in_digits, out_digits = l.split(' | ')
    in_digits = list(in_digits.split())
    out_digits = list(out_digits.split())
    total += find_digits(in_digits, out_digits)
print('Total of outputs is', total)
