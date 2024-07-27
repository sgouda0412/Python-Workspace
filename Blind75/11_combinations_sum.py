from typing import List


def combinationSum(candidates: List[int], target: int) -> List[List[int]]:
    result = []
    dfs(candidates, target, [], result)
    return result

def dfs(nums, target, path, result):
    if target < 0:
        return
    if target == 0:
        result.append(path)
        return
    for i in range(len(nums)):
        dfs(nums[i:], target - nums[i], path+[nums[i]], result)


if __name__ == "__main__":
    candidates = [2,3,6,7]
    target = 7

    print(combinationSum(candidates, target))