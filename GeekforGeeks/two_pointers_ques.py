def two_sum(arr, target):
    if len(arr) < 2:
        return
    i = 0
    j = len(arr) - 1

    while i < j:
        sum = arr[i] + arr[j]
        if sum == target:
            return [i, j]
        elif sum < target:
            i = i + 1
        else:
            j = j - 1
    return [-1, -1]


if __name__ == "__main__":
    arr = [1, 2, 4, 6, 7, 9]
    target = 3
    arr.sort()
    print(two_sum(arr, target))


# ------------------------------------------------------------------------------
def move_zeroes_at_the_end(nums, n):
    j = 0
    for i in range(n):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 2, 3, 4, 0, 8]
    n = len(nums)
    print(move_zeroes_at_the_end(nums, n))
