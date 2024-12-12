import re

#test_str = "xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"

DO = 1
DONT = 0

current = 1

regex_do = r"(do)[^n't]"
regex_dont = r"(don't)"
regex_mul = r"mul\([0-9]{1,},[0-9]{1,}\)"

with open('/real_input.txt', 'r') as f:
    test_str = f.readlines()

def multiply_tup(tup):
    return tup[0] * tup[1]

sum_len = 0
new_test_str = ""
for i in range(0, len(test_str)):
    new_test_str += test_str[i]

all_sum = 0

i = 0
while i < len(new_test_str):
    string_t_search = new_test_str[i:]
    if current == 1:
        match_dont = re.search(regex_dont, string_t_search)
        if match_dont is None:
            at_moment_test = re.findall(regex_mul, string_t_search)
            for j in at_moment_test:
                tup = j.strip("mul")
                tup = eval(tup)
                all_sum += multiply_tup(tup)
            i = len(new_test_str)
        else:
            f = match_dont.start()
            l = match_dont.end()
            print(f)
            at_moment_test = re.findall(regex_mul, string_t_search[:f])
            for j in at_moment_test:
                tup = j.strip("mul")
                tup = eval(tup)
                all_sum += multiply_tup(tup)
            i = i + l
            current = 0
    
    elif current == 0:
        match_do = re.search(regex_do, string_t_search)
        if match_do is None:
            i = len(new_test_str)
        else:
            l = match_do.end()
            i = l + i
            current = 1
    
print(all_sum)

