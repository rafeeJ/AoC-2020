import re

f = open('input.txt', 'r')

s = ''
for i in f:
    s = s + i

passport_list = s.split('\n\n')

passport_list = [i.replace('\n', ' ').strip().split(' ') for i in passport_list]

count = 0
clean_list = []
for i in passport_list:
    d = {x[:3]:x[4:] for x in i}
    clean_list.append(d)

valid_passports = []
for d in clean_list:
    if len(d) < 7: continue
    elif 'cid' in d.keys() and len(d) == 7: continue 
    else: valid_passports.append(d)

print('Number of valid passports for P1: {}'.format(len(valid_passports)))

valid_passports_ptwo = []
for p in valid_passports:
    valid = True
    for k, v in p.items():
        if k == 'byr':
            if int(v) not in range(1920, 2003): valid = False
        if k == 'iyr':
            if int(v) not in range(2010, 2021): valid = False
        if k == 'eyr':
            if int(v) not in range(2020, 2031): valid = False
        if k == 'hgt':
            if v[-2:] == 'in':
                if int(v[:-2]) not in range(59, 77): valid = False
            if v[-2:] == 'cm':
                if int(v[:-2]) not in range(150, 194): valid = False
        if k == 'hcl':
            if not re.match('#(\d|\w){6}', v): valid = False
        if k == 'ecl':
            if v not in ['amb','blu','brn','gry','grn','hzl','oth']: valid = False
        if k == 'pid':
            if len(v) != 9 or int(v[0]) != 0: valid = False
    if valid:
        valid_passports_ptwo.append(p)
        
print(len(valid_passports_ptwo))