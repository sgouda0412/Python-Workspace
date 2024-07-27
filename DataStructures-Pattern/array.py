class Solution:
    from typing import List

    def findDuplicate(self, nums: List[int]) -> int:
        fast = slow = nums[0]
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]

            if slow == fast:
                break

        fast = nums[0]
        while fast != slow:
            fast = nums[fast]
            slow = nums[slow]

        return slow


if __name__ == "__main__":
    nums = [1, 3, 4, 2, 2]
    print(Solution().findDuplicate(nums))  # Output should be 2
