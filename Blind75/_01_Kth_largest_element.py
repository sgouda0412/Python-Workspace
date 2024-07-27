from heapq import heappush, heappop
from typing import List
from collections import defaultdict, deque, OrderedDict, ChainMap, UserDict, UserList, UserString
from itertools import chain, combinations, combinations_with_replacement, compress, count, cycle, accumulate, islice


def kth_largest(nums, k):
    heap = []
    for num in nums:
        heappush(heap, num)
        if len(heap) > k:
            heappop(heap)
    
    return heap[0]



if __name__ == "__main__":
    nums = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    print(kth_largest(nums, k))