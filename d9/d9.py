f = open('input.txt', 'r')
cypher = [int(i) for i in f]

def get_preamble(list, index, size):
    """
    Function that returns the preamble for a given element

    Returns: List
    """
    if size > index:
        return []
    else:
        return [list[i] for i in range(index - size, index)]

def check_valid(preamble, target):
    """
    Function to determine whether the target is valid

    Returns boolean
    """
    d = {}
    for i in range(len(preamble)):
        if target - preamble[i] in d:
            return True
        else:
            d[preamble[i]] = i
    #print(d)
    return False

def part_one(cypher_in):
    for idx, num in enumerate(cypher_in):
        preamble = get_preamble(cypher_in, idx, 25)
        if len(preamble) == 0: continue
        else:
            if(check_valid(preamble, num)): continue
            else:
                return(num) 
                break

#print(part_one(cypher[:26]))
weakness = part_one(cypher)
print('Part 1 solution: {}'.format(weakness))

def part_two(cypher_in, target):
    for i,v in enumerate(cypher_in):
        current = 0
        upper_bound = 1
        while current != target:
            current = sum([cypher_in[x] for x in range(i, i+upper_bound)])
            if current < target: upper_bound += 1
            elif current > target: break
            else: return [cypher_in[x] for x in range(i, i+upper_bound)]  
    return True

enc_weakness = part_two(cypher, weakness)
print('Part 2 solution: {}'.format(min(enc_weakness)+ max(enc_weakness)))