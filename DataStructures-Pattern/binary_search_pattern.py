def minimum_in_sorted_rotated_arr(nums):
    l = 0
    r = len(nums) - 1

    while l < r:
        m = (l + r) // 2
        if nums[m] > nums[r]:
            l = m + 1
        else:
            r = m
    return nums[l]


def search_in_a_sorted_rotated_arr(nums, target):
    # [4, 5, 6, 7, 0, 1, 2]
    l = 0
    r = len(nums) - 1

    while l < r:
        m = (l + r) // 2
        if nums[m] == target:
            return m
        if nums[l] <= nums[m]:
            if nums[l] <= target <= nums[m]:
                r = m - 1
            else:
                l = m + 1
        else:
            if nums[m] <= target <= nums[r]:
                l = m + 1
            else:
                r = m - 1
    return -1 if nums[r] != target else r


if __name__ == "__main__":
    nums = [6, 5, 4, 1, 2, 3]
    nums1 = [4, 5, 6, 7, 0, 1, 2]
    target = 0
    print(minimum_in_sorted_rotated_arr(nums))
    print(search_in_a_sorted_rotated_arr(nums1, target))
