from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        ans = 0
        prefix = 0
        prefixToIndex = {0: -1}

        for i, num in enumerate(nums):
            prefix += 1 if num else -1
            ans = max(ans, i - prefixToIndex.setdefault(prefix, i))

        return ans


if __name__ == "__main__":
    nums = [1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 1]
    print(Solution().findMaxLength(nums))
