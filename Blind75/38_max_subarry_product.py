from typing import List


def maxProduct(nums: List[int]) -> int:
    ans = max(nums)
    maximum = minimum = 1

    for i in nums:
        temp = maximum * i
        maximum = max(maximum * i, minimum * i, i)
        minimum = min(temp, minimum * i, i)
        ans = max(ans, maximum)
    return ans


if __name__ == "__main__":
    nums = [2, 3, 0, 7, 2, 0, -2, -2, 4]
    print(maxProduct(nums))
