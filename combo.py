# Alright, this one can be tricky but I'm sure you can do it.

# Create a function named combo that takes two ordered iterables. These could be tuples, lists, strings, whatever.

# Your function should return a list of tuples. Each tuple should hold the first item in each iterable, then the second set, then the third, and so on. Assume the iterables will be the same length.

# Check the code below for an example.

# e.g.

# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]

def combo(iterable_1, iterable_2):
    list_of_tuples = []
    for index in range(len(iterable_1)):
        list_of_tuples.append((iterable_1[index], iterable_2[index]))
    return list_of_tuples
