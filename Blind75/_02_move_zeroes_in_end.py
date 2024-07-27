def move_zeroes_at_the_end(nums):
    index = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[index] = nums[i]
            index += 1

    for i in range(index, len(nums)):
        nums[i] = 0
    return nums

if __name__ == "__main__":
    nums = [0, 1, 0, 2, 3, 4, 0, 8]
    print(move_zeroes_at_the_end(nums))