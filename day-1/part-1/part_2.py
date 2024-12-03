def times_repeated(number, list):
    if type(number) != int:
        raise ValueError("Number must be an integer")
    else:
        return list.count(number)