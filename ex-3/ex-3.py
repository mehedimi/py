# Read numbers from file

def read_from_file():
    txt = open('ex-3-sample.txt', 'r')
    txt_list = txt.readlines()
    txt_list.pop()
    numbers = map(lambda x: float(x.rstrip()), txt_list)
    txt.close()

    return list(numbers)


# Calculate average of numbers

def calculate_avg():
    numbers = read_from_file()
    return sum(numbers) / len(numbers)


print(calculate_avg())
