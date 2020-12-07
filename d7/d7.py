import more_itertools

f = open('input.txt', 'r')

def process_bag(bag):
    s = bag.split(' bags contain ')
    bag = s[0]
    contains = s[1].strip().replace('.','').split(',')
    formatted_bags = []
    for b in contains:
        if b == 'no other bags': 
            return bag, [(0,0)]
        else:
            c = b.strip().split(' ')
            formatted_bags.append((c[0],'{} {}'.format(c[1], c[2])))
    return bag, formatted_bags

def find_container_bags(bag, d):
    bags = []
    for k,v in d.items():
        if bag in v.keys():
            bags.append(k)
    return bags

def search_bags(target, d):
    l = []
    if len(find_container_bags(target, d)) == 0:
        return target
    else:
        for i in find_container_bags(target, d):
            l.append(i)
            l.append(search_bags(i, d))
    return l

d = {}
for b in f:
    bag, contain = process_bag(b)
    d[bag] = {i[1]:int(i[0]) for i in contain}  

bags = search_bags('shiny gold', d)
unique_bags = len({i:1 for i in list(more_itertools.collapse(bags))})
print(unique_bags)