# This code is fragile. When one item is added/removed from one of the lists, the outputs of the program will not be
# as expected.

names = ['Vera', 'Chuck', 'Samantha', 'Roberto', 'Joe', 'Dave', 'Tina', 'Ringo']
salaries = [2000, 1800, 1800, 2100, 2000, 2200, 2300, 1900]

count = len(names)
for c in range(count):
    print(f'{names[c]}, ${salaries[c]}')
