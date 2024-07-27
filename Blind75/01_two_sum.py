from typing import List, Tuple, Callable
from collections import OrderedDict, defaultdict, deque, Counter, UserDict, UserList, UserString
from collections import OrderedDict, defaultdict
from itertools import chain, combinations, compress, combinations_with_replacement, cycle, count, accumulate
from functools import cached_property, lru_cache, singledispatch, cmp_to_key



def two_sum(nums : List, target : int):
    lookup = {}

    for index, value in enumerate(nums):
        diff = target - value

        if diff in lookup:
            return [lookup[target - value], index]
        
        lookup[value] = index
    return [-1, -1]


if __name__ == "__main__":
    nums: list = [2, 1, 9, 11]
    target = 9
    print(two_sum(nums, target))