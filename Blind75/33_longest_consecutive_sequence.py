from typing import List
class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ns = set(nums)
        largest = 0

        for i in nums:
            if i - 1 not in ns:
                lth = 0
                while i + lth in ns:
                    lth += 1
                largest = max(largest, lth)
        return largest



if __name__ == "__main__":
    nums = [100,4,200,1,3,2]
    object = Solution()
    print(object.longestConsecutive(nums))