from typing import List
def containsDuplicate(nums: List[int]) -> bool:
    hs = set()

    for i in nums:
        if i in hs:
            return True
        else:
            hs.add(i)
    return False

if __name__ == "__main__":
    nums = [1, 2, 3, 4, 1]
    print(containsDuplicate(nums))