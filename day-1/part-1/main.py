
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


def main():
    a = []
    b = []
    difference_list = []
    with open('input.txt', 'r') as f:
        split_numbers(f.readlines(), a, b)

    if len(a) != len(b):
        print("Invalid input")
    
    else:
        for i in range(0, len(a)):
            small_number_a = select_small_number(a)
            small_number_b = select_small_number(b)
            difference = abs(small_number_b - small_number_a)
            difference_list.append(difference)
    
    print(sum(difference_list))
    




if __name__ == "__main__":
    main()