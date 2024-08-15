import math

lst = [1, 4, 5, 67, 2, 3, 5, 6, 1, 23, 4, 6, 7, 1, 2, 2, 234, 3, 32, 1, 12, 2, 2]

# Mean - Add all up and divide by length
def mean(lst):
    total = sum(lst)
    average = total / len(lst)
    return average

# Median - Sort and find middle number
def median(lst):
    lst.sort()
    length = len(lst)
    mid = length / 2
    mid = math.ceil(mid)
    return lst[mid]

# Mode - most occuring number - Without using the counter module
mode = [[x, lst.count(x)] for x in set(lst)]

mean(lst)
median(lst)
