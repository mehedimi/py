list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]

print("Before adding 7000 on list1 list")

print(list1)

print("After adding 7000 on list1 list")

list1[2][2].append(7000)

print(list1)
