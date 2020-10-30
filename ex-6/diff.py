#!/usr/bin/env python3

first_file = input('Enter first file name: ').strip()
second_file = input('Enter second file name: ').strip()

f1 = open(first_file, 'r')
f2 = open(second_file, 'r')

first_contents = f1.readlines()
second_contents = f2.readlines()

f1.close()
f2.close()


def index_in_list(a_list, i):
    return i < len(a_list)


for index in range(len(first_contents)):
    if index_in_list(second_contents, index):
        if first_contents[index] == second_contents[index]:
            print('Yes')
        else:
            print('No')
    else:
        break
