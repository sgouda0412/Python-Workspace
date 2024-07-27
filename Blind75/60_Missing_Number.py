from typing import List

def missingNumber(nums: List[int]) -> int:
    ans = len(nums)

    for i in range(len(nums)):
        ans += i - nums[i]
    return ans

if __name__ == "__main__":
    nums = [3, 0, 1, 2, 5]
    print(missingNumber(nums))