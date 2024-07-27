from typing import List

def findMin(nums: List[int]) -> int:
    N = len(nums)
    l = 0
    r = N - 1

    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    return nums[l]


if __name__ == "__main__":
    nums = [3,4,5,1,2]
    print(findMin(nums))
