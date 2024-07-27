def contains_duplicates(nums):
    s = set()
    for i in nums:
        if i in s:
            return True
        s.add(i)
    return False


if __name__ == "__main__":
    nums = [1, 2, 3, 2]
    print(contains_duplicates(nums))
