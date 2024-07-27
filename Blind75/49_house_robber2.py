from typing import List
def rob1(self, nums: List[int]) -> int:
    return max(nums[0], self.rob(nums[1:]), self.rob(nums[:-1]))


def rob(self, nums: List[int]) -> int:
    r1 = r2 = 0

    for n in nums:
        t = max(r1 + n, r2)
        r1 = r2
        r2 = t

    return r2

if __name__ == "__main__":
    nums = [1,2,3,1]
    object = Solution()
    print(object.rob1(nums))