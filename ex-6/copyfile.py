#!/usr/bin/env python3

first_file = input('Enter first file name: ').strip()
second_file = input('Enter second file name: ').strip()

f1 = open(first_file, 'r')
f2 = open(second_file, 'w')

content = f1.read()
f2.write(content)
f1.close()
f2.close()
