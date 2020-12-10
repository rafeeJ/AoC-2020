f = open('input.txt', 'r')

x = sorted([int(i.strip()) for i in f])
device_joltage_adapter = max(x) + 3
y = x.copy() + [device_joltage_adapter]
print(y)

print('Looking for adapter with {}\n'.format(device_joltage_adapter))

charging_outlet_joltage = 0
diff_d_fr = {1: 0, 2: 0, 3: 0}
for idx, val in enumerate(y):
    diff = abs(charging_outlet_joltage - val)
    #print('Difference between output ({}J) and input ({}J) is {}'.format(charging_outlet_joltage, val, diff))
    diff_d_fr[diff] = diff_d_fr[diff] + 1
    charging_outlet_joltage = val
#print(diff_d_fr)
print('Solution to part 1: {}'.format(diff_d_fr[1] * diff_d_fr[3]))

valid_connectors = {i:[i-1, i-2, i-3]for i in y}
#print(valid_connectors)

d = {}
d[0] = 1
for i in y:
    d[i] = d.get(i - 1, 0) + d.get(i - 2, 0) + d.get(i - 3, 0)
print('Solution to part 1: {}'.format(d[y[-1]]))


"""
Below is an example of what happens when I don't read the full question! :)

# def lookup(target, adapters):
#     return {k:v for k,v in adapters.items() if target in v}

# diff_d = {1: 0, 2: 0, 3: 0}

# while True:
#     poss_adapters = {}
#     for o in range(charging_outlet_joltage+1, charging_outlet_joltage+4):
#         poss_adapters.update(lookup(o, joltage_adapters))
#     print('These are the rated adapters for {}J -> {}'.format(charging_outlet_joltage, poss_adapters))
    
#     adapters = len(poss_adapters)
#     closest_adapter = min(poss_adapters.keys())
#     print('Closest adapter is {}J'.format(closest_adapter))
    
#     diff = abs(closest_adapter - charging_outlet_joltage)
#     print('Difference between the rating and current voltage is {}'.format(diff))
#     if diff not in diff_d.keys():
#         diff_d[diff] = 1
#     else:
#         diff_d[diff] = diff_d[diff] + 1

#     print('\n')
#     charging_outlet_joltage = closest_adapter
#     if charging_outlet_joltage == device_joltage_adapter:
#         break
# print('solution to part 1: {}'.format(diff_d[1] * diff_d[3]))
"""