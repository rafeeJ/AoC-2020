f = open('input.txt', 'r')

l = [int(i) for i in f]

# Part One
for i in l:
    diff = 2020 - i
    if diff in l: print('{}'.format(int(i)*diff))

# Part Two
t = [2020-i for i in l]
for i, v in enumerate(t):
    for idx, val in enumerate(l):
        if i == idx: continue
        else:
            diff = v - val
            if diff in l: print('{}, {}, {}'.format(l[i], l[idx], diff))