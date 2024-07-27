from typing import List
from collections import defaultdict, ChainMap, UserDict, UserString


class Solution:
    def duplicates(self, n: int, arr: List[int]) -> List[int]:
        l = []
        for i in range(len(arr)):
            if arr.count(arr[i]) > 1:
                l.append(arr[i])
            else:
                continue
        if l == []:
            l.append(-1)
        return list(set(l))

    # def _duplicates(self, n: int, arr: List[int]) -> List[int]:

    #     l = []
    #     c = set()

    #     for i in range(n):
    #         if arr[i] not in l:
    #             l.append(arr[i])
    #         else:
    #             c.add(arr[i])

    #     if len(c) == 0:
    #         return [-1]
    #     else:
    #         return list(c)


if __name__ == "__main__":

    x: Solution = Solution()
    n: int = 4
    l: List[int] = [0, 2, 2, 3]
    print(x.duplicates(n, l))
# print(x._duplicates(n, l))
