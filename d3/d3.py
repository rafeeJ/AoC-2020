f = open('input.txt', 'r')
#o = open("part_two.txt", "a")

# step = 3
# count = 0
# pos = 3

def clean_input():
    return [i.strip() for i in f]
    
# Part one almagomation Lol
#
# for i,v in enumerate(clean_input()):
#     if i == 0: continue
#     coord = str(v[pos])
#     x = list(v)
#     if coord == '#':
#         count+=1
#         x[pos] = 'X'
#         o.write("".join(x) + '\n')
#     else:
#         x[pos] = 'O'
#         o.write("".join(x) + '\n')
#     pos += step
#     if pos >= len(v):
#         pos = pos % len(v)
# print(count)

def traverse_hill(down, right, trees):
    count = 0
    pos = 0 + right
    for i,v in enumerate(trees):
        if i == 0 or i % down != 0: continue
        coord = v[pos]
        if coord == '#': count += 1
        pos += right
        if pos >= len(v):
            pos = pos % len(v)
    return count

l = clean_input()

print(traverse_hill(1, 1, l))
print(traverse_hill(1, 3, l))
print(traverse_hill(1, 5, l))
print(traverse_hill(1, 7, l))
print(traverse_hill(2, 1, l))