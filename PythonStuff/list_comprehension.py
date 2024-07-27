# elegant and consise way of creating a list

x = [x for x in range(10)]
print(x)

numbers = [12, 13, 14]
doubled = [x * 2 for x in numbers]
print(doubled)

squared = [x**2 for x in numbers]
print(squared)

listed = [x for x in [1, 2, 3]]
print(listed)

filtered_list = [i for i in range(11) if i % 2 == 0]
print(filtered_list)


matrix = [[j for j in range(3)] for i in range(3)]

print(matrix)

# Using list comprehension to iterate through loop
List = [character for character in "Geeks 4 Geeks!"]

# Displaying list
print(List)

from typing import List


def segregate(arr: list[int]) -> list[int]:
    res = [0] * arr.count(0) + [1] * arr.count(1)
    return res


# Driver program
if __name__ == "__main__":
    arr = [0, 1, 0, 1, 0, 0, 1, 1, 1, 0]
    print(segregate(arr))


# Function to Sort even-placed elements
# in increasing and odd-placed in decreasing
# order


def evenOddSort(input):

    # separate even odd indexed elements list
    evens = [input[i] for i in range(0, len(input)) if i % 2 == 0]
    odds = [input[i] for i in range(0, len(input)) if i % 2 != 0]

    # sort evens in ascending and odds in
    # descending using sorted() method
    print(sorted(evens) + sorted(odds, reverse=True))


# Driver program
if __name__ == "__main__":
    input = [0, 1, 2, 3, 4, 5, 6, 7]
    evenOddSort(input)


s = [[1, 1], [2, 4], [3, 9], [4, 16], [5, 25]]
sq = [x.append(10) for x in s]
print(s)


# no of set bits
n = 11

print(bin(n).count("1"))
