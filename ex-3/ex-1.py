side_a = float(input('Enter triangle side a: '))
side_b = float(input('Enter triangle side b: '))
side_c = float(input('Enter triangle side c: '))

p = (side_a + side_b + side_c)
t = side_a * 3

if p == t:
    print('The triangle is Equilateral')
else:
    print('The triangle is Non Equilateral')
