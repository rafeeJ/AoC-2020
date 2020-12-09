f = open('input.txt', 'r')
cypher = [int(i) for i in f]

def get_preamble(list, index, size):
    """
    Function that returns the preamble for a given element

    Returns: List
    """
    # Check if the number can actually have a valid preamble.
    if size > index:
        return []
    else:
        # Groovy list notation that returns the preamble.
        return [list[i] for i in range(index - size, index)]

def check_valid(preamble, target):
    """
    Function to determine whether the target is valid | Simple twosum

    Returns boolean
    """
    d = {}
    # For all values in preamble...
    for i in range(len(preamble)):
        # If the difference is already in d, return True...
        if target - preamble[i] in d:
            return True
        # Otherwise add the number to the dictionary...
        else:
            d[preamble[i]] = i
    return False

def part_one(cypher_in):
    """
    Function to calculate answer for part one.
    
    Returns: Number where the preamble doesn't compute a valid target
    """
    # For each number in cypher...
    for idx, num in enumerate(cypher_in):
        # Get the preamble...
        preamble = get_preamble(cypher_in, idx, 25)
        # Check if it's an invalid preamble...
        if len(preamble) == 0: continue
        else:
            # If valid preamble, check if the number is valid...
            if(check_valid(preamble, num)): continue
            else:
                # If not, finish the loop and return the invalid number.
                return(num) 
                break

#print(part_one(cypher[:26]))
weakness = part_one(cypher)
print('Part 1 solution: {}'.format(weakness))

def part_two(cypher_in, target):
    """
    Function to brute force an answer for part two. 

    Returns: List of the contiguous values in cypher_in that sum to target
    """
    # For all the numbers in the cypher...
    for i,v in enumerate(cypher_in):
        # Set some prelim vartiables.
        # Current tracks the sum of continuous list items.
        # Upper bound is a pointer that tracks the end of the list from given index. 
        current = 0
        upper_bound = 1
        # Loop while current is not equal to target...
        while current != target:
            # Get sum of continuous list items through list comprehension.
            current = sum([cypher_in[x] for x in range(i, i+upper_bound)])
            # If current = target, return the list...
            # Otherwise either break if too large, or increase upper_bound pointer.
            if current < target: upper_bound += 1
            elif current > target: break
            else: return [cypher_in[x] for x in range(i, i+upper_bound)]  
    return []

enc_weakness = part_two(cypher, weakness)
print('Part 2 solution: {}'.format(min(enc_weakness)+ max(enc_weakness)))