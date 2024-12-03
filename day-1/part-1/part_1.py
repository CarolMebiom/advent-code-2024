def split_numbers(input, list_a, list_b):
    try:
        for i in range(0, len(input)):
            input_list = input[i].split()
            list_a.append(int(input_list[0]))
            list_b.append(int(input_list[1]))
    except KeyError:
        raise KeyError("Input must be a list of strings")
    except TypeError:
        raise TypeError("Input must be a list of strings")
    except AttributeError:
        raise AttributeError("A and B must be a list of strings")

def select_small_number(list_a):
    try:
        small_number = min(list_a)
        small_number_index = list_a.index(small_number)
        list_a.pop(small_number_index)
        return small_number
    except AttributeError:
        raise AttributeError("Input must be a list of integers")

