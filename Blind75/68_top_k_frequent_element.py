from typing import List
from collections import Counter
import heapq


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)
        c = sorted(c, key=lambda x : c[x], reverse=True)
        return c[:k]
    
    def topKFrequent2(self, nums: List[int], k: int) -> List[int]:
        c = Counter(nums)

        c = [(-v, k) for k, v in c.items()]
        heapq.heapify(c)
        output = []

        for i in range(k):
            item = heapq.heappop(c)
            output.append(item[1])
        return output

if __name__ == "__main__":
    nums = [1,1,1,2,2,3,3,3]
    k = 2
    object = Solution()
    print(object.topKFrequent(nums,k)) 
    print(object.topKFrequent2(nums,k)) 