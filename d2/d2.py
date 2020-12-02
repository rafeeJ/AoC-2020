f = open('input.txt', 'r')

def sanitise_line(s):
    s = s.split(':')
    target = s[0][-1]
    password = s[1].strip()
    target_range = s[0][:-1].split('-')
    return password, target, (int(target_range[0]), int(target_range[1]))

# Part 1
count = 0
for i in f:
    p, t, r = sanitise_line(i)
    c=0
    for i in p: 
        if i == t: c+=1
    if c in range(r[0], r[1]+1):
        count +=1
#print(count)

f = open('input.txt', 'r')

count_two = 0
for i in f:
    p, t, r = sanitise_line(i)
    pos_one = p[r[0]-1]
    pos_two = p[r[1]-1]
    if pos_one == pos_two:
        continue
    if pos_one == t or pos_two == t:
        count_two +=1
print(count_two)