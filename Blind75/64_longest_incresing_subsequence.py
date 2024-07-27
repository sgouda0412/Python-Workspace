from typing import List
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        lis = [1] * len(nums)

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    print(lis[i])
                    print(lis[j])
                    lis[i] = max(lis[i], 1 + lis[j])


        return max(lis)


if __name__ == "__main__":
    nums = [10,9,2,5,3,7,101,18]
    object = Solution()
    print(object.lengthOfLIS(nums))