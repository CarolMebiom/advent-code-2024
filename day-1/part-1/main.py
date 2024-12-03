from part_1 import select_small_number, split_numbers
from part_2 import times_repeated

def main():
    a = []
    b = []
    difference_list = []
    with open('part-1/input.txt', 'r') as f:
        split_numbers(f.readlines(), a, b)

    if len(a) != len(b):
        print("Invalid input")
    
    else:
        for i in range(0, len(a)):
            small_number_a = select_small_number(a)
            small_number_b = select_small_number(b)
            difference = abs(small_number_b - small_number_a)
            difference_list.append(difference)
    
    
    similarity_list = []
    a = []
    b = []
    sum_similarity = 0
    with open('part-1/input.txt', 'r') as f:
        split_numbers(f.readlines(), a, b)
        
    for i in a:
        similarity_list.append(times_repeated(i, b))

    if len(a) != len(similarity_list):
        print("Invalid input")
    
    else:
        for i in range(0, len(a)):
            sum_similarity += a[i] * similarity_list[i]
    
    print(sum_similarity)

        
    





if __name__ == "__main__":
    main()