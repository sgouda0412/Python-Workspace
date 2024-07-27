from typing import List

def canJump(nums: List[int]) -> bool:
    if not nums:
        return False
    if len(nums) == 1:
        return True
    
    f = len(nums) - 1

    for i in range(len(nums)-1, -1, -1):
        if i + nums[i] >= f:
            f = i

    return True if f == 0 else False


if __name__ == "__main__":
    nums =  [2,3,1,1,4]
    print(canJump(nums))