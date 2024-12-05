
def check_all_increasing(line):
    for i in range(len(line) - 1):
        if line[i] > line[i + 1]:
            return False
    return True

def check_all_decreasing(line):
    for i in range(len(line) - 1):
        if line[i] < line[i + 1]:
            return False
    return True

def check_gap(line):
    for i in range(len(line) - 1):
        if abs(line[i] - line[i + 1]) > 3:
            return False
        elif abs(line[i] - line[i + 1]) < 1:
            return False
    return True
            

def main():
    file_path = input("Enter the file path: ")
    count_safe_reports = 0
    with open(file_path, 'r') as f:
       for line in f:
           line = line.split()
           int_line = list(map(int, line))

           if check_all_increasing(int_line) or check_all_decreasing(int_line):
               if check_gap(int_line):
                   count_safe_reports += 1
          
    print(count_safe_reports)

if __name__ == "__main__":
    main()