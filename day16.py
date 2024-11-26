# Day 16 part 1

filename = 'test16.txt'

with open(filename) as f:
    ls = f.read().strip().split('\n')

# change the hex input to binary
bin_list = []
for l in ls:
    cur_line = ''
    for c in l:
        binary = bin(int(c, 16))[2:].zfill(4)
        cur_line = cur_line + binary
    bin_list.append(cur_line)
    print(cur_line)

def binToParts(s, l=-1, n=-1):
    version = int(s[:3], 2)
    id = int(s[3:6], 2)
    i = 0
    s = s[6:]
    new_bin = ''
    if id == 4:
        last_group = False
        while len(s) > 0 and not last_group:
            if len(s) > 4:
                new_bin = new_bin + s[1:5]
                if s[0] == 0:
                    last_group = True
                if len(s) > 5:
                    s = s[5:]
                else:
                    s = ''
            else:
                s = ''
        val = int(new_bin, 2)
        return([version, id, val])
    else:
        if s[0] == '0':
            l_id = 0
            bit_len = int(s[1:16], 2)
            s = s[16:]
            return(binToParts(s, l=bit_len))
        else:
            l_id = 1
            sub_p_num = int(s[1:12], 2)
            s = s[12:]
            return(binToParts(s, n=sub_p_num))


print(binToParts(bin_list[0]))
