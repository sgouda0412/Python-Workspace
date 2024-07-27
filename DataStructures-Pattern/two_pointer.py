class Solution:
    from typing import List

    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        csum = float("inf")
        for i in range(len(nums) - 2):
            l = i + 1
            r = len(nums) - 1
            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == target:
                    return total

                if abs(total - target) < abs(csum - target):
                    csum = total

                if total < target:
                    l += 1
                else:
                    r -= 1
        return csum


if __name__ == "__main__":
    nums = [-1, 2, 1, -4]
    target = 1
    print(Solution().threeSumClosest(nums, target))
