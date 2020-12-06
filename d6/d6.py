f = open('input.txt', 'r')

def get_unique_answers(group):
    """
    Function to return unique number of questions answered.

     group: list of questions answered.
    """
    # Create a set by iterating over a string of the combined passengers.
    return len({i for i in "".join(group)})

# Create a list of the groups
groups = ''.join(f).split('\n\n')
# For each group, split into a list of each passenger
groups = [i.replace('\n', ' ').split(' ') for i in groups]

# Create a list with elements of unique answers!
total_sum = sum([get_unique_answers(group) for group in groups])
# And print sum for part 1!
print(total_sum)

# Group looks like: ['fjmz', 'mjczf', 'unkzjm']
def get_answer_dict(group):
    """
    Function to return number of answers by all members of group

    group: list of questions answered.
    """
    passengers = len(group)
    d = {}
    # Iterate over each passenger in the group...
    for passenger in group:
        # Iterate over all the questions answered yes to...
        for q in passenger:
            # If the question letter has not been logged, add it...
            if q not in d.keys():
                d[q] = 1
            # Else, increment the count.
            else:
                d[q] = d[q] + 1
    # Return the length of the array containing all question names where the logged
    # number is equal to the number of passengers.
    return len([k for k,v in d.items() if v==passengers])

sum_all_answers = sum([get_answer_dict(group) for group in groups])
print(sum_all_answers)