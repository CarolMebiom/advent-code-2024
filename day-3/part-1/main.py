import re

regex = r"mul\([0-9]{1,},[0-9]{1,}\)"

def multiply_tup(tup):
    return tup[0] * tup[1]

with open('real_input.txt', 'r') as f:
    test_str = f.readlines()

length = len(test_str)
all_sum = 0
for i in range(0, length):
    at_moment_test = re.findall(regex, test_str[i])
    for i in at_moment_test:
        tup = i.strip("mul")
        tup = eval(tup)
        all_sum += multiply_tup(tup)

print(all_sum)