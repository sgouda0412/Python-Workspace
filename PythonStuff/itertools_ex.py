# https://levelup.gitconnected.com/mastering-pythons-itertools-module-a-comprehensive-tutorial-c1ece6fbaa1b

# Python3 code to demonstrate list
# concatenation using itertools.chain()
import itertools

# Initializing lists
test_list1 = [1, 4, 5, 6, 5]
test_list2 = [3, 5, 7, 2, 5]

# using itertools.chain() to concat
res_list = list(itertools.chain(test_list1, test_list2))  # Printing concatenated list
print("Concatenated list using itertools.chain() : " + str(res_list))


import itertools

# Initialize empty array with length 10 filled with 0's
a = list(itertools.repeat(0, 10))
print(a)

# Initialize 2D empty array with 3 rows and 4 columns filled with 0's
b = [list(itertools.repeat(0, 4)) for i in range(3)]
print(b)


from itertools import islice


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b


print(list(islice(fibonacci(50), 20)))
